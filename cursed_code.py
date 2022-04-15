''' cursed_code.py - A library of utterly cursed code for everyday use.  Enjoy. '''

def isFalse(value: bool) -> bool:
    if not value:
        return value
    else:
        return False

def isTrue(value: bool) -> bool:
    def _isFalse(_value: bool) -> bool:
        if not _value:
            return _value
        else:
            return False
    return not _isFalse(value)

def add(a: int, b: int) -> int:
    from time import sleep, time
    start = time()
    sleep(a)
    sleep(b)
    return int(time() - start)

def multiply(a: int, b: int) -> int:
    from time import sleep, time
    start = time()
    for _ in range(a):
        sleep(b)
    return int(time() - start)

def isEven(number: int) -> bool:
    if not number % 2 == 0:
        raise Exception(f"{number} isn't even.")
    return True

def isOdd(number: int) -> bool:
    try:
        number = number / (number & 1)
        return True
    except:
        return False

def wait(waitTime: int):
    from datetime import datetime
    from time import sleep
    start = datetime.utcnow()
    while (datetime.utcnow() - start).total_seconds() < waitTime:
        sleep(1)

def wait_N(N: int):
    i = 0
    while i < N:
        i += 1

