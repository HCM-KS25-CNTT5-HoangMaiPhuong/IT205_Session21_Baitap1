import unittest

from wallet import (
    Wallet,
    InvalidAmountError,
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):

    def test_deposit_success(self):
        wallet = Wallet()

        wallet.deposit(500000)

        self.assertEqual(
            wallet.balance,
            500000
        )

    def test_transfer_insufficient_balance(self):
        wallet = Wallet()

        with self.assertRaises(
            InsufficientBalanceError
        ):
            wallet.transfer(
                "0987654321",
                500000
            )

    def test_invalid_amount(self):
        wallet = Wallet()

        with self.assertRaises(
            InvalidAmountError
        ):
            wallet.deposit(-100000)


if __name__ == "__main__":
    unittest.main()