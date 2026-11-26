"""Finite semantic checks for colored equivalence classes and rare-class counts.
This program does not prove asymptotic theorems or establish priority.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
from functools import lru_cache
from math import comb, exp


def model(blocks):
    colors, classes = [], []
    for i,(a,b) in enumerate(blocks):
        colors += [1]*a + [0]*b
        classes += [i]*(a+b)
    return tuple(colors), tuple(classes)


def profile(blocks,q):
    d=defaultdict(int)
    for a,b in blocks:
        d[(min(a,q),min(b,q))]+=1
    return tuple(sorted((t,min(c,q)) for t,c in d.items()))


def ef_equivalent(left,right,q):
    (A,C),(B,D)=left,right
    @lru_cache(None)
    def play(chosen,depth):
        # chosen = sequence of cross-model pebble pairs, positional equality allowed
        if any((A[x]!=B[y]) for x,y in chosen):return False
        for i,(x,y) in enumerate(chosen):
            for xx,yy in chosen[i+1:]:
                if (x==xx)!=(y==yy) or (C[x]==C[xx])!=(D[y]==D[yy]):return False
        if depth==0:return True
        for x in range(len(A)):
            if not any(play(chosen+((x,y),),depth-1) for y in range(len(B))):return False
        for y in range(len(B)):
            if not any(play(chosen+((x,y),),depth-1) for x in range(len(A))):return False
        return True
    return play((),q)


def main():
    types=[(a,b) for a in range(4) for b in range(4) if a+b>0]
    families=[]
    for k in (1,2,3):
        for z in combinations_with_replacement(types,k):
            if sum(a+b for a,b in z)<=8:families.append(z)
    checks=0
    grouped=defaultdict(list)
    for q in (1,2,3):
        grouped.clear()
        for z in families:grouped[profile(z,q)].append(z)
        for grp in grouped.values():
            # diverse representatives; if collisions, test q-game independently
            if len(grp)>1:
                for i in range(min(5,len(grp)-1)):
                    a,b=grp[i],grp[-i-1]
                    assert ef_equivalent(model(a),model(b),q),(q,a,b)
                    checks+=1
    # Independent direct probability computations for rare class events.
    probability_checks=0
    for r in (0,1,2):
        for m in (12,16,20,24):
            p=comb(m,r)*2.0**(-m)
            for target_lambda in (0.2,1.0,2.0):
                k=max(1,round(target_lambda/p))
                exact= - __import__('math').expm1(k*__import__('math').log1p(-p))
                approx=1-exp(-k*p)
                assert abs(exact-approx)<=max(1.0e-12, 2*k*p*p), (r,m,k)
                probability_checks+=1
    print(f"COLORED_EQUIVALENCE_VERIFY_OK EF={checks} probability={probability_checks}")

if __name__ == '__main__':main()
