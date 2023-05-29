from django.test import Client, TestCase
from .models import Doctor, Patient, Assistance, passwordHasher, emailHasher

class DoctorsTestCase(TestCase):

    def setUp(self):
        """Function to initialize objects and things required during testing the
            methods of this class."""

        # Setting up test doctor instances and storing in test database
        email = "abcdefgh@gmail.com"
        passwordHash = passwordHasher("12345")
        emailHash = emailHasher(email)
        d1 = Doctor.objects.create(name = "Abcd Efgh", address = "Aaaa, Bbbbb, 110011", contactNumber = "8888888888", specialization = "ENT", email = email, passwordHash = passwordHash, emailHash = emailHash)

        email = "ijklmnop@gmail.com"
        passwordHash = passwordHasher("67890")
        emailHash = emailHasher(email)
        d2 = Doctor.objects.create(name = "Ijkl Mnop", address = "Cccc, Dddd, 001100", contactNumber = "9999999999", specialization = "EYE", email = email, passwordHash = passwordHash, emailHash = emailHash)

    def testDoctorCount(self):
        """Function to check the correct number of doctors stored in database."""

        # Getting all the doctors and then asserting their correct count
        doctors = Doctor.objects.all()
        self.assertEqual(doctors.count(), 2)

    def testDoctorDetails(self):
        """Function to check the if doctor details stored in database are correct."""

        # Getting all the doctors available
        doctors = Doctor.objects.all()

        # Confirming the details of the first doctor inserted as in setUp() method
        d1 = doctors[0]
        emailHash = emailHasher(d1.email)
        passwordHash = passwordHasher("12345")
        self.assertTrue(d1.name == "Abcd Efgh" and d1.address == "Aaaa, Bbbbb, 110011" and d1.contactNumber == "8888888888" and d1.specialization == "ENT" and d1.email == "abcdefgh@gmail.com" and d1.passwordHash == passwordHash and d1.emailHash == emailHash)

        # Confirming the details of the second doctor inserted as in setUp() method
        d2 = doctors[1]
        emailHash = emailHasher(d2.email)
        passwordHash = passwordHasher("67890")
        self.assertTrue(d2.name == "Ijkl Mnop" and d2.address == "Cccc, Dddd, 001100" and d2.contactNumber == "9999999999" and d2.specialization == "EYE" and d2.email == "ijklmnop@gmail.com" and d2.passwordHash == passwordHash and d2.emailHash == emailHash)

    def testDuplicatePasswordHashes(self):
        """Function to confirm that different passwords give different hashes. Otherwise hashing technique would be weak"""

        # Getting all the doctors from database
        doctors = Doctor.objects.all()

        # List to store password hashes
        passwordHashes = []

        # Appending password hashes to the list for each doctor
        for doctor in doctors:
            passwordHashes.append(doctor.passwordHash)

        # Using set to merge duplicate password hashes and then using list to access
        # the number of password hashes remaining after removing duplicates (if any)
        passwordHashes = set(passwordHashes)
        passwordHashes = list(passwordHashes)

        # Asserting that the number of password hashes are still 2 if hashing technique is strong
        self.assertEqual(len(passwordHashes), 2)

    def testDuplicateEmailHashes(self):
        """Function to confirm that different emails give different hashes. Otherwise hashing technique would be weak"""

        # Getting all the doctors from database
        doctors = Doctor.objects.all()

        # List to store email hashes
        emailHashes = []

        # Appending email hashes to the list for each doctor
        for doctor in doctors:
            emailHashes.append(doctor.emailHash)

        # Using set to merge duplicate email hashes and then using list to access
        # the number of email hashes remaining after removing duplicates (if any)
        emailHashes = set(emailHashes)
        emailHashes = list(emailHashes)

        # Asserting that the number of password hashes are still 2 if hashing technique is strong
        self.assertEqual(len(emailHashes), 2)

