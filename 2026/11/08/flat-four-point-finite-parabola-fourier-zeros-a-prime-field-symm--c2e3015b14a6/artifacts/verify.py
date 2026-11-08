"""Exact integer/cyclotomic corroboration of phase-only four-atom parabola zeros.
Run with Python 3.8+; no third-party dependencies.
"""
from itertools import combinations, permutations, product

MATCHINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))


def is_central(p, xs):
    return any((xs[i]+xs[j]-xs[k]-xs[l]) % p == 0
               for ((i,j),(k,l)) in MATCHINGS)


def exact_zeros(p, xs, signed_exponents):
    # Each coefficient equals sign * exp(2*pi*i*exponent/p).
    # Since p>=5, sum of four signed p-th roots is zero iff every
    # cyclotomic coefficient count is zero (sum of counts is in [-4,4],
    # so it cannot be a nonzero multiple of p).
    result = []
    for a in range(p):
        for b in range(p):
            hist = [0]*p
            for x,(sign,e) in zip(xs,signed_exponents):
                hist[(e+a*x*x+b*x) % p] += sign
            if not any(hist):
                result.append((a,b))
    return result


def independent_matching(p, xs, matching):
    ((i,j),(k,l))=matching
    dx1=(xs[i]*xs[i]-xs[j]*xs[j])%p
    dy1=(xs[i]-xs[j])%p
    dx2=(xs[k]*xs[k]-xs[l]*xs[l])%p
    dy2=(xs[k]-xs[l])%p
    return (dx1*dy2-dx2*dy1)%p!=0


def check_all():
    checks=0
    for p in (5,7,11,13):
        for S in combinations(range(p),4):
            central=is_central(p,S)
            # Test all four count strata with explicitly constructed coefficient vectors.
            assert len(exact_zeros(p,S,[(1,0)]*4))==0
            checks+=1
            # Arrange labels so the first two matchings are independent.
            xs=next(t for t in permutations(S)
                    if independent_matching(p,t,MATCHINGS[0])
                    and independent_matching(p,t,MATCHINGS[1]))
            two=exact_zeros(p,xs,[(1,0),(-1,0),(-1,0),(1,1)])
            assert len(two)==2,(p,S,xs,two)
            checks+=1
            # Coefficients (1,-1,i,-i). A vanishing sum splits into Q(zeta)
            # and i*Q(zeta), so both matched pairs must vanish separately.
            one=[]
            for a in range(p):
                for b in range(p):
                    u=lambda k:(a*xs[k]*xs[k]+b*xs[k])%p
                    if u(0)==u(1) and u(2)==u(3): one.append((a,b))
            assert one==[(0,0)],(p,S,xs,one)
            checks+=1
            if central:
                m=next(m for m in MATCHINGS if not independent_matching(p,S,m))
                coeff=[None]*4
                for i,j in m:
                    coeff[i]=(1,0);coeff[j]=(-1,0)
                line=exact_zeros(p,S,coeff)
                assert len(line)==p,(p,S,line)
                checks+=1
        print('WITNESSES_PASS',p,checks)
    # Exhaustive finite test for sign/root-phase coefficient alphabet in p=5,7.
    # Global coefficient is normalized to 1; every remaining coefficient
    # ranges over +/- every pth root, so all relevant discrete phase patterns
    # are included, not just the explicit witnesses.
    for p in (5,7):
        alphabet=[(s,e) for s in (1,-1) for e in range(p)]
        for S in combinations(range(p),4):
            ceiling=p if is_central(p,S) else 2
            observed=set()
            for tail in product(alphabet, repeat=3):
                nzeros=len(exact_zeros(p,S,[(1,0),*tail]))
                assert nzeros<=ceiling,(p,S,tail,nzeros,ceiling)
                observed.add(nzeros)
                checks+=1
            assert observed==({0,1,2,p} if is_central(p,S) else {0,1,2}), (p,S,observed)
        print('EXHAUSTIVE_PHASE_ALPHABET_PASS',p,checks)
    print('FOUR_ATOM_PARABOLA_CHECKS_PASS',checks)

if __name__=='__main__': check_all()
