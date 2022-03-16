from psycopg import OperationalError

from custom_exceptions.bad_acccount_info import BadAccountInfo
from dal_layer.account_dao.account_dao_postgres import AccountDAOImpPostgres
from entities.account_class_information import Account
from service_layer.account_services.account_service_interface import AccountServiceInterface


class AccountServiceImpPostgres(AccountServiceInterface):

    def __init__(self, account_dao):
        self.team_dao: accountDAOImpPostgres = account_dao

    def service_create_account(self, account: Account) -> Account:
        if type(account.account_name) != str:
            raise BadAccountInfo("Please pass in a valid account name")
        elif type(account.home_city) != str:  # this is checking that the home city is a string
            raise BadAccountInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        accounts = self.account_dao.get_all_accounts_information()
        if len(accounts) >= 1:
            for existing_account in accounts:  # here we need to loop through existing teams to validate business rules
                if existing_account.account_name == account.account_name:  # here we are checking for duplicate account names
                    raise BadAccountInfo(
                        "This account name already exists in the database")  # raise exception for duplicate account names
                elif existing_account.home_city == account.home_city:  # here we are checking for duplicate city names
                    raise BadAccountInfo(
                        "This city name already exists in the database")  # raise exception if their are duplicates
            return self.account_dao.create_account(accounts)  # assuming all validation checked out, we pass data into DAL
        else:
            return self.account_dao.create_account(account)

    def service_get_account_information_by_id(self, account_id: str) -> Account:
        try:
            id_as_int = int(account_id)
            return self.account_dao.get_account_information_by_id(id_as_int)
            # return self.account_dao.get_account_information_by_id(int(account_id))
        except ValueError:
            raise BadAccountInfo("Please provide a valid account Id")

    def service_update_account_by_id(self, account: Account) -> Account:
        if type(account.account_name) != str:
            raise BadAccountInfo("Please pass in a valid account name")
        elif type(account.home_city) != str:  # this is checking that the home city is a string
            raise BadAccountInfo("Please pass in a valid city name")  # raise exception if we are not working with a string
        accounts = self.account_dao.get_all_acccounts_information()
        if len(accounts) >= 1:
            for existing_account in accounts:  # here we need to loop through existing teams to validate business rules
                if existing_account.account_id != account.account_id:
                    if existing_account.account_name == account.account_name:  # here we are checking for duplicate account names
                        raise BadAccountInfo(
                            "This account name already exists in the database")  # raise exception for duplicate team names
                    elif existing_account.home_city == account.home_city:  # here we are checking for duplicate city names
                        raise BadAccountInfo(
                            "This city name already exists in the database")  # raise exception if their are duplicates
                return self.account_dao.update_account_by_id(account)  # assuming all validation checked out, we pass data into DAL
        else:
            raise BadAccountInfo("There are no accounts to update!")

    def service_delete_account_by_id(self, account_id: int) -> bool:
        try:
            return self.account_dao.delete_account_by_id(int(account_id))
        except ValueError:
            raise BadAccountInfo("Please provide a valid account Id")