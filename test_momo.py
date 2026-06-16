import pytest
import momo_wallet

from momo_wallet import (
    deposit,
    transfer,
    InvalidAmountError,
    InsufficientBalanceError
)


def setup_function():
    """
    Reset balance before each test.
    """
    momo_wallet.balance = 0


def test_deposit_success():
    """
    Test successful deposit.
    """
    deposit(500000)

    assert momo_wallet.balance == 500000


def test_transfer_insufficient_balance():
    """
    Test insufficient balance.
    """
    with pytest.raises(
        InsufficientBalanceError
    ):
        transfer(
            "0987654321",
            500000
        )


def test_invalid_amount():
    """
    Test invalid amount.
    """
    with pytest.raises(
        InvalidAmountError
    ):
        deposit(-1000)