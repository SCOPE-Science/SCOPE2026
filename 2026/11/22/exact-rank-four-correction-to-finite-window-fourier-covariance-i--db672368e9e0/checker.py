#!/usr/bin/env python3
"""Standalone exact checks for finite-window telegraph covariance identities.

Uses only Python standard library. The stochastic model is stationary; this
code checks finite matrices, not an infinite-parameter proof.
"""
from fractions import Fraction as F
from math import exp, pi, cos, sin, sqrt

def rank(mat):
    a = [list(map(F, row)) for row in mat]
    n, m = len(a), len(a[0]); h = 0
    for j in range(m):
        pivot = next((i for i in range(h, n) if a[i][j]), None)
        if pivot is None: continue
        a[h], a[pivot] = a[pivot], a[h]
        d = a[h][j]
        a[h] = [x/d for x in a[h]]
        for i in range(n):
            if i != h and a[i][j]:
                b = a[i][j]
                a[i] = [x - b*y for x,y in zip(a[i], a[h])]
        h += 1
        if h == n:break
    return h

def t(r,d): return r**d

def p(r,d,m): return (r**d+r**(m-d))/(1-r**m)

def rp(r,d,m):
    return (d*r**d+(m-d)*r**(m-d))/(1-r**m) + m*r**m*(r**d+r**(m-d))/(1-r**m)**2

def sym_matrix(m,func): return [[func(abs(i-j),i==j) for j in range(m)] for i in range(m)]

def cross_basis(r,m):
    return [[r**i, i*r**i, r**(m-i), (m-i)*r**(m-i)] for i in range(m)]

def mat_UMUt(U,M):
    n=len(U)
    return [[sum(U[i][k]*M[k][h]*U[j][h] for k in range(4) for h in range(4)) for j in range(n)] for i in range(n)]

m=6
r,u,A,B,noise=F(1,2),F(1,3),F(2),F(3),F(1,7)
non_C=sym_matrix(m, lambda d,diag:A*t(r,d)+B*t(u,d)+(noise if diag else 0))
non_P=sym_matrix(m, lambda d,diag:A*p(r,d,m)+B*p(u,d,m)+(noise if diag else 0))
non_E=[[non_C[i][j]-non_P[i][j] for j in range(m)] for i in range(m)]
assert rank(non_E)==4
assert all(non_E[i][j]==-A*(r**i*r**(m-j)+r**(m-i)*r**j)/(1-r**m)-B*(u**i*u**(m-j)+u**(m-i)*u**j)/(1-u**m) for i in range(m) for j in range(m))
print('PASS: two-exponential exact periodization identity and sharp rank four (rational m=6)')

V,K=F(2),F(1)
res_C=sym_matrix(m,lambda d,diag: (V+K*d)*t(r,d)+(noise if diag else 0))
res_P=sym_matrix(m,lambda d,diag: V*p(r,d,m)+K*rp(r,d,m)+(noise if diag else 0))
res_E=[[res_C[i][j]-res_P[i][j] for j in range(m)] for i in range(m)]
U=cross_basis(r,m)
h=V+K*m*r**m/(1-r**m)
M=[[0,0,h,K],[0,0,K,0],[h,K,0,0],[K,0,0,0]]
UM=mat_UMUt(U,M)
assert all(res_E[i][j]==-UM[i][j]/(1-r**m) for i in range(m) for j in range(m))
assert rank(U)==rank(M)==rank(res_E)==4
print('PASS: resonant derivative identity, rank-four factorization and basis independence (rational m=6)')

# Direct Markov moment equations for the numerical choice in Fang et al.
a,b,k,delta,spacing,obs_var=0.5,0.5,30.,1.,1.,0.01
s=a+b;rho=a/s;mean=k*rho/delta
d=k*rho*(1-rho)/(delta+s)
c=k*d;VV=mean+c/delta;KK=c*spacing;rr=exp(-delta*spacing)
assert abs(mean-15.)<1e-12 and abs(VV-127.5)<1e-12 and abs(KK-112.5)<1e-12
print('PASS: telegraph stationary mean=15, variance=127.5, resonant temporal coefficient=112.5')

def cov_fft(q,w,n=240):
    # Unit-unitary DFT covariance from the original nonperiodic Toeplitz kernel.
    # This intentionally does not use the rank-four formula.
    zq=[complex(cos(-2*pi*q*j/n),sin(-2*pi*q*j/n)) for j in range(n)]
    zw=[complex(cos(-2*pi*w*j/n),sin(-2*pi*w*j/n)) for j in range(n)]
    yy=0j
    for i in range(n):
        for j in range(n):
            gap=abs(i-j)
            cij=(VV+KK*gap)*rr**gap+(obs_var if i==j else 0.)
            yy+=zq[i]*zw[j].conjugate()*cij
    return yy/n

for j,l in ((0,16),(0,84),(16,84)):
    cv=cov_fft(j,l);v1=cov_fft(j,j).real;v2=cov_fft(l,l).real
    cor=abs(cv)/sqrt(v1*v2)
    print('raw covariance', j, l, cv, v1, v2)
    assert abs(cv)>1e-8 and cor<1
    print(f'PASS: normalized cross-bin covariance ({j},{l}) = {cor:.10f} != 0')
print('ALL EXACT AND NUMERICAL CHECKS PASS')
