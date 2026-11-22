#!/usr/bin/env python3
"""Exact verification of a graded finite-extension counting identity."""
from itertools import product
from math import comb
from hashlib import sha256

I = [1,2,1,1]
J = [1,1,2,1]

def multiply(f,g):
    out=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):
            out[i+j]+=a*b
    return out

def brute(k):
    # V component has vertices a,b,c and strict relations a<c,b<c.
    edges=[(3*i,3*i+2) for i in range(k)] + [(3*i+1,3*i+2) for i in range(k)]
    out=[0]*(3*k+1)
    for s in product(range(3),repeat=3*k):
        # 0=below new vertex; 1=incomparable; 2=above new vertex.
        L=[i for i,t in enumerate(s) if t==0]
        U=[i for i,t in enumerate(s) if t==2]
        # Transitive closure and forbidden comparabilities fully checked.
        if any(s[a]>s[b] for a,b in edges):continue
        if any((l,u) not in edges for l in L for u in U):continue
        out[len(L)+len(U)]+=1
    return out

def profile(k,pa,pb):
    out=[x+y for x,y in zip(pa,pb)]
    out[0]-=1
    out[2]+=2*k
    out[3]+=k
    return out

def unimodal(a):
    # Local version: all entries after the first strict descent cannot rise.
    falling=False
    for x,y in zip(a,a[1:]):
        if y<x:falling=True
        if y>x and falling:return False
    return True

def logconcave(a):
    return all(a[j]*a[j]>=a[j-1]*a[j+1] for j in range(1,len(a)-1))

def main():
    pa=pb=[1]
    hashes=[]
    first_failure=None
    first_log_failure=None
    for k in range(1,104):
        pa=multiply(pa,I)
        pb=multiply(pb,J)
        c=profile(k,pa,pb)
        if k<=3:
            actual=brute(k)
            assert c==actual,(k,c,actual)
        u=unimodal(c)
        if not u and first_failure is None:first_failure=k
        if not logconcave(c) and first_log_failure is None:first_log_failure=k
        hashes.append(sha256((','.join(str(x) for x in c)+'\n').encode()).hexdigest())
        if k==103:
            diff=c[153]-c[154]
            print('k103_c153',c[153]);print('k103_c154',c[154]);print('k103_c155',c[155]);print('k103_c156',c[156]);print('k103_valley_difference',diff)
            assert c[153]>c[154]==c[155]<c[156]
    print('brute_checks=1,2,3')
    print('first_unimodality_failure=',first_failure)
    print('first_logconcavity_failure=',first_log_failure)
    print('profile_hashes_sha256=',sha256(('\n'.join(hashes)+'\n').encode()).hexdigest())
    assert first_failure==103
    assert first_log_failure==103
    print('VERIFY_OK')

if __name__=='__main__':main()
