#!/usr/bin/env python3
"""Reproducible tests for the rank-two first-order dihedral classification.

All data are generated from D_n = C_n semidirect C_2, n >= 3.  This is
finite corroboration; the all-n assertion requires the arithmetic proof.
"""
from collections import defaultdict

# Group elements are encoded by s*n+i, with 0<=i<n and s in {0,1}.
def mult(n, a, b):
    sa, ia = divmod(a, n)
    sb, ib = divmod(b, n)
    return (sa ^ sb)*n + ((ia + (1-2*sa)*ib) % n)

def signature_arithmetic(n):
    assert n >= 3
    ans = set()
    for a in range(2*n):
        sqa = mult(n,a,a)
        ainverse = (-a)%n if a < n else a
        pairtypes = set()
        for b in range(2*n):
            sqb = mult(n,b,b)
            pairtypes.add((a==0,b==0,a==b,sqa==0,sqb==0,
                           sqa==b,sqb==a,ainverse==b))
        ans.add((a==0,sqa==0,frozenset(pairtypes)))
    return frozenset(ans)

def signature_full_atomic(n):
    # Independently use all equality and relation atoms on {e,a,b}.
    # This implementation never invokes the eight-predicate reduction.
    N=2*n
    mul = [[mult(n, a,b) for b in range(N)] for a in range(N)]
    ans=set()
    for a in range(N):
        ext=set()
        for b in range(N):
            w=(0,a,b)
            eq=tuple(w[i]==w[j] for i in range(3) for j in range(3))
            rel=tuple(mul[w[i]][w[j]]==w[k]
                      for i in range(3) for j in range(3) for k in range(3))
            ext.add((eq,rel))
        ans.add(frozenset(ext))
    return frozenset(ans)

def predicted_class(n):
    assert n >= 3
    if n in (3,4,5,6,8):
        return ('isolated',n)
    t=n
    v2=0
    while t%2==0:
        t//=2
        v2+=1
    return ('stable', n%3==0, min(3,v2))

def main():
    cl=defaultdict(list)
    for n in range(3,301):
        cl[signature_arithmetic(n)].append(n)
    assert len(cl)==13, len(cl)
    n_to_sig={n:k for k,ns in cl.items() for n in ns}
    assert all((n_to_sig[n]==n_to_sig[m])==(predicted_class(n)==predicted_class(m))
               for n in range(3,301) for m in range(3,301))
    print('ARITHMETIC_PROFILE_OK n=3..300 classes=13')

    direct={n:signature_full_atomic(n) for n in range(3,34)}
    assert all((direct[n]==direct[m])==(n_to_sig[n]==n_to_sig[m])
               for n in direct for m in direct)
    print('INDEPENDENT_FULL_ATOMIC_OK n=3..33 ordered_model_pairs=961')

    reps=[]
    for ns in cl.values():reps.append(min(ns))
    reps.sort()
    assert reps==[3,4,5,6,7,8,9,10,12,16,18,20,24],reps
    print('MINIMUM_CLASS_REPRESENTATIVES_OK',','.join(map(str,reps)))
    assert 2*max(reps)==48
    print('SHARP_FAMILY_REPRESENTATIVE_OK group_order=48')
    
    # Sanity-check specified reduction against all 27 ternary atoms for selected groups.
    def reduced(n,a,b):
        sq_a=mult(n,a,a);sq_b=mult(n,b,b)
        return (a==0,b==0,a==b,sq_a==0,sq_b==0,
                sq_a==b,sq_b==a,mult(n,a,b)==0)
    for n in range(3,30):
        by_reduced=defaultdict(set)
        for a in range(2*n):
            for b in range(2*n):
                w=(0,a,b)
                raw=(tuple(w[i]==w[j] for i in range(3) for j in range(3)),
                     tuple(mult(n,w[i],w[j])==w[k]
                          for i in range(3) for j in range(3) for k in range(3)))
                by_reduced[reduced(n,a,b)].add(raw)
        assert all(len(s)==1 for s in by_reduced.values()),n
    print('ATOMIC_REDUCTION_OK groups=3..29 all_pair_types')
    print('VERIFY_OK')
if __name__=='__main__':main()
