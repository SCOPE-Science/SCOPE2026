"""Reproducible numerical diagnostics for equal-tangent observers of ellipsoids.

Pure Python 3, no external packages. Tangency is imposed algebraically:
for the ellipsoid with semiaxes a_i and apex p, the tangency points are
(a_i u_i) where |u|=1 and sum (p_i/a_i)u_i=1.
This diagnostic does not replace the theorem's all-observer proof.
"""
import math

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(v): return math.sqrt(dot(v,v))
def sub(a,b): return [x-y for x,y in zip(a,b)]
def mul(a,c): return [c*x for x in a]

def basis_perp(b):
    q=mul(b,1.0/norm(b))
    out=[]
    for k in range(len(b)):
        v=[float(k==i) for i in range(len(b))]
        v=sub(v,mul(q,dot(v,q)))
        for w in out: v=sub(v,mul(w,dot(v,w)))
        r=norm(v)
        if r>1e-9: out.append(mul(v,1.0/r))
    assert len(out)==len(b)-1
    return out

def squared_lengths(axes,p,samples=512):
    b=[x/a for x,a in zip(p,axes)]
    N2=dot(b,b); assert N2>1
    rho=math.sqrt(1-1/N2)
    center=mul(b,1/N2)
    basis=basis_perp(b)
    if len(axes)==2:
        vlist=[basis[0],mul(basis[0],-1.0)]
    else:
        vlist=[ [math.cos(2*math.pi*k/samples)*basis[0][i]+math.sin(2*math.pi*k/samples)*basis[1][i] for i in range(len(b))] for k in range(samples)]
    result=[]
    for v in vlist:
        u=[center[i]+rho*v[i] for i in range(len(b))]
        t=[axes[i]*u[i] for i in range(len(b))]
        assert abs(dot(u,u)-1)<1e-10
        assert abs(dot(b,u)-1)<1e-10
        result.append(dot(sub(p,t),sub(p,t)))
    return result

def test():
    cases=[
      ((3,2,1),(0,0,4),False), ((3,2,1),(3.5,0,0),False),
      ((3,2,1),(3,0,1.6),False), ((3,3,1),(0,0,2),True),
      ((3,3,1),(4,0,0),False), ((2,2,2),(3,0,0),True),
      ((3,2),(3.5,0),True), ((3,2),(0,2.5),True),
      ((3,2),(3,2),False), ((4,3,3,3),(5,0,0,0),True),
      ((4,3,2,1),(5,0,0,0),False),
    ]
    for axes,p,want in cases:
        vals=squared_lengths(axes,p)
        spread=max(vals)-min(vals)
        assert (spread<1e-10)==want,(axes,p,spread,want)
        print('dimension',len(axes),'axes',axes,'apex',p,'squared-length spread',format(spread,'.12g'))
    print('11 diagnostic scenarios passed')

if __name__=='__main__': test()
