"""Exact symbolic diagnostics for polygon-product barycentric denominators."""
import sympy as s
from itertools import combinations

def poly_data(vertices, x, y):
    V=[(s.Rational(a),s.Rational(b)) for a,b in vertices]
    m=len(V)
    edges=[(V[(i+1)%m][0]-V[i][0],V[(i+1)%m][1]-V[i][1]) for i in range(m)]
    cross=lambda a,b:a[0]*b[1]-a[1]*b[0]
    turns=[cross(edges[i-1],edges[i]) for i in range(m)]
    assert all(c>0 for c in turns), (V,turns)
    ell=[e[0]*(y-V[i][1])-e[1]*(x-V[i][0]) for i,e in enumerate(edges)]
    p=[s.expand(turns[i]*s.prod(ell[j] for j in range(m) if j not in ((i-1)%m,i))) for i in range(m)]
    q=s.expand(sum(p))
    assert all(s.expand(sum(p[i]*V[i][z] for i in range(m))-(x if z==0 else y)*q)==0 for z in (0,1))
    assert all(s.expand(p[i].subs({x:a,y:b})- (q.subs({x:a,y:b}) if i==j else 0))==0 for j,(a,b) in enumerate(V) for i in range(m))
    return ell,q,p

def residuals(ell,x,y):
    m=len(ell); out=[]
    for i,j in combinations(range(m),2):
        if (i-j)%m in (1,m-1): continue
        solution=s.solve([ell[i],ell[j]],(x,y),dict=True)
        if solution:out.append((solution[0][x],solution[0][y]))
    return sorted(set(out))

def min_deg_by_interpolation(pts,x,y,degree_cap=5):
    # Finite rational-point vanishing: find least nonzero polynomial degree.
    for degree in range(degree_cap+1):
        monomials=[x**i*y**j for i in range(degree+1) for j in range(degree+1-i)]
        mat=s.Matrix([[f.subs({x:a,y:b}) for f in monomials] for a,b in pts])
        if mat.rank()<len(monomials):return degree
    raise RuntimeError('degree cap insufficient')

def check(name,vertices,expected):
    x,y=s.symbols('x y')
    ell,q,p=poly_data(vertices,x,y)
    pts=residuals(ell,x,y)
    actual=s.Poly(q,x,y).total_degree()
    minimum=min_deg_by_interpolation(pts,x,y)
    assert actual==expected==minimum,(name,actual,expected,minimum)
    print(name, 'm',len(vertices),'residual',len(pts),'adjoint-degree',actual,'minimum-residual-degree',minimum)
    return (q,p,vertices)

square=check('parallelogram',[(0,0),(3,0),(3,2),(0,2)],0)
quad=check('generic-quad',[(0,0),(3,0),(4,2),(-1,3)],1)
trapezoid=check('trapezoid',[(0,0),(4,0),(3,2),(1,2)],1)
pentagon=check('pentagon',[(0,0),(3,0),(4,2),(2,4),(-1,3)],2)
hexagon=check('symmetric-hexagon',[(2,0),(1,2),(-1,2),(-2,0),(-1,-2),(1,-2)],2)

# Check product affine precision and nonnegative vertex normalization
x,y,z,t=s.symbols('x y z t')
q1,p1,v1=quad;q2,p2,v2=trapezoid
Q=s.expand(q1.subs({'x':x,'y':y})*q2.subs({'x':z,'y':t}))
P=[s.expand(a.subs({'x':x,'y':y})*b.subs({'x':z,'y':t})) for a in p1 for b in p2]
assert s.expand(sum(P)-Q)==0
assert s.Poly(Q,x,y,z,t).total_degree()==2
for k,target in enumerate((x,y,z,t)):
    coords=[(a[0],a[1],b[0],b[1])[k] for a in v1 for b in v2]
    assert s.expand(sum(A*coord for A,coord in zip(P,coords))-target*Q)==0
print('product two nonparallelogram quadrilaterals: 16 numerators, degree exactly 2, affine precision verified')
print('all exact symbolic checks passed')
