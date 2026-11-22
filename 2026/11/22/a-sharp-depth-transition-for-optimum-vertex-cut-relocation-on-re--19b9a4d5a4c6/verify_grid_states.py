"""Independent finite parameter-space check of the closed-form grid-cut theorem.

Python standard library only. Run: python3 verify_grid_states.py
"""
from collections import Counter, deque


def triples(n,w,r):
    z=set()
    for a in range(n):
        for b in range(1,n-1):
            for c in range(n):
                if abs(a-b)>1 or abs(b-c)>1:continue
                if r>1 and not(a==0 or a==n-1):continue
                if r<w-2 and not(c==0 or c==n-1):continue
                z.add((a,b,c))
    return z


def analyze(z,rule):
    neighbours={v:set() for v in z};E=0
    for (a,b,c) in z:
        for j in range(3):
            for t in range(0,max(max(q) for q in z)+1):
                p=[a,b,c];p[j]=t;p=tuple(p)
                if p== (a,b,c) or p not in z:continue
                if rule=='slide' and abs(t-(a,b,c)[j])!=1:continue
                neighbours[(a,b,c)].add(p)
        E+=len(neighbours[(a,b,c)])
    left=set(z);component_sizes=[]
    while left:
        seed=left.pop();vis={seed};Q=deque([seed])
        while Q:
            for u in neighbours[Q.popleft()]:
                if u not in vis:vis.add(u);Q.append(u);left.discard(u)
        component_sizes.append(len(vis))
    degrees=Counter(map(len,neighbours.values()))
    return E//2, sorted(component_sizes), dict(degrees)


def main():
    count=0
    for w in range(4,12):
        for n in range(3,31):
            for r in range(1,w-1):
                z=triples(n,w,r)
                TS=analyze(z,'slide');TJ=analyze(z,'jump')
                if r in (1,w-2):
                    expect=(6,(4,[3,3],{1:4,2:2}),((9,[6],{3:6}) if n==3 else (6,[3,3],{2:6})))
                elif n==3: expect=(4,(0,[1]*4,{0:4}),(4,[4],{2:4}))
                else: expect=(2,(0,[1,1],{0:2}),(0,[1,1],{0:2}))
                assert (len(z),TS,TJ)==expect,((n,w,r),(len(z),TS,TJ),expect)
                count+=1
    print('PARAMETER_CHECK_PASS',count,'instances: orders 3..30, widths 4..11, every nonboundary terminal row')


if __name__=='__main__':main()
