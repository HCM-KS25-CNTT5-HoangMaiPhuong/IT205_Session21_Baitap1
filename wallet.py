import logging


logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    """Raised when amount <= 0."""


class InsufficientBalanceError(Exception):
    """Raised when balance is insufficient."""


class Wallet:
    """MoMo wallet simulation."""

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        """Deposit money into wallet."""
        if amount <= 0:
            logging.error(
                f"InvalidAmountError: Attempted to process "
                f"{amount} VND."
            )
            raise InvalidAmountError

        self.balance += amount

        logging.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {self.balance}"
        )

    def transfer(self, phone, amount):
        """Transfer money to another account."""
        if amount <= 0:
            logging.error(
                f"InvalidAmountError: Attempted to process "
                f"{amount} VND."
            )
            raise InvalidAmountError

        if amount > self.balance:
            logging.error(
                f"InsufficientBalanceError: Attempted "
                f"to transfer {amount} VND with "
                f"balance {self.balance} VND."
            )
            raise InsufficientBalanceError

        if amount >= 10000000:
            logging.warning(
                f"High value transaction detected: "
                f"{amount} VND to {phone}"
            )

        self.balance -= amount

        logging.info(
            f"Transfer successful: -{amount} VND "
            f"to {phone}. Current Balance: "
            f"{self.balance}"
        )

    def get_balance(self):
        """Return current balance."""
        logging.info(
            f"Balance checked. Current Balance: "
            f"{self.balance}"
        )
        return self.balance