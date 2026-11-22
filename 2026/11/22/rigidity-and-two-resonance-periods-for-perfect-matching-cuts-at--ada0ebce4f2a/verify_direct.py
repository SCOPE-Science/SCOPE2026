#!/usr/bin/env python3
"""Independent direct graph-neighborhood verification of the four formulas.
Enumerates cyclic outer transitions and checks all six neighbors per column.
"""

def words(n):
    # Enumerate independent cyclic subsets of the outer rim's n edges,
    # with an even number of boundary transitions (closure of a coloring).
    def rec(i,first,prev,m,c):
        if i==n:
            if prev and first:return
            if c%2==0:yield m
            return
        for bit in (0,1):
            if bit and prev:continue
            if i==n-1 and bit and first:continue
            yield from rec(i+1,first if i else bit,bit,m|(bit<<i),c+bit)
    yield from rec(0,0,0,0,0)

def direct(k,n):
    count=0
    for mask in words(n):
        t=[(mask>>i)&1 for i in range(n)]
        a=[0]*n
        for i in range(1,n):a[i]=a[i-1]^t[i-1]
        d=[1-t[i-1]-t[i] for i in range(n)]
        b=[a[i]^d[i] for i in range(n)]
        if all((a[i]!=a[(i-1)%n])+(a[i]!=a[(i+1)%n])+(a[i]!=b[i])==1 and
               (b[i]!=b[(i-k)%n])+(b[i]!=b[(i+k)%n])+(b[i]!=a[i])==1
               for i in range(n)):
            count+=1
    return count

def formula(k,n):
    return 1+(2 if k%2 and n%4==0 else 0)+(5 if k==7 and n%5==0 else 0)

if __name__=='__main__':
    for k in range(4,8):
        v=[]
        for n in range(2*k+1,25):
            actual=direct(k,n);expected=formula(k,n)
            assert actual==expected,(k,n,actual,expected)
            if actual>1:v.append((n,actual))
        print(f'k={k} tested_n=[{2*k+1},24] exceptional_counts={v}')
    print('PASS: direct full-graph predicate agrees with all four formulas.')
