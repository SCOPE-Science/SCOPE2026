#!/usr/bin/env python3
"""Direct palindrome-prefix poset verification; standard library only."""
from itertools import product

def palindromes(q,n):
    for m in range(1,n+1):
        for a in product(range(q),repeat=(m+1)//2):
            yield a+a[-2::-1] if m%2 else a+a[::-1]

def direct(q,n):
    words=tuple(palindromes(q,n)); leaves=[]
    for w in words:
        if not any(len(z)>len(w) and z[:len(w)]==w for z in words):
            leaves.append(w)
    assert all(not (a!=b and len(a)<=len(b) and b[:len(a)]==a) for a in leaves for b in leaves)
    # Recurrence for maximum size of an antichain in the palindromic prefix-poset.
    def best(w):
        children=[z for z in words if len(z)>len(w) and z[:len(w)]==w and not any(len(w)<len(t)<len(z) and t[:len(w)]==w and z[:len(t)]==t for t in words)]
        return max(1,sum(best(z) for z in children))
    roots=[w for w in words if not any(len(z)<len(w) and w[:len(z)]==z for z in words)]
    assert sum(best(r) for r in roots)==len(leaves)
    return len(leaves)

if __name__=='__main__':
    expected={(2,1):2,(2,2):2,(2,3):4,(2,4):6,(2,5):10,(2,6):16,(2,7):26,(2,8):38,(2,9):62,(2,10):88,(2,11):140,(2,12):194,(3,1):3,(3,2):3,(3,3):9,(3,4):15,(3,5):33,(3,6):57,(3,7):123,(3,8):195,(3,9):411,(3,10):639,(4,3):16,(4,4):28,(4,5):76,(4,6):136,(4,7):364,(4,8):604}
    for (q,n),value in expected.items():
        got=direct(q,n)
        assert got==value,(q,n,got,value)
    print('Direct prefix-poset recurrence and leaf antichains: PASS for',len(expected),'cases')
