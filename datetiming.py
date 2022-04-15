#! /usr/bin/env python
from datetime import datetime, timedelta
from traceback import print_exc

class DateTiming:
    def __init__(self):
        self.datetime = datetime.utcnow()

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = timedelta(seconds=other)

        if isinstance(other, timedelta):
            _datetiming = DateTiming()
            _datetiming.datetime = self.datetime + other
            return _datetiming
        else:
            raise Exception('Can only add number or timedelta!')

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = timedelta(seconds=other)

        if isinstance(other, DateTiming):
            other = other.datetime

        if isinstance(other, timedelta):
            _datetiming = DateTiming()
            _datetiming.datetime = self.datetime - other
            return _datetiming
        elif isinstance(other, datetime):
            return (self.datetime - other).total_seconds()
        else:
            raise Exception('Can only subtract number, timedelta, or datetime!')

    def __str__(self):
        return self.datetime.strftime('%m/%d/%Y %H:%M:%S.%f')

    def __repr__(self):
        return self.datetime.strftime('%m/%d/%Y %H:%M:%S.%f')

    def __getattr__(self, attribute):
        if attribute == 'datetime':
            return getattr(self, datetime)
        else:
            return getattr(self.datetime, attribute)

    def __setattr__(self, attribute, value):
        if attribute == 'datetime':
            self.__dict__[attribute] = value
        else:
            if attribute in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'tzinfo']:
                kwargs = {attribute: value}
                self.__dict__['datetime'] = self.__dict__['datetime'].replace(**kwargs)
            else:
                return setattr(self.datetime, attribute, value)
        return

def unit_test():
    def p(i, v):
        print('{0:<71} = {1}'.format(i, v))

    def t(i, b='-'):
        length = 100
        bar = b * length
        newline = '\n'
        split = length - len(i)
        front = split // 2
        back = split - front
        label = '{0}{1}{2}'.format(" " * front, i, " " * back)
        print('{0}{1}{2}{1}{0}'.format(bar, newline, label))

    t('UNIT TEST', b='=')

    t('start = new DateTiming()')
    start = DateTiming()
    p('start', start)

    t('subtract int')
    prev = start - 5
    p('prev', prev)

    t('add int')
    step = start + 5
    p('step', step)

    t('subtract DateTiming()')
    end = DateTiming()
    p('end', end)
    diff = end - start
    p('diff', diff)
    diff2 = DateTiming() - end
    p('diff2', diff2)

    t('getattr')
    new = DateTiming()
    p('new', new)
    p('new.year', new.year)
    p('new.month', new.month)
    p('new.day', new.day)
    p('new.hour', new.hour)
    p('new.minute', new.minute)
    p('new.second', new.second)
    p('new.microsecond', new.microsecond)

    t('setattr')
    new.microsecond = 0
    p('new.microsecond', new.microsecond)
    p('new', new)

    new.second = 0
    p('new.second', new.second)
    p('new', new)

    new.minute = 0
    p('new.minute', new.minute)
    p('new', new)

    new.hour = 0
    p('new.hour', new.hour)
    p('new', new)

    new.day = 1
    p('new.day', new.day)
    p('new', new)

    new.month = 1
    p('new.month', new.month)
    p('new', new)

    new.year = 1970
    p('new.year', new.year)
    p('new', new)

    t('AttributeError getattr')
    try:
        attempt = new.years
    except:
        print_exc()

    t('AttributeError setattr')
    try:
        new.seconds = 20
    except:
        print_exc()


    t('DONE!', b='=')

if __name__ == '__main__':
    unit_test()