class PatientsTestCase(TestCase):

    def setUp(self):
        """Function to initialize objects and things required during testing the
            methods of this class."""

        # Setting up test patient instances and storing in test database
        email = "12345@gmail.com"
        passwordHash = passwordHasher("abcdefgh")
        emailHash = emailHasher(email)
        p1 = Patient.objects.create(name = "Abcd Efgh", address = "Aaaa, Bbbbb, 110011", contactNumber = "8888888888", userId = "B17CS101", email = email, passwordHash = passwordHash, emailHash = emailHash)

        email = "67890@gmail.com"
        passwordHash = passwordHasher("ijklmnop")
        emailHash = emailHasher(email)
        p2 = Patient.objects.create(name = "Ijkl Mnop", address = "Cccc, Dddd, 001100", contactNumber = "9999999999", userId = "B17CS102", email = email, passwordHash = passwordHash, emailHash = emailHash)

    def testPatientCount(self):
        """Function to check the correct number of patients stored in database."""

        # Getting all the patients and then asserting their correct count
        patients = Patient.objects.all()
        self.assertEqual(patients.count(), 2)

    def testPatientDetails(self):
        """Function to check the if patient details stored in database are correct."""

        # Getting all the patients available from database
        patients = Patient.objects.all()

        # Confirming the details of the first patient inserted as in setUp() method
        p1 = patients[0]
        emailHash = emailHasher(p1.email)
        passwordHash = passwordHasher("abcdefgh")
        self.assertTrue(p1.name == "Abcd Efgh" and p1.address == "Aaaa, Bbbbb, 110011" and p1.contactNumber == "8888888888" and p1.userId == "B17CS101" and p1.email == "12345@gmail.com" and p1.passwordHash == passwordHash and p1.emailHash == emailHash)

        # Confirming the details of the second patient inserted as in setUp() method
        p2 = patients[1]
        emailHash = emailHasher(p2.email)
        passwordHash = passwordHasher("ijklmnop")
        self.assertTrue(p2.name == "Ijkl Mnop" and p2.address == "Cccc, Dddd, 001100" and p2.contactNumber == "9999999999" and p2.userId == "B17CS102" and p2.email == "67890@gmail.com" and p2.passwordHash == passwordHash and p2.emailHash == emailHash)

    def testDuplicatePasswordHashes(self):
        """Function to confirm that different passwords give different hashes. Otherwise hashing technique would be weak"""

        # Getting all the patients from database
        patients = Patient.objects.all()

        # List to store password hashes
        passwordHashes = []

        # Appending password hashes to the list for each patient
        for patient in patients:
            passwordHashes.append(patient.passwordHash)

        # Using set to merge duplicate password hashes and then using list to access
        # the number of password hashes remaining after removing duplicates (if any)
        passwordHashes = set(passwordHashes)
        passwordHashes = list(passwordHashes)

        # Asserting that the number of password hashes are still 2 if hashing technique is strong
        self.assertEqual(len(passwordHashes), 2)

    def testDuplicateEmailHashes(self):
        """Function to confirm that different emails give different hashes. Otherwise hashing technique would be weak"""

        # Getting all the patients from database
        patients = Patient.objects.all()

        # List to store email hashes
        emailHashes = []

        # Appending email hashes to the list for each patient
        for patient in patients:
            emailHashes.append(patient.emailHash)

        # Using set to merge duplicate email hashes and then using list to access
        # the number of email hashes remaining after removing duplicates (if any)
        emailHashes = set(emailHashes)
        emailHashes = list(emailHashes)

        # Asserting that the number of password hashes are still 2 if hashing technique is strong
        self.assertEqual(len(emailHashes), 2)

