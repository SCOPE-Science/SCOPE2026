#!/usr/bin/env python3
"""Finite computational cross-checks for the binary (1,3) pseudoperiodic shift."""
from itertools import product

FORBIDDEN = {"0101", "0111", "1000", "1010"}

def direct(w):
    n = len(w)
    return all(w[i] == w[(i+1)%n] or w[i] == w[(i+3)%n]
               for i in range(n))

def run_condition(w):
    n=len(w)
    if all(c==w[0] for c in w): return True
    starts = [i for i in range(n) if w[(i-1)%n] != w[i]]
    lengths = [(starts[(j+1)%len(starts)]-starts[j])%n
               for j in range(len(starts))]
    return (all(1<=v<=2 for v in lengths)
            and all(not (lengths[j]==1 and lengths[(j+1)%len(lengths)]==1)
                    for j in range(len(lengths))))

def transfer():
    a=[[0]*8 for _ in range(8)]
    for st in range(8):
        for bit in (0,1):
            word = ((st << 1)|bit) & 15
            if ((word>>3)&1) != ((word>>2)&1) and ((word>>3)&1) != (word&1):
                continue
            a[st][word&7]=1
    return a

def mat_mul(a,b):
    n=len(a);return [[sum(a[i][k]*b[k][j] for k in range(n))
                     for j in range(n)] for i in range(n)]

def traces(nmax):
    a=transfer();t=[[int(i==j) for j in range(8)] for i in range(8)]
    result=[]
    for n in range(1,nmax+1):
        t=mat_mul(t,a)
        result.append(sum(t[i][i] for i in range(8)))
    return result

def cubic_counts(nmax):
    u=[3,0,2];v=[3,0,-2]
    for j in range(3,nmax+1):
        u.append(u[j-2]+u[j-3]);v.append(-v[j-2]+v[j-3])
    return [2+u[n]+v[n] for n in range(1,nmax+1)]

def main():
    t=traces(100);r=cubic_counts(100)
    assert t==r,(t,r)
    cases=0
    for n in range(1,18):
        total=0
        for bits in product('01',repeat=n):
            w=''.join(bits)
            d=direct(w)
            assert d == run_condition(w),(n,w,d)
            assert d == all(''.join(w[(i+j)%n] for j in range(4)) not in FORBIDDEN
                            for i in range(n)),(n,w)
            total+=int(d);cases+=1
        assert total==r[n-1],(n,total,r[n-1])
    assert all(x>=2 for x in t)
    print('PASS: %d exhaustively enumerated cyclic binary words (lengths 1..17)'%cases)
    print('PASS: local (1,3), cyclic-run and four-forbidden-factor criteria agree')
    print('PASS: 100 period counts agree with 8-state graph and dual cubic recurrences')
    print('first 20 period counts:',t[:20])
if __name__=='__main__':main()
