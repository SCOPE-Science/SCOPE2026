"""Independent finite checks for sharp three-character fourth-moment classifications.

Uses group addition and direct character orthogonality. Finite checks supplement,
not replace, the general six-collision-pattern proof.
"""
from itertools import combinations, product
from fractions import Fraction
from cmath import exp, pi
from math import isclose, sqrt

VALUES = {
    'sidon': Fraction(5,3), 'single_involution': Fraction(2),
    'single_progression': Fraction(15,7), 'cyclic_four': Fraction(7,3),
    'klein_four': Fraction(7,3), 'cyclic_three': Fraction(3)
}

def elems(moduli):
    return list(product(*(range(m) for m in moduli)))

def plus(a,b,moduli):
    return tuple((x+y)%m for x,y,m in zip(a,b,moduli))

def collision_structure(S,moduli):
    fibers={}
    for i in range(3):
        for j in range(i,3):
            fibers.setdefault(plus(S[i],S[j],moduli),[]).append((i,j))
    mid=[]; invol=[]
    for i in range(3):
        others=[j for j in range(3) if j != i]
        if plus(S[i],S[i],moduli)==plus(S[others[0]],S[others[1]],moduli): mid.append(i)
    for i,j in combinations(range(3),2):
        if plus(S[i],S[i],moduli)==plus(S[j],S[j],moduli): invol.append((i,j))
    if len(mid)==3 and not invol: tag='cyclic_three'
    elif len(invol)==3 and not mid: tag='klein_four'
    elif len(mid)==1 and len(invol)==1: tag='cyclic_four'
    elif len(mid)==1 and not invol: tag='single_progression'
    elif len(invol)==1 and not mid: tag='single_involution'
    elif not invol and not mid: tag='sidon'
    else: raise AssertionError(('unexpected collisions',moduli,S,mid,invol,fibers))
    return tag,mid,invol,fibers

def conv(S,moduli,a):
    fibers={}
    for i in range(3):
        for j in range(3):
            w=plus(S[i],S[j],moduli)
            fibers[w]=fibers.get(w,0)+a[i]*a[j]
    return fibers

def norm4(S,moduli,a):
    return sum(abs(z)**2 for z in conv(S,moduli,a).values())

def peak(S,moduli,tag,mid,invol):
    if tag=='single_involution':
        i,j=invol[0]; a=[0,0,0]; a[i]=1;a[j]=1; return a
    if tag=='single_progression':
        a=[sqrt(2)]*3; a[mid[0]]=sqrt(3); return a
    return [1,1,1]

def direct_norm4(S,moduli,a):
    G=elems(moduli)
    t=0.
    for g in G:
        f=sum(a[i]*exp(2j*pi*sum(si*gi/m for si,gi,m in zip(S[i],g,moduli))) for i in range(3))
        t+=abs(f)**4
    return t/len(G)

groups=[(n,) for n in range(3,34)]+[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4),(2,2,2),(2,2,3)]
case_counts={tag:0 for tag in VALUES}
max_err=0.; tested=0; random_cases=0; direct_cases=0
for mods in groups:
    G=elems(mods); zero=tuple(0 for _ in mods)
    nonzero=[g for g in G if g!=zero]
    for u,v in combinations(nonzero,2):
        S=(zero,u,v)
        tag,mid,invol,cs=collision_structure(S,mods)
        case_counts[tag]+=1
        a=peak(S,mods,tag,mid,invol)
        q=norm4(S,mods,a)/(sum(abs(x)**2 for x in a)**2)
        assert isclose(q,float(VALUES[tag]),rel_tol=1e-13,abs_tol=1e-13),(mods,S,tag,q)
        tested+=1
        # Finite, exact-integer arbitrary complex tests of every declared upper bound.
        # The coefficients are Gaussian integers; no rounding is used here.
        for seed in range(4):
            b=[complex((7*i+3*seed+len(G))%5-2,(11*i+seed+len(G))%5-2) for i in range(3)]
            mass=sum(int(z.real)**2+int(z.imag)**2 for z in b)
            if not mass:continue
            d=conv(S,mods,b)
            moment=sum(int(z.real)**2+int(z.imag)**2 for z in d.values())
            bound=VALUES[tag]
            assert bound.denominator*moment<=bound.numerator*mass**2,(mods,S,tag,b,moment)
            random_cases+=1
        if len(G)<=9:
            direct=direct_norm4(S,mods,a)
            max_err=max(max_err,abs(direct-norm4(S,mods,a)))
            assert isclose(direct,norm4(S,mods,a),rel_tol=2e-12,abs_tol=2e-12)
            direct_cases+=1
assert all(case_counts.values()),case_counts
print('VERIFY_OK', 'triples=',tested, 'gaussian_integer_tests=',random_cases,'direct_Fourier=',direct_cases,'max_fourier_error=',f'{max_err:.2e}','cases=',case_counts)
