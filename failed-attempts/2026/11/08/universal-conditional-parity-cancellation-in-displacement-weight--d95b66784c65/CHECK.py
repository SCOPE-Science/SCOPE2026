#!/usr/bin/env python3
"""Finite exact verification of the parking-outcome parity factorization."""
from itertools import permutations, product
from math import comb


def hval(kernel, d):
    if kernel == 'uniform': return 1
    if kernel == 'unit': return int(d <= 1)
    if kernel == 'linear': return d + 1
    if kernel == 'geometric': return 2 ** d
    if kernel == 'restricted': return (1, 3, 0)[d] if d <= 2 else 0
    raise ValueError(kernel)


def F(kernel, ell):
    return sum(hval(kernel, d) for d in range(ell))


def outcome_weight(p, kernel):
    w = 1
    for i, x in enumerate(p):
        j = i - 1
        while j >= 0 and p[j] < x:
            j -= 1
        w *= F(kernel, i - j)
    return w


def parity(p):
    return -1 if sum(x > y for i, x in enumerate(p) for y in p[i+1:]) % 2 else 1


def qbin_minus_one(N, K):
    if N % 2 == 0 and K % 2 == 1:
        return 0
    return comb(N // 2, K // 2)


def recurrences(kernel, limit):
    T = [1]
    A = [1]
    rows = {}
    for n in range(1, limit + 1):
        signrow = []
        totalrow = []
        for k in range(1, n + 1):
            a, b = k - 1, n - k
            signrow.append(F(kernel, k) * (-1)**b * qbin_minus_one(n-1,a) * A[a] * A[b])
            totalrow.append(F(kernel, k) * comb(n-1, a) * T[a] * T[b])
        A.append(sum(signrow))
        T.append(sum(totalrow))
        rows[n] = (tuple(signrow), tuple(totalrow))
    return A, T, rows


def brute_permutations(kernel,n):
    sr=[0]*n;tr=[0]*n
    for p in permutations(range(1,n+1)):
        w=outcome_weight(p,kernel)
        k=p.index(n)
        sr[k]+=parity(p)*w
        tr[k]+=w
    return tuple(sr),tuple(tr)


def brute_preferences(kernel, n):
    sr=[0]*n; tr=[0]*n
    for prefs in product(range(1,n+1),repeat=n):
        free=set(range(1,n+1));pos=[0]*n
        w=1;valid=True
        for i,choice in enumerate(prefs):
            options=[x for x in free if x>=choice]
            if not options:
                valid=False;break
            spot=min(options);free.remove(spot)
            pos[i]=spot
            w*=hval(kernel,spot-choice)
        if not valid or not w:continue
        p=[0]*n
        for car,spot in enumerate(pos):p[spot-1]=car+1
        k=pos[-1]-1
        sr[k]+=w*parity(p);tr[k]+=w
    return tuple(sr),tuple(tr)


def main():
    checks=0
    for kernel in ('uniform','unit','linear','geometric','restricted'):
        A,T,rows=recurrences(kernel, 16)
        for n in range(1,9):
            b=brute_permutations(kernel,n)
            assert rows[n] == b, (kernel,n,rows[n],b)
            checks+=2*n
            if n <= 5:
                e=brute_preferences(kernel,n)
                assert e == b, (kernel,n,e,b)
                checks+=2*n
            if n % 2:
                assert all(rows[n][0][k-1]==0 for k in range(2,n+1,2))
                checks+=n//2
            assert rows[n][1]==tuple(F(kernel,k)*comb(n-1,k-1)*T[k-1]*T[n-k] for k in range(1,n+1))
            checks+=n
        assert all(T[n]>0 for n in range(17))
        checks+=17
    A,T,_=recurrences('uniform', 13)
    assert A[:10] == [1,1,1,4,11,72,335,2944,19449,211520]
    checks+=10
    assert T[1:10]==[(n+1)**(n-1) for n in range(1,10)]
    checks+=9
    assert recurrences('uniform',5)[2][5][0]==(11,0,6,0,55)
    checks+=5
    U, UT, _ = recurrences('unit', 16)
    fub=[1]
    for m in range(1,10):
        fub.append(sum(comb(m,j)*fub[m-j] for j in range(1,m+1)))
    for n in range(0,17):
        assert U[n]==fub[(n+1)//2], (n,U[n])
        checks+=1
    for n in range(1,10):
        assert UT[n]==fub[n]
        checks+=1
    print(f'VERIFY_OK {checks} exact assertions; kernels=5; permutation_orders<=8; direct_preference_orders<=5; recursion_orders<=16')

if __name__=='__main__':
    main()
