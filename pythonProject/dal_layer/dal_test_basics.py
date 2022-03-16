class CustomerInterface:
    #ACCOUNTS ARE CREATING AND DELETING AN ACCOUNT?
    @abstractmethod
    def customer(self, number_one, number_two):
        pass

#i wonder if i should add customer first name and last names
#and customer id to this part


class CustomerImplementaiton(CustomerInterface):
    @bstractmethod
def customer(self,first_name,last_name):
    pass

def customer_id(self, id):
    pass

class CustomerImplementation(CustomerInterface):
    @abstractmethod
    def customer(self, number_one, number_two):
        pass

## SERVICE LAYER-
#Bank accounts may not have a negative value
# Bank accounts must work with numbers
# Bank accounts must have unique Ids


#dal
# Customer first and last names may not exceed 20 characters
#Customers must have unique Ids



