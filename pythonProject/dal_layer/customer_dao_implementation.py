from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from service_layer.customer_class_information import Customer


class CustomerDAOImp(CustomerDAOInterface):
    customer_list = [Customer(1, 1, "Micheal", "Williams", 22)]
    id_generator = 2

    # Create
    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.id_generator
        self.id_generator += 1
        self.customer_list.append(customer)
        return customer

    # Read
    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                return customer
        raise IdNotFound("No customer matches the id given: please try again!")

    # Update
    def update_customer_by_id(self, customer: Customer) -> Customer:
        for old_customer in self.customer_list:
            if old_customer.customer_id == customer.player_id:
                old_player = customer
                return old_customer
        raise IdNotFound("No customer matches the id given: please try again!")

    # Delete
    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                self.customer_list.remove(customer)
                return True
        raise IdNotFound("No customer matches the id given: please try again!")

