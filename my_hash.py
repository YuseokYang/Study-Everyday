from typing import Any, Type

class ChainedHash:
    def __init__(self, length : int = 10) -> None:
        self.length = length
        self.hash_table = [[] for _ in range(self.length)]
    
    def _hashing(self, key : Any) -> int:
        self.hash_value = sum([ord(s) for s in str(key)])
        return self.hash_value % self.length
    
    def add(self, key: Any, value: Any) -> bool:
        index = self._hashing(key)
        for i, (k, v) in enumerate(self.hash_table[index]):
            if k == key:  # 기존 키가 있다면 값을 업데이트
                self.hash_table[index][i] = (key, value)
                return True
        self.hash_table[index].append((key, value))  # 새로운 키 추가
        return True
        
        
    def remove(self, key: Any) -> bool:
        index = self._hashing(key)
        if self.hash_table[index] is not None:
            for collision_idx, collision_values in enumerate(self.hash_table[index]):
                if key == collision_values[0]:
                    del self.hash_table[index][collision_idx]
                    return True
            return False
        return False
        
        
    def search(self, key : Any) -> Any:
        index = self._hashing(key)
        if self.hash_table[index] is not None:
            for collision_values in self.hash_table[index]:
                if key == collision_values[0]:
                    return collision_values[1]
            return False
        else:
            return False
        
    def dump(self) -> None:
        print(self.hash_table)








from enum import Enum

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])  # 메뉴를 선언

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <=  n <=  len(Menu):
            return Menu(n)

hash = ChainedHash(13)     # 크기가 13인 해시 테이블을 생성

while True:
    menu = select_menu()   # 메뉴 선택

    if menu == Menu.추가:  # 추가
        key = input('추가할 키를 입력하세요.: ')
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = input('삭제할 키를 입력하세요.: ')
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:  # 검색
        key = input('검색할 키를 입력하세요.: ')
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        hash.dump()

    else:  # 종료
        break