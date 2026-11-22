#!/usr/bin/env python3
"""Exact-arithmetic reproducibility checks for the joint mod-five theorem."""
from math import comb
from collections import defaultdict

DIGITS = ((0,0),(0,1),(3,1),(1,1),(2,0))
IM = ((1,0),(0,1),(-1,0),(0,-1))

def mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def power(a,k):
    b=(1,0)
    while k:
        if k&1:b=mul(b,a)
        a=mul(a,a);k//=2
    return b

def eig(r,s):
    z=(0,0)
    for a,b in DIGITS:
        w=IM[(r*a+s*b)%4]
        z=(z[0]+w[0],z[1]+w[1])
    return z

def fft_cell(L,e,f):
    z=(0,0)
    for r in range(4):
        for s in range(4):
            w=mul(IM[(-r*e-s*f)%4],power(eig(r,s),L))
            z=(z[0]+w[0],z[1]+w[1])
    assert z[1]==0 and z[0]%16==0
    return z[0]//16

def group_next(counts):
    nxt=defaultdict(int)
    for (e,f),n in counts.items():
        for a,b in DIGITS:
            nxt[((e+a)%4,(f+b)%4)]+=n
    return dict(nxt)

def residues_direct(N):
    t=[1,1];d=[1,3]
    for n in range(1,N-1):
        tt=( (2*n+1)*t[-1]+3*n*t[-2])//(n+1)
        dd=(3*(2*n+1)*d[-1]-n*d[-2])//(n+1)
        assert ((2*n+1)*t[-1]+3*n*t[-2])%(n+1)==0
        assert (3*(2*n+1)*d[-1]-n*d[-2])%(n+1)==0
        t.append(tt);d.append(dd)
    for n in range(min(36,N)):
        assert t[n]==sum(comb(n,2*j)*comb(2*j,j) for j in range(n//2+1))
        assert d[n]==sum(comb(n,j)**2 *2**j for j in range(n+1))
    return t,d

def main():
    checks=0
    for r in range(4):
        for s in range(4):
            target = (((2,0) if r%2==0 else (0,0)))
            if r==0: target=(2+3*IM[s][0],3*IM[s][1])
            if r==2: target=(2-IM[s][0],-IM[s][1])
            if r%2: target=IM[s]
            assert eig(r,s)==target
            checks+=1
    p={1:0,2:1,4:2,3:3}; q={1:0,3:1,4:2,2:3}
    seqT,seqD=residues_direct(5**5)
    for n in range(5**5):
        e=f=0;m=n
        while m:
            a,b=DIGITS[m%5];e=(e+a)%4;f=(f+b)%4;m//=5
        assert seqT[n]%5 == pow(2,e,5)
        assert seqD[n]%5 == pow(3,f,5)
        checks+=2
    counts={(0,0):1}
    for L in range(0,25):
        if L:
            counts=group_next(counts)
        table={(e,f):counts.get((e,f),0) for e in range(4) for f in range(4)}
        assert sum(table.values())==5**L
        A={e:sum(table[e,f] for f in range(4)) for e in range(4)}
        B={f:sum(table[e,f] for e in range(4)) for f in range(4)}
        for e in range(4):
            for f in range(4):
                assert table[e,f]==fft_cell(L,e,f)
                checks+=1
        for f in range(4):
            assert table[1,f]==table[3,f]
            assert table[0,f]-table[2,f]==int(f==L%4)
            checks+=2
        assert A[0] == (5**L+3)//4 and all(A[e]==(5**L-1)//4 for e in (1,2,3))
        assert sum((-1)**(e+f)*v for (e,f),v in table.items()) == 3**L
        assert sum((-1)**e*v for (e,f),v in table.items())==1
        assert sum((-1)**f*v for (e,f),v in table.items())==(-1)**L
        s=sum((16*table[e,f]-5**L)**2 for e in range(4) for f in range(4))
        assert s==16*(2*13**L+9**L+2*5**L+10)
        mixed=sum((16*table[e,f]-4*A[e]-4*B[f]+5**L)**2 for e in range(4) for f in range(4))
        assert mixed==16*(9**L+2*5**L+6)
        if L==3:
            assert {(e,f) for e,f in table if table[e,f] == 0}=={(1,0),(3,0)}
        if L==4: assert min(table.values())==16
        checks+=7
    print(f'PASS {checks} exact independent assertions: 3125 individual sequence checks, 25 full Fourier/moment levels, initial binomial identity checks; all 16 cells attained at L=4.')

if __name__=='__main__': main()
