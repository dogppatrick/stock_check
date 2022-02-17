import pandas as pd
import numpy as np
from random import randint

def random_cond():
    cond = [[True, False],[False,True],[False,False]]
    return cond[randint(0,2)]

def create_sample_data(fn='test_data.csv'):
    data = [[i] +random_cond() for i in range(7,7+30*2,2)]
    df = pd.DataFrame(data,columns=['idx','Buy', 'Sell'])
    df.to_csv(fn, index=False)

create_sample_data()
df = pd.read_csv("test_data.csv",index_col='idx')
data = np.array(df)
indexes = list(df.index)
L = len(data)
print(f'{L} data in test')
result_index = []
target_action = None
for i in range(L):
    buy, sell = data[i]
    idx = indexes[i]
    note = '*'
    if not buy and not sell:
        action = None
    else:
        # 不會有 buy , sell = True, True 的情況
        action = 'buy' if buy else 'sell'
    if not target_action and action:
        # 交易完成>>None
        target_action = 'buy' if action=='sell' else 'sell'
        tmp = idx
    elif target_action and target_action == action:
        target_action = None
        result_index.append(tmp)
        result_index.append(idx)
    else:
        note = ''
    log = f'index :{idx}, data:{data[i]}, action:{action} {note}'
    if action:
        print(log)
print(result_index)