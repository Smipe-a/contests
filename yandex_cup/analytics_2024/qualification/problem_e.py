from collections import List


def search_logn(n: int, m: int, matrix: List[List[int]]):
    """
        Time Complexity: O(logn)
    """
    pass

def search_nm(n: int, m: int, matrix: List[List[int]]):
    """
        Time Complexity: O(n * m)
    """
    # 111111111
    # 110000011
    # 101000101
    # 100101001
    # 100010001
    # 100101001
    # 101000101
    # 110000011
    # 111111111
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(m)]

    def find_left(m, n, matrix):
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    return i, j

    def find_right(n, t, matrix):
        for i in range(n - 1, -1, -1):
            if matrix[t][i] == '1':
                return t, i

    def check_border(lui, luj, ruj, matrix):
        ldi = lui + (ruj - luj)
        for j in range(luj, ruj + 1):
            if matrix[lui][j] == '0' or matrix[ldi][j] == '0':
                print('Printing error')
                return False
        for i in range(lui, ldi + 1):
            if matrix[i][luj] == '0' or matrix[i][ruj] == '0':
                print('Printing error')
                return False
        return True

    def check_diagonal(lui, luj, ruj, matrix):
        length = ruj - luj - 1
        for lt in range(length):
            if matrix[lui + 1 + lt][luj + 1 + lt] == '0' or matrix[lui + 1 + lt][ruj - 1 - lt] == '0':
                print('Not marked')
                return False
        print('Marked')
        return True

    lui, luj = find_left(m, n, matrix)
    rui, ruj = find_right(n, lui, matrix)
    check = check_border(lui, luj, ruj, matrix)
    if check:
        check_diagonal(lui, luj, ruj, matrix)


if __name__ == '__main__':
    search_nm()
    #search_logn()
