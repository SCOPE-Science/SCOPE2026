"""Exact-rational checks for a complete-bipartite continuous-type swap game."""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement

def dist(x,y):
    return abs(x-y)

def cost(types,A,i):
    B=set(range(len(types)))-A
    N=B if i in A else A
    return sum((dist(types[i],types[j]) for j in N), F(0))/len(N)

def potential(types,A):
    B=set(range(len(types)))-A
    return sum((dist(types[i],types[j]) for i,j in combinations(sorted(A),2)),F(0))/len(A)+sum((dist(types[i],types[j]) for i,j in combinations(sorted(B),2)),F(0))/len(B)

def cross_cost(types,A):
    B=set(range(len(types)))-A
    return sum((dist(types[i],types[j]) for i in A for j in B),F(0))

def check(types,a):
    n=len(types); ids=set(range(n)); Bbase=set(range(n))
    cnt=0
    for inds in combinations(range(n),a):
        A=set(inds); B=Bbase-A
        p=potential(types,A)
        for x in A:
            for y in B:
                An=(A-{x})|{y}
                old=cost(types,A,x)+cost(types,A,y)
                new=cost(types,An,x)+cost(types,An,y)
                assert potential(types,An)-p==old-new, (types,a,inds,x,y)
                cnt+=1
    return cnt

checks=0; profiles=0
for n in range(2,8):
    for seq in combinations_with_replacement((F(0),F(1,3),F(2,3),F(1)),n):
        for a in range(1,n):
            checks+=check(seq,a)
            profiles+=1

# Seven-agent exact Price-of-Stability witness, normalized types (0,0,0,0,1/4,3/4,1).
types=tuple(map(F,(0,0,0,0,1,3,4)))
a=2;n=len(types)
by_type={}; strict=0; total=0
for c in combinations(range(n),a):
    A=set(c);B=set(range(n))-A
    w=cross_cost(types,A)
    improving=[]
    for x in A:
        for y in B:
            N=(A-{x})|{y}
            if cost(types,N,x)<cost(types,A,x) and cost(types,N,y)<cost(types,A,y):
                improving.append((x,y))
    key=tuple(sorted(types[i] for i in A))
    if key in by_type:
        assert by_type[key]==(w,bool(improving))
    else:
        by_type[key]=(w,bool(improving))
    strict+=bool(improving);total+=1
expected={(0,0):(16,True),(0,1):(15,True),(0,3):(17,False),(0,4):(20,False),(1,3):(20,True),(1,4):(23,False),(3,4):(33,True)}
assert by_type=={tuple(map(F,k)):v for k,v in expected.items()}, (by_type,expected)
assert min(v[0] for v in by_type.values())==15
assert min(v[0] for v in by_type.values() if not v[1])==17
assert F(17,15)>1
print('PASS: %d exact swap identities over %d graph/type profiles; %d witness placements, %d improving, PoS=17/15.'%(checks,profiles,total,strict))
for k,v in sorted(by_type.items()): print(k,v)
