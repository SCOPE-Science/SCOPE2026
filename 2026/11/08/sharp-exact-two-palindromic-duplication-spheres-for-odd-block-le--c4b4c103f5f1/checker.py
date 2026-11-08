"""Finite checks for the exact-two high-alphabet palindromic-duplication theorem.
Python 3 stdlib only. This is corroboration; the uniform proof is in RESULT.md.
"""
from collections import defaultdict
from itertools import product
from math import comb

def pal(word, k, i):
    return word[:i+k]+word[i:i+k][::-1]+word[i+k:]

def promised(n,k):
    return (n-k+1)*(n+1)-comb(max(0,n-2*k+2),2)

def check_distinct(n,k):
    base=tuple(range(n))
    fibers=defaultdict(list)
    for i in range(n-k+1):
        y=pal(base,k,i)
        for j in range(n+1):
            z=pal(y,k,j)
            fibers[z].append((i,j))
    assert len(fibers)==promised(n,k),(n,k,len(fibers),promised(n,k))
    actual={frozenset(v) for v in fibers.values() if len(v)==2}
    assert all(len(v)<=2 for v in fibers.values()),(n,k,'fiber>2')
    expected={frozenset(((a,b+k),(b,a))) for a in range(n-k+1)
              for b in range(a+k,n-k+1)}
    assert actual==expected,(n,k,'unexpected collision',actual^expected)
    assert sum(len(v) for v in fibers.values())==(n-k+1)*(n+1)
    return len(fibers),len(actual)

def check_general_upper(q,n,k):
    # For arbitrary source, the forced disjoint-operation commuting pairs
    # give the same universal upper bound.
    for base in product(range(q),repeat=n):
        z=set()
        for i in range(n-k+1):
            y=pal(base,k,i)
            for j in range(n+1):z.add(pal(y,k,j))
        assert len(z)<=promised(n,k),(q,n,k,len(z))

def main():
    runs=0
    for k in range(2,9):
        for n in range(k,20):
            check_distinct(n,k)
            runs+=1
    for q in (2,3):
        for n in range(2,8):
            for k in range(2,n+1):
                check_general_upper(q,n,k)
    # Show k=1 boundary fails (the all-distinct word of length 1 has one
    # exact-two descendant despite two ordered histories).
    assert len({pal(pal((0,),1,0),1,j) for j in range(2)})==1
    print('PASS',runs,'distinct-symbol pairs; all forced fibers; small alphabet upper bounds; k=1 boundary')

if __name__=='__main__':main()
