"""Exact checks for a mean-zero Sobolev evaluation theorem on equilateral complete bipartite metric graphs.

Requires Python 3 and SymPy. This finite checker supports, but does not replace,
the symbolic proof of the formula for arbitrary integers m,n >= 2.
"""
from sympy import (symbols, Rational, factor, simplify, Matrix, zeros,
                   limit, oo)

m,n,t=symbols('m n t',integer=True,positive=True)
L=m*n
D=m*n-m-n
quad=(3*m-2)/(3*m*n)+(n-2)*t/n-D*t*t/(m*n)
base_A=(1-t)/n
base_B=(Rational(1,2)-t)/(m*n)
base_b=base_B+t/m
mass_degree=n*base_A+m*(n*base_B+t/m)
shift=(Rational(1,6)-t*(1-t)-mass_degree)/(2*L)
# This is the exact point-source Green value on a distinguished edge.
green=(1-t)*(base_A+shift)+t*(base_b+shift)+t*(1-t)*(1-Rational(1,2)/L)
assert simplify(green-quad)==0
assert simplify(mass_degree-(Rational(3,2)-t))==0
assert simplify(shift-(t*t-Rational(4,3))/(2*L))==0
star=m*(n-2)/(2*D)
sharp=(3*m*m*n*n-20*m*n+8*m+8*n)/(12*m*n*D)
assert simplify(quad-(sharp-D/(m*n)*(t-star)**2))==0
assert simplify(star-Rational(1,2)-(n-m)/(2*D))==0
assert simplify(sharp-sharp.xreplace({m:n,n:m}))==0
assert simplify(sharp.subs(m,2)-(3*n-2)/(6*n))==0
assert simplify(quad.subs({m:2,n:2})-Rational(1,3))==0
assert simplify(limit(sharp,n,oo)-m/(4*(m-1)))==0
assert limit(limit(sharp,n,oo),m,oo)==Rational(1,4)
print('SYMBOLIC_ALL_DIMENSIONS_CHECKS_PASSED')

def exact_subdivision_green(ma,nb,x):
    """Independent network construction: insert x as a new Kirchhoff node."""
    x=Rational(x)
    assert 0<x<1
    N=ma+nb
    src=N
    edges=[]
    for i in range(ma):
        for j in range(nb):
            u,v=i,ma+j
            if i==0 and j==0:
                edges.extend([(u,src,x),(src,v,1-x)])
            else:
                edges.append((u,v,Rational(1)))
    length=sum([e[2] for e in edges], Rational(0))
    assert length==ma*nb
    Q=zeros(N+1)
    half=[Rational(0) for _ in range(N+1)]
    cubes=Rational(0)
    for u,v,ell in edges:
        Q[u,u]+=1/ell
        Q[v,v]+=1/ell
        Q[u,v]-=1/ell
        Q[v,u]-=1/ell
        half[u]+=ell/2
        half[v]+=ell/2
        cubes+=ell**3
    rhs=Matrix([(int(i==src)-half[i]/length) for i in range(N+1)])
    assert sum(rhs)==0
    # Ground vertex zero, then select unique arclength-mean-zero translate.
    u=Matrix([Rational(0)]+list(Q[1:,1:].inv()*rhs[1:,:]))
    assert Q*u==rhs
    integral=sum((ell*(u[a]+u[b])/2-ell**3/(12*length) for a,b,ell in edges), Rational(0))
    translate=-integral/length
    g=u[src]+translate
    energy=sum(((u[b]-u[a])**2/ell+ell**3/(12*length**2) for a,b,ell in edges),Rational(0))
    assert energy==g
    return g

count=0
for M in range(2,7):
    for N in range(2,7):
        xs=[Rational(1,4),Rational(1,2),Rational(3,4)]
        if M*N-M-N>0:
            xs.append(Rational(M*(N-2),2*(M*N-M-N)))
        for x in set(z for z in xs if 0<z<1):
            expected=quad.subs({m:M,n:N,t:x})
            actual=exact_subdivision_green(M,N,x)
            assert actual==expected,(M,N,x,actual,expected)
            count+=1
        if (M,N)!=(2,2):
            xt=Rational(M*(N-2),2*(M*N-M-N))
            assert 0<=xt<=1
            assert factor(quad.subs({m:M,n:N,t:xt})-sharp.subs({m:M,n:N}))==0
            if M>2 and N>2:
                assert 0<xt<1
print('EXACT_SUBDIVISION_AND_ENERGY_CHECKS_PASSED',count)
print('ALL_COMPLETE_BIPARTITE_SOBOLEV_CHECKS_PASSED')
