from abc import ABC, abstractmethod


class AccountInterface(ABC):
    #ACCOUNTS ARE CREATING AND DELETING AN ACCOUNT?
    @abstractmethod
    def accounts(self, number_one, number_two):
        pass

    # TRANSACTIONS ARE viewing accounts, transferring, deposits, withdrawing,etc.
    @abstractmethod
    def transactions(self, number_one, number_two):
        pass

    ###QUESTION WHERE DO I CREATE CUSTOMER INTERFACES DO THEY GO RIGHT HERE BELOW ACCOUNT INTERFACES PROBABLY??
    ## CALLED CREATE AND DELETE CUSTOMER put in dal test basics file
    ### @abstractmethod

class AccountImplementation(AccountInterface):

    @abstractmethod
    def accounts(self, number_one, number_two):
        pass

    @abstractmethod
    def transactions(self, number_one, number_two):
        pass

    # tests to make sure hey put in all seven digits of bank account number.#

    # only if need changed 0 to -1 so it could include 0 in an account
    # these methods should only work with integers: we don't want to mess with fractions or anything else
    # also, it should only work with positive numbers
    def addition(self, number_one, number_two):
        if isinstance(number_one, int) and isinstance(number_two, int):  # this line is checking the input types
            if number_one > -1 and number_two > 0:  # this line checks that we are working with positive numbers
                return number_one + number_two
            else:
                return "bad input: please only enter whole positive numbers"  # this is returned if we have a 0 or less input
        else:
            return "bad input: please only enter whole positive numbers"  # this returns if we have non integer data types





def

















   # MY EXAMPLES
   # @abstractmethod
    #def view_all_accounts(self, number_one, number_two):
     #   pass

    #@abstractmethod
    #def withdraw_specific_account_by_id(self, number_one, number_two):
       # pass

    #@abstractmethod
    #def deposit_into_specific_account_by_id(self, number_one, number_two):
      #  pass

    #@abstractmethod
    #def transfer_between_accounts_by_id(self, number_one, number_two):
    #    pass

    #@abstractmethod
   # def close_account_by_id(self, number_one, number_two):
      ###  pass

   # @abstractmethod
    #def remove_customer_by_id(self, number_one, number_two):
        #pass
















"