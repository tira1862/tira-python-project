from service_layer.bank_class_information import Bank

class BankDAOInterface(ABC):

    #Create

    @abstactmethod
    def create_bank(self, bank: Bank)-> Bank:
        pass
        # bank data that is needed

    # read
    @abstractmethod
    def get_bank_account_information_by_id(self, bank_id: int)-> Bank:
        # to get new bank info from database
        pass

    # update
    @abstractmethod
    def update_bank_account_by_id(self, bank: Bank)-> Bank:
        # updating bank data inside database
        pass

    # delete
    @abstractmethod
    def delete_bank_account_by_id(self, account_id: int)-> bool:
        # to remove bank acct data from database
        pass






