"""Exact certificate verifier for finite-chain counting-noise theorem.
Run: python verify.py   (requires sympy, numpy, scipy).
"""
import json
from itertools import product
from pathlib import Path
import sympy as S
import numpy as np
from scipy.linalg import expm

u=S.symbols('u')
STATES=list(product([0,1],repeat=3))
INDEX={x:j for j,x in enumerate(STATES)}
N=8
NAMES=['injection','extraction','hop12','hop23','adsorption','desorption']

def matrices(rate):
    Q=S.zeros(N)
    J=[S.zeros(N) for _ in range(6)]
    for j,x in enumerate(STATES):
        ev=[]
        if x[0]==0:ev.append(((1,x[1],x[2]),1,0))
        if x[2]==1:ev.append(((x[0],x[1],0),1,1))
        if x[0] and not x[1]:ev.append(((0,1,x[2]),1,2))
        if x[1] and not x[2]:ev.append(((x[0],0,1),1,3))
        if not x[1]:ev.append(((x[0],1,x[2]),rate,4))
        if x[1]:ev.append(((x[0],0,x[2]),1,5))
        for y,lam,k in ev:
            i=INDEX[y]
            assert i!=j
            Q[i,j]+=lam
            Q[j,j]-=lam
            J[k][i,j]+=lam
    return Q,J

def coeff(p):
    return list(map(int,S.Poly(S.expand(p),u).all_coeffs()))

def poly(cs):
    return S.Poly.from_list(cs,gens=u).as_expr()

C=json.loads(Path(__file__).with_name('certificate.json').read_text())
assert C['states']==[''.join(map(str,x)) for x in STATES]
Q,J=matrices(u)
assert all(S.expand(sum(Q[:,j]))==0 for j in range(N))
B=Q.copy(); B[-1,:]=S.ones(1,N)
unit=S.zeros(N,1);unit[-1]=1
INV=B.inv(); pi=INV*unit
assert all(S.factor(x)>0 for x in pi.subs(u,1))
assert all(S.cancel(z)==0 for z in Q*pi)
for k,name in [(0,'injection'),(1,'extraction'),(4,'adsorption'),(5,'desorption')]:
    d=C['channels'][name]
    mean=S.factor((S.ones(1,N)*J[k]*pi)[0])
    rhs=-(J[k]*pi-mean*pi);rhs[-1]=0
    r=INV*rhs
    f=S.cancel((mean+2*(S.ones(1,N)*J[k]*r)[0])/mean)
    n,den=S.fraction(f)
    assert coeff(n)==d['fano_num'],name
    assert coeff(den)==d['fano_den'],name
    a,b=S.fraction(S.cancel(mean))
    assert coeff(a)==d['mean_num'] and coeff(b)==d['mean_den'],name
    fder=S.cancel(S.diff(f,u))
    dn,dd=S.fraction(fder)
    content,primitive=S.Poly(dn,u).primitive()
    assert str(content)==d['derivative_factor'],name
    assert coeff(dd)==d['derivative_den'],name
    assert coeff(primitive.as_expr())==d['derivative_num_primitive'],name
    assert all(z>0 for z in d['derivative_den'])
    assert all(z>0 for z in d['fano_den'])
    signs=[1 if z>0 else -1 for z in d['derivative_num_primitive']]
    changes=sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
    assert changes=={'injection':0,'extraction':1,'adsorption':1,'desorption':2}[name]
    assert S.factor(S.limit(f,u,0,dir='+'))==S.Rational(d['derivative_limit_zero'])
    assert S.factor(S.limit(f,u,S.oo))==S.Rational(d['derivative_limit_infty'])
    if name=='extraction': assert primitive.eval(u,0)<0 and primitive.eval(u,3)>0
    if name=='adsorption': assert primitive.eval(u,0)<0 and primitive.eval(u,3)>0
    if name=='desorption':
        assert primitive.eval(u,0)>0 and primitive.eval(u,S.Rational(1,4))<0 and primitive.eval(u,1)>0
    for lo,hi,m in d['positive_root_brackets']:
        lo=S.Rational(lo);hi=S.Rational(hi)
        assert lo>0 and lo<hi and m==1
        assert primitive.eval(u,lo)*primitive.eval(u,hi)<0
    print(name, 'exact formulas and global derivative root count: PASS')

# Independent count-moment propagation check using a 24-state block ODE.
for val in (S.Rational(1,10),S.Rational(7,10),S.Rational(1),S.Rational(3),S.Rational(10)):
    Q0,Js0=matrices(val)
    Qa=np.array(Q0,float)
    for k,name in [(0,'injection'),(1,'extraction'),(4,'adsorption'),(5,'desorption')]:
        Ja=np.array(Js0[k],float)
        A=Qa.copy();A[-1,:]=1
        b=np.zeros(N);b[-1]=1
        p=np.linalg.solve(A,b)
        current=float((np.ones(N)@Ja@p))
        M=np.zeros((3*N,3*N))
        M[:N,:N]=Qa
        M[N:2*N,:N]=Ja
        M[N:2*N,N:2*N]=Qa
        M[2*N:,N:2*N]=2*Ja
        M[2*N:,:N]=Ja
        M[2*N:,2*N:]=Qa
        z0=np.zeros(3*N);z0[:N]=p
        t=500.
        z=expm(t*M)@z0
        m1=sum(z[N:2*N]);m2=sum(z[2*N:])
        estimated=(m2-m1*m1)/m1
        d=C['channels'][name]
        target=float(poly(d['fano_num']).subs(u,val)/poly(d['fano_den']).subs(u,val))
        assert abs(m1/t-current)<1.e-8,(name,val,m1/t,current)
        assert abs(estimated-target)<.007,(name,val,estimated,target)
print('20 independent finite-time count-moment propagation comparisons: PASS')
print('ALL CHECKS PASSED')
