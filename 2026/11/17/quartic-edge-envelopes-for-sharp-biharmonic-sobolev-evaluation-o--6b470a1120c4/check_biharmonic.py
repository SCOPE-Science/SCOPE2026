"""Exact rational independent checks of the metric-graph H2 evaluation envelope.
Requires sympy. Executes both an unsubdivided endpoint formula and independently
re-solves the Kirchhoff graph after subdivision of the queried edge.
"""
from fractions import Fraction
import sympy as S
import random

def vertex_green(n,edges,source):
    # Each edge is (u,v,length) with rational positive length.
    T=sum((q for _,_,q in edges),S.Rational(0))
    L=S.zeros(n); b=S.zeros(n,1)
    b[source]=1
    for i,j,q in edges:
        L[i,i]+=1/q;L[j,j]+=1/q
        L[i,j]-=1/q;L[j,i]-=1/q
        b[i]-=q/(2*T);b[j]-=q/(2*T)
    v=S.Matrix(list(L[:n-1,:n-1].inv()*b[:n-1,0])+[S.Rational(0)])
    mass=sum((q*(v[i]+v[j])/2 -q**3/(12*T) for i,j,q in edges),S.Rational(0))
    v-=S.ones(n,1)*(mass/T)
    assert L*v==b
    assert S.simplify(sum((q*(v[i]+v[j])/2-q**3/(12*T) for i,j,q in edges),S.Rational(0)))==0
    return v

def pairing(va,vb,edges):
    T=sum((q for _,_,q in edges),S.Rational(0))
    ans=S.Rational(0)
    for i,j,q in edges:
        h=q*q/(2*T)
        a=[va[i],va[j]-va[i]-h,h]
        b=[vb[i],vb[j]-vb[i]-h,h]
        ans += q*sum((a[k]*b[l]/(k+l+1) for k in range(3) for l in range(3)),S.Rational(0))
    return S.factor(ans)

def envelope(va,vb,edges,e,t):
    i,j,ell=edges[e];T=sum((q for _,_,q in edges),S.Rational(0))
    Qa=pairing(va,va,edges);Qb=pairing(vb,vb,edges);Cab=pairing(va,vb,edges)
    A=va[i]; B=va[j];D=vb[j]
    assert va[j]==vb[i]
    poly= (1-t)**2*Qa+2*t*(1-t)*Cab+t**2*Qb +ell**2*t*(1-t)/(12*T)*(
       8*A*T+4*B*T-ell**2 +t*(-12*A*T+8*B*T+4*D*T-ell**2)
       +t**2*(4*A*T-8*B*T+4*D*T+ell**2)) +ell**3*t**2*(1-t)**2*(4*T-3*ell)/(12*T)
    return S.factor(poly)

def direct_subdivided(n,edges,e,t):
    assert 0<t<1
    i,j,ell=edges[e]
    es=edges[:e]+[(i,n,ell*t),(n,j,ell*(1-t))]+edges[e+1:]
    v=vertex_green(n+1,es,n)
    return pairing(v,v,es)

