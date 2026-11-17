"""Finite exhaustive verification of dissociation enumerators for triangular graphs.
Only Python 3 standard library is required. No expected family is used to determine
validity: degrees are tested directly in the induced line graph.
"""
from collections import Counter
from itertools import combinations
from math import factorial


def predicted(n):
    all_sets=Counter()
    maximal=Counter()
    for a in range(n//3+1):
        for b in range((n-3*a)//2+1):
            c=n-3*a-2*b
            count=factorial(n)//(2**a*factorial(a)*2**b*factorial(b)*factorial(c))
            size=2*a+b
            all_sets[size]+=count
            if c==0 or (c==1 and b==0):
                maximal[size]+=count
    return all_sets,maximal


def directly_is_dissociation(mask, neigh):
    s=mask
    while s:
        b=s&-s;i=b.bit_length()-1;s-=b
        if (mask&neigh[i]).bit_count()>1:
            return False
    return True


def main():
    total=0;valid_total=0;maximal_total=0
    for n in range(3,8):
        edges=list(combinations(range(n),2))
        N=len(edges)
        neigh=[sum(1<<j for j,(u,v) in enumerate(edges)
                   if j!=i and (e[0] in (u,v) or e[1] in (u,v)))
              for i,e in enumerate(edges)]
        actual_all=Counter();actual_max=Counter()
        valid=bytearray(1<<N)
        for m in range(1<<N):
            good=directly_is_dissociation(m,neigh)
            valid[m]=good
            if good:
                actual_all[m.bit_count()]+=1;valid_total+=1
        for m in range(1<<N):
            if not valid[m]:continue
            if all((m>>j&1) or not valid[m|(1<<j)] for j in range(N)):
                actual_max[m.bit_count()]+=1;maximal_total+=1
        p_all,p_max=predicted(n)
        assert p_all==actual_all,(n,'all',p_all,actual_all)
        assert p_max==actual_max,(n,'max',p_max,actual_max)
        assert set(actual_max)==set(range((n+1)//2,(2*n)//3+1)),(n,actual_max)
        print(f'n={n}, all={dict(sorted(actual_all.items()))}, maximal={dict(sorted(actual_max.items()))}')
        total+=1<<N
    print(f'VERIFY_OK n=3..7 subsets={total} dissociation_sets={valid_total} maximal_sets={maximal_total} full_polynomial=PASS maximal_polynomial=PASS interval_spectrum=PASS')

if __name__=='__main__':main()
