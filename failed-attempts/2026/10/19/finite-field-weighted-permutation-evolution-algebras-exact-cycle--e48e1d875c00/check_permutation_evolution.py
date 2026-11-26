#!/usr/bin/env python3
"""Exhaustive finite multiplicative-group verification of weighted permutation evolution algebras.

The structure constants are represented by exponents modulo q-1; only the
multiplicative group of the finite field is needed for this computation.
"""
from itertools import permutations, product
from math import gcd, factorial
from collections import deque, Counter


def cycles_of(sigma):
    done=set(); result=[]
    for i in range(len(sigma)):
        if i in done: continue
        c=[]; j=i
        while j not in done:
            done.add(j); c.append(j); j=sigma[j]
        result.append(tuple(c))
    return result


def h(l,m):
    g=gcd(m,2**l-1)
    return sum(gcd(g,2**r-1) for r in range(l))//l


def expected_class_count(n,m):
    a=[0]*(n+1);a[0]=1
    for l in range(1,n+1):
        for _ in range(h(l,m)):
            for j in range(l,n+1): a[j]+=a[j-l]
    return a[n]


def change_by_swap(state,j,m):
    s,aa=state;n=len(s)
    t=list(range(n)); t[j],t[j+1]=t[j+1],t[j]
    inv=[0]*n
    for i,u in enumerate(t): inv[u]=i
    return tuple(inv[s[t[i]]] for i in range(n)),tuple(aa[t[i]] for i in range(n))


def change_by_scale(state,j,m):
    s,aa=state
    return s,tuple((aa[i]+2*(i==j)-(s[i]==j))%m for i in range(len(s)))


def orbit_class_count(n,m):
    states={(p,a) for p in permutations(range(n)) for a in product(range(m),repeat=n)}
    ct=0
    while states:
        seed=states.pop(); q=deque([seed]);ct+=1
        while q:
            st=q.popleft()
            children=[change_by_swap(st,j,m) for j in range(n-1)]+[change_by_scale(st,j,m) for j in range(n)]
            for c in children:
                if c in states:
                    states.remove(c);q.append(c)
    return ct


def automorphism_count(s,a,m):
    n=len(s);count=0
    for p in permutations(range(n)):
        inv=[0]*n
        for i,u in enumerate(p): inv[u]=i
        snew=tuple(inv[s[p[i]]] for i in range(n))
        if snew!=s:continue
        for x in product(range(m),repeat=n):
            if all((2*x[i]+a[p[i]]-x[s[i]]-a[i])%m==0 for i in range(n)):
                count+=1
    return count


def inv_class_and_stabilizer(c,a,m):
    l=len(c);g=gcd(m,2**l-1)
    weights=[a[i] for i in c]
    P=sum((2**(l-1-i))*weights[i] for i in range(l))%g
    orbit={P*(2**r)%g for r in range(l)}
    return min(orbit),g*l//len(orbit), (1+g if P==0 else 1)


def predicted_aut_and_idempotents(s,a,m):
    types=Counter();aut=1;ids=1
    for c in cycles_of(s):
        label,z,ids_c=inv_class_and_stabilizer(c,a,m)
        types[(len(c),label,z,ids_c)]+=1
        aut*=z;ids*=ids_c
    for k in types.values():aut*=factorial(k)
    return aut,ids


def idempotents_bruteforce(s,a,m):
    n=len(s);ct=0
    for x in product(range(-1,m),repeat=n):
        if all( (x[s[i]]==-1 if x[i]==-1 else x[s[i]]>=0 and (a[i]+2*x[i])%m==x[s[i]]) for i in range(n)):
            ct+=1
    return ct


def run():
    checks=[(2,1),(3,1),(3,2),(4,2),(5,2),(7,2),(4,3),(5,3),(7,3),(8,3),(4,4),(5,4)]
    for q,n in checks:
        m=q-1
        predicted=expected_class_count(n,m)
        observed=orbit_class_count(n,m)
        assert observed==predicted,(q,n,observed,predicted)
        print('CLASS_OK',q,n,observed)
    for q,n in [(3,2),(4,2),(5,3),(7,3),(8,3)]:
        m=q-1
        for s in permutations(range(n)):
            for aa in product(range(m),repeat=n):
                pred_aut,pred_id=predicted_aut_and_idempotents(s,aa,m)
                obs_aut=automorphism_count(s,aa,m)
                obs_id=idempotents_bruteforce(s,aa,m)
                assert(pred_aut,pred_id)==(obs_aut,obs_id),(q,n,s,aa,pred_aut,obs_aut,pred_id,obs_id)
        print('AUT_IDEMPOTENT_OK',q,n)
    print('CHECKER_OK')

if __name__=='__main__':run()
