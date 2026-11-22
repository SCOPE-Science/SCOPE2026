#!/usr/bin/env python3
"""Reproducible numerical cross-checks for exact Fourier algebra coset norm formulas.
Numerical checks supplement, and do not establish, the analytical assertions.
"""
import cmath
import itertools
import math


def elements(moduli):
    return list(itertools.product(*(range(q) for q in moduli)))


def add(x, y, moduli):
    return tuple((a+b)%q for a,b,q in zip(x,y,moduli))


def neg(x, moduli):
    return tuple((-a)%q for a,q in zip(x,moduli))


def closure(generators, moduli):
    z=tuple(0 for _ in moduli)
    s={z}
    todo=[z]
    while todo:
        x=todo.pop()
        for g in generators:
            y=add(x,g,moduli)
            if y not in s:
                s.add(y);todo.append(y)
    return frozenset(s)


def all_subgroups(moduli):
    e=elements(moduli)
    found={closure([],moduli)}
    frontier=list(found)
    while frontier:
        h=frontier.pop()
        for x in e:
            k=closure([*h,x],moduli)
            if k not in found:
                found.add(k);frontier.append(k)
    return sorted(found,key=lambda h:(len(h),sorted(h)))


def fourier_algebra_norm(mask, moduli):
    e=elements(moduli)
    N=len(e)
    ans=0.0
    for chi in e:
        s=sum(cmath.exp(-2j*math.pi*sum(k*x/q for k,x,q in zip(chi,y,moduli))) for y in mask)
        ans+=abs(s)/N
    return ans


def order_in_quotient(d, L, moduli):
    zero=tuple(0 for _ in moduli)
    k=zero
    for m in range(1,len(elements(moduli))+1):
        k=add(k,d,moduli)
        if k in L:
            return m
    raise AssertionError('quotient order not found')


def formula(H,K,x,y,moduli):
    J=H&K
    L=closure([*H,*K],moduli)
    a=len(J)/len(K)
    b=len(J)/len(H)
    if add(x,neg(y,moduli),moduli) in L:
        return 1+2*(1-a)*(1-b)
    m=order_in_quotient(add(x,neg(y,moduli),moduli),L,moduli)
    pm=sum(abs(a+b*cmath.exp(2j*math.pi*j/m)) for j in range(m))/m
    return 2-a-b+pm


def main():
    count=0
    # Separate direct transforms: cyclic and noncyclic examples, all cosets.
    for moduli in [(2,), (3,), (4,), (5,), (6,), (8,), (9,), (12,), (2,2), (2,3), (2,4), (3,3), (2,2,2)]:
        e=elements(moduli)
        subs=all_subgroups(moduli)
        for H in subs:
            for K in subs:
                cosets_h={frozenset(add(x,h,moduli) for h in H) for x in e}
                cosets_k={frozenset(add(y,k,moduli) for k in K) for y in e}
                for A in cosets_h:
                    for B in cosets_k:
                        x=next(iter(A));y=next(iter(B))
                        lhs=fourier_algebra_norm(A|B,moduli)
                        rhs=formula(H,K,x,y,moduli)
                        assert abs(lhs-rhs)<4e-12,(moduli,H,K,x,y,lhs,rhs)
                        count+=1
    # Strict polygon order law, sampled at a range of unequal/symmetric pairs.
    for r in [0.03,0.2,0.75,0.99,1.0]:
        M=lambda m: sum(abs(1+r*cmath.exp(2j*math.pi*j/m)) for j in range(m))/m
        for m in range(2,17):
            assert M(m)>=M(2)-1e-11
            assert M(m)<=M(3)+1e-11
            if m>=4 and m%2==0 and (r>=.2 or m<=8):
                assert M(m)>M(m-2)+1e-12
            if m>=5 and m%2==1 and (r>=.2 or m<=7):
                assert M(m)<M(m-2)-1e-12
            count+=1
    # Endpoint phases at equal radii, asymptotic signed m^-2.
    for m in [24,48,96,192]:
        M=sum(abs(1+cmath.exp(2j*math.pi*j/m)) for j in range(m))/m
        d=(M-4/math.pi)*m*m
        target=(-math.pi/3 if m%2==0 else math.pi/6)
        assert abs(d-target)<0.003,(m,d,target)
        count+=1
    for m in [25,49,97,193]:
        M=sum(abs(1+cmath.exp(2j*math.pi*j/m)) for j in range(m))/m
        d=(M-4/math.pi)*m*m
        assert abs(d-math.pi/6)<0.003,(m,d)
        count+=1
    print('PASS',count,'separate direct-DFT and polygon assertions')

if __name__=='__main__':
    main()
