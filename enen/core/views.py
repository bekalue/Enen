from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Patient, Assistance, passwordHasher, emailHasher
from django.db.models import Count, Q
from rest_framework import viewsets
from .serializers import DoctorSerializer, PatientSerializer, AssistanceSerializer

def responseHeadersModifier(response):
    """Funtion to edit response headers so that no cached versions can be viewed. Returns the modified response."""
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"
    return response

def requestSessionInitializedChecker(request):
    """Function to initialize request sessions if they don't exist."""

    # Checking if session variables exist
    if not request.session.get('isDoctor'):
        request.session['isDoctor'] = ""
    if not request.session.get('isLoggedIn'):
        request.session['isLoggedIn'] = False
    if not request.session.get('userEmail'):
        request.session['userEmail'] = ""
    if not request.session.get('Name'):
        request.session['Name'] = ""
    if not request.session.get('numberNewAssistances'):
        request.session['numberNewAssistances'] = ""

    # Returning request
    return request


def index(request):
    """ Function for displaying main page of website. """
    # Editing response headers so as to ignore cached versions of pages
    response = render(request,"core/index.html")
    return responseHeadersModifier(response)

def register(request):
    """ Function for displaying registration page. """

    # If user wants to register
    if request.method == "GET":
        # Editing response headers so as to ignore cached versions of pages
        response = render(request,"core/register.html")
        return responseHeadersModifier(response)
    
    # If user wants to submit registration form
    elif request.method == "POST":

        # Getting data from form
        userFirstName = request.POST["userFirstName"]
        userLastName = request.POST["userLastName"]
        userEmail = request.POST["userEmail"]
        userId = request.POST["userId"]
        userAddress = request.POST["userAddress"]
        userContactNo = request.POST["userContactNo"]
        userPassword = request.POST["userPassword"]
        userConfirmPassword = request.POST["userConfirmPassword"]

        # Check if a user with the same email or user ID already exists
        if Patient.objects.filter(email=userEmail).exists() or Patient.objects.filter(userId=userId).exists():
            # Storing failure message in the context variable
            context = {
                "message": "A user with this email or user ID already exists. Please try again with different information."
            }

            # Editing response headers so as to ignore cached versions of pages
            response = render(request, "core/register.html", context)
            return responseHeadersModifier(response)

        # If both the passwords match
        elif userPassword == userConfirmPassword:

            name = userFirstName + " " + userLastName

            # Encrypting password to store inside database
            passwordHash = passwordHasher(userPassword)

            # Encrypting email to store inside database
            emailHash = emailHasher(userEmail)

            # Creating a patient object and saving inside the database
            patient = Patient(name = name,userId = userId, email = userEmail, passwordHash = passwordHash, address = userAddress, contactNumber = userContactNo, emailHash = emailHash )
            patient.save()

            # Storing success message in the context variable
            context = {
                "message":"User Registration Successful. Please Login."
            }

            # Editing response headers so as to ignore cached versions of pages
            response = render(request, "core/register.html",context)
            return responseHeadersModifier(response)

        # If the passwords given don't match
        else:
            # Storing failure message in the context variable
            context = {
                "message":"Passwords do not match. Please register again."
            }

            # Editing response headers so as to ignore cached versions of pages
            response = render(request,"core/register.html",context)
            return responseHeadersModifier(response)

    # For any other method of request, sending back the registration page.
    else:

        # Editing response headers so as to ignore cached versions of pages
        response = render(request,"core/register.html")
        return responseHeadersModifier(response)

