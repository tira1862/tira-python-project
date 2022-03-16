from abc import ABC, abstractmethod

from entities.account_class_information import Account

"""
This is the interface for the team service object. 
"""

class AccountServiceInterface(ABC):

    # create
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        """This method will validate the team information is correct before passing it to the DAL"""
        pass

    # read
    @abstractmethod
    def service_get_account_information_by_id(self, account_id: str) -> Account:
        """This method will validate a correct identifier is being used before passing it to the DAL"""
        pass

    # update
    @abstractmethod
    def service_update_account_by_id(self, account: Account) -> Account:
        """This method will validate the team information is correct before passing it to the DAL"""
        pass

    # delete
    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> bool:
        """This method will validate a correct identifier is being used before passing it to the DAL"""
        pass