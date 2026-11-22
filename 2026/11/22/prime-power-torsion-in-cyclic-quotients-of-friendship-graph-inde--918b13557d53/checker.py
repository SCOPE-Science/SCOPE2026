"""Finite checks for prime-power torsion criterion in friendship-complex cyclic quotients.
All calculations use finite combinatorics and exact integer arithmetic.
"""
from math import gcd, comb
from itertools import product

def smallest_prime_factor(n):
    return next(p for p in range(2,n+1) if n%p==0)

def is_prime_power(n):
    p=smallest_prime_factor(n)
    t=n
    while t%p==0:t//=p
    return (t==1,p)

def check_fixed_cycles(n):
    fixed=[]
    for k in range(1,n):
        seen=set();orbits=[]
        for x in range(n):
            if x in seen:continue
            y=x; orb=[]
            while y not in seen:
                seen.add(y);orb.append(y);y=(y+k)%n
            orbits.append(orb)
        assert len(orbits)==gcd(n,k)
        # A vector invariant under this permutation is constant on each orbit.
        # Intersecting the zero-sum hyperplane reduces dimension by precisely one.
        if len(orbits)>=2:fixed.append(k)
    d=n
    for k in fixed:d=gcd(d,k)
    ispp,p=is_prime_power(n)
    assert d==(p if ispp else 1),(n,d,p,ispp)
    return d,len(fixed)

def face_counts(n):
    # One of empty, +, - on each triangular petal; the apex is a separate face.
    by_size=[0]*(n+1)
    for choice in product((0,1,2),repeat=n):
        k=sum(x!=0 for x in choice)
        by_size[k]+=1
    assert all(by_size[k]==comb(n,k)*2**k for k in range(n+1))
    # Sphere Euler characteristic for n-dimensional cross-polytope boundary.
    euler=sum((-1)**(k-1)*by_size[k] for k in range(1,n+1))
    assert euler==1+(-1)**(n-1)
    return sum(by_size),euler

if __name__=='__main__':
    for n in range(4,51):
        d,ct=check_fixed_cycles(n)
        print(f'{n}: fixed_rotations={ct}, quotient_pi1_order={d}',end='')
        if n<=8:
            faces,chi=face_counts(n)
            print(f', nonempty_sphere_faces={faces-1}, sphere_euler={chi}',end='')
        print()
    print('PASS: all exact tests')
