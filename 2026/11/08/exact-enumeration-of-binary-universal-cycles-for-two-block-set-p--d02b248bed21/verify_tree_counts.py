#!/usr/bin/env python3
"""Exact directed Laplacian-tree computation for binary punctured de Bruijn graphs.

All arithmetic is integer; Bareiss elimination has exact divisions.
"""
def determinant_bareiss(matrix):
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    sign = 1
    prev = 1
    if n == 0:
        return 1
    for k in range(n-1):
        if a[k][k] == 0:
            other = next((i for i in range(k+1,n) if a[i][k] != 0), None)
            if other is None:
                return 0
            a[k],a[other]=a[other],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev == 0
                a[i][j] = numerator//prev
        for i in range(k+1,n):
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def tree_count(m):
    v = 1 << (m-1)
    lap = [[0]*v for _ in range(v)]
    for s in range(v):
        for b in (0,1):
            if (s,b)==(0,0):
                continue  # omit the zero self-loop
            t=((s<<1)|b)&(v-1)
            lap[s][s]+=1
            lap[s][t]-=1
    # Directed matrix-tree theorem, root at the zero state.
    return determinant_bareiss([row[1:] for row in lap[1:]])


def main():
    for m in range(2,7):
        measured=tree_count(m)
        predicted=1 << ((1 << (m-1))-m)
        assert measured==predicted,(m,measured,predicted)
        print(f'window_difference_length={m} tree_count={measured}')
    print('TREE_CERTIFICATE_OK')


if __name__ == '__main__':
    main()
