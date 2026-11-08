"""Verify the elementary inequalities in the analytic proof and exact-n convergence; no finite test is a proof of the limiting statement.
Run: python verify_asymptotic.py
"""
import sympy as s
m=s.symbols('m',integer=True,positive=True)
k=s.symbols('k',integer=True,positive=True)
B=m*(2*m-1)
A=(m-1)*(2*m-3)
p1=(A-(k-1))/(B-k)
assert s.factor(p1.subs(k,1)-(2*m-3)/(2*m+1))==0
assert s.factor(p1.subs(k,m)-(m-2)/m)==0
assert s.simplify(s.diff(p1,k)+(4*m-4)/(B-k)**2)==0
p2=((2*m-4)*(2*m-5)/2)/(B-2)
gap=s.factor((m-1)**2/(m+1)**2-p2)
assert s.factor(gap-4*(2*m*m-2*m-3)/((m+1)**2*(2*m*m-m-2)))==0
assert s.simplify(s.diff(((2*m-4)*(2*m-5)/2-(k-2))/(B-k),k)-(((2*m-4)*(2*m-5)/2)+2-B)/(B-k)**2)==0
for M in range(3,120):
    assert all(s.Rational(M-2,M)<=p1.subs({m:M,k:K})<=s.Rational(2*M-3,2*M+1) for K in range(1,M+1))
    assert gap.subs(m,M)>0
print('PASS: symbolic factorization of one- and two-tag survival inequalities')

# Independent floating-point recurrence tests for the asymptotic trend.
from functools import lru_cache
@lru_cache(None)
def q(k,l):
    t=2*k+l
    if t==2: return float(k==1)
    e=t*(t-1)/2-k
    v=0.
    if l>=2: v+=(l*(l-1)/2/e)*q(k,l-2)
    if k and l: v+=(2*k*l/e)*q(k-1,l)
    if k>=2: v+=(2*k*(k-1)/e)*q(k-2,l+2)
    return v
for n in [10,20,50,100,200,400]:
    v=n*q(n,0)
    assert 0<=v<=3*n*n/(4*n*n-1)+1e-12
    print(f'n={n} n*p_n={v:.10f} gap_to_3/4={.75-v:.10f}')
print('PASS: checked convergence trend; limiting proof is in RESULT.md')
