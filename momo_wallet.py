"""
MoMo Wallet Simulation
"""

import logging


logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

balance = 0


class InvalidAmountError(Exception):
    """
    Raised when amount is less than or equal to 0.
    """


class InsufficientBalanceError(Exception):
    """
    Raised when balance is insufficient.
    """


def format_money(amount):
    """
    Format money with commas.
    """
    return f"{amount:,}"


def validate_amount(amount):
    """
    Validate transaction amount.
    """
    if amount <= 0:
        raise InvalidAmountError(
            f"Attempted to process {amount} VND."
        )


def deposit(amount):
    """
    Deposit money into wallet.
    """
    global balance

    validate_amount(amount)

    balance += amount

    logging.info(
        "Deposit successful: +%s VND. "
        "Current Balance: %s",
        amount,
        balance
    )

    return balance


def transfer(phone, amount):
    """
    Transfer money to another account.
    """
    global balance

    validate_amount(amount)

    if balance < amount:
        raise InsufficientBalanceError(
            f"Attempted to transfer {amount} VND "
            f"with balance {balance} VND."
        )

    if amount >= 10000000:
        logging.warning(
            "High value transaction detected: "
            "%s VND to %s",
            amount,
            phone
        )

    balance -= amount

    logging.info(
        "Transfer successful: -%s VND to %s. "
        "Current Balance: %s",
        amount,
        phone,
        balance
    )

    return balance


def is_valid_phone(phone):
    """
    Check phone number format.
    """
    return phone.isdigit() and len(phone) == 10


def handle_deposit():
    """
    Handle deposit process.
    """
    while True:
        try:
            print("\n--- NẠP TIỀN VÀO VÍ ---")

            amount = int(
                input("Nhập số tiền cần nạp: ")
            )

            deposit(amount)

            print(
                f"\nNạp tiền thành công: "
                f"+{format_money(amount)} VND"
            )

            print(
                f"Số dư hiện tại: "
                f"{format_money(balance)} VND"
            )

            break

        except ValueError:
            logging.error(
                "ValueError: Invalid numeric "
                "input for deposit."
            )

            print(
                "Lỗi: Vui lòng nhập số tiền hợp lệ."
            )

        except InvalidAmountError as error:
            logging.error(
                "InvalidAmountError: %s",
                error
            )

            print(
                "Lỗi: Số tiền giao dịch "
                "phải lớn hơn 0."
            )


def handle_transfer():
    """
    Handle transfer process.
    """
    try:
        print("\n--- CHUYỂN TIỀN ---")

        phone = input(
            "Nhập số điện thoại người nhận: "
        )

        if not is_valid_phone(phone):
            print(
                "Lỗi: Số điện thoại phải gồm "
                "đúng 10 chữ số."
            )
            return

        amount = int(
            input("Nhập số tiền cần chuyển: ")
        )

        transfer(phone, amount)

        print(
            f"\nChuyển tiền thành công tới "
            f"{phone}."
        )

        print(
            f"Số tiền đã chuyển: "
            f"{format_money(amount)} VND"
        )

        print(
            f"Số dư còn lại: "
            f"{format_money(balance)} VND"
        )

    except ValueError:
        logging.error(
            "ValueError: Invalid numeric "
            "input for transfer."
        )

        print(
            "Lỗi: Vui lòng nhập số tiền hợp lệ."
        )

    except InvalidAmountError as error:
        logging.error(
            "InvalidAmountError: %s",
            error
        )

        print(
            "Lỗi: Số tiền giao dịch "
            "phải lớn hơn 0."
        )

    except InsufficientBalanceError as error:
        logging.error(
            "InsufficientBalanceError: %s",
            error
        )

        print(
            "\nGiao dịch thất bại: "
            "Số dư của bạn không đủ."
        )

        print(
            f"Số dư hiện tại: "
            f"{format_money(balance)} VND"
        )


def show_balance():
    """
    Display current balance.
    """
    print("\n--- SỐ DƯ VÍ MOMO ---")

    print(
        f"Số dư hiện tại: "
        f"{format_money(balance)} VND"
    )

    logging.info(
        "Balance checked. "
        "Current Balance: %s",
        balance
    )


def show_transaction_history():
    """
    Display transaction history.
    """
    print("\n--- LỊCH SỬ GIAO DỊCH ---")

    try:
        with open(
            "momo_transactions.log",
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read().strip()

            if content:
                print(content)
            else:
                print(
                    "Chưa có lịch sử giao dịch "
                    "nào trong hệ thống."
                )

    except FileNotFoundError:
        print(
            "Chưa có lịch sử giao dịch "
            "nào trong hệ thống."
        )


def display_menu():
    """
    Display menu.
    """
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Xem lịch sử giao dịch")
    print("5. Thoát chương trình")
    print("=====================================")


def main():
    """
    Main program.
    """
    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":
            handle_deposit()

        elif choice == "2":
            handle_transfer()

        elif choice == "3":
            show_balance()

        elif choice == "4":
            show_transaction_history()

        elif choice == "5":
            logging.info("System shutdown")

            print(
                "\nCảm ơn bạn đã sử dụng dịch vụ."
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ."
            )


if __name__ == "__main__":
    main()