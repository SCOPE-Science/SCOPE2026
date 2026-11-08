"""Exact finite checks of sharp fourth moments on double-layer path/cycle graphs.
The universal inequality and equality classification are established in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random

def base_edges(kind,n):
    assert (kind=='path' and n>=2) or (kind=='cycle' and n>=5)
    return [(i,i+1) for i in range(n-1)]+([(n-1,0)] if kind=='cycle' else [])

def actual_fourth(kind,n,r,a,b):
    edges=base_edges(kind,n)
    assert len(a)==len(b)==len(edges) and len(r)==n
    ss=Q(0)
    # One sign can be fixed, but complete independent enumeration is intentionally used.
    for signs in product((-1,1), repeat=2*n):
        top=signs[:n];bot=signs[n:]
        f=sum((r[i]*top[i]*bot[i] for i in range(n)),Q(0))
        f+=sum((a[j]*top[u]*top[v]+b[j]*bot[u]*bot[v] for j,(u,v) in enumerate(edges)),Q(0))
        ss+=f**4
    return ss / (1<<(2*n))

def predicted(kind,n,r,a,b):
    edges=base_edges(kind,n)
    S=sum((c*c for c in r+a+b),Q(0))
    return 3*S*S-2*sum((c**4 for c in r+a+b),Q(0))+24*sum((r[u]*r[v]*a[j]*b[j] for j,(u,v) in enumerate(edges)),Q(0))

def deficit(kind,n,r,a,b):
    edges=base_edges(kind,n)
    S=sum((c*c for c in r+a+b),Q(0))
    R=sum((x*x for x in r),Q(0))
    s=[a[j]*a[j]+b[j]*b[j] for j in range(len(a))]
    T=sum(s,Q(0));Qr=sum((x**4 for x in r),Q(0))
    h=[abs(r[u]*r[v]) for u,v in edges]
    f=[max(Q(0),3*hh-R) for hh in h]
    g=[max(Q(0),R-3*hh) for hh in h]
    # Base quadratic identity, plus exact symmetrization losses.
    rhs=(R-T)**2+sum(((ss-2*ff)**2 for ss,ff in zip(s,f)),Q(0))
    rhs+=4*sum((gg*ss for gg,ss in zip(g,s)),Q(0))
    rhs+=2*Qr-4*sum((ff*ff for ff in f),Q(0))
    rhs+=sum(((aa*aa-bb*bb)**2 for aa,bb in zip(a,b)),Q(0))
    rhs+=12*sum((hh*(abs(aa)-abs(bb))**2 for hh,aa,bb in zip(h,a,b)),Q(0))
    rhs+=48*sum((max(Q(0),-r[u]*r[v]*a[j]*b[j]) for j,(u,v) in enumerate(edges)),Q(0))
    return 4*S*S-predicted(kind,n,r,a,b),rhs,2*Qr-4*sum((ff*ff for ff in f),Q(0))

def verify():
    rng=Random(3379);total=0;enum=0
    for kind,n in [('path',2),('path',3),('path',4),('cycle',5),('cycle',6)]:
        m=len(base_edges(kind,n))
        for _ in range(40):
            r=[Q(rng.randrange(-3,4)) for _ in range(n)]
            a=[Q(rng.randrange(-3,4)) for _ in range(m)]
            b=[Q(rng.randrange(-3,4)) for _ in range(m)]
            if not any(r+a+b):continue
            d,rhs,sharp=deficit(kind,n,r,a,b)
            assert d==rhs and d>=0 and sharp>=0,(kind,n,r,a,b,d,rhs,sharp)
            total+=1
            if n<=5 and _<5:
                assert actual_fourth(kind,n,r,a,b)==predicted(kind,n,r,a,b)
                enum+=1
        # Every vertical square has exact equality for positive sign product.
        for j,(u,v) in enumerate(base_edges(kind,n)):
            r=[Q(0)]*n;r[u]=r[v]=Q(1)
            a=[Q(0)]*m;b=[Q(0)]*m;a[j]=b[j]=Q(1)
            d,rhs,sharp=deficit(kind,n,r,a,b)
            assert d==rhs==sharp==0
            assert predicted(kind,n,r,a,b)==4*sum((c*c for c in r+a+b),Q(0))**2
            a[j]=Q(-1)
            assert predicted(kind,n,r,a,b)<4*sum((c*c for c in r+a+b),Q(0))**2
    # Exact local two-active edge lemma on small integer energy arrays.
    count=0
    for n in range(2,9):
        for z in product(range(4),repeat=n):
            if not any(z):continue
            R=sum(z)
            w=[max(Q(0),Q(3,2)*(z[i]+z[i+1])-R) for i in range(n-1)]
            assert 2*sum((a*a for a in w),Q(0))<=sum(a*a for a in z)
            count+=1
    print('EXACT_MOMENT_IDENTITY_AND_GLOBAL_DEFICIT_OK',total)
    print('DIRECT_FULL_SIGN_ENUMERATION_OK',enum)
    print('EXACT_POSITIVE_PART_PATH_LEMMA_GRID_OK',count)
    print('EXACT_EQUALITY_WITNESSES_OK')
    print('ALL_OVERLAPPING_SQUARE_PRISM_CHECKS_PASSED')

if __name__=='__main__': verify()