class AssistancesTestCase(TestCase):

    def setUp(self):
        """Function to initialize objects and things required during testing the
            methods of this class."""

        # Setting up test doctor instances and storing in test database
        email = "abcdefgh@gmail.com"
        passwordHash = passwordHasher("12345")
        emailHash = emailHasher(email)
        d1 = Doctor.objects.create(name = "Abcd Efgh", address = "Aaaa, Bbbbb, 110011", contactNumber = "8888888888", specialization = "ENT", email = email, passwordHash = passwordHash, emailHash = emailHash)

        email = "ijklmnop@gmail.com"
        passwordHash = passwordHasher("67890")
        emailHash = emailHasher(email)
        d2 = Doctor.objects.create(name = "Ijkl Mnop", address = "Cccc, Dddd, 001100", contactNumber = "9999999999", specialization = "EYE", email = email, passwordHash = passwordHash, emailHash = emailHash)

        # Setting up test patient instances and storing in test database
        email = "12345@gmail.com"
        passwordHash = passwordHasher("abcdefgh")
        emailHash = emailHasher(email)
        p1 = Patient.objects.create(name = "Abcd Efgh", address = "Aaaa, Bbbbb, 110011", contactNumber = "8888888888", userId = "B17CS101", email = email, passwordHash = passwordHash, emailHash = emailHash)

        email = "67890@gmail.com"
        passwordHash = passwordHasher("ijklmnop")
        emailHash = emailHasher(email)
        p2 = Patient.objects.create(name = "Ijkl Mnop", address = "Cccc, Dddd, 001100", contactNumber = "9999999999", userId = "B17CS102", email = email, passwordHash = passwordHash, emailHash = emailHash)

        # Setting up test Assistance instances and storing in test database
        symptoms = "aaaaa bbbbb"
        Assistance1 = Assistance.objects.create(doctor = d1, patient = p1, symptoms = symptoms)

        symptoms = "ccccc ddddd"
        Assistance2 = Assistance.objects.create(doctor = d2, patient = p2, symptoms = symptoms)

    def testAssistanceCount(self):
        """Function to check the correct number of Assistances stored in database."""

        # Getting all the Assistances and then asserting their correct count
        assistances = Assistance.objects.all()
        self.assertEqual(assistances.count(), 2)

    def testIncompleteAssistance(self):
        """Function to check the status of incomplete Assistances. """

        # Getting all the Assistances
        assistances = Assistance.objects.all()

        # Asserting all the Assistances (which are incomplete)
        # to be new and not completed
        for assistance in assistances:
            self.assertTrue(assistance.isNew)
            self.assertFalse(assistance.isCompleted)

    def testCompleteAssistance(self):
        """Function to check the status of incomplete Assistances. """

        # Getting all the Assistances
        assistances = Assistance.objects.all()

        # Completing all the Assistances in the database as a doctor
        # would, setting the isNew property false and isCompleted true,
        # also setting their Assistance text
        for assistance in assistances:
            assistance.assistanceText = "Aaaaaa Bbbbbb Cccccc Dddddd"
            assistance.isNew = False
            assistance.isCompleted = True

        # Asserting all the attributes of the completed Assistances as required
        Assistance1 = assistances[0]
        self.assertTrue(Assistance1.doctor.id == Doctor.objects.get(email="abcdefgh@gmail.com").id and Assistance1.patient.id == Patient.objects.get(email = "12345@gmail.com").id and Assistance1.assistanceText == "Aaaaaa Bbbbbb Cccccc Dddddd")
        self.assertTrue(Assistance1.isCompleted)
        self.assertFalse(Assistance1.isNew)

        Assistance2 = assistances[1]
        self.assertTrue(Assistance2.doctor.id == Doctor.objects.get(email="ijklmnop@gmail.com").id and Assistance2.patient.id == Patient.objects.get(email = "67890@gmail.com").id and Assistance2.assistanceText == "Aaaaaa Bbbbbb Cccccc Dddddd")
        self.assertTrue(Assistance2.isCompleted)
        self.assertFalse(Assistance2.isNew)

def checkResponseHeaders(response):
    """Function for checking if the response headers are modified as required."""
    return response["Cache-Control"] == "no-cache, no-store, must-revalidate" and response["Pragma"] == "no-cache" and response["Expires"] == "0"

