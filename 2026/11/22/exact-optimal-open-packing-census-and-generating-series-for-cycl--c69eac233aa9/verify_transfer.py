#!/usr/bin/env python3
"""Independent transfer calculation of open packing optima on C_n square K_m.
No external dependencies. 0 represents an empty clique fibre, 1..m its selected vertex.
"""
from collections import defaultdict


def transfer_counts(n, m):
    assert n >= 5 and m >= 3
    alphabet = range(m + 1)
    allowed = [(u,v) for u in alphabet for v in alphabet if not(u and v and u != v)]
    result = defaultdict(int)
    for first, second in allowed:
        cur = {(first,second,int(first>0)+int(second>0)):1}
        for _ in range(2,n):
            nxt=defaultdict(int)
            for (a,b,wt),count in cur.items():
                for c in alphabet:
                    if (b and c and b!=c) or (a and c and a==c):
                        continue
                    nxt[(b,c,wt+int(c>0))]+=count
            cur=nxt
        for (before,last,wt),count in cur.items():
            if (last and first and last!=first): continue
            if (before and first and before==first): continue
            if (last and second and last==second): continue
            # The initial adjacent pair was tested when the loop began.
            result[wt]+=count
    return dict(result)


def formula(n,m):
    a=m-1
    k, r=divmod(n,3)
    if r==0:
        return 2*k, 3*(a**k+(-1)**k*a)
    if r==1:
        return 2*k, n*(a**k+a**(k-1)+(k*a**(k+1)+k*a*(-1)**(k-1))//2)
    return 2*k+1, n*a*(a**k-(-1)**k)

if __name__=='__main__':
    for m, end in ((3,23),(4,19),(5,15),(6,12)):
        for n in range(5,end+1):
            observed=transfer_counts(n,m)
            expected=formula(n,m)
            actual=(max(observed), observed[max(observed)])
            assert actual==expected, (m,n,actual,expected)
            print('PASS',m,n,actual[0],actual[1],sum(observed.values()))
    print('TRANSFER_VERIFIED')
