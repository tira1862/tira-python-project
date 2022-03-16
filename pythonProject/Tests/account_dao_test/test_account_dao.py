"""This module contains account dao unit tests"""
from unittest.mock import MagicMock, patch

from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_dao_postgres import AccountDAOImpPostgres
from entities.account_class_information import Account

account_dao = AccountDAOImpPostgres()  # I will be using this account dao object for all my account dao tests.

"""

The tests in this module were crafted to check two things:
1. when the correct data is provided to the method, the method returns the expected return value

2. when the data you want to work with does not exist, a message indicating it does not exist should be returned
"""

def test_create_account_success():
    test_account = Account(0, "Hillman Credit Union", "Phoenix")
    result = account_dao.create_account(test_account)
    print(result.account_id)
    assert result.account_id != 0


def test_catch_non_unique_id():
    #test give so no setting the id manually
    test_account = Account(1, "Providence Bank", "San Diego.")
    result = account_dao.create_account(test_account)
    assert result.account_id != 1


"""
get account tests
"""


def test_get_account_info_by_id_success():
    result = account_dao.get_account_information_by_id(1)
    assert result.account_id == 1


def test_get_account_using_non_existant_id():
    try:
        account_dao.get_bank_information_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


"""
update bank tests
"""


def test_update_account_by_id_success():
    new_bank_name = Account(1, "Allegiant Bank", "Deer Park")
    result = Account_dao.update_account_by_id(new_account_name)
    assert result.account_name == "Allegiant Bank"


def test_update_account_using_non_existant_id():
    try:
        new_account_name = Account(0, "Allegiant Bank", "Deer Park")
        account_dao.update_account_by_id(new_account_name)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


"""
delete bank tests
"""


def test_delete_account_by_id_success():
    result = account_dao.delete_account_by_id(1)
    assert result


def test_delete_account_with_non_existant_id():
    try:
        account_dao.delete_account_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No account matches the id given: please try again!"


def test_get_all_accounts_success(): # iam wondering if this is the one for no Negative values but it seems like it would say 0
    result = account_dao.get_all_accounts_information()
    assert len(result) >= 1


@patch("dal_layer.account_dao.account_dao_postgres.AccountDAOImpPostgres.get_all_accounts_information")
def test_no_accounts_found(mock):
    """this is not actually testing my method, just raising an exception and catching it in the except block"""
    try:
        mock.side_effect = BadAccountInfo("No accounts were found")
        account_dao.get_all_accounts_information()
        assert False
    except BadAccountInfo as e:
        assert str(e) == "No accounts were found"