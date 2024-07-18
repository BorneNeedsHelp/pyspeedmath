import threading
from math import sqrt

class speedmath:
    @staticmethod
    def speedmath1(num, num2, Type):
        try:
            num = int(num)
            num2 = int(num2)
            Type = str(Type)
        except (ValueError, TypeError):
            raise ValueError("num, num2 needs to be int, Type needs to be str")
        if Type == "+":
            fanum = num + num2
            print(fanum)
        elif Type == "-":
            fsnum = num - num2
            print(fsnum)
        elif Type == "*":
            fmnum = num * num2
            print(fmnum)
        elif Type == "/":
            fdnum = num / num2
            print(fdnum)
        elif Type == "**":
            fenum = num ** num2
            print(fenum)
        elif Type == ">>":
            fbsnum = num >> num2
            print(fbsnum)
        elif Type == "<<":
            fbsnum2 = num << num2
            print(fbsnum2)
        elif Type == "///":
            fsqrtnum = sqrt(num)
            fsqrtnum2 = sqrt(num2)
            print(fsqrtnum, "  ", fsqrtnum2)
        else:
            raise TypeError("Type must be +, -, *, /, **, >>, <<, ///")

    @staticmethod
    def speedmath2(num3, num4, Type2):
        try:
            num3 = int(num3)
            num4 = int(num4)
            Type2 = str(Type2)
        except (ValueError, TypeError):
            raise ValueError("num, num2 needs to be int, Type needs to be str")
        if Type2 == "+":
            fanum2 = num3 + num4
            print(fanum2)
        elif Type2 == "-":
            fsnum2 = num3 - num4
            print(fsnum2)
        elif Type2 == "*":
            fmnum2 = num3 * num24
            print(fmnum2)
        elif Type2 == "/":
            fdnum2 = num3 / num4
            print(fdnum2)
        elif Type2 == "**":
            fenum2 = num3 ** num4
            print(fenum2)
        elif Type2 == ">>":
            fbsnum3 = num3 >> num4
            print(fbsnum3)
        elif Type2 == "<<":
            fbsnum4 = num << num2
            print(fbsnum4)
        elif Type2 == "///":
            fsqrtnum3 = sqrt(num3)
            fsqrtnum4 = sqrt(num4)
            print(fsqrtnum3, "  ", fsqrtnum4)
        else:
            raise TypeError("Type must be +, -, *, /, **, >>, <<, ///")

    @staticmethod
    def speedmath3(num5, num6, Type3):
        try:
            num5 = int(num5)
            num6 = int(num6)
            Type3 = str(Type3)
        except (ValueError, TypeError):
            raise ValueError("num, num2 needs to be int, Type needs to be str")
        if Type3 == "+":
            fanum3 = num5 + num6
            print(fanum3)
        elif Type3 == "-":
            fsnum3 = num5 - num6
            print(fsnum3)
        elif Type3 == "*":
            fmnum3 = num5 * num26
            print(fmnum3)
        elif Type3 == "/":
            fdnum3 = num5 / num26
            print(fdnum3)
        elif Type3 == "**":
            fenum3 = num5 ** num6
            print(fenum3)
        elif Type3 == ">>":
            fbsnum5 = num5 >> num6
            print(fbsnum5)
        elif Type3 == "<<":
            fbsnum6 = num5 << num6
            print(fbsnum6)
        elif Type3 == "///":
            fsqrtnum5 = sqrt(num5)
            fsqrtnum6 = sqrt(num6)
            print(fsqrtnum5, "  ", fsqrtnum6)
        else:
            raise TypeError("Type must be +, -, *, /, **, >>, <<, ///")

    @staticmethod
    def START(inum, inum2, inum3, inum4, inum5, inum6, iType, iType2, iType3):
        t1 = threading.Thread(target=speedmath.speedmath1, args=(inum, inum2, iType))
        t2 = threading.Thread(target=speedmath.speedmath2, args=(inum3, inum4, iType2))
        t3 = threading.Thread(target=speedmath.speedmath3, args=(inum5, inum6, iType3))

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

    @staticmethod
    def speedmath_Help():
        with open("HELPFILE", 'w+') as f:
            f.read()

if __name__ == "__main__":
    try:
        inum = int(input("Num:"))
        inum2 = int(input("Num2:"))
        inum3 = int(input("Num3:"))
        inum4 = int(input("Num4:"))
        inum5 = int(input("Num5:"))
        inum6 = int(input("Num6:"))
        itype = input("Type:")
        itype2 = input("Type2:")
        itype3 = input("Type3:")
    except (ValueError, TypeError):
        raise TypeError("num, num2, num3, num4, num5, num6 needs to be an int, Type, Type2, Type3 needs to be a str")
    else:
        START(inum, inum2, inum3, inum4, inum5, inum6, itype, itype2, itype3)
