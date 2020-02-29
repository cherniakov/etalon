
from .base import *

try:
    from .local import *
except ImportError:
    print("Отсутсвует модуль local. Создайте его из local.py.template")

