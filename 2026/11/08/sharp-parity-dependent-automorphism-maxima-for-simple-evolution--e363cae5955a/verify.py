#!/usr/bin/env python3
"""Exhaustive small binary structure matrices and orbit-type witness checks."""
import itertools, math

def determinant_nonzero(rows,n):
    # Row reduction over F_2.
    r=list(rows)
    for k in range(n):
        j=next((j for j in range(k,n) if (r[j]>>k)&1),None)
        if j is None: return False
        r[j],r[k]=r[k],r[j]
        for j in range(n):
            if j!=k and ((r[j]>>k)&1): r[j]^=r[k]
    return True

def strongly_connected(rows,n):
    def reach(start,transpose=False):
        seen=1<<start
        while True:
            nxt=seen
            for i in range(n):
                if (seen>>i)&1:
                    if transpose:
                        nxt|=sum(1<<j for j in range(n) if (rows[j]>>i)&1)
                    else:
                        nxt|=rows[i]
            if nxt==seen: break
            seen=nxt
        return seen==(1<<n)-1
    return reach(0) and reach(0,True)

def aut_order(rows,n):
    total=0
    for p in itertools.permutations(range(n)):
        if all(((rows[p[i]]>>p[j])&1)==((rows[i]>>j)&1)
               for i in range(n) for j in range(n)):
            total+=1
    return total

def full_symmetric(n):
    return tuple(((1<<n)-1)^(1<<i) for i in range(n))

def hub_leaves(n):
    return tuple([((1<<n)-1)]+[(1<<0)|(1<<i) for i in range(1,n)])

def directed_cycle(n):
    return tuple(1<<((i+1)%n) for i in range(n))

for n in range(1,5):
    maxaut=0; maxima=0; candidates=0
    for rows in itertools.product(range(1<<n),repeat=n):
        if not determinant_nonzero(rows,n) or not strongly_connected(rows,n): continue
        candidates+=1
        a=aut_order(rows,n)
        if a>maxaut: maxaut=a;maxima=1
        elif a==maxaut: maxima+=1
    expected= 1 if n==1 else (math.factorial(n) if n%2==0 else (3 if n==3 else math.factorial(n-1)))
    assert maxaut==expected,(n,maxaut,expected)
    print(f'EXHAUSTIVE n={n} simple_matrices={candidates} maximum={maxaut} maximizers={maxima}')

for n in [2,4,6,8]:
    A=full_symmetric(n)
    assert determinant_nonzero(A,n) and strongly_connected(A,n)
    assert aut_order(A,n)==math.factorial(n)
    print(f'EVEN_WITNESS n={n} order={math.factorial(n)}')

for n in [3,5,7]:
    A=hub_leaves(n)
    assert determinant_nonzero(A,n) and strongly_connected(A,n)
    assert aut_order(A,n)==math.factorial(n-1)
    print(f'ODD_WITNESS n={n} order={math.factorial(n-1)}')
A=directed_cycle(3)
assert determinant_nonzero(A,3) and strongly_connected(A,3) and aut_order(A,3)==3
print('EXCEPTION n=3 order=3')

# Binary rank and connectedness of all S_n invariant matrices for odd n <= 9.
for n in [3,5,7,9]:
    good=0
    for diag,offdiag in itertools.product((0,1),repeat=2):
        A=tuple(sum(1<<j for j in range(n) if (diag if i==j else offdiag)) for i in range(n))
        if determinant_nonzero(A,n) and strongly_connected(A,n): good+=1
    assert good==0
    print(f'ODD_FULL_SYMMETRY_OBSTRUCTION n={n} good={good}')
print('VERIFY_OK exhaustive_n=1..4; witness_n=2,3,4,5,6,7,8; odd_obstructions=3,5,7,9')
