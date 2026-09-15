import sympy as sp
x,y=sp.symbols('x y')
from collections import defaultdict
def add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,0)+v
        if c[k]==0: del c[k]
    return c
def mul(a,b):
    c=defaultdict(int)
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            c[(k1[0]+k2[0],k1[1]+k2[1])]+=v1*v2
    return {k:v for k,v in c.items() if v!=0}
def pw(a,n):
    r={(0,0):1}
    for _ in range(n): r=mul(r,a)
    return r
def mutate_laurent(Wd, v):
    v1,v2=v
    M=(v2,-v1)
    exps=[-u[0]*v1-u[1]*v2 for u in Wd]
    N=max([0]+[-e for e in exps if e<0])
    F={(0,0):1,(M[0],M[1]):1}
    num={(0,0):0}
    for u,c in Wd.items():
        e=-u[0]*v1-u[1]*v2
        num=add(num,mul({u:c}, pw(F,e+N)))
    if (0,0) in num and num[(0,0)]==0: del num[(0,0)]
    den=pw(F,N)
    num_e=sum(c*x**a*y**b for (a,b),c in num.items())
    den_e=sum(c*x**a*y**b for (a,b),c in den.items())
    R=sp.cancel(num_e/den_e)
    n2,d2=sp.fraction(R)
    n2=sp.expand(n2); d2=sp.expand(d2)
    try:
        td=sp.Poly(d2,x,y).as_dict()
    except Exception:
        return None
    if len(td)!=1: return None
    (ea,eb),cc=next(iter(td.items()))
    if abs(int(cc))!=1: return None
    try:
        qd=sp.Poly(n2,x,y).as_dict()
    except Exception:
        return None
    Qd={(a-ea,b-eb):int(cc2) for (a,b),cc2 in qd.items() if cc2!=0}
    if mul(Qd,den)!=num:
        return None
    return Qd
def trop(u,v):
    s=u[0]*v[1]-u[1]*v[0]
    m=s if s>0 else 0
    return (u[0]+m*v[0], u[1]+m*v[1])
def mutate_seed(Wd, dirs, j):
    vj=dirs[j]
    W2=mutate_laurent(Wd,vj)
    if W2 is None: return None
    nd=[]
    for i,u in enumerate(dirs):
        if i==j: nd.append((-vj[0],-vj[1]))
        else: nd.append(trop(u,vj))
    return W2,nd
