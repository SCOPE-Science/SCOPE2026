"""Finite exact checks for the sharp spread-preservation criterion.

No finite enumeration is used as a proof of the universal statements.
"""
from fractions import Fraction
from itertools import combinations, product


def spread(values):
    m = len(values)
    return Fraction(sum(v*v for v in values), m) - Fraction(sum(values)**2, m*m)


def actual_graph_spread_small(d, chords):
    """Enumerate anchored integer-valued Lipschitz maps on a tiny cube.

    A separate general theorem guarantees existence of integer maximizers;
    this routine is only a finite check for d<=3.
    """
    assert d <= 3
    verts = sorted(range(1 << d), key=lambda x:(x.bit_count(),x))
    ans = Fraction(-1)
    count = 0
    vals={0:0}
    def rec(k):
        nonlocal ans,count
        if k == len(verts):
            count+=1
            v = spread([vals[x] for x in range(1<<d)])
            if v>ans:ans=v
            return
        x=verts[k]
        nb=[vals[x^(1<<i)] for i in range(d) if (x&(1<<i))]
        for v in range(max(nb)-1, min(nb)+2):
            if all(abs(v-n)<=1 for n in nb):
                if any((x==u and w in vals and abs(v-vals[w])>1) or
                       (x==w and u in vals and abs(v-vals[u])>1)
                       for u,w in chords):
                    continue
                vals[x]=v;rec(k+1);del vals[x]
    rec(1)
    return ans,count


def proper_signs(d,triples):
    return [t for t in product((-1,1),repeat=d)
            if all(abs(sum(t[i] for i in triple))==1 for triple in triples)]


def main():
    for d in (1,2,3):
        no, cnt = actual_graph_spread_small(d,())
        assert no == Fraction(d,4),(d,no)
        print('CUBE_INTEGER_EXHAUSTIVE',d,cnt,no)
    for S in ((0,1,2),):
        chords=[(0, sum(1<<i for i in S))]
        yes,cnt=actual_graph_spread_small(3,chords)
        assert yes==Fraction(3,4)
        print('ONE_LONG_CHORD_EXACT_INTEGER_SPREAD',yes,cnt)
    for d in range(3,9):
        for size in range(2,d+1):
            for S in combinations(range(d),size):
                sig=[1]*d
                for j,i in enumerate(S): sig[i]=(-1)**j
                assert abs(sum(sig[i] for i in S))<=1
        print('ALL_SINGLE_CHORD_BALANCED_SIGN_WITNESSES',d)
    # Seven lines in the Fano projective plane: every point pair lies on one line.
    fano=sorted(tuple(sorted(((i+j)%7 for j in (0,1,3)))) for i in range(7))
    assert len(set(fano))==7
    pairs=[tuple(sorted(p)) for E in fano for p in combinations(E,2)]
    assert len(pairs)==21 and len(set(pairs))==21
    assert not proper_signs(7,fano)
    print('FANO_SEVEN_TRIPLE_NON_2_COLORABILITY_OK')
    assert not proper_signs(5,list(combinations(range(5),3)))
    assert proper_signs(4,list(combinations(range(4),3)))
    print('COMPLETE_TRIPLE_SYSTEMS_K4_YES_K5_NO_OK')
    # Verify Fourier Poincare deficit identity on all inputs to a tiny sample.
    d=3
    vals=[0,1,2,1,0,2,2,-1]
    N=1<<d
    coeff=[]
    for S in range(N):
        coeff.append(Fraction(sum(vals[x]*(-1)**((S&x).bit_count()) for x in range(N)),N))
    var=spread(vals)
    assert var==sum(coeff[S]**2 for S in range(1,N))
    lhs=sum(Fraction(sum((vals[x]-vals[x^(1<<i)])**2 for x in range(N)),4*N) for i in range(d))
    assert lhs==sum(S.bit_count()*coeff[S]**2 for S in range(1,N))
    assert lhs-var==sum((S.bit_count()-1)*coeff[S]**2 for S in range(1,N))
    print('EXACT_FOURIER_POINCARE_GAP_IDENTITY_OK')
    print('ALL_HYPERCUBE_CHORD_PRESERVATION_CHECKS_OK')

if __name__=='__main__':
    main()
