# Enen

![Enen](https://img.shields.io/github/last-commit/bekalue/Enen)
![Django](https://img.shields.io/badge/Django-4.2.1-green)
![py](https://img.shields.io/badge/Python-3.11.3-yellowgreen)
![stat](https://img.shields.io/badge/status-up-green)

> The word `Enen` is a common and versatile expression in Amharic Language that is used to convey comfort, sympathy, or empathy. It is often used when someone is experiencing physical or emotional pain, and can be used to show that the speaker cares and wants to offer support.

> For example, if a child falls and scrapes their knee, a mother might say `enen` while comforting the child and tending to their injury. Similarly, if someone is upset or crying, a friend might say `enen` to show that they understand and want to offer support.

> The expression can also be used in other situations where someone is experiencing discomfort or distress. For example, if someone is feeling cold, a friend might offer them a blanket and say `enen` to show that they care and want to help.


## About The Project
__Enen__ is a simple web application that connects people with immediate virtual care for non-life-threatening illnesses and injuries. This app helps people avoid in-person doctor’s or clinic visits for minor health issues and questions that can easily be addressed via a one time Message or Phone calls. It connects users with remote physicians and doctors.

## Usage
### Windows Powershell
```powershell
git clone https://github.com/bekalue/Enen.git
cd Enen
.\env\Scripts\Activate.ps1                        (To activate virtual environment)
pip install -r requirements.txt
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
source env/Scripts/activate                        (To activate virtual environment)
cd enen
pip install django
pip install pycrypto
python3 manage.py runserver
```
To deactivate the virtual environment on Ubuntu, simply type:
```powershell
deactivate
```
## Technologies Used

- Django
- HTML/CSS
- Bootstrap
- SQLite
