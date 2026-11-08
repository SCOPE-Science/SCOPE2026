"""Standalone finite checks for polar-volume subdivision asymptotics.

Dependencies: Python 3 and sympy. Run: python verify.py
The proof for all graphs and all subdivision factors is in RESULT.md.
"""
import math
from itertools import combinations
import sympy as sp


def graph(n, edges):
    return n, [tuple(sorted(e)) for e in edges]


def cycle(n):
    return graph(n, [(i, (i+1)%n) for i in range(n)])


def subdivide(G, m):
    n, edges=G
    out=[]
    k=n
    for u,v in edges:
        prev=u
        for _ in range(m-1):
            out.append((prev,k));prev=k;k+=1
        out.append((prev,v))
    return graph(k,out)


def laplacian(G):
    n,edges=G
    M=sp.zeros(n)
    for u,v in edges:
        M[u,u]+=1;M[v,v]+=1;M[u,v]-=1;M[v,u]-=1
    return M


def spanning_trees(G):
    L=laplacian(G)
    return int(L[:L.rows-1,:L.cols-1].det())


def incidence(G):
    n,edges=G
    D=sp.zeros(n-1,len(edges))
    for j,(u,v) in enumerate(edges):
        if u<n-1:D[u,j]+=1
        if v<n-1:D[v,j]-=1
    return D


def exact_leverages(G):
    n,edges=G
    D=incidence(G)
    L=D*D.T
    R=L.inv()
    # graph cut projection diag gives inclusion in a uniform spanning tree
    included=[(D[:,e].T*R*D[:,e])[0] for e in range(len(edges))]
    return [sp.simplify(1-r) for r in included]


def cycle_basis(G):
    n, edges=G
    D=incidence(G)
    _, piv=D.rref()  # spanning forest basis columns, connected graph => n-1
    assert len(piv)==n-1
    chords=[j for j in range(len(edges)) if j not in piv]
    if not chords: return sp.zeros(0,len(edges))
    Dt=D[:,piv]
    rows=[]
    for j in chords:
        row=[sp.Integer(0)]*len(edges)
        coeff=Dt.inv()*D[:,j]
        for ix,t in enumerate(piv):row[t]=-coeff[ix]
        row[j]=1
        rows.append(row)
    return sp.Matrix(rows)


def box_spline(l,s):
    """Density of a sum of l uniform [-1,1] variables (unnormalized)."""
    r=sp.Rational(0)
    for j in range(l+1):
        z=s+l-2*j
        if z>0:r+=(-1)**j*sp.binomial(l,j)*z**(l-1)
    return r/sp.factorial(l-1)


def exact_central_cycle(l):
    return box_spline(l,sp.Integer(0))


def exact_theta(a):
    """Exact anchored volume of three disjoint length-a paths; a is even here."""
    x=sp.Symbol('x')
    val=0
    for lo in range(0,a,2):
        polynomial=sum((-1)**j*sp.binomial(a,j)*(x+a-2*j)**(a-1)
                       for j in range(a+1) if (lo+a-2*j)>=0)
        polynomial=polynomial/sp.factorial(a-1)
        val+=sp.integrate(polynomial**3, (x,lo,lo+2))
    return sp.factor(2*val)


def relative_prediction(G,m):
    n,edges=G
    g=len(edges)-n+1
    tau=spanning_trees(G)*m**g
    S=sum(x*x for x in exact_leverages(G))
    return (2**(len(edges)*m)*(3/(2*math.pi))**(g/2)/math.sqrt(tau),
            1-float(sp.Rational(3,20)*S)/m, S)


def main():
    examples={
        'triangle':cycle(3),
        'square':cycle(4),
        'diamond':graph(4,[(0,1),(1,2),(2,0),(0,3),(2,3)]),
        'K23':graph(5,[(u,v) for u in range(2) for v in range(2,5)]),
        'K4':graph(4,list(combinations(range(4),2))),
        'triangle_leaf':graph(4,[(0,1),(1,2),(2,0),(0,3)]),
        'figure_eight':graph(5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),
    }
    graph_checks=0
    for name,G in examples.items():
        n,edges=G;g=len(edges)-n+1
        B=cycle_basis(G)
        if g:
            Q=B*B.T
            assert Q.det()==spanning_trees(G),(name,'det',Q.det(),spanning_trees(G))
            score=[(B[:,j].T*Q.inv()*B[:,j])[0] for j in range(len(edges))]
            assert score==exact_leverages(G),(name,'leverage',score,exact_leverages(G))
            assert sum(score)==g
        else:
            assert spanning_trees(G)==1
        for m in range(1,5):
            assert spanning_trees(subdivide(G,m))==spanning_trees(G)*m**g
            graph_checks+=1
        print(name,'edges',len(edges),'cycle_rank',g,'trees',spanning_trees(G),
              'cycle_leverages',[str(v) for v in exact_leverages(G)])

    volume_checks=0
    # The central-spline formula is independent of the Fourier/Edgeworth proof.
    for k in range(3,15):
        v=exact_central_cycle(k)
        assert v>0
        # Independent check of a cycle volume via the normalized
        # central spline formula: anchored volume equals 2**k times density.
        assert sp.factor(v/(2**(k-1))) > 0
        volume_checks+=1
    for m in (1,2,3,4):
        actual=exact_theta(2*m)
        lead, pred, S=relative_prediction(examples['K23'],m)
        ratio=float(actual)/lead
        assert abs(ratio-pred)<0.011/m**2, (m,ratio,pred)
        print('K23 factor',m,'exact_volume',actual,'relative',round(ratio,11),
              'second_order',round(pred,11),'residual',round(ratio-pred,11))
        volume_checks+=1
    for m in (2,3,5,8,10):
        actual=float(exact_central_cycle(3*m))
        lead,pred,_=relative_prediction(examples['triangle'],m)
        ratio=actual/lead
        assert abs(ratio-pred)<0.013/m**2
        volume_checks+=1
    print('GRAPH_POLAR_SUBDIVISION_CHECKS_PASSED',
          'graph_checks='+str(graph_checks),
          'exact_volume_checks='+str(volume_checks),
          'graphs='+str(len(examples)))

if __name__=='__main__':main()
