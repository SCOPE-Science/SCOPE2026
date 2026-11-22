"""Finite independent checks of even-dihedral retraction classification.

Usage: python verify_dihedral.py
No third-party dependencies. The group is represented by (rotation exponent, reflection bit).
"""
from collections import Counter
from math import gcd, prod


def mul(n, x, y):
    return ((x[0]+(-1 if x[1] else 1)*y[0]) % n, x[1]^y[1])


def power(n, x, k):
    t=(0,0)
    for _ in range(k):
        t=mul(n,t,x)
    return t


def inv(n,x):
    return ((-x[0] if not x[1] else x[0]) % n,x[1])


def hom(n, image_r, image_s, element):
    a,e=element
    return mul(n,power(n,image_r,a),power(n,image_s,e))


def retractions(n):
    group=[(j,b) for j in range(n) for b in (0,1)]
    ans={}
    for x in group:
        if power(n,x,n)!=(0,0):
            continue
        for y in group:
            if power(n,y,2)!=(0,0):
                continue
            if mul(n,mul(n,y,x),y)!=inv(n,x):
                continue
            if hom(n,x,y,x)!=x or hom(n,x,y,y)!=y:
                continue
            image={hom(n,x,y,g) for g in group}
            ans[(x,y)]=len(image)
    return ans


def unitary_divisors(n):
    return [d for d in range(1,n+1) if n%d==0 and gcd(d,n//d)==1]


def predicted(n):
    assert n>=4 and n%2==0
    e=int(n%4==2)
    ans=Counter({1:1})
    for d in unitary_divisors(n):
        ans[2*n//d]+=d
    ans[2]+=n+2*e
    return ans


def aut_conjugate(n, params, psi):
    """Conjugate endomorphism by a unit automorphism of D_{2n}."""
    x,y=params
    u,v=psi
    u_inverse=pow(u,-1,n)
    # inverse automorphism maps r to r^(u^-1), s to r^(-u^-1 v) s.
    pre_r=(u_inverse,0)
    pre_s=(-u_inverse*v % n,1)
    img_r=hom(n,x,y,pre_r)
    img_s=hom(n,x,y,pre_s)
    return (hom(n,(u,0),(v,1),img_r),hom(n,(u,0),(v,1),img_s))


def actual_orbits(n, retracts):
    all_aut=[(u,v) for u in range(n) if gcd(u,n)==1 for v in range(n)]
    remaining=set(retracts)
    sizes=[]
    while remaining:
        p=min(remaining)
        orbit={aut_conjugate(n,p,psi) for psi in all_aut}
        assert orbit <= set(retracts), (n,p,orbit-set(retracts))
        assert len(orbit & remaining)==len(orbit), 'orbits overlap'
        sizes.append(len(orbit))
        remaining-=orbit
    return Counter(sizes)


def predicted_orbits(n):
    e=int(n%4==2)
    c=Counter({1:1}) # trivial
    for d in unitary_divisors(n):
        c[d]+=1
    c[n]+=1 # reflection generator image
    if e:
        c[2]+=1
    return c


def classified_maps(n):
    """Explicit four-family classification, constructed without enumerating homomorphisms."""
    maps={((0,0),(0,0))}
    for a in range(n):
        if (a*a-a)%n:
            continue
        for b in range(n):
            if a*b % n == 0:
                maps.add(((a,0),(b,1)))
    for c in range(n):
        maps.add(((c,1),(c,1) if c%2==0 else (0,0)))
    if n%4==2:
        maps.add(((n//2,0),(0,0)))
        maps.add(((n//2,0),(n//2,0)))
    return maps


def omega(n):
    count=0
    p=2
    while p*p<=n:
        if n%p==0:
            count+=1
            while n%p==0:
                n//=p
        p+=1
    if n>1:
        count+=1
    return count


def run():
    tests=0
    for n in range(4,33,2):
        R=retractions(n)
        assert set(R)==classified_maps(n), ("classification mismatch", n, set(R)^classified_maps(n))
        got=Counter(R.values())
        expect=predicted(n)
        assert got==expect, ('rank spectrum',n,got,expect)
        counts=actual_orbits(n,R)
        wanted=predicted_orbits(n)
        assert counts==wanted, ('orbits',n,counts,wanted)
        assert sum(counts.values())==2**omega(n)+2+int(n%4==2)
        print('n=%-2d |retractions|=%-5d image_order=%s orbit_sizes=%s' % (n,len(R),dict(sorted(got.items())),dict(sorted(counts.items()))))
        tests+=1
    print('EVEN_DIHEDRAL_RETRACTION_RANK_ORBIT_CLASSIFICATION_PASSED cases='+str(tests))


if __name__ == '__main__':
    run()