class ClientsInteractionTestCase(TestCase):

    def setUp(self):
        """Function to initialize objects and things required during testing the
            methods of this class."""

        # Initializing the doctors required during testing and saving into database
        email = "abcdefgh@gmail.com"
        passwordHash = passwordHasher("12345")
        emailHash = emailHasher(email)
        d1 = Doctor.objects.create(name = "Abcd Efgh", address = "Aaaa, Bbbbb, 110011", contactNumber = "8888888888", specialization = "ENT", email = email, passwordHash = passwordHash, emailHash = emailHash)

        email = "ijklmnop@gmail.com"
        passwordHash = passwordHasher("67890")
        emailHash = emailHasher(email)
        d2 = Doctor.objects.create(name = "Ijkl Mnop", address = "Cccc, Dddd, 001100", contactNumber = "9999999999", specialization = "EYE", email = email, passwordHash = passwordHash, emailHash = emailHash)

        # Initializing the patients required during testing and saving into database
        email = "12345@gmail.com"
        passwordHash = passwordHasher("abcdefgh")
        emailHash = emailHasher(email)
        p1 = Patient.objects.create(name = "Abcd Efgh", address = "Aaaa, Bbbbb, 110011", contactNumber = "8888888888", userId = "B17CS101", email = email, passwordHash = passwordHash, emailHash = emailHash)

        email = "67890@gmail.com"
        passwordHash = passwordHasher("ijklmnop")
        emailHash = emailHasher(email)
        p2 = Patient.objects.create(name = "Ijkl Mnop", address = "Cccc, Dddd, 001100", contactNumber = "9999999999", userId = "B17CS102", email = email, passwordHash = passwordHash, emailHash = emailHash)

        # Initializing the Assistances required during testing and saving into database
        symptoms = "aaaaa bbbbb"
        Assistance1 = Assistance.objects.create(doctor = d1, patient = p1, symptoms = symptoms)

        symptoms = "ccccc ddddd"
        Assistance2 = Assistance.objects.create(doctor = d2, patient = p2, symptoms = symptoms)

    def testValidIndexPage(self):
        """Function for testing the index page."""
        client = Client()

        # Requesting by GET method for page
        response = client.get("/")

        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/index.html', 'core/base.html')

    def testValidContactUsPage(self):
        """Function for testing the contact us page."""
        client = Client()

        # Requesting by GET method for page
        response = client.get("/contact")

        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/doctors.html', 'core/base.html')

    def testGetRegisterPage(self):
        """Function for testing the register page by GET method."""
        client = Client()

        # Requesting by GET method for page
        response = client.get("/register")
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/register.html', 'core/base.html')

    def testPostRegisterPage(self):
        """Function for testing the register page by POST method."""
        client = Client()

        # Requesting by POST method for page with correct input(matching passwords)
        response = client.post("/register", {"userFirstName" : "AA", "userLastName" : "BB", "userEmail" : "abcd@gmail.com", "userId" : "B99CS099", "userAddress" : "CC, DD", "userContactNo" : "9999999999", "userPassword" : "12345", "userConfirmPassword" : "12345"})
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/register.html', 'core/base.html')
        # Asserting successful registration in the message
        self.assertIn("Registration Successful", response.context["message"])

        # Requesting by POST method for page with incorrect input(passwords not matching)
        response = client.post("/register", {"userFirstName" : "AA", "userLastName" : "BB", "userEmail" : "abcde@gmail.com", "userId" : "c99CS099", "userAddress" : "CC, DD", "userContactNo" : "9999999999", "userPassword" : "12346", "userConfirmPassword" : "123456"})
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/register.html', 'core/base.html')
        # Asserting failure of registration(passwords do not match) in the message
        self.assertIn("Passwords do not match", response.context["message"])

    def testGetLoginPageWithNoSessionInfo(self):
        """Function for testing the login page by GET method."""
        client = Client()

        # Requesting by GET method for page
        response = client.get("/login")
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html', 'core/base.html')
        self.assertTrue(checkResponseHeaders(response))

    def testPostDoctorLoginPage(self):
        """Function for testing the login page by POST method for doctors."""
        client = Client()

        # Requesting by POST method for page with a user not existing in the database
        response = client.post("/login", {"useremail" : "notregisteredemail@gmail.com", "userpassword" : "123456"})
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/login.html', 'HealthCentre/base.html')
        # Asserting user does not exist in the message
        self.assertIn("User does not exist", response.context["message"])

        # Requesting by POST method for page with incorrect password
        response = client.post("/login", {"useremail" : "abcdefgh@gmail.com", "userpassword" : "assumewrongpassword"})
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/login.html', 'core/base.html')
        # Asserting invalid credentials in the message
        self.assertIn("Invalid Credentials.", response.context["message"])

        # Requesting by POST method for page with correct password
        response = client.post("/login", {"useremail" : "abcdefgh@gmail.com", "userpassword" : "12345"})
        # Asserting correct status code(of redirecting to other page) and response headers
        self.assertEqual(response.status_code, 302)
        self.assertTrue(checkResponseHeaders(response))
        # Asserting correct variable values in the session
        self.assertTrue(client.session["isLoggedIn"])
        self.assertTrue(client.session["isDoctor"])
        self.assertEqual(client.session["userEmail"], emailHasher("abcdefgh@gmail.com"))
        self.assertEqual(client.session["Name"], "Abcd Efgh")
        self.assertEqual(client.session["numberNewAssistances"], 1)

    def testGetDoctorLoginProfilePageWithSessionInfo(self):
        """Function for testing the login page once a doctor is already logged in previously
           and now a session is used to log him/her in with asking for credentials."""
        client = Client()

        # Logging in once with correct credentials by the POST method for the page
        client.post("/login", {"useremail" : "abcdefgh@gmail.com", "userpassword" : "12345"})
        # Requesting by GET method for login page after being logged in once already
        response = client.get("/login")
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/userDoctorRequestPortal.html', 'core/base.html')
        # Asserting correct variable values in the session
        self.assertTrue(client.session["isLoggedIn"])
        self.assertTrue(client.session["isDoctor"])
        self.assertEqual(client.session["userEmail"], emailHasher("abcdefgh@gmail.com"))
        self.assertEqual(client.session["Name"], "Abcd Efgh")
        self.assertEqual(client.session["numberNewAssistances"], 1)
        # Checking the Assistances in the doctor's history to ensure it is his account
        for Assistance in response.context["user"]:
            self.assertEqual(Assistance.doctor.email, "abcdefgh@gmail.com")

    def testPostPatientLoginPage(self):
        """Function for testing the login page by POST method for patients."""
        client = Client()

        # Requesting by POST method for page with a user not existing in the database
        response = client.post("/login", {"useremail" : "notregisteredemail@gmail.com", "userpassword" : "123456"})
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/login.html', 'core/base.html')
        # Asserting user does not exist in the message
        self.assertIn("User does not exist", response.context["message"])

        # Requesting by POST method for page with incorrect password
        response = client.post("/login", {"useremail" : "12345@gmail.com", "userpassword" : "assumewrongpassword"})
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/login.html', 'core/base.html')
        # Asserting invalid credentials in the message
        self.assertIn("Invalid Credentials.", response.context["message"])

        # Completing the Assistance in setUp() for checking patient history
        Assistance1 = Assistance.objects.get(patient = Patient.objects.get(email = "12345@gmail.com"))
        Assistance1.assistanceText = "XYZ Advice.. Complete"
        Assistance1.isCompleted = True
        Assistance1.save()

        # Requesting by POST method for page with correct password
        response = client.post("/login", {"useremail" : "12345@gmail.com", "userpassword" : "abcdefgh"})
        # Asserting correct status code(of redirecting to other page) and response headers
        self.assertEqual(response.status_code, 302)
        self.assertTrue(checkResponseHeaders(response))
        # Asserting correct variable values in the session
        self.assertTrue(client.session["isLoggedIn"])
        self.assertFalse(client.session["isDoctor"])
        self.assertEqual(client.session["userEmail"], emailHasher("12345@gmail.com"))
        self.assertEqual(client.session["Name"], "Abcd Efgh")
        self.assertEqual(client.session["numberNewAssistances"], 1)

    def testGetPatientLoginProfilePageWithSessionInfo(self):
        """Function for testing the login page once a patient is already logged in previously
           and now a session is used to log him/her in with asking for credentials."""
        client = Client()

        # Logging in once with correct credentials by the POST method for the page
        client.post("/login", {"useremail" : "12345@gmail.com", "userpassword" : "abcdefgh"})

        # Completing the Assistance in setUp() for checking patient history
        assistance1 = Assistance.objects.get(patient = Patient.objects.get(email = "12345@gmail.com"))
        assistance1.assistanceText = "XYZ Advice.. Complete"
        assistance1.isCompleted = True
        assistance1.save()

        # Requesting by GET method for login page after being logged in once already
        response = client.get("/login")
        # Asserting correct status code, response headers and templates
        self.assertEqual(response.status_code, 200)
        self.assertTrue(checkResponseHeaders(response))
        self.assertTemplateUsed(response, 'core/userPatientRequestPortal.html', 'core/base.html')
        # Asserting correct variable values in the session
        self.assertTrue(client.session["isLoggedIn"])
        self.assertFalse(client.session["isDoctor"])
        self.assertEqual(client.session["userEmail"], emailHasher("12345@gmail.com"))
        self.assertEqual(client.session["Name"], "Abcd Efgh")
        self.assertEqual(client.session["numberNewAssistances"], 1)
        # Checking the Assistances in the patient's history to ensure it is his account
        for assistance in response.context["user"]:
            self.assertEqual(assistance.patient.email, "12345@gmail.com")

    def testDoctorLogoutPage(self):
        """Function for testing the logout page for doctors."""
        client = Client()

        # Logging in once with correct credentials by the POST method for the login page
        client.post("/login", {"useremail" : "abcdefgh@gmail.com", "userpassword" : "12345"})
        # Using session to login again
        client.get("/login")
        # Requesting by POST method for logout page after being logged in once already
        response = client.get("/logout")
        # Asserting correct status code(of redirecting to other page) and response headers
        self.assertEqual(response.status_code, 302)
        self.assertTrue(checkResponseHeaders(response))
        # Asserting correct variable values in the session once logged out(all should be blank to convey no meaning)
        self.assertEqual(client.session["isDoctor"], "")
        self.assertFalse(client.session["isLoggedIn"])
        self.assertEqual(client.session["userEmail"], "")
        self.assertEqual(client.session["Name"], "")
        self.assertEqual(client.session["numberNewAssistances"], "")

    def testPatientLogoutPage(self):
        """Function for testing the logout page for patients."""
        client = Client()

        # Logging in once with correct credentials by the POST method for the login page
        client.post("/login", {"useremail" : "12345@gmail.com", "userpassword" : "abcdefgh"})
        # Using session to login again
        client.get("/login")
        # Requesting by POST method for logout page after being logged in once already
        response = client.get("/logout")
        # Asserting correct status code(of redirecting to other page) and response headers
        self.assertEqual(response.status_code, 302)
        self.assertTrue(checkResponseHeaders(response))
        # Asserting correct variable values in the session once logged out(all should be blank to convey no meaning)
        self.assertEqual(client.session["isDoctor"], "")
        self.assertFalse(client.session["isLoggedIn"])
        self.assertEqual(client.session["userEmail"], "")
        self.assertEqual(client.session["Name"], "")
        self.assertEqual(client.session["numberNewAssistances"], "")