def login(request):
    """ Function for logging in the user. """

    # Calling session variables checker
    request = requestSessionInitializedChecker(request)

    # If the request method is post
    if request.method == "GET":
        try:

            # If the user is already logged in inside of his sessions, and is a doctor, then no authentication required
            if request.session['isLoggedIn'] and request.session['isDoctor']:

                # Accessing the doctor user and all his/her records
                doctor = Doctor.objects.get(emailHash = request.session['userEmail'])
                records = doctor.doctorRecords.all()

                # Getting the count of the new Assistances pending
                numberNewPendingAssistances = doctor.doctorRecords.aggregate(newPendingAssistances = Count('pk', filter =( Q(isNew = True) & Q(isCompleted = False) ) ))['newPendingAssistances']

                # Storing the same inside the session variables
                request.session['numberNewAssistances'] = numberNewPendingAssistances

                # Storing the required information inside the context variable
                context = {
                    "message" : "Successfully Logged In.",
                    "isAuthenticated" : True,
                    "user": records.order_by('-timestamp')
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request,"core/userDoctorRequestPortal.html", context)
                return responseHeadersModifier(response)

            # If the user is already logged in inside of his sessions, and is a patient, then no authentication required
            elif request.session['isLoggedIn'] and (not request.session['isDoctor']):

                # Accessing the patient user and all his/her records
                patient = Patient.objects.get(emailHash = request.session['userEmail'])
                records = patient.patientRecords.all()

                # Getting the count of the new Assistances pending
                numberNewAssistances = patient.patientRecords.aggregate(newCompletedAssistances = Count('pk', filter =( Q(isNew = True) & Q(isCompleted = True) ) ) )['newCompletedAssistances']

                # Storing the same inside the session variables
                request.session['numberNewAssistances'] = numberNewAssistances

                # Updating the completed records
                for record in records:
                    if record.isCompleted:
                        record.isNew = False
                        record.save()

                # Storing the required information inside the context variable
                context = {
                    "message" : "Successfully Logged In.",
                    "isAuthenticated" : True,
                    "user": records.order_by('-timestamp')
                    }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request,"core/userPatientRequestPortal.html", context)
                return responseHeadersModifier(response)

            else:
                # Editing response headers so as to ignore cached versions of pages
                response = render(request,"core/login.html")
                return responseHeadersModifier(response)

        # If any error occurs, sending back a new blank page
        except:

            # Editing response headers so as to ignore cached versions of pages
            response = render(request,"core/login.html")
            return responseHeadersModifier(response)

    # If the request method is post
    elif request.method == "POST":

        # Extracting the user information from the post request
        userName = request.POST["useremail"]
        userPassword = request.POST["userpassword"]

        # If such a patient exists
        try:
            patient = Patient.objects.get(email = userName)

            # Storing required session information
            request.session['isDoctor'] = False

        # Otherwise trying if a doctor exists
        except Patient.DoesNotExist:
            try:
                doctor = Doctor.objects.get(email = userName)

                # Storing required session information
                request.session['isDoctor'] = True

            # If no such doctor or patient exists
            except Doctor.DoesNotExist:

                # Storing message inside context variable
                context = {
                    "message":"User does not exist. Please register first."
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request,"core/login.html", context)
                return responseHeadersModifier(response)

        # Getting the hash of user inputted password
        passwordHash = passwordHasher(userPassword)

        # If the logged in user is a doctor
        if request.session['isDoctor']:

            # Accessing all records of doctor
            records = doctor.doctorRecords.all()

            # Getting the count of new Assistances
            numberNewPendingAssistances = doctor.doctorRecords.aggregate(newPendingAssistances = Count('pk', filter =( Q(isNew = True) & Q(isCompleted = False) ) ))['newPendingAssistances']

            # Storing the same inside request variable
            request.session['numberNewAssistances'] = numberNewPendingAssistances

            # If the inputted hash and the original user password hash match
            if passwordHash == doctor.passwordHash:

                # Storing required information in session variable of request
                request.session['isLoggedIn'] = True
                request.session['userEmail'] = doctor.emailHash
                request.session['Name'] = doctor.name

                # Redirecting to avoid form resubmission
                # Redirecting to home page
                # Editing response headers so as to ignore cached versions of pages
                response = HttpResponseRedirect(reverse('index'))
                return responseHeadersModifier(response)

            # Else if the password inputted is wrong and doesn't match
            else:

                # Storing message inside context variable
                context = {
                    "message":"Invalid Credentials.Please Try Again."
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request,"core/login.html", context)
                return responseHeadersModifier(response)

        # Otherwise if the user is a patient
        else:

            # Accessing all records of patient
            records = patient.patientRecords.all()

            # Getting the count of new Assistances
            numberNewAssistances = patient.patientRecords.aggregate(newCompletedAssistances = Count('pk', filter =( Q(isNew = True) & Q(isCompleted = True) ) ))['newCompletedAssistances']

            # Storing the same inside request variable
            request.session['numberNewAssistances'] = numberNewAssistances

            # Updating the completed records
            for record in records:
                if record.isCompleted :
                    record.isNew = False
                    record.save()

            # If the inputted hash and the original user password hash match
            if passwordHash == patient.passwordHash:

                # Storing required information in session variable of request
                request.session['isLoggedIn'] = True
                request.session['userEmail'] = patient.emailHash
                request.session['Name'] = patient.name
                request.session['isDoctor'] = False

                # Redirecting to avoid form resubmission
                # Redirecting to home page
                # Editing response headers so as to ignore cached versions of pages
                response = HttpResponseRedirect(reverse('index'))
                return responseHeadersModifier(response)

            # Else if the password inputted is wrong and doesn't match
            else:

                # Storing message inside context variable
                context = {
                    "message":"Invalid Credentials. Please Try Again."
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request,"core/login.html", context)
                return responseHeadersModifier(response)
    # For any other method of access, returning a new blank login page
    else:
        response = render(request,"core/login.html")
        return responseHeadersModifier(response)

