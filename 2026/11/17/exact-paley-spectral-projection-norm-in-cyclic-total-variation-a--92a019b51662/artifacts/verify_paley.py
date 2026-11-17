import cmath, math


def primes(bound):
    return [p for p in range(5,bound+1) if all(p%d for d in range(2, math.isqrt(p)+1)) and p%4==1]

def chec(p):
    residues={i*i%p for i in range(1,p)}
    assert len(residues)==(p-1)//2
    chi=lambda i: 0 if i%p==0 else (1 if i%p in residues else -1)
    k=[(p-1)/(2*p) if j==0 else (-1+math.sqrt(p)*chi(j))/(2*p) for j in range(p)]
    kfft=[(sum(cmath.exp(2j*math.pi*t*x/p) for t in residues)/p).real for x in range(p)]
    assert max(abs(a-b) for a,b in zip(k,kfft))<2e-12
    l=[]
    for d in range(1,p):
        diff=sum(abs(k[x]-k[(x-d)%p]) for x in range(p))
        want=1+(p-1-2*chi(d))/(2*math.sqrt(p))
        assert abs(diff-want)<1e-9,(p,d,diff,want)
        l.append(diff/2)
    target=.5+(p+1)/(4*math.sqrt(p))
    assert abs(max(l)-target)<1e-9
    d=next(i for i in range(1,p) if chi(i)<0)
    # take h=indicator of consecutive vertices [0,d), D h=delta_{d-1}-delta_{p-1}
    h=[1. if i<d else 0. for i in range(p)]
    D=lambda a: [a[(i+1)%p]-a[i] for i in range(p)]
    tv=lambda a: sum(abs(z) for z in D(a))
    proj=lambda a: [sum(k[(i-j)%p]*a[j] for j in range(p)) for i in range(p)]
    assert abs(tv(proj(h))/tv(h)-target)<1e-9,(p,d,tv(proj(h))/tv(h),target)
    # unitary frequency radial soft-threshold, choose arbitrary lambda 1, perturbation scaled to small Fourier coefficient
    FT=lambda a: [sum(a[j]*cmath.exp(-2j*math.pi*r*j/p) for j in range(p))/math.sqrt(p) for r in range(p)]
    IFT=lambda a: [sum(a[r]*cmath.exp(2j*math.pi*r*j/p) for r in range(p))/math.sqrt(p) for j in range(p)]
    eps=.1/math.sqrt(p)
    hh=[eps*v for v in h]; hf=FT(hh)
    basefreq=[0j]*p
    for r in residues:
        basefreq[r]=2*hf[r]/abs(hf[r])
    base=IFT(basefreq)
    assert max(abs(x.imag) for x in base)<1e-10
    base=[x.real for x in base]
    def shrink(v):
        a=FT(v)
        b=[a[0]]+[ (0j if abs(z)<=1 else (1-1/abs(z))*z) for z in a[1:]]
        return [z.real for z in IFT(b)]
    diff=[a-b for a,b in zip(shrink([a+b for a,b in zip(base,hh)]),shrink(base))]
    ph=proj(hh)
    assert max(abs(x-sum(hh)/p-y) for x,y in zip(diff,ph))<2e-9
    assert abs(tv(diff)/tv(hh)-target)<3e-9
    return d,target
for p in primes(197):
    d,target=chec(p)
    print('PALEY',p,'nonresidue_witness',d,'sharp_BV_norm',f'{target:.12f}')
print('EXACT_PALEY_AND_RADIAL_SOFT_THRESHOLD_WITNESS_CHECKS_PASS',len(primes(197)))
