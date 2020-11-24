import sys
import unicodedata


def Ini():

    sys.path.append("D:\testcode")


def Is_num(a):

    try:
        float(a)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(a)
        return True
    except (ValueError, TypeError):
        pass
    return False
