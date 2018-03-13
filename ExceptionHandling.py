"""
Exceptions are errors
"""
import traceback

def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except Exception as e:
        print("In the except block", e)
        #traceback.print_exception()
        #raise Exception(e)
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally, always executed")

exceptionHandling()
