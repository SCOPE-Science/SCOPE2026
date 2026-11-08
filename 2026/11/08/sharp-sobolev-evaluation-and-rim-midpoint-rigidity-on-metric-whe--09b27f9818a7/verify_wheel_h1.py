"""Independent rational PDE check for the squared evaluation norm on unit metric wheels.
Run with Python 3 and SymPy: python verify_wheel_h1.py

For each selected observation point, independently split the observed metric
edge and solve the Kirchhoff Poisson problem with constant arclength forcing.
The evaluation is read from its mean-zero solution, not from the projection
formula used in the accompanying analysis.
"""
from fractions import Fraction
from sympy import Matrix, Rational, eye, ones, simplify


def wheel_edges(m):
    # Hub index zero; cyclic rim vertices 1,...,m.
    return [(0,i) for i in range(1,m+1)] + [
        (i,1+i%m) for i in range(1,m+1)]


def weighted_laplacian(v,edges):
    L=Matrix.zeros(v,v)
    for a,b,length in edges:
        c=1/length
        L[a,a]+=c;L[b,b]+=c;L[a,b]-=c;L[b,a]-=c
    return L


def pde_evaluation(m,edge,t):
    """Solve -g''=delta_x-ds/(2m), integral g=0, return g(x)."""
    base=wheel_edges(m)
    ecount=len(base)
    Ltotal=Rational(ecount)
    a,b=base[edge]
    t=Rational(t)
    if t==0:
        x=a; edges=[(v,w,Rational(1)) for v,w in base]; n=m+1
    elif t==1:
        x=b; edges=[(v,w,Rational(1)) for v,w in base]; n=m+1
    else:
        x=m+1; n=m+2
        edges=[(v,w,Rational(1)) for i,(v,w) in enumerate(base) if i!=edge]
        edges.extend(((a,x,t),(x,b,1-t)))
    L=weighted_laplacian(n,edges)
    atom=Matrix.zeros(n,1); atom[x]=1
    mean_coeff=Matrix.zeros(n,1)
    for a,b,length in edges:
        mean_coeff[a]+=length/(2*Ltotal)
        mean_coeff[b]+=length/(2*Ltotal)
    rhs=atom-mean_coeff
    assert sum(rhs)==0
    Q=ones(n,n)/n
    vals=(L+Q).inv()*rhs
    # On each segment the unique solution is a linear interpolation plus
    # s(s-length)/(2*Ltotal); the exact integral of that parabola is
    # -length**3/(12*Ltotal).
    integral=0
    for a,b,length in edges:
        integral+=length*(vals[a]+vals[b])/2-length**3/(12*Ltotal)
    answer=simplify(vals[x]-integral/Ltotal)
    return answer


def graph_resolvent(m):
    edges=[(a,b,Rational(1)) for a,b in wheel_edges(m)]
    L=weighted_laplacian(m+1,edges)
    H=(L+ones(m+1,m+1)/(m+1)).inv()-ones(m+1,m+1)/(m+1)
    return simplify(H[0,0]+H[1,1]-2*H[0,1])


def expected(m,ty,t,u):
    t=Rational(t)
    hub=Rational(9,16*m)
    rim=u-Rational(15,16*m)
    constant=Rational(1,24*m)
    if ty=='spoke':
        return simplify(hub+(rim-hub)*t+(1-u-Rational(1,2*m))*t*(1-t)+constant)
    return simplify(rim+(u-Rational(1,2*m))*t*(1-t)+constant)


def main():
    cases=0
    for m in range(3,12):
        u=graph_resolvent(m)
        assert u>Rational(4,9) and u<=Rational(1,2)
        optimal_spoke=simplify((1-Rational(2,m))/(2*(1-u-Rational(1,2*m))))
        assert 0<optimal_spoke<1
        for typ,edge in [('spoke',0),('rim',m)]:
            for t in [0,Rational(1,4),Rational(1,2),Rational(3,4),1] + ([optimal_spoke] if typ=='spoke' else []):
                val=pde_evaluation(m,edge,t)
                want=expected(m,typ,t,u)
                assert val==want,(m,typ,t,val,want)
                cases+=1
        rimpeak=expected(m,'rim',Rational(1,2),u)
        spokepeak=expected(m,'spoke',optimal_spoke,u)
        if m==3: assert spokepeak==rimpeak==Rational(41,144)
        else: assert rimpeak>spokepeak
        assert rimpeak==5*u/4-Rational(49,48*m)
    print('EXACT_CENTERED_KIRCHHOFF_POISSON_CHECKS_PASSED',cases)
    print('EXACT_RIM_SPOKE_GAP_AND_EXTREMIZER_CHECKS_PASSED',9)
    print('ALL_METRIC_WHEEL_SOBOLEV_CHECKS_PASSED')

if __name__=='__main__':
    main()
