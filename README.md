# Enen

![Enen](https://img.shields.io/github/last-commit/bekalue/Enen)
![Django](https://img.shields.io/badge/Django-4.2.1-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.2.1-blueviolet)
![py](https://img.shields.io/badge/Python-3.11.3-yellowgreen)
![stat](https://img.shields.io/badge/status-up-green)

> Do you want to know why i named my project `Enen`?🤷🏽‍♂️ Well....

> The word `Enen` is a common and versatile expression in Amharic Language that is used to convey comfort, sympathy, or empathy. It is often used when someone is experiencing physical or emotional pain, and can be used to show that the speaker cares and wants to offer support.

> For example, if a child falls and scrapes their knee, a mother might say `enen` while comforting the child and tending to their injury. Similarly, if someone is upset or crying, a friend might say `enen` to show that they understand and want to offer support.

> The expression can also be used in other situations where someone is experiencing discomfort or distress. For example, if someone is feeling cold, a friend might offer them a blanket and say `enen` to show that they care and want to help.

<p align="center">
  <img src="assets/site.png" width="900" title="Home Page">
</p>

## About The Project 🤔
__Enen__ is a simple web application that connects people with immediate virtual care for non-life-threatening illnesses and injuries. This app helps people avoid in-person doctor’s or clinic visits for minor health issues and questions that can easily be addressed via a one time Message or Phone calls. It connects users with remote physicians and doctors, providing convenient and accessible healthcare from the comfort of their own homes..

## Live Site 🕸️
__Website Link__: [Enen](http://enen.bekalue.tech/)

## Key Features ⭐

- User authentication and registration
- Interface for interaction of Doctors and Users through the Request and Recieve Help portal
- User profile and Information
- History of Interaction between Doctor And User
- Show users for available Doctors And their Phone Numbers
- API routes that enables a web client to communicate with web server

## Technologies Used 💻

- Django
- HTML/CSS/Javascript
- Bootstrap
- SQLite

## Getting Started 💁🏽
### Windows Powershell
```powershell
git clone https://github.com/bekalue/Enen.git
cd Enen
.\env\bin\Activate.ps1                        (To activate virtual environment)
pip install -r requirements.txt               (To Install all The dependencies)
cd enen
py manage.py runserver
```
To deactivate the virtual environment on powershell, simply type:
```powershell
deactivate
```
### Linux Ubuntu 20.04.6 LTS
```shell
git clone https://github.com/bekalue/Enen.git
cd Enen
source ./env/bin/activate                        (To activate virtual environment)
cd enen
pip install django
pip install pycrypto
pip install -r requirements.txt
python3 manage.py runserver
```
To deactivate the virtual environment on Ubuntu, simply type:
```powershell
deactivate
```

## Architecture 📐✏️

### Data Model

Enen data model defines three classes: `Doctor`, `Patient`, and `Assistance`, which represent doctors, patients(registered users seeking medical attention), and assistance records, respectively. These classes are subclasses of Django's `Model` class and define the structure of the database tables that will store information about doctors, patients, and assistance records.

The `Doctor` class has several fields that store information about a doctor, including their name, address, contact number, email address, specialization, password hash, email hash, and profile image. 

The `Patient` class has similar fields to the `Doctor` class but also includes a `userId` field that stores a unique identifier for each patient or a registered user.

The `Assistance` class represents an assistance record and has fields for storing the assistance text, the doctor and patient associated with the record (represented as foreign keys), the timestamp of when the record was created, whether the record is new or not (represented as a boolean), whether the record is completed or not (represented as a boolean), and the symptoms or case associated with the record.

These classes define the structure of the database tables that will store information about doctors, patients, and assistance records in this a Django application.

<p align="center">
  <img src="assets/data_model.png" width="900" title="data model">
</p>

## Acknowledgement🫂
