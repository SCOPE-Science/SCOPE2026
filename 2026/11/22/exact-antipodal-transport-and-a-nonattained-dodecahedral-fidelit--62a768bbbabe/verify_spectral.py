"""Independent exact labelled-graph and spectral verification.
Run: python verify_spectral.py  (requires networkx, sympy).
"""
from collections import defaultdict
import networkx as nx
import sympy as S

FIVE = [('tetrahedron',nx.tetrahedral_graph()),
        ('cube',nx.cubical_graph()),
        ('octahedron',nx.octahedral_graph()),
        ('dodecahedron',nx.dodecahedral_graph()),
        ('icosahedron',nx.icosahedral_graph())]
TARGET = {
 'tetrahedron':{S.Integer(3):(1,None),S.Integer(-1):(3,None)},
 'cube':{S.Integer(3):(1,1),S.Integer(-3):(1,-1),S.Integer(1):(3,-1),S.Integer(-1):(3,1)},
 'octahedron':{S.Integer(4):(1,1),S.Integer(-2):(2,1),S.Integer(0):(3,-1)},
 'dodecahedron':{S.Integer(3):(1,1),S.Integer(-2):(4,1),S.Integer(1):(5,1),-S.sqrt(5):(3,-1),S.sqrt(5):(3,-1),S.Integer(0):(4,-1)},
 'icosahedron':{S.Integer(5):(1,1),S.Integer(-1):(5,1),-S.sqrt(5):(3,-1),S.sqrt(5):(3,-1)}
}
for name,G in FIVE:
    ids=sorted(G.nodes)
    A=S.Matrix([[int(G.has_edge(u,v)) for v in ids] for u in ids])
    n=len(ids)
    eig=A.eigenvals()
    assert {k:v for k,v in eig.items()}=={k:v[0] for k,v in TARGET[name].items()}, (name,eig)
    dist=dict(nx.all_pairs_shortest_path_length(G))
    dia=max(dist[ids[0]].values())
    antipodes=[ [v for v in ids if dist[u][v]==dia] for u in ids]
    P=S.zeros(n)
    if all(len(v)==1 for v in antipodes):
        for i,u in enumerate(ids):P[i,ids.index(antipodes[i][0])]=1
        assert P*P==S.eye(n) and P*A==A*P
    for lam,m in eig.items():
        E=S.eye(n)
        for mu in eig:
            if mu!=lam:E=E*(A-mu*S.eye(n))/(lam-mu)
        assert S.simplify(S.trace(E)-m)==0
        assert all(S.simplify(E[i,i]-S.Rational(m,n))==0 for i in range(n))
        if all(len(v)==1 for v in antipodes):
            sign=TARGET[name][lam][1]
            assert S.simplify(S.trace(P*E)-sign*m)==0,(name,lam)
            assert S.simplify(P*E-sign*E)==S.zeros(n)
    # Every non-antipodal pair has an eigenspace projector violating strong cospectrality.
    for i in range(n):
        for j in range(i+1,n):
            if all(len(v)==1 for v in antipodes) and ids[j]==antipodes[i][0]:continue
            witness=False
            for lam,m in eig.items():
                E=S.eye(n)
                for mu in eig:
                    if mu!=lam:E=E*(A-mu*S.eye(n))/(lam-mu)
                r=S.simplify(E[i,j]/E[i,i])
                if S.simplify(r*r-1)!=0: witness=True;break
            assert witness,(name,i,j)
    print(name,'n',n,'edges',G.number_of_edges(),'spectrum',eig,'nonantipodal exclusion PASS')

x=S.symbols('x',real=True)
# Cross-polytope octahedron amplitude and maximum 3/4.
co={-2:1,1:2,0:-3}
def modulus_poly(co):
    dd=defaultdict(int)
    for i,a in co.items():
        for j,b in co.items():dd[i-j]+=a*b
    return S.expand(dd[0]+sum(2*dd[k]*S.chebyshevt(k,x) for k in range(1,max(dd)+1)))
octpoly=modulus_poly(co)
assert S.factor(octpoly)==4*(x-1)**2*(4*x+5)
assert octpoly.subs(x,-S.Rational(1,2))==27
assert S.expand(S.diff(octpoly,x)-24*(x-1)*(2*x+1))==0

# Dodecahedral irrational two-frequency torus, optimized at phase cos(sqrt(5)t)=+1.
cp={-3:1,-1:5,2:4,0:-10}
cm={-3:1,-1:5,2:4,0:2}
Pplus=modulus_poly(cp)
assert S.factor(Pplus)==4*(x-1)**2*(32*x**3+64*x**2+76*x+53)
assert S.expand(S.diff(Pplus,x)-40*(x-1)*(2*x+1)*(8*x**2+4*x+3))==0
assert Pplus.subs(x,-S.Rational(1,2))==243
# Other torus endpoint contributes <= (1+5+4+2)^2=144 by triangle inequality.
assert sum(abs(v) for v in cm.values())**2==144
assert S.factor(modulus_poly(cm)-Pplus)!=0

# Constructive convergents to sqrt(5): alternating Pell equations and parity.
p0,p1,q0,q1=2,9,1,4
for r in range(16):
    if r==0:p,q=p0,q0
    elif r==1:p,q=p1,q1
    else:
        p0,p1=p1,4*p1+p0
        q0,q1=q1,4*q1+q0
        p,q=p1,q1
    assert p*p-5*q*q==(-1)**(r+1)
    assert (p-q)%2==1
    if r%2==1:assert q%2==0 and p%2==1
print('octahedral and dodecahedral exact extremum PASS; Pell sequence PASS')
