from custom_exceptions.bad_account_info import BadaccountInfo
from dal_layer.account_dao.acount_dao_imp import AccountDAOImp
from service_layer.account_class_information import account
from service_layer.account_services.account_service_imp import AccountServiceImp

"""
Because I need to work with so many different ACCOUNTS that have some kind of bad data I have decided to pre-make these
objects in my code. This way I can call the specific object that I need for my test when necessary
"""

account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)
duplicate_account_name = Account(0, "Hillman Credit Union", "Phoenix") #is this from the biz rules?
duplicate_city_name = Account(0, "name is fine", "Providence") #changed
non_string_Account_name = Account(0, 10.7, "Dallas")
non_string_city_name = Account(0, "New York City", True)

duplicate_account_name_update = Account(1,"Hillman Credit Union","Phoenix)    #changed
duplicate_city_name_update = Account(1, "name is fine", "Providence")
non_string_account_name_update = Account(1, 10.7, "Dallas") #changed
non_string_city_name_update = Account(1, "New York City", True)

"""
ACCOUNTS may not have neg values
have to work with nos
must have unique ids

customers msut have unique ids
first and last names to not exceed 20 chars

I wonder if first_name and last_name <= 20 would work

from LECTURE:
create team tests
business logic:
    Teams may not have the same name
    Teams may not be located in the same city
    Teams may not have duplicate Ids (this is handled in the DAL)
    
    rules for project:
    
    no negative values
    work with numbers
    bank accounts and customer account must have unique ids
    first and last name not exceed 20 characters
        
"""

"""
In these tests I am trying to think of the different ways that my account data needs to be verified, and for each way
I am writing a test to ensure that my methods, when implemented, will actually perform the necessary validation on 
the data. In particular, these tests are making sure that my Business Rules are being followed, and that the correct
data types are being used for each part of the account data.
"""


def test_check_no_duplicate_accounts_create_account(): #rule must have unique ids
    try:
        account_service.service_create_account(duplicate_account_name)
        assert False
    except BadaccountInfo as e:
        assert str(e) == "This account name already exists in the database"


def test_check_no_negative_values_create_account(): # no neg values
    try:
        account_service.service_create_account():
        assert False # may need more code but this is a start such as 1 < x < 10
    except BadaccountInfo as e:
        assert str(e) == "Your account is insufficient to complete the transaction"


def test_catch_non_string_account_name_create_account(): # if someone tries to put in numbers instead of letters for a name
    try:
        account_service.service_create_account(non_string_account_name)
        assert False
    except BadaccountInfo as e:
        assert str(e) == "Please pass in a valid account name"


"""
account test
"""


def test_cant_typecast_to_int(): #I need to change this test
    try:
        account_service.service_get_account_information_by_id("one")
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid account Id"

def test_get_account_successfuly_typecast_string():
    result = account_service.service_get_account_information_by_id("1")
    assert result.account_id == 1


# string is successfully type casted into an int

"""
update team tests
"""



def test_catch_non_string_update_customer():
    try:
        account_service.service_update_account_by_id(non_string_account_name_update)
        assert False        # To handle putting in numbers instead of strings for customers
    except BadaccountInfo as e:
        assert str(e) == "Please enter in up to 20 letters only"


def test_catch_non_string_account_name_update_team():
    try:
        account_service.service_update_account_by_id(non_string_account_name_update)
        assert False
    except BadaccountInfo as e:
        assert str(e) == "Please pass in a valid account name"

def test_check_no_duplicate_names_update_account():
    try:
        account_service.account_dao.get_all_accounts_information = MagicMock(
            return_value=[Account(20, "Hillman Credit Union", "something")])
        account_service.service_update_account_by_id(duplicate_account_name_update)
        assert False
    except AccountTeamInfo as e:
        assert str(e) == "This account name already exists in the database"


def test_no_accounts_in_database():
    try:
        account_service.account_dao.get_all_accounts_information = MagicMock(result_value=[])
        account_service.service_update_account_by_id(duplicate_account_name_update)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "There are no accounts to update!"

"""
delete test #ok
"""


def test_catch_non_numeric_id_delete_account(): #ok
    try:
        account_service.service_delete_account_by_id("one")
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid account Id"

def test_pass_int_into_delete_method():
    account_service.account_dao.delete_account_by_id = MagicMock(return_value="just need to check int was used")
    account_service.service_delete_account_by_id("1")
    account_service.account_dao.delete_account_by_id.assert_called_with(1)