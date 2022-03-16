from custom_exceptions.bad_account_info import BadAccountInfo
from dal_layer.account_dao.account_dao_interface import AccountDAOInterface
from entities.team_class_information import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface

"""
This module implements the Team service interface. Here is where we define HOW the data being worked with is validated,
and we define what needs to happen if the data is NOT validated. This could be because the data type provided is wrong,
Business Rules are not being adhered to, or any other reason why the data should not be passed into the Data Access 
Layer.
Another thing to note is that it is ok if there is overlap in the names of the different methods between the service
layer and the data access layer, but the ideal is that your method names in your service layer should reflect the
particular user story that they are meant to implement.
"""

class AccountServiceImp(AccountServiceInterface):

    def __init__(self, account_dao: AccountDAOInterface):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        if type(account.account_name) != str:  # this is checking that the account name is a string
            raise BadAccountInfo("Please pass in a valid account name")  # raise exception if we are not working with a string
        elif type(account.home_city) != str:  # this is checking that the home city is a string
            raise BadAccountInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        for existing_account in self.account_dao.accounts_list:  # here we need to loop through existing teams to validate business rules
            if existing_account.account_name == account.account_name:  # here we are checking for duplicate team names
                raise BadAccountInfo(
                    "This name already exists in the database")  # raise exception for duplicate account names
            elif existing_account.home_city == account.home_city:  # here we are checking for duplicate city names
                raise BadAccountInfo(
                    "This city name already exists in the database")  # raise exception if there are duplicates
        return self.account_dao.create_account(account)  # assuming all validation checked out, we pass data into DAL

    def service_get_account_information_by_id(self, account_id: str) -> Account:
        try:
            return self.account_dao.get_account_information_by_id(int(account_id))
        except ValueError:
            raise BadAccountInfo("Please provide a valid account Id")

    def service_update_account_by_id(self, account: Account) -> Account:
        if type(account.account_name) != str:  # this is checking that the account name is a string
            raise BadAccountInfo("Please pass in a valid account name")  # raise exception if we are not working with a string
        elif type(account.home_city) != str:  # this is checking that the home city is a string
            raise BadAccountInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        for existing_account in self.account_dao.account_list:  # here we need to loop through existing account to validate business rules
            if existing_account.account_name == account.account_name:  # here we are checking for duplicate account names
                raise BadAccountInfo("This account name already exists in the database")  # raise exception for duplicate account names
            elif existing_account.home_city == account.home_city:  # here we are checking for duplicate city names
                raise BadAccountInfo("This city name already exists in the database")  # raise exception if their are duplicates
        return self.account_dao.update_account_by_id(account)  # assuming all validation checked out, we pass data into DAL

    def service_delete_account_by_id(self, account_id: int) -> bool:
        if type(account_id) == int:
            return self.account_dao.delete_account_by_id(account_id)
        else:
            raise BadAccountInfo("Please provide a valid account Id")