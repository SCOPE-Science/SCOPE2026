"""Exact finite verification of total and paired domination on two graphs."""
from functools import lru_cache

N = 16
GEN = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}


def adjacency(kind):
    out=[]
    for u in range(N):
        a,b=divmod(u,4)
        if kind=='S':
            out.append(sum(1<<v for v in range(N) if
               ((v//4-a)%4,(v%4-b)%4) in GEN))
        else:
            out.append(sum(1<<v for v in range(N) if
               (v!=u) and ((v//4==a) or (v%4==b))))
    return out


def calculate(kind):
    adj=adjacency(kind)
    T=[0]*17; P=[0]*17; four_nonmatched=[]
    @lru_cache(None)
    def has_matching(mask):
        if not mask: return True
        low=mask&-mask
        u=low.bit_length()-1
        opts=adj[u]&mask
        while opts:
            bit=opts&-opts
            if has_matching(mask^low^bit): return True
            opts^=bit
        return False
    for mask in range(1<<N):
        if not all(mask & nb for nb in adj): continue
        size=mask.bit_count()
        T[size]+=1
        if size%2==0 and has_matching(mask):P[size]+=1
        elif size==4: four_nonmatched.append(mask)
    return adj,T,P,four_nonmatched

s,ts,ps,notpair=calculate('S')
r,tr,pr,_=calculate('R')
point=[0,8,2,10,7,3,5,1,14,6,12,4,9,13,11,15]
block=[11,1,9,3,2,4,0,6,5,15,7,13,12,10,14,8]
assert sorted(point)==list(range(16)) and sorted(block)==list(range(16))
assert all(bool(s[u]>>v&1)==bool(r[point[u]]>>block[v]&1)
           for u in range(N) for v in range(N))
T=[0,0,0,0,80,1056,4768,9520,12150,11280,7992,4368,1820,560,120,16,1]
S_P=[0,0,0,0,48,0,4384,0,12054,0,7992,0,1820,0,120,0,1]
R_P=[0,0,0,0,80,0,4464,0,12150,0,7992,0,1820,0,120,0,1]
assert ts==tr==T and ps==S_P and pr==R_P
assert len(notpair)==32
for mask in notpair:
    degrees=sorted((s[v]&mask).bit_count() for v in range(N) if mask>>v&1)
    assert degrees==[1,1,1,3]
# One of two symmetric independent triples in the neighborhood of each S vertex.
for center in range(N):
    assert sum((mask>>center&1) and (s[center]&mask).bit_count()==3
               for mask in notpair)==2
print('PASS bitmask: 65536 subsets per graph; total=',ts)
print('PASS paired S=',ps)
print('PASS paired R=',pr)
print('PASS nonpairable total-dominating 4-sets are 32 distinct claws')
print('PASS incidence bipartition-preserving maps')
