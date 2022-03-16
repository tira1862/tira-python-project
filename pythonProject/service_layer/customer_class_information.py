class Customer:

    def __init__(self, customer_id: int, first_name: str, last_name: str, customer_city: int):
        self.customer_id = customer_id # maybe this one should say account id instead?
        self.first_name = first_name
        self.last_name = last_name
        self.customer_city = customer_city #not sure if this one is necessary may need later for sql


    def convert_to_dictionary(self):
        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "second_name": self.last_name
            "customer_city": self.customer_city,
        }

