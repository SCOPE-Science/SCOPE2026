"""Independent finite checks of the two-extra-good value-blind EFX theorem.
This is a finite regression test, not a substitute for the proof for all n.
"""
from itertools import product, combinations, permutations
from math import comb, factorial
from fractions import Fraction

def efx_recompute(recipients, values, n):
    bundles = [tuple(g for g, r in enumerate(recipients) if r == i) for i in range(n)]
    for i in range(n):
        for j in range(n):
            for removed in bundles[j]:
                if sum(values[x] for x in bundles[i]) < sum(values[x] for x in bundles[j] if x != removed):
                    return False
    return True

def analytic_counts(values):
    # Equal entries allowed. Formula counts distinct unlabelled partition choices.
    n = len(values)-2
    m = len(values)
    t = 0
    d = 0
    for tri in combinations(range(m), 3):
        single = [x for x in range(m) if x not in tri]
        if min(values[x] for x in single) >= sum(sorted((values[x] for x in tri), reverse=True)[:2]):
            t += 1
    for quad in combinations(range(m), 4):
        rest = [x for x in range(m) if x not in quad]
        for k in range(1,4):
            pair1 = (quad[0], quad[k])
            pair2 = tuple(x for x in quad if x not in pair1)
            if rest and min(values[x] for x in rest) < max(values[x] for x in quad):
                continue
            if sum(values[x] for x in pair1) >= max(values[x] for x in pair2) and sum(values[x] for x in pair2) >= max(values[x] for x in pair1):
                d += 1
    return t,d

def direct_counts(values):
    n=len(values)-2
    tally=[0,0]
    for seq in product(range(n), repeat=len(values)):
        if not efx_recompute(seq,values,n):continue
        sizes=sorted(seq.count(i) for i in range(n))
        if sizes == [1]*(n-1)+[3]:tally[0]+=1
        elif sizes == [1]*(n-2)+[2,2]:tally[1]+=1
        else:raise AssertionError((n,values,seq))
    return tuple(tally)

def main():
    total=0
    for n in range(2,5):
        m=n+2
        vals=[tuple(range(m,0,-1)),tuple([1]*m), tuple(range(16,16-(n-2),-1))+(6,4,3,1),tuple(range(22,22-(n-2),-1))+(10,4,3,1)]
        if n<=3:
            vals += list(permutations(range(1,m+1)))
        for v in vals:
            t,d=analytic_counts(v)
            direct=direct_counts(v)
            assert direct==(t*factorial(n),d*factorial(n)), (n,v,t,d,direct)
            total += n**m
        a,b=comb(m,3),3*comb(m,4)
        assert Fraction(a,a+b)*Fraction(1,a)==Fraction(b,a+b)*Fraction(1,b)==Fraction(1,a+b)
        assert analytic_counts(vals[2])==(0,1), (n,analytic_counts(vals[2]))
        assert analytic_counts(vals[3])==(1,0), (n,analytic_counts(vals[3]))
        print(f'n={n}: minimax={Fraction(1,a+b)}, scenarios={len(vals)}')
    print('PASS',total,'exhaustive EFX recomputations')
if __name__=='__main__':main()
