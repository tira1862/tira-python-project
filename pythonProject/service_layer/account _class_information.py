class Account:

    def __init__(self, bank_id: int, bank_name: str, home_city: str):

        self.bank_id = bank_id
        self.bank_name = bank_name
        self.home_city = home_city


    def convert_to_dictionary(self):
        return {
            "bank_id": self.bank_id,
            "bank_name": self.bank_name,
            "home_city": self.home,
        }











