import my_module
import my_module as mm
from my_module import *

if __name__ == '__main__':
    append_item("Happy")
    append_item("Angry")
    append_item("Sad")
    append_item("Cry")
    append_item("Danger")
    print(get_datas())
    print(get_data(3))