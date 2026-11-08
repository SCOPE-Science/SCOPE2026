#!/usr/bin/env python3
"""Reproduce exact dyadic symbol-count extrema for digit-sum-mod-3 words.

No nonstandard dependencies. The finite recurrence computes exact prefix-difference
extrema using the dyadic self-similarity of the binary digit-sum sequence.
"""

def predicted(k):
    n=1 << k
    if k % 2 == 0:
        h=k//2
        v=(n-1)//3
        return (v-h, v+h+1)
    h=(k-1)//2
    v=(n+1)//3
    return (v-h-1, v+h+1)


def next_extrema(C, low, high):
    E=lambda a,b:C[b]-C[a]
    low2=[[0]*3 for _ in range(3)]
    high2=[[0]*3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            aa=(a-1)%3;bb=(b-1)%3
            low2[a][b]=min(low[a][b],E(a,b)+low[aa][bb])
            high2[a][b]=max(high[a][b],E(a,b)+high[aa][bb])
    return [C[j]+C[(j-1)%3] for j in range(3)],low2,high2


def run_recurrence(max_k=120):
    C=[1,0,0]
    low=[[0]*3 for _ in range(3)]
    high=[[0]*3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            v=int(b==0)-int(a==0)
            low[a][b]=min(0,v)
            high[a][b]=max(0,v)
    snapshots={}
    for k in range(max_k+1):
        l=min(C[a]+low[a][b] for a in range(3) for b in range(3))
        u=max(C[a]+high[a][b] for a in range(3) for b in range(3))
        assert (l,u)==predicted(k),(k,(l,u),predicted(k))
        assert sum(C)==2**k
        assert all(low[a][b]==-high[b][a] for a in range(3) for b in range(3))
        snapshots[k]=(C[:],[row[:] for row in low],[row[:] for row in high])
        C,low,high=next_extrema(C,low,high)
    for k in range(2,max_k-5):
        C,L,H=snapshots[k]
        C6,L6,H6=snapshots[k+6]
        shift=21*2**k
        assert all(C6[a]==C[a]+shift for a in range(3))
        assert all(L6[a][b]==L[a][b]-3 for a in range(3) for b in range(3) if a!=b)
        assert all(H6[a][b]==H[a][b]+3 for a in range(3) for b in range(3) if a!=b)
    return snapshots


def direct_phases(k):
    n=2**k
    digits=[i.bit_count()%3 for i in range(n)]
    C=[digits.count(a) for a in range(3)]
    visited=set()
    for a in range(3):
        for b in range(3):
            count=C[a]
            visited.add(count)
            for v in digits:
                count+=int(v==b)-int(v==a)
                visited.add(count)
    return (min(visited),max(visited),visited)


def direct_windows(k,N=20000):
    n=2**k
    word=[i.bit_count()%3 for i in range(N+n)]
    p=[0]
    for symbol in word:p.append(p[-1]+int(symbol==0))
    return {p[i+n]-p[i] for i in range(N)}


def main():
    snapshots=run_recurrence(120)
    for k in range(0,13):
        lo,hi,S=direct_phases(k)
        assert (lo,hi)==predicted(k)
        assert S==set(range(lo,hi+1))
    for k in range(0,11):
        seen=direct_windows(k,20000)
        lo,hi=predicted(k)
        assert seen==set(range(lo,hi+1)),(k,len(seen),lo,hi)
    pairs=[(0,1),(0,2),(1,2)]
    for k in range(2,9):
        C,lo,hi=snapshots[k]
        print('k=',k,'C=',C,'minmax=',[(lo[a][b],hi[a][b]) for a,b in pairs])
    print('VERIFIED: exact recurrence k=0..120, six-step induction k=2..114, 13 phase enumerations, 11 literal sliding-window enumerations')

if __name__=='__main__': main()
