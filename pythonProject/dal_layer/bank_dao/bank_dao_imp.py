from bank_dao_interface import BankDAOInterface


class BankDAOImp(BankDAOInterface):


    def create_bank(self, bank: Bank) -> Bank:
        # Bank needs to be given an Id, and it needs to be added to the list
        bank.bank_id = self.id_generator  # this changes the bank's Id to whatever the id generator is set to
        self.id_generator += 1  # this ensures that the next team will have a newly generated Id
        self.banks_list.append(bank)  # this adds the new bank to my team database
        return bank  # this returns the bank object with its newly generated Id

    def get_bank_information_by_id(self, bank_id: int) -> Bank:
        for bank in self.banks_list:
            if bank.bank_id == bank_id:
                return bank
        raise IdNotFound("No bank matches the id given: Try again!")

    def update_bank_by_id(self, bank: Bank) -> Bank:
        for old_bank in self.bank_list:
            if bank.bank_id == old_bank.bank_id:
                old_bank = bank
                return old_bank
        raise IdNotFound("No bank matches the id given. Try again!")

    def delete_bank_by_id(self, bank_id: int) -> bool:
        for bank in self.banks_list:
            if bank.bank_id == bank_id:
                self.banks_list.remove(bank)
                return True
        raise IdNotFound("No team matches the id given: please try again!")



