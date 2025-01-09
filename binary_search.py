from typing import Any, Sequence

def binary_search(data:Sequence, key:Any) ->int:
    pl = 0
    pr = len(data)-1
    while True:
        
        pc = (pl+pr) // 2
        
        if key == data[pc]:
            return pc
        elif key > data[pc]:
            pl = pc + 1
        else:
            pr = pc-1
        
        if pl > pr:
            break
    raise ValueError




if __name__=='__main__':
    data_len = int(input('list 크기: '))
    
    data = [None]*data_len
    
    data[0] = int(input('data[0]: ' ))
    for value in range(1,data_len):
        while True:
            data[value] = int(input(f'data[{value}]: '))
            if data[value] >= data[value-1]:
                break
            
    print(f'data: {data}')
    
    key = int(input('찾고자 하는 값: '))
    
    try:
        idx = binary_search(data, key)
    except ValueError:
            print(f'찾고자하는 값 {key}가 존재하지 않음')
    else:
        print(f'찾고자하는 값 {key}는 x[{idx}]에 위치')
    
    