def logout(request):
    """Function to log out the user."""
    # Erasing all the information of the session variables if user is logged out
    request.session['isDoctor'] = ""
    request.session['isLoggedIn'] = False
    request.session['userEmail'] = ""
    request.session['Name'] = ""
    request.session['numberNewAssistances'] = ""

    # Redirecting to avoid form resubmission
    # Redirecting to home page
    # Editing response headers so as to ignore cached versions of pages
    response = HttpResponseRedirect(reverse('login'))
    return responseHeadersModifier(response)

def contact(request):
    """Function to display contact information."""

    context = {
        "doctors" : Doctor.objects.all(),
        "message":"Please Login First."
    }
    if request.session.get('isLoggedIn', False):
        # Editing response headers so as to ignore cached versions of pages
        response = render(request,"core/doctors.html",context)
        return responseHeadersModifier(response)
    else:
        # Editing response headers so as to ignore cached versions of pages
        response = render(request, "core/doctors.html", context)
        return responseHeadersModifier(response)

def onlinehelp(request):
    """Function to submit online Assistance request to doctor."""

    # Calling session variables checker
    request = requestSessionInitializedChecker(request)

    # If the request method is get
    if request.method == "GET":

        # If the user is logged in
        if request.session['isLoggedIn']:

            # Portal only for patient Assistance request submission, not for doctors
            if not request.session['isDoctor']:

                # Storing available doctors inside context variable
                context = {
                    "doctors" : Doctor.objects.all().order_by('specialization')
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request, "core/help.html", context)
                return responseHeadersModifier(response)

        # If the user is not logged in
        else:

            # Storing message inside context variable
            context = {
                    "message":"Please Login First."
            }

            # Editing response headers so as to ignore cached versions of pages
            response = render(request, "core/help.html", context)
            return responseHeadersModifier(response)

    # If the user is posting the Assistance request
    elif request.method == "POST":

        # Accepting only if the user is logged in
        if request.session['isLoggedIn']:

            # If the Assistance is being submitted back by a doctor
            if request.session['isDoctor']:

                # Extracting information from post request
                assistanceText = request.POST['Assistance']

                # Updating the Assistance and saving it
                assistance = Assistance.objects.get(pk = request.POST['AssistanceID'])
                assistance.assistanceText = assistanceText
                assistance.isCompleted = True
                assistance.isNew = True
                assistance.save()

                # Getting the records of the doctor
                records = Doctor.objects.get(emailHash = request.session['userEmail']).doctorRecords.all()

                # Storing required information inside context variable
                context = {
                    "user" : records,
                    "successAssistanceMessage" : "Assistance Successfully Submitted."
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request, "core/userDoctorRequestPortal.html", context)
                return responseHeadersModifier(response)

            # Else if the patient is submitting Assistance request
            else:

                # Extracting information from post request and getting the corresponding doctor
                doctor = Doctor.objects.get(pk = request.POST["doctor"])
                symptoms = request.POST["symptoms"]

                # Saving the Assistance under the concerned doctor
                assistance = Assistance(doctor = doctor, patient = Patient.objects.get(emailHash = request.session['userEmail']), symptoms = symptoms)
                assistance.save()

                # Storing information inside context variable
                context = {
                    "successAssistanceMessage" : "Assistance Successfully Requested.",
                    "doctors"  : Doctor.objects.all().order_by('specialization')
                }

                # Editing response headers so as to ignore cached versions of pages
                response = render(request, "core/help.html", context)
                return responseHeadersModifier(response)

        # Else if the user is not logged in
        else:

            # Storing information inside context variable
            context = {
                    "successAssistanceMessage":"Please Login First.",
            }

            # Editing response headers so as to ignore cached versions of pages
            response = render(request, "core/login.html", context)
            return responseHeadersModifier(response)

    # For any other method of access, returning a new blank online Assistance page
    else:

        # Editing response headers so as to ignore cached versions of pages
        response = render(request, "core/help.html")
        return responseHeadersModifier(response)


