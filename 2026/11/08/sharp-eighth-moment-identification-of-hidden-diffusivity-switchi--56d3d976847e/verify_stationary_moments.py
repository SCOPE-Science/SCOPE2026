#!/usr/bin/env python3
"""Exact algebraic diagnostics for the stationary-moment inverse theorem.
Uses only Python's standard library; no third-party packages.
"""
from fractions import Fraction as F

checks=0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def beta_moment(n,q):
    r=F(1)
    for j in range(n):
        r *= (q+j)/(2*q+j)
    return r

def y_moments_from_generator(nmax,gamma,k):
    # Solve the stationary two-state PDMP moment hierarchy.
    lam=2*gamma
    u=F(1,2)
    moments=[F(1)]
    for n in range(1,nmax+1):
        moments.append(u)
        u *= (n*lam+k)/(n*lam+2*k)
    return moments

def markov_position_moments(nmax,gamma,k,Dlo,Dhi):
    # Solve the state-resolved stationary diffusion generator exactly.
    lo=hi=F(1,2)
    results=[F(1)]
    for n in range(1,nmax+1):
        a=2*n*gamma+k
        det=a*a-k*k
        fac=2*n*(2*n-1)
        L=fac*Dlo*lo
        H=fac*Dhi*hi
        lo,hi=(a*L+k*H)/det,(k*L+a*H)/det
        results.append(lo+hi)
    return results

def normal_even_factor(n):
    a=1
    for j in range(1,2*n,2): a*=j
    return a

def gaussian_beta_moments(nmax,gamma,k,Dlo,Dhi):
    q=k/(2*gamma)
    a=Dlo/gamma; delta=(Dhi-Dlo)/gamma
    Y=[beta_moment(j,q) for j in range(nmax+1)]
    moments=[]
    for n in range(nmax+1):
        from math import comb
        vn=sum((F(comb(n,j))*a**(n-j)*delta**j*Y[j] for j in range(n+1)), F(0))
        moments.append(normal_even_factor(n)*vn)
    return moments

def infer_exact(m2,m4,m8,gamma):
    M=m2; B=m4/F(3)-M*M
    R=(m8/F(105)-M**4-6*M*M*B)/(B*B)
    check(B>0 and 1<R<3 and (3-R)*M*M>2*R*B,'all admissibility inequalities')
    q=3*(R-1)/(2*(3-R))
    halfsq=B*(2*q+1)
    # Return squared radius, avoiding irrational sqrt in exact rational tests.
    k=2*gamma*q
    EPR=3*gamma*B*(R-1)/((3-R)*M*M-2*R*B)
    return M,halfsq,k,EPR,R

samples=[(F(1),F(3),F(2),F(4)),(F(2),F(1,2),F(1,3),F(5)),
         (F(3,2),F(9,4),F(2),F(9,2)),(F(4),F(7),F(1,4),F(11,4)),
         (F(5,3),F(1),F(1,2),F(8,3))]
for gamma,k,lo,hi in samples:
    q=k/(2*gamma)
    Y=y_moments_from_generator(8,gamma,k)
    for n in range(9):
        check(Y[n]==beta_moment(n,q),f'PDMP beta moment n={n}')
    direct=markov_position_moments(5,gamma,k,lo,hi)
    mixture=gaussian_beta_moments(5,gamma,k,lo,hi)
    for n in range(6):
        check(direct[n]==mixture[n],f'generator vs mixture n={n}')
    M,hs,k_hat,epr,R=infer_exact(direct[1],direct[2],direct[4],gamma)
    check(k_hat==k,'switching rate inversion')
    check(M==(lo+hi)/(2*gamma),'diffusivity mean inversion')
    check(hs==((hi-lo)/(2*gamma))**2,'diffusivity gap inversion')
    expected=gamma*k*(hi-lo)**2/(4*lo*hi*(gamma+k))
    check(epr==expected,'entropy production inversion')
    B=direct[2]/3-M*M
    check(direct[3]==15*(M**3+3*M*B),'sixth moment locked by lower moments')

# Two different physical systems have exactly the same moments through order six.
gamma=F(1)
first=markov_position_moments(4,gamma,F(3),F(2),F(4))
second=markov_position_moments(4,gamma,F(8),F(3,2),F(9,2))
check(first[:4]==second[:4],'nonidentifiability through sixth moments')
check(first[4]!=second[4],'eighth moments separate examples')
check(first[1]==3 and first[2]==F(111,4) and first[3]==F(1755,4),'shared moment values')
check(first[4]==F(79485,8),'first eighth moment')
check(second[4]==F(1749195,176),'second eighth moment')
_,_,k1,epr1,_=infer_exact(first[1],first[2],first[4],gamma)
_,_,k2,epr2,_=infer_exact(second[1],second[2],second[4],gamma)
check((k1,k2)==(3,8),'distinct rates')
check((epr1,epr2)==(F(3,32),F(8,27)),'distinct entropy production')
print(f'PASS {checks} exact rational assertions')
print('shared (m2,m4,m6) =',first[1:4])
print('distinct m8 =',first[4],second[4])
print('distinct entropy production =',epr1,epr2)
