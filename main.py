import pandas as pd
import numpy as np
from tabulate import tabulate

def add_item(item_name, item_amount, item_price):
    item_name = str(input("Mohon masukkan barang yang ingin dibeli: "))
    item_amount = int(input("Mohon masukkan jumlah barang yang ingin dibeli: "))
    item_price = int(input("Mohon masukkan harga dari barang yang dibeli: "))
    print(tabulate(item_name,item_amount,item_price))
    
add_item("handphone",2,5000000)