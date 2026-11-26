#!/usr/bin/env python3
"""Exact finite checks for epistemic/probability commutation theorem. Stdlib."""
from itertools import product

def partitions(n):
    def rec(i,blocks):
        if i==n:
            yield tuple(tuple(b) for b in blocks);return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i+1,blocks)
            blocks[j].pop()
        blocks.append([i]);yield from rec(i+1,blocks);blocks.pop()
    yield from rec(0,[])

def probs(n,den):
    return [v for v in product(range(den+1),repeat=n) if sum(v)==den]

def check_direct(B,mu,n,den):
    for C in B:
        for w in C:
            for P in range(1<<n):
                left=min(sum(mu[v][z] for z in range(n) if (P>>z)&1) for v in C)
                kn=[D for D in B if all((P>>z)&1 for z in D)]
                right=sum(mu[w][z] for D in kn for z in D)
                if left!=right:return False
    return True

def check_character(B,mu,n,den):
    for C in B:
        q=tuple(sum(mu[C[0]][z] for z in D) for D in B)
        if any(tuple(sum(mu[v][z] for z in D) for D in B)!=q for v in C):return False
        supp=[D for D,a in zip(B,q) if a]
        for pts in product(*supp):
            if not any(all(all(mu[v][z]==(q[B.index(D)] if z==point else 0) for z in D) for D,point in zip(supp,pts)) for v in C):return False
    return True

def exhaustive():
    cases=0;passing=0
    for n in (1,2,3):
        for B in partitions(n):
            p=probs(n,2)
            for mu in product(p,repeat=n):
                a=check_direct(B,mu,n,2)
                b=check_character(B,mu,n,2)
                assert a==b,(n,B,mu,a,b)
                cases+=1;passing+=a
    print('FINITE_EXHAUSTIVE_OK',cases,'matching_cases',passing)

def multi_block():
    # Source C of size 4, target D and E of size 2 each. All four
    # extreme joint selections with q(D)=q(E)=1/2.
    B=((0,1,2,3),(4,5),(6,7))
    mu=[]
    for d,e in product((4,5),(6,7)):
        a=[0]*8;a[d]=1;a[e]=1;mu.append(tuple(a))
    mu.extend([tuple(2 if i==w else 0 for i in range(8)) for w in range(4,8)])
    assert check_direct(B,mu,8,2) and check_character(B,mu,8,2)
    print('SHARP_MULTI_BLOCK_OK',len(B[0]),2*2)

if __name__=='__main__':exhaustive();multi_block()