def test():
    cases=[(2,[(0,1,S.Rational(1))]),
      (2,[(0,1,S.Rational(1)),(0,1,S.Rational(2))]),
      (3,[(0,1,S.Rational(1)),(1,2,S.Rational(3,2))]),
      (3,[(0,1,S.Rational(1)),(1,2,S.Rational(2)),(2,0,S.Rational(3))]),
      (4,[(0,1,S.Rational(1)),(0,2,S.Rational(3,2)),(0,3,S.Rational(2))]),
      (4,[(0,1,S.Rational(1)),(1,2,S.Rational(2)),(2,3,S.Rational(3)),(3,0,S.Rational(2)),(0,2,S.Rational(3,2))]),
      (5,[(0,1,S.Rational(1)),(1,2,S.Rational(2)),(2,0,S.Rational(1)),(2,3,S.Rational(3)),(3,4,S.Rational(3,2)),(4,2,S.Rational(2))])]
    rg=random.Random(7)
    for n in range(3,6):
        for rep in range(1):
            edges=[]
            for v in range(1,n):
                edges.append((rg.randrange(v),v,S.Rational(rg.randint(1,7),rg.randint(1,4))))
            for i in range(n):
                for j in range(i+1,n):
                    if not any({x,y}=={i,j} for x,y,_ in edges) and rg.random()<.24:
                        edges.append((i,j,S.Rational(rg.randint(1,5),rg.randint(1,4))))
            cases.append((n,edges))
    count=0
    t=S.symbols('t')
    for n,edges in cases:
        vgreen=[vertex_green(n,edges,v) for v in range(n)]
        T=sum((q for _,_,q in edges),S.Rational(0))
        # Independent graph effective resistance: connected Laplacian solve voltage.
        L=S.zeros(n)
        for i,j,q in edges:
            L[i,i]+=1/q;L[j,j]+=1/q;L[i,j]-=1/q;L[j,i]-=1/q
        foster_sum=S.Rational(0)
        for e,(i,j,q) in enumerate(edges):
            Qa=pairing(vgreen[i],vgreen[i],edges)
            Qb=pairing(vgreen[j],vgreen[j],edges)
            poly=envelope(vgreen[i],vgreen[j],edges,e,t)
            assert S.expand(poly.subs(t,0)-Qa)==0
            assert S.expand(poly.subs(t,1)-Qb)==0
            vector=S.zeros(n,1);vector[i]=1;vector[j]=-1
            voltage=L[:n-1,:n-1].inv()*vector[:n-1,0]
            r=voltage[i]-(voltage[j] if j<n-1 else 0) if i<n-1 else 0-voltage[j]
            lead=S.Poly(poly,t).coeff_monomial(t**4)
            assert S.simplify(lead-q*q*(q-r-q*q/T)/3)==0
            foster_sum+=3*lead/q**3
            for tv in (S.Rational(1,5),S.Rational(2,5),S.Rational(1,2),S.Rational(4,5)):
                predicted=poly.subs(t,tv)
                direct=direct_subdivided(n,edges,e,tv)
                assert predicted==direct,(n,edges,e,tv,predicted,direct)
                count+=1
        assert S.simplify(foster_sum-(len(edges)-n))==0
    # Differentiate a closed-form interval example: the equality at endpoints
    # and its exact middle reduction follow without numerical spectral truncation.
    edges=[(0,1,S.Rational(1))];G0=vertex_green(2,edges,0);G1=vertex_green(2,edges,1)
    assert S.factor(envelope(G0,G1,edges,0,t))==S.Rational(1,45)-t**2*(1-t)**2/S.Integer(3) or S.simplify(envelope(G0,G1,edges,0,t)-(S.Rational(1,45)-t**2*(1-t)**2/S.Integer(3)))==0
    # A circle can be represented without loops by parallel edges; its norm is
    # homogeneous at every point and equals the inverse-square spectral sum.
    es=[(0,1,S.Rational(1)),(0,1,S.Rational(2))]
    vs=[vertex_green(2,es,i) for i in (0,1)]
    for e in range(2):
        assert S.simplify(envelope(vs[0],vs[1],es,e,t)-S.Rational(3)**3/720)==0
    print('TWO_EDGE_METRIC_CIRCLE_CONSTANT_PASSED')
    print('FOSTER_CYCLE_RANK_QUARTIC_SUMS_PASSED',len(cases))
    print('INDEPENDENT_SUBDIVIDED_GRAPH_GREEN_COMPARISONS_PASSED',count)
    print('EXACT_BIHARMONIC_QUARTIC_LEADING_COEFFICIENT_PASSED',sum(len(ed) for _,ed in cases))
    print('EXACT_INTERVAL_NEUMANN_BIHARMONIC_EXAMPLE_PASSED')
    print('ALL_BIHARMONIC_ENVELOPE_CHECKS_PASSED')

if __name__=='__main__':test()
