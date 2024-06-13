def quangan(year):
    check = False
    if year % 4 == 0 and year % 100 != 0:
        check = True
    elif year % 400 == 0:
        check = True

    return check


year = 2000


if quangan(year) == True:
    if year >= 2000:
        print("nam nhuan sau 1999")
else:
    print("k phai nhuan")

"""
Khai báo function/procedure:
def <tên=identifier> (parameter1):
    code
    return
"""
