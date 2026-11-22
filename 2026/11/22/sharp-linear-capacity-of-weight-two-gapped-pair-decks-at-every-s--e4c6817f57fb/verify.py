"""Exact finite corroboration of sparse separated-pair deck counts.
Run: python3 verify.py
Python standard library only.
"""
from collections import defaultdict
from itertools import combinations


def direct_deck(n, gap, a, b):
    w = [0] * n
    w[a] = w[b] = 1
    counts = [0, 0, 0, 0]
    for i in range(n):
        for j in range(i + gap, n):
            counts[2*w[i] + w[j]] += 1
    return (2, tuple(counts))


def formula_deck(n, gap, a, b):
    far = int(b-a >= gap)
    c01 = max(a-gap+1,0) + max(b-gap+1,0) - far
    c10 = max(n-gap-a,0) + max(n-gap-b,0) - far
    c11 = far
    c00 = (n-gap)*(n-gap+1)//2 - c01-c10-c11 if n >= gap else 0
    return (2, (c00,c01,c10,c11))


def layer(n, gap, a, b):
    r=gap-1
    right=n-gap
    excess=(max(r-a,0)+max(a-right,0)
             +max(r-b,0)+max(b-right,0))
    far=int(b-a>=gap)
    u=max(a-r,0)+max(b-r,0)-far
    return far,excess,u


def predicted(n,s):
    if s == 2:
        return 5*n-15
    return (2*s+2)*n-3*s*s-2*s-3


def verify():
    total=0
    direct_checks=0
    cases=0
    for s in range(2,21):
        for n in range(3*s-2,6*s+9):
            profiles=set()
            layers=defaultdict(set)
            for a,b in combinations(range(n),2):
                actual=formula_deck(n,s,a,b)
                if s<=7 and n<=27:
                    assert actual==direct_deck(n,s,a,b),(n,s,a,b,actual,direct_deck(n,s,a,b))
                    direct_checks+=1
                profiles.add(actual)
                far,excess,u=layer(n,s,a,b)
                layers[(far,excess)].add(u)
                total+=1
            expect=predicted(n,s)+(n==3*s-2)
            assert len(profiles)==expect,(n,s,len(profiles),expect)
            r=s-1
            h=n-2*s+1
            if n>=3*s-1:
                for j in range(2*r+1):
                    if s>=3:
                        if j==0:count0=2*n-4*s+1
                        elif j<=r:count0=2*(r-j+1)
                        elif j<2*r:count0=2
                        else:count0=0
                    else:
                        count0=(n-3 if j==0 else 2 if j==1 else 0)
                    if j<=r:count1=2*n-6*s+3+3*j
                    else:count1=2*s-1-j
                    assert len(layers[(0,j)])==count0,(s,n,0,j,len(layers[(0,j)]),count0)
                    assert len(layers[(1,j)])==count1,(s,n,1,j,len(layers[(1,j)]),count1)
            cases+=1
    print(f'PASS: {cases} (gap,length) cases; {total} source words; {direct_checks} literal pair enumerations; exact profile counts; complete layer counts')

if __name__=='__main__':
    verify()
