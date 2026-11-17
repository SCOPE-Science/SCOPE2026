"""Exact rational checks for weighted two-cell means under complete-pair variation.

Only finite checks: the unrestricted theorem is proved analytically.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def gini(x):
    return sum((abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1,len(x))),F(0))


def norm_formula(a,b,p,q):
    n=a+b
    assert len(p)==a and len(q)==b and sum(p)==sum(q)==1
    terms=[]
    for weights in (p,q):
        acc=F(0)
        for j,w in enumerate(sorted(weights,reverse=True),1):
            acc+=w
            terms.append(F(a*b)*acc/F(j*(n-j)))
    return max(terms)


def exhaustive_cuts(a,b,p,q):
    n=a+b; best=F(0); cuts=[]
    for k in range(1,n):
        for S in combinations(range(n),k):
            x=[F(int(i in S)) for i in range(n)]
            u=sum((p[i]*x[i] for i in range(a)),F(0))
            v=sum((q[j]*x[a+j] for j in range(b)),F(0))
            out=[u]*a+[v]*b
            t=gini(out)/gini(x)
            if t>best: best=t;cuts=[S]
            elif t==best: cuts.append(S)
    return best,cuts


def direct_map(a,b,p,q,x):
    u=sum((p[i]*x[i] for i in range(a)),F(0))
    v=sum((q[j]*x[a+j] for j in range(b)),F(0))
    return [u]*a+[v]*b

r=Random(136617)
count=0
for a in range(1,6):
    for b in range(1,6):
        for _ in range(3):
            p=[F(r.randrange(1,11)) for i in range(a)]
            q=[F(r.randrange(1,11)) for i in range(b)]
            p=[x/sum(p) for x in p]
            q=[x/sum(q) for x in q]
            theor=norm_formula(a,b,p,q)
            enumerated,_=exhaustive_cuts(a,b,p,q)
            assert theor==enumerated,(a,b,p,q,theor,enumerated)
            assert F(1)<=theor<=F(a*b,a+b-1)
            for _ in range(5):
                x=[F(r.randrange(-20,21),r.randrange(1,10)) for i in range(a+b)]
                if gini(x): assert gini(direct_map(a,b,p,q,x))<=theor*gini(x)
            count+=1
print('EXACT_ALL_TWO_CLASS_CUTS_AND_RATIONAL_INPUTS_PASSED',count)

p=[F(2,3),F(1,3)];q=[F(1,2),F(1,2)]
assert norm_formula(2,2,p,q)==1
p2=[F(4,5),F(1,5)]
assert norm_formula(2,2,p2,q)==F(16,15)
assert norm_formula(2,2,[F(3,4),F(1,4)],q)==1
print('EXACT_NONBISTOCHASTIC_CONTRACTION_AND_SHARP_FOUR_POINT_THRESHOLD_PASSED')

for a in range(1,41):
    for b in range(1,41):
        n=a+b
        p=[F(1,a)]*a;q=[F(1,b)]*b
        assert norm_formula(a,b,p,q)==1
        assert F(a*b,n-1)>=1
        if a==1 or b==1: assert F(a*b,n-1)==1
        elif a*b>n-1: pass
print('UNIFORM_STABILITY_AND_PARTITION_ENVELOPE_BOUND_PASSED',40*40)
print('ALL_WEIGHTED_TWO_CELL_GINI_CHECKS_PASSED')

# Sharp (separate-cell) total-variation stability radii around uniform masses.
for a in range(2,18):
    for b in range(2,18):
        r_a=F(a-1,a*b)
        r_b=F(b-1,a*b)
        # The first violated cut is a singleton when either cell's TV-radius is exceeded.
        eps_a=min(F(1,10000), (F(a-1,a)-r_a)/2)
        eps_b=min(F(1,10000), (F(b-1,b)-r_b)/2)
        assert eps_a>0 and eps_b>0
        da=r_a+eps_a
        db=r_b+eps_b
        p=[F(1,a)+da]+[F(1,a)-da/F(a-1)]*(a-1)
        q=[F(1,b)]*b
        assert min(p)>0 and sum(p)==1 and norm_formula(a,b,p,q)>1
        p=[F(1,a)]*a
        q=[F(1,b)+db]+[F(1,b)-db/F(b-1)]*(b-1)
        assert min(q)>0 and sum(q)==1 and norm_formula(a,b,p,q)>1
        # Large finite sample of rate vectors whose TV distances respect both radii.
        for _ in range(3):
            wp=[F(r.randrange(1,10)) for i in range(a)]
            wq=[F(r.randrange(1,10)) for i in range(b)]
            wp=[v/sum(wp) for v in wp]; wq=[v/sum(wq) for v in wq]
            dp=sum((abs(v-F(1,a)) for v in wp),F(0))/2
            dq=sum((abs(v-F(1,b)) for v in wq),F(0))/2
            sc=min(F(1),r_a/(dp if dp else F(1)),r_b/(dq if dq else F(1)))
            pp=[F(1,a)+sc*(v-F(1,a)) for v in wp]
            qq=[F(1,b)+sc*(v-F(1,b)) for v in wq]
            assert norm_formula(a,b,pp,qq)==1
print('EXACT_STABILITY_RADII_AND_NEARBY_SHARP_VIOLATIONS_PASSED',16*16)
