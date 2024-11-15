from typing import Iterable

# 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(value: int) -> Iterable[int]:
    count: int = 1
    acc: int = 1
    prev: int = 0

    yield 1
    
    while count < value:
        new_value = prev + acc
        yield new_value
        prev = acc
        acc = new_value
        count += 1
        

print(list(fibonacci(8)))
    
