#!/usr/bin/env python3
"""Gold-graph fourth-moment test and affine F4-line incidence code rank.
Standard-library only: `python gold_checker.py`.
Finite checks support, but do not replace, the all-dimension proof.
"""
import cmath
import itertools
import random


def field(k, coeff):
    """Binary extension F_2[t]/(t^k + sum coeff[i] t^i), irreducible given."""
    q=1<<k
    def mul(a,b):
        z=0
        while b:
            if b&1:z^=a
            a<<=1
            if a&q:a^=q|sum(c<<i for i,c in enumerate(coeff))
            b>>=1
        return z
    def powf(a,n):
        z=1
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n>>=1
        return z
    assert all(powf(a,q-1)==1 for a in range(1,q))
    return q,mul,powf


def fibers_energy(q,mul,f):
    d={}
    for a in range(q):
        aa=mul(mul(mul(mul(a,a),a),a),a)
        for b in range(q):
            bb=mul(mul(mul(mul(b,b),b),b),b)
            key=(a^b,aa^bb)
            d[key]=d.get(key,0j)+f[a]*f[b]
    return sum(abs(z)**2 for z in d.values())


def gf2_rank(rows):
    piv={}
    for row in rows:
        v=row
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return len(piv)


def f4_basis(q,mul,w):
    basis=[]; spans={0}
    for x in range(1,q):
        if x not in spans:
            basis.append(x)
            spans={v^mul(u,x) for v in spans for u in (0,1,w,w^1)}
    m=len(basis)
    assert 4**m==q
    element_coords={}
    for cs in itertools.product((0,1,w,w^1),repeat=m):
        x=0
        for a,b in zip(cs,basis):x^=mul(a,b)
        assert x not in element_coords
        element_coords[x]=cs
    assert len(element_coords)==q
    return basis,element_coords


def run():
    rng=random.Random(261726)
    # Irreducible polynomials: t^2+t+1, t^4+t+1, t^6+t+1,
    # t^8+t^4+t^3+t+1 (AES modulus).
    polynomials=[(2,[1,1]),(4,[1,1,0,0]),(6,[1,1,0,0,0,0]),
                 (8,[1,1,0,1,1,0,0,0])]
    grand=0
    for k,c in polynomials:
        q,mul,powf=field(k,c)
        omegas=[z for z in range(q) if (mul(z,z)^z^1)==0]
        assert len(omegas)==2
        w=omegas[0]
        four={0,1,w,w^1}
        m=k//2
        basis,coords=f4_basis(q,mul,w)
        assert len(basis)==m
        lines={frozenset((x,x^s,x^mul(w,s),x^mul(w^1,s)))
               for s in range(1,q) for x in range(q)}
        assert len(lines)==(q-1)*q//12
        matrix=[sum(1<<x for x in L) for L in lines]
        rank=gf2_rank(matrix)
        assert q-rank==m*m+m+1,(q,q-rank)
        print(f'GF({q}): {len(lines)} affine F4-lines; GF(2) incidence rank {rank}; nullity {q-rank}.')
        # Complete sign census when q <=16.
        if q<=16:
            count=sum(all((mask & row).bit_count()%2==0 for row in matrix)
                      for mask in range(1<<q))
            assert count==2**(m*m+m+1),(q,count)
            print(f'  complete {1<<q}-sign census: {count} optimal patterns.')
        trials=3 if q==256 else 10
        for trial in range(trials):
            f={x:complex(rng.randint(-4,4),rng.randint(-4,4)) for x in range(q)}
            en=fibers_energy(q,mul,f)
            s=sum(abs(z)**2 for z in f.values())
            assert en <= (5-4/q)*s*s+1e-6*(1+s*s),(q,trial,en,s)
            grand+=1
        # Independent full family of optimizers via trace of quadratic F4 polynomials.
        for trial in range(trials):
            b=[rng.choice(tuple(four)) for _ in range(m)]
            a={(i,j):rng.choice(tuple(four)) for i in range(m) for j in range(i+1,m)}
            const=rng.randrange(2)
            f={}
            for x,cs in coords.items():
                t=0
                for i in range(m):t^=mul(b[i],cs[i])
                for (i,j),v in a.items():t^=mul(v,mul(cs[i],cs[j]))
                bit=t^mul(t,t)
                assert bit in (0,1)
                f[x]=(-1)**(const^bit)
            assert all(sum(1 if f[x]<0 else 0 for x in L)%2==0 for L in lines)
            en=fibers_energy(q,mul,f)
            exact=(5-4/q)*q*q
            assert abs(en-exact)<1e-8*(1+exact),(q,trial,en,exact)
            grand+=1
    print(f'PASS: {grand} direct complex-energy tests plus incidence-rank and complete small-field sign checks.')

if __name__=='__main__':run()
