from typing import List

'''
    take a function that recieve and input a list with strings and a distance and return if the input contains
    the list of of strings with less or equal between other phrases. 
'''

def check_distance(input: str, items: List[str], distance: int) -> bool:
    entries = input.split(' ');
    current_item = 0
    positions = []
    for i, entry in enumerate(entries):
        if (entry == items[current_item]):
            positions.append(i)
            if (len(positions) > 1 and positions[-1] - (positions[-2] + 1) > distance):
                break;
            current_item += 1

    if (len(items) > len(positions)):
        return False

    return True


print(check_distance('should i I take one two aspirine second i or i', ['i', 'take', 'aspirine', 'i', 'i'], 0)) # False

print(check_distance('should i I take one two aspirine second i or i', ['i', 'take', 'aspirine', 'i', 'i'], 2)) # True

print(check_distance('should i I take one two aspirine second second second i or i', ['i', 'take', 'aspirine', 'i', 'i'], 2)) # False

print(check_distance('should i I take one two aspirine second second second i or i', ['i', 'take', 'aspirine', 'i', 'i'], 5)) # True
