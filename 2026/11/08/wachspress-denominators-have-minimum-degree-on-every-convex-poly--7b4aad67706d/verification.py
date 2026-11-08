"""Exact algebraic checks for the planar Wachspress-denominator theorem."""
from fractions import Fraction
import sympy as s

x,y=s.symbols('x y')

def polygon_wachspress(V):
    V=[tuple(map(s.Rational,p)) for p in V]
    n=len(V)
    def det(a,b): return a[0]*b[1]-a[1]*b[0]
    E=[(V[(i+1)%n][0]-V[i][0],V[(i+1)%n][1]-V[i][1]) for i in range(n)]
    L=[s.expand(det(E[i],(x-V[i][0],y-V[i][1]))) for i in range(n)]
    k=[det(E[(i-1)%n],E[i]) for i in range(n)]
    assert all(z>0 for z in k), 'Polygon must be strictly convex and CCW'
    w=[s.expand(k[i]*s.prod(L[j] for j in range(n) if j not in ((i-1)%n,i))) for i in range(n)]
    q=s.Poly(s.expand(sum(w)),x,y)
    assert s.expand(sum(w[i]*V[i][0] for i in range(n))-x*q.as_expr())==0
    assert s.expand(sum(w[i]*V[i][1] for i in range(n))-y*q.as_expr())==0
    for i in range(n):
        assert w[i].subs({x:V[i][0],y:V[i][1]})==q.as_expr().subs({x:V[i][0],y:V[i][1]})
        assert q.as_expr().subs({x:V[i][0],y:V[i][1]})>0
    for i in range(n):
        t=s.Symbol('t')
        subs={x:V[i][0]+t*E[i][0],y:V[i][1]+t*E[i][1]}
        nonadj=[j for j in range(n) if j not in ((i-1)%n,i,(i+1)%n)]
        rhs=k[i]*k[(i+1)%n]*s.prod(L[j] for j in nonadj)
        assert s.expand((q.as_expr()-rhs).subs(subs))==0, (i, title if 'title' in locals() else '')
    for i in range(n):
        # Each nonadjacent, nonparallel facet intersection is a distinct zero of q on L_i.
        points=[]
        for j in range(n):
            if j in ((i-1)%n,i,(i+1)%n):continue
            sol=s.solve_poly_system([L[i],L[j]],x,y)
            if sol:
                assert len(sol)==1
                point=sol[0]
                assert point not in points
                points.append(point)
                assert q.as_expr().subs({x:point[0],y:point[1]})==0
        assert q.as_expr().subs({x:V[i][0]+s.Symbol('t')*E[i][0],y:V[i][1]+s.Symbol('t')*E[i][1]})!=0
    return q

def hexagon(t,z):
    return [(t,0),(1,0),(1,z-1),(z-1,1),(0,1),(0,t)]

cases=[('triangle',[(0,0),(1,0),(0,1)],0),
       ('parallelogram',[(0,0),(2,0),(3,1),(1,1)],0),
       ('trapezoid',[(0,0),(2,0),(3,1),(0,1)],1),
       ('pentagon',[(0,0),(2,0),(3,1),(1,3),(-1,2)],2),
       ('central hexagon',hexagon(s.Rational(1,3),s.Rational(5,3)),2),
       ('noncentral paired hexagon',hexagon(s.Rational(1,5),s.Rational(3,2)),3)]
for title,vertices,degree in cases:
    q=polygon_wachspress(vertices)
    assert q.total_degree()==degree,(title,q)
    print(title,'facets',len(vertices),'denominator degree',q.total_degree(),'terms',len(q.terms()))
print('PASS: all exact symbolic Wachspress identities, degrees, residual zeros, and vertex nonvanishing')

def residual_conic_rank(V):
    V=[tuple(map(s.Rational,p)) for p in V]
    E=[(V[(i+1)%len(V)][0]-V[i][0],V[(i+1)%len(V)][1]-V[i][1]) for i in range(len(V))]
    def det(a,b): return a[0]*b[1]-a[1]*b[0]
    L=[s.expand(det(E[i],(x-V[i][0],y-V[i][1]))) for i in range(len(V))]
    rows=[]
    for i in range(len(V)):
        for j in range(i+1,len(V)):
            if (j-i)%len(V) in (1,len(V)-1):continue
            v=s.solve_poly_system([L[i],L[j]],x,y)
            if v:
                a,b=v[0]
                rows.append([1,a,b,a*a,a*b,b*b])
    return len(rows),s.Matrix(rows).rank()
assert residual_conic_rank(hexagon(s.Rational(1,3),s.Rational(5,3)))==(6,5)
assert residual_conic_rank(hexagon(s.Rational(1,5),s.Rational(3,2)))==(6,6)
print('PASS: exact residual conic matrix rank is 5 for symmetric and 6 for noncentral parallel-paired hexagon')
