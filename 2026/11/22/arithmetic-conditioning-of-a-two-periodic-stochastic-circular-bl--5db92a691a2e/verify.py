"""Reproducibility checks for a phase-two nearest-neighbor circular blur."""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

def blur(q,a,b,dtype=float):
    n=2*q
    M=np.zeros((n,n),dtype=dtype)
    for i in range(n):
        t=a if i%2==0 else b
        M[i,i]=1-t
        M[i,(i-1)%n]+=t/2
        M[i,(i+1)%n]+=t/2
    return M

def blocks(q,a,b):
    return [np.array([[1-a,a*(1+np.exp(-2j*np.pi*k/q))/2],
                       [b*(1+np.exp( 2j*np.pi*k/q))/2,1-b]],complex)
            for k in range(q)]

def symbol_formula(q,a,b):
    vals=[]
    for k in range(q):
        c=math.cos(math.pi*k/q)**2
        S=(1-a)**2+(1-b)**2+(a*a+b*b)*c
        D=(1-a)*(1-b)-a*b*c
        sm2=(2*D*D)/(S+math.sqrt(max(0,S*S-4*D*D)))
        sp2=(S+math.sqrt(max(0,S*S-4*D*D)))/2
        vals.extend((math.sqrt(sm2),math.sqrt(sp2)))
    return sorted(vals)

assertions=0
for a,b in [(0.2,0.6),(0.75,4/7),(0.72,0.82),(0.58,0.4)]:
  for q in range(2,17):
    mat=blur(q,a,b)
    assert np.allclose(mat.sum(1),1); assertions+=1
    s=np.linalg.svd(mat,compute_uv=False)
    sb=sorted(np.concatenate([np.linalg.svd(B,compute_uv=False) for B in blocks(q,a,b)]))
    sf=symbol_formula(q,a,b)
    assert np.allclose(sorted(s),sb,atol=2e-13); assertions+=1
    assert np.allclose(sorted(s),sf,atol=2e-13); assertions+=1
    if a+b>1:
      alpha=math.acos(math.sqrt((1-a)*(1-b)/(a*b)))/math.pi
      det_formula=-4**(1-q)*(a*b)**q*math.sin(math.pi*q*alpha)**2
      assert abs(np.linalg.det(mat)-det_formula)<1e-9; assertions+=1

# Exact rational case a=3/4,b=4/7, alpha=1/3.
a=sp.Rational(3,4);b=sp.Rational(4,7)
for q in range(2,10):
    M=sp.zeros(2*q)
    for i in range(2*q):
        t=a if i%2==0 else b
        M[i,i]=1-t
        M[i,(i-1)%(2*q)]+=t/2
        M[i,(i+1)%(2*q)]+=t/2
    d=M.det(method='domain-ge')
    assert (d==0)==(q%3==0);assertions+=1
    if q%3==0: assert M.nullspace() and len(M.nullspace())==2;assertions+=1
    else: assert M.rank()==2*q;assertions+=1
    # Exact double-angle sine-square value via Chebyshev.
    v=sp.simplify(-sp.Rational(4)**(1-q)*(a*b)**q*(1-sp.cos(2*sp.pi*q/3))/2)
    assert sp.simplify(d-v)==0;assertions+=1

for alpha in [(math.sqrt(2)-1), 0.11000100000000001]:
    a=.75;b=1/(1+3*math.cos(math.pi*alpha)**2)
    S0=(1-a)**2+(1-b)**2+a*a+b*b
    M=math.sqrt((S0+math.sqrt(S0*S0-4*(1-a-b)**2))/2)
    Sstar=(1-a)**2+(1-b)**2+(a*a+b*b)*math.cos(math.pi*alpha)**2
    const=M*math.sqrt(Sstar)/(math.pi*a*b*math.sin(2*math.pi*alpha))
    for q in [80,200,500,1000]:
        sigma=symbol_formula(q,a,b)
        kappa=sigma[-1]/sigma[0]
        dist=abs(q*alpha-round(q*alpha))
        if dist>1e-10:
           ratio=kappa*dist/q/const
           assert abs(ratio-1)<.08,(alpha,q,ratio)
           assertions+=1
print('VERIFY_OK',assertions)
