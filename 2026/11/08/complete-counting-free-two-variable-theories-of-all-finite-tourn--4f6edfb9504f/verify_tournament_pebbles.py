#!/usr/bin/env python3
"""Independent exhaustive two-pebble-game check on selected finite tournaments.

The safety-game fixed point tests arbitrary finite play lengths over all possible
pebble placements; this is still finite corroboration, not an infinite proof.
"""
from itertools import combinations
import random


def from_mask(n,mask):
    E=[[False]*n for _ in range(n)]
    for k,(i,j) in enumerate(combinations(range(n),2)):
        E[i][j] = (mask>>k)&1 == 0
        E[j][i] = not E[i][j]
    return E


def head_core_tail(a,core,b):
    n=a+len(core)+b
    E=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            E[i][j]=True
    for i in range(len(core)):
        for j in range(len(core)):
            E[a+i][a+j]=core[i][j]
    for i in range(n):
        for j in range(i+1,n):
            if not E[i][j]: E[j][i]=True
    return E


def invariant(E):
    cur=list(range(len(E))); a=b=0
    while True:
        src=[v for v in cur if all(v==u or E[v][u] for u in cur)]
        if not src: break
        cur.remove(src[0]); a+=1
    if not cur: return ('T',a)
    while True:
        sink=[v for v in cur if all(v==u or E[u][v] for u in cur)]
        if not sink: break
        cur.remove(sink[0]); b+=1
    return ('N',a,b)


def two_pebble_equal(A,B):
    n=len(A); m=len(B)
    # A state records the positions of the named pebbles 0,1 in both models.
    def valid(s):
        x,y,u,v=s
        if (x==-1)!=(u==-1) or (y==-1)!=(v==-1): return False
        if x==-1 or y==-1: return True
        return (x==y)==(u==v) and A[x][y]==B[u][v] and A[y][x]==B[v][u]
    states=[]
    for x in range(-1,n):
        for y in range(-1,n):
            for u in ([-1] if x==-1 else range(m)):
                for v in ([-1] if y==-1 else range(m)):
                    s=(x,y,u,v)
                    if valid(s): states.append(s)
    good=set(states); rounds=0
    while True:
        rounds+=1; bad=set()
        for s in good:
            if s==(-1,-1,-1,-1):
                pass
            for i in range(2):
                for side in range(2):
                    target_range=range(n if side==0 else m)
                    reply_range=range(m if side==0 else n)
                    for target in target_range:
                        found=False
                        for reply in reply_range:
                            t=list(s)
                            t[i if side==0 else i+2]=target
                            t[i+2 if side==0 else i]=reply
                            if tuple(t) in good:
                                found=True;break
                        if not found:
                            bad.add(s);break
                    if s in bad: break
                if s in bad: break
        if not bad: break
        good.difference_update(bad)
        if not good: break
        assert rounds < 30
    return (-1,-1,-1,-1) in good, rounds


def run():
    tri=from_mask(3,0b100) # may be transitive! choose correct cyclic by explicit matrix
    tri=[[False,True,False],[False,False,True],[True,False,False]]
    reg5=[[False]*5 for _ in range(5)]
    for i in range(5):
        for d in (1,2): reg5[i][(i+d)%5]=True
    rng=random.Random(1729)
    pairs=[]
    for a in range(3):
        for b in range(3):
            pairs.append((head_core_tail(a,tri,b),head_core_tail(a,reg5,b)))
    for n in range(1,7):
        pairs += [(head_core_tail(0,tri,0), from_mask(n,rng.randrange(1<<(n*(n-1)//2)))) for _ in range(8)]
    for _ in range(100):
        n=rng.randint(1,6); m=rng.randint(1,6)
        pairs.append((from_mask(n,rng.randrange(1<<(n*(n-1)//2))),
                      from_mask(m,rng.randrange(1<<(m*(m-1)//2)))))
    depths=[]
    for A,B in pairs:
        actual,r=two_pebble_equal(A,B)
        expected=invariant(A)==invariant(B)
        if actual!=expected: raise AssertionError((len(A),len(B),invariant(A),invariant(B),actual))
        depths.append(r)
    print('independent two-pebble pairs:',len(pairs))
    print('pairs equivalent by game:',sum(invariant(a)==invariant(b) for a,b in pairs))
    print('largest fixed-point iteration count:',max(depths))
    print('agreement with source/sink profile: PASS')

if __name__=='__main__': run()
