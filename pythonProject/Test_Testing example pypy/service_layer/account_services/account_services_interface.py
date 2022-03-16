
from abc import ABC, abstractmethod

from service_layer.account_class_information import Account

"""
This is the interface for the team service object. Inside the class I will define the different User Story operations
that we will need to implement. These methods will need to check and validate the data that is being passed into them
to ensure that all Business Rules and programming logic is being followed. If any Business Rules or programming logic
are not validated, the data must NOT be passed into the data access layer, and instead some sort of error message must
be returned
"""

class AccountServiceInterface(ABC):

    # create
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        """This method will validate the information is correct before passing it to the DAL"""
        pass

    # read
    @abstractmethod
    def service_get_account_information_by_id(self, account_id: str) -> Account:
        """This method will validate a correct identifier is being used before passing it to the DAL"""
        pass

    # update
    @abstractmethod
    def service_update_account_by_id(self, account: Account) -> Account:
        """This method will validate the information is correct before passing it to the DAL"""
        pass

    # delete
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        """This method will validate a correct identifier is being used before passing it to the DAL"""
        pass



















from abc import ABC, abstractmethos



#create
        @abstractMethod
        def create_account_withdrawal(self, t:T):
        pass

#read
        @abstractmethod
        def _account(self):

#update
        @abstractMethod
        def create_account_withdrawal(self, t:T):
        pass

#delete
        @abstractmethod
        def remove_account(self):