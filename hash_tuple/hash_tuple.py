#Read an integer indicating the number of elements, take space-separated integers as input, store them in a tuple, 
#and print the hash value of that tuple using Python’s built-in hash() function.

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print(hash(t))
