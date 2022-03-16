from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from service_layer.customer_class_information import Customer

customer_dao = CustomerDAOImp()

"""
create tests
business logic:
    Customers may not have the same Id ( this will be handled in the service layer )
"""


def test_create_customer_success():
    test_customer = Customer(0,1,"New","Customer",10)
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0


def test_catch_non_unique_id():
    """check that providing an ID does not ruin the method"""
    test_customer = Customer(1,1,"Bad","Id",0)
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 1


"""
get tests
"""


def test_get_customer_info_by_id_success():
    result = customer_dao.get_customer_by_id(1)
    assert result.customer_id == 1


def test_get_customer_using_non_existant_id():
    try:
        customer_dao.get_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"


"""
update tests
"""


def test_update_customer_by_id_success():
    new_customer_name = Customer(1,1, "Minnie", "Orlando", 50)
    result = customer_dao.update_customer_by_id(new_customer_name)
    assert result.first_name == "Minnie"


def test_update_customer_using_non_existant_id():
    try:
        new_customer_name = Customer(0,1, "David", "Topeka",50)
        customer_dao.update_customer_by_id(new_customer_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"


"""
delete tests
"""


def test_delete_customer_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result


def test_delete_customer_with_non_existant_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"