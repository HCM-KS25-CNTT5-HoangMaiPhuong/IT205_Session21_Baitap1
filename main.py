from wallet import (
    Wallet,
    InvalidAmountError,
    InsufficientBalanceError
)


def deposit_money(wallet):
    while True:
        try:
            print("\n--- NẠP TIỀN VÀO VÍ ---")

            amount = int(
                input("Nhập số tiền cần nạp: ")
            )

            wallet.deposit(amount)

            print(
                f"\nNạp tiền thành công: "
                f"+{amount:,} VND"
            )

            print(
                f"Số dư hiện tại: "
                f"{wallet.balance:,} VND"
            )

            break

        except ValueError:
            print(
                "Lỗi: Vui lòng nhập số tiền hợp lệ."
            )

        except InvalidAmountError:
            print(
                "Lỗi: Số tiền giao dịch "
                "phải lớn hơn 0."
            )
            break


def transfer_money(wallet):
    try:
        print("\n--- CHUYỂN TIỀN ---")

        phone = input(
            "Nhập số điện thoại người nhận: "
        ).strip()

        if not (
            phone.isdigit() and len(phone) == 10
        ):
            print(
                "Số điện thoại không hợp lệ."
            )
            return

        amount = int(
            input("Nhập số tiền cần chuyển: ")
        )

        wallet.transfer(phone, amount)

        print(
            f"\nChuyển tiền thành công tới "
            f"số điện thoại {phone}."
        )

        print(
            f"Số tiền đã chuyển: "
            f"{amount:,} VND"
        )

        print(
            f"Số dư còn lại: "
            f"{wallet.balance:,} VND"
        )

    except ValueError:
        print(
            "Lỗi: Vui lòng nhập số tiền hợp lệ."
        )

    except InvalidAmountError:
        print(
            "Lỗi: Số tiền giao dịch "
            "phải lớn hơn 0."
        )

    except InsufficientBalanceError:
        print(
            "\nGiao dịch thất bại: "
            "Số dư của bạn không đủ."
        )

        print(
            f"Số dư hiện tại: "
            f"{wallet.balance:,} VND"
        )


def show_balance(wallet):
    print("\n--- SỐ DƯ VÍ MOMO ---")

    print(
        f"Số dư hiện tại: "
        f"{wallet.get_balance():,} VND"
    )


def main():
    wallet = Wallet()

    while True:
        print("\n========== VÍ MOMO GIẢ LẬP ==========")
        print("1. Nạp tiền vào ví")
        print("2. Chuyển tiền")
        print("3. Xem số dư hiện tại")
        print("4. Thoát chương trình")
        print("===================================")

        choice = input(
            "Chọn chức năng (1-4): "
        ).strip()

        if choice == "1":
            deposit_money(wallet)

        elif choice == "2":
            transfer_money(wallet)

        elif choice == "3":
            show_balance(wallet)

        elif choice == "4":
            print(
                "Cảm ơn bạn đã sử dụng dịch vụ."
            )
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()