"""Finite diagnostics for an exact-real reciprocal sine-square boundary theorem.
Only proof in RESULT.md establishes infinite limits and total variation.
"""
import math
from sympy import symbols, pi, sin, simplify, diff
x,y,a,b=symbols('x y a b',positive=True)
A=a*pi/x+b*y
B=b*pi*y+a*x
f=sin(A)**2; g=sin(B)**2
J=simplify(diff(f,x)*diff(g,y)-diff(f,y)*diff(g,x))
assert simplify(J+a*b*(1+pi*pi/x**2)*sin(2*A)*sin(2*B))==0

def phases(b,v):
    angle=math.asin(math.sqrt(v)); r=[]
    for k in range(0,math.ceil(b)+2):
        for rho in (k*math.pi+angle,(k+1)*math.pi-angle):
            if rho<=b*math.pi+1e-12:
                r.append(rho)
    return r

def root(a,rho,n,psi):
    L=n+psi/math.pi-rho/math.pi**2
    return 2*a/(L+math.sqrt(L*L+4*a*a/math.pi**2))

def annulus(a,b,u,v,delta):
    angle=math.asin(math.sqrt(u)); rhos=phases(b,v)
    count=0; w=0.0; errors=[]
    for rho in rhos:
      for psi in (angle, math.pi-angle):
       for n in range(max(1,int(a/delta)-9),int(2*a/delta)+11):
        X=root(a,rho,n,psi); Y=(rho-a*X)/(b*math.pi)
        if delta/2<=X<=delta and 0<Y<1:
            count+=1
            u1=math.sin(a*math.pi/X+b*Y)**2
            v1=math.sin(b*math.pi*Y+a*X)**2
            errors.append(max(abs(u1-u),abs(v1-v)))
            w+=1/(4*a*b*(1+math.pi**2/X**2)*math.sqrt(u*(1-u)*v*(1-v)))
    p=len(rhos)/(2*b*math.pi**2*math.sqrt(u*(1-u)*v*(1-v)))
    return count,w,p,max(errors,default=0)

for a0,b0,u0,v0 in [(.6,2.,.36,.64),(.6,.5,.36,.64),(.6,1.3,.36,.64),(.6,.4,.36,.94)]:
  for d in (.04,.02,.01):
    N,W,p,e=annulus(a0,b0,u0,v0,d)
    assert e<2e-11,(a0,b0,d,e)
    if p>0:
        rel=abs(W/(d/2)/p-1)
        assert rel<0.10,(b0,d,rel)
    else:
        assert N==0 and W==0
    print(f'a={a0}, b={b0}, v={v0}, delta={d}, M={len(phases(b0,v0))}, N={N}, density={W/(d/2):.7f}, limit={p:.7f}, residual={e:.2g}')
print('PASS: exact Jacobian identity; phase inverse residuals; finite annular density diagnostics')
