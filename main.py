import logging
logging.basicConfig(
    filename="momo_transactions.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y%m%d %H:%M:%S",
    encoding="utf-8",
    level=logging.DEBUG
)
balance = 0
def deposit (current_balance, deposit_amount):
    if deposit_amount <= 0 :
        raise ValueError("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
    current_balance+=deposit_amount
    logging.info(f"Deposit successful: +{deposit_amount} VND. Current Balance: {current_balance}")
    return current_balance

def transfer (user_phone,money_transfer,current_balance):
    if money_transfer <= 0 :
        raise ValueError ("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
    if current_balance < money_transfer :
        logging.error(f"InsufficientBalanceError: Attempted to transfer {money_transfer} VND with balance {current_balance} VND.")
        raise ValueError ("Giao dịch thất bại: Số dư của bạn không đủ.")
    if money_transfer >= 10000000:
        logging.warning(f"High value transaction detected: {current_balance} VND to {user_phone}.")

    current_balance -= money_transfer
    logging.info(f" Transfer successful: -{money_transfer} VND to {user_phone}. Current Balance: {current_balance}")
    return current_balance

while True:
    print(" VÍ MOMO GIẢ LẬP ".center(50, "="))
    print("1. Nạp tiền vào ví.")
    print("2. Chuyển tiền.")
    print("3. Xem số dư hiện tại.")
    print("4. Thoát chương trình.")
    choice = input("Nhập vào lựa chọn của bạn:")
    match choice :
        case "1":
            while True:
                try:
                    money_input= int(input("Nhập số tiền cần nạp:"))
                    
                    balance = deposit(balance,money_input)
                    print(f"Nạp tiền thành công: {money_input:,} VND")
                    
                    print(f"Số dư hiện tại {balance:,} VND")
                except ValueError as e:
                    if "lớn hơn 0" in str(e):
                        print(e)
                        logging.error(f"InvalidAmountError: Attempted to process {money_input} VND.")
                    else:
                        print("Vui lòng nhập số cho số tiền")
                        logging.error("ValueError: Invalid numeric input for deposit.")    
                else:
                    break
        case "2":
            phone = None
            while True:
                phone = input("Nhập vào số điện thoại:").strip()
                if len(phone) <10:
                    print("Số điện thoại phải có 10 chữ số.")
                    continue
                break
            while True:
                try:
                    money_transfer = int(input("Nhập vào số tiền:"))
                    balance = transfer(phone,money_transfer,balance)
                    
                    
                    print(f"Chuyển tiền thành công tới số điện thoại {phone}")
                    print(f"Số tiền đã chuyển: {money_transfer} VND")
                    print(f"Số dư còn lại: {balance} VND")
                except ValueError as e:
                    if "lớn hơn 0" in str(e):
                        print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                    elif "Số dư của bạn không đủ" in str(e):
                        print("Giao dịch thất bại: Số dư của bạn không đủ.")
                    else :
                        print("Phải nhập số.")
                else:
                    break
                
        case "3":
            print(f"Số dư hiện tại: {balance} VND ")
            logging.info(f"Balance checked. Current Balance: {balance}")
        case "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ")
            logging.info("System shutdown")
            break
    