
# Test Interview

We as a loyalty provider, has Programs, which represent specific cashback programs that run on our 
infrastructure; and has Banks which provide the transactions to redeem in the cashback programs.

## code setup


To start this project run

To create virtual environment
```bash
  python3 -m venv venv
  venv\Scripts\activate.bat
```
Installing required libraries
```bash
  pip install -r requirements.txt
```
To migrate
```bash
  python manage.py makemigrations
  python manage.py migrate
```
To run server
```bash
  python manage.py runserver
```

## To access the API's
Bank =>http://localhost:8000/api/v1/banks/

    POST : {
      name: "Name",
      countries: "[countries]"
    }

Program =>http://localhost:8000/api/v1/programs/
    
    POST : {
      name: "Name",
      currency: "currency",
      return_percentage: 0.0
    }

Transactions =>http://localhost:8000/api/v1/transactions/

    POST : {
      bank: "bank_obj",
      currency: "program_obj",
      countries: "countries",
      currency: "currency"
    }


    
## Required Validations in transictions

* It checks country with its currency.
* It checks whether the country is valid or not.
* It checks whether the currency is valid or not. 