def requests(request):

    doctor = Doctor.objects.get(emailHash = request.session['userEmail'])
    records = doctor.doctorRecords.all()

    # Getting the count of the new Assistances pending
    numberNewPendingAssistances = doctor.doctorRecords.aggregate(newPendingAssistances = Count('pk', filter =( Q(isNew = True) & Q(isCompleted = False) ) ))['newPendingAssistances']

    # Storing the same inside the session variables
    request.session['numberNewAssistances'] = numberNewPendingAssistances

    # Storing the required information inside the context variable
    context = {
        "message" : "Successfully Logged In.",
        "isAuthenticated" : True,
        "user": records.order_by('-timestamp')
    }

    # Editing response headers so as to ignore cached versions of pages
    response = render(request,"core/userDoctorRequestPortal.html", context)
    return responseHeadersModifier(response)


def about(request):
    """Function to display about bekalu's information."""

    # Editing response headers so as to ignore cached versions of pages
    response = render(request, "core/me.html")
    return responseHeadersModifier(response)

def profile(request):
    """Function to display profile information."""

    # Calling session variables checker
    request = requestSessionInitializedChecker(request)

    # If the request method is get
    if request.method == "GET":
        
        # If the user is logged in
        if request.session['isLoggedIn']:
            
            # Portal only for patient Assistance request submission, not for doctors
            if request.session['isDoctor']:

                # fetching the doctor records
                doctor = Doctor.objects.get(emailHash = request.session['userEmail'])

                # Storing message inside context variable
                context = {
                    "user": doctor
                    }
                
                # Editing response headers so as to ignore cached versions of pages
                response = render(request, "core/profile.html", context)
                return responseHeadersModifier(response)
            
            # If the user is a patient
            else:
                
                # fetching the patient records
                patient = Patient.objects.get(emailHash = request.session['userEmail'])

                # Storing available doctors inside context variable
                context = {
                    "user" : patient
                    }
                
                # Editing response headers so as to ignore cached versions of pages
                response = render(request, "core/profile.html", context)
                return responseHeadersModifier(response)
            

def update_profile_picture(request):
    """Function to update profile picture."""

    if request.method == 'POST':

        if request.session['isDoctor']:
            user = Doctor.objects.get(emailHash=request.session['userEmail'])
        else:
            user = Patient.objects.get(emailHash=request.session['userEmail'])
        image = request.FILES.get('image')

        if image:

            # Delete old profile picture if it is not the default picture
            if user.image and user.image.url != '/media/profile_images/default.jpg':
                user.image.delete()
                user.image = image
                user.save()
                context = {
                    'message': 'Profile picture updated successfully!',
                    'user': user
                    }
                return render(request, 'core/profile.html', context)
            else:
                # If the user's profile picture is the default picture, just update it
                user.image = image
                user.save()
                context = {
                    'message': 'Profile picture updated successfully!',
                    'user': user
                    }
                return render(request, 'core/profile.html', context)
        else:
            context = {
                'user': user,
                'message': 'Please select an image to upload.'
                }
            return render(request, 'core/profile.html', context)
    else:
        return redirect('profile')

def delete_profile_picture(request):
    """Function to delete profile picture."""

    if request.method == 'POST':
        if request.session['isDoctor']:
            user = Doctor.objects.get(emailHash=request.session['userEmail'])
        else:
            user = Patient.objects.get(emailHash=request.session['userEmail'])

        # Check if the user's profile picture is the default picture
        if user.image.name == 'profile_images/default.jpg':
            context = {
                'user': user,
                'message': 'You have not uploaded any profile picture yet!'
                }
            return render(request, 'core/profile.html', context)
        else:
            user.image.delete(save=False)
            user.image = 'profile_images/default.jpg'
            user.save()
            context = {
                'user': user,
                'message': 'Profile picture deleted successfully!'
                }
            return render(request, 'core/profile.html', context)
    else:
        return redirect('profile')


class DoctorViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Doctors to be viewed or edited."""

    # Querying all the doctors
    queryset = Doctor.objects.all()
    # Serializing the data
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Patients to be viewed or edited."""

    # Querying all the patients
    queryset = Patient.objects.all()
    # Serializing the data
    serializer_class = PatientSerializer

class AssistanceViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows Assistances to be viewed or edited."""

    # Querying all the Assistances
    queryset = Assistance.objects.all()
    # Serializing the data
    serializer_class = AssistanceSerializer

def page_not_found(request, exception):
    """Function to display 404 error page."""

    # Editing response headers so as to ignore cached versions of pages
    response = render(request, "core/404.html")
    return responseHeadersModifier(response)
