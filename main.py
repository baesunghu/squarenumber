import win32print
import win32api
import lib
a=lib.lib(1)
print(a.PrintAndChoicePrinters(2))


# win32api.ShellExecute(0, 'print', "test.pdf",
#                       f'/d:"{"Samsung M332x 382x 402x Series,Samsung M332x 382x 402x Series Class Driver"}"', '.', 0)
