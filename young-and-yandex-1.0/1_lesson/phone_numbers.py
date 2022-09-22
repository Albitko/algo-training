phone_book = []
added_numer = input()

def unify_phone_number(phone_number: str) -> str:
    if phone_number[0] == "8":
        phone_number = phone_number[1:]
    elif phone_number[:2] == "+7":
        phone_number = phone_number[2:]
    
    phone_number = phone_number.replace("-", "")

    if phone_number[0] == "(" and phone_number[4] == ")":
        phone_number = phone_number[1:]
        phone_number = phone_number[:3] + phone_number[4:]

    if len(phone_number) == 7:
        phone_number = "495" + phone_number

    if len(phone_number) != 10 :
        return ""

    return phone_number
    
for i in range(3):
    phone_book.append(input())

for phone_number in phone_book:
    if unify_phone_number(added_numer) == unify_phone_number(phone_number):
        print("YES")
    else:
        print("NO")
