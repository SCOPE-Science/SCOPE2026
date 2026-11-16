"""Reproducible exact and numerical checks for two five-point lattice filters.

Dependencies: Python >=3.10, SymPy, NumPy.
Run: python verify_two_stencils.py
"""
from math import lcm, pi
from itertools import combinations_with_replacement
import numpy as np
from sympy import Poly, ZZ, cyclotomic_poly, symbols

X = symbols('X')
RATIONAL = (-2,-1,0,1,2)
# (central weights alpha,beta): unordered scalar multiplier pair
PAIRS = {(-u-v, -u*v): ('rational',u,v) for u,v in combinations_with_replacement(RATIONAL,2)}
# Irrational conjugates have t^2 + alpha*t - beta=0.
PAIRS.update({(1,1): ('quadratic',5), (-1,1): ('quadratic',10),
              (0,2): ('quadratic',8), (0,3): ('quadratic',12)})
assert len(PAIRS) == 19

def count_rational(u,m):
    return {2:int(True),-2:int(m%2==0),-1:2*int(m%3==0),
            0:2*int(m%4==0),1:2*int(m%6==0)}[u]

def predicted(m,n,alpha,beta):
    typ,*values = PAIRS[(alpha,beta)]
    if typ=='rational':
        u,v=values
        a = count_rational(u,m)*count_rational(v,n)
        if u!=v:
            a += count_rational(v,m)*count_rational(u,n)
        return a
    d=values[0]
    return 8*int(m%d==0 and n%d==0)

def exact_rational_parameters(m,n):
    L=lcm(m,n)
    modulus = Poly(cyclotomic_poly(L,X),X,domain=ZZ)
    powers=[Poly(X**j,X,domain=ZZ).rem(modulus) for j in range(L)]
    u_vals=[]
    v_vals=[]
    for a in range(m):
        z=L*a//m
        u_vals.append((powers[z]+powers[(-z)%L]).rem(modulus))
    for b in range(n):
        z=L*b//n
        v_vals.append((powers[z]+powers[(-z)%L]).rem(modulus))
    found={key:0 for key in PAIRS}
    for u in u_vals:
        for v in v_vals:
            alpha=-(u+v).rem(modulus)
            beta=-(u*v).rem(modulus)
            if alpha.degree()<=0 and beta.degree()<=0:
                key=(int(alpha.TC()),int(beta.TC()))
                assert key in PAIRS, (m,n,key)
                found[key] += 1
    return found

def numerical_count(m,n,alpha,beta):
    u=2*np.cos(2*pi*np.arange(m)/m)
    v=2*np.cos(2*pi*np.arange(n)/n)
    A=alpha+u[:,None]+v[None,:]
    B=beta+u[:,None]*v[None,:]
    return int(np.sum((abs(A)<1e-8)&(abs(B)<1e-8)))

def main():
    exact_count=0
    for m in range(3,15):
        for n in range(3,15):
            found=exact_rational_parameters(m,n)
            for (alpha,beta),value in found.items():
                assert value==predicted(m,n,alpha,beta),(m,n,alpha,beta,value)
            exact_count+=1
    checks=0
    for m in range(3,61):
        for n in range(3,61):
            for alpha,beta in PAIRS:
                assert numerical_count(m,n,alpha,beta)==predicted(m,n,alpha,beta),(m,n,alpha,beta)
                checks+=1
    print('parameter pairs:',len(PAIRS),'(15 rational and 4 quadratic)')
    for key in [(1,1),(0,2),(0,3),(-1,1),(1,2),(0,0)]:
        print('weights',key,'nullity on 60x60:',predicted(60,60,*key))
    print('PASS:',exact_count,'exact entire-grid cyclotomic classifications and',checks,'numerical parameter/grid tests')
    print('Finite tests support but do not establish the all-size classification.')

if __name__=='__main__':
    main()
