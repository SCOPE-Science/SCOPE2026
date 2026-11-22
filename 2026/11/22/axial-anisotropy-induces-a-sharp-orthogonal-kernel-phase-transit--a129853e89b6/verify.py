"""Exact-rational checks for the axially stretched octahedral orthogonal kernel.

All infinite-parameter claims have separate analytic proofs; these finite checks
exercise the explicit vertices, supporting planes and volume formulas.
"""
from fractions import Fraction as Q
from itertools import product, combinations

ZERO = Q(0)
ONE = Q(1)

def vec(*xs):
    return tuple(Q(x) for x in xs)

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def supporting_forms(s):
    s = Q(s)
    coefs = [(Q(2)/s,ONE,ONE), (ONE,ONE+s,ONE), (ONE,ONE,ONE+s)]
    return [(tuple(e[i]*c[i] for i in range(3)),i)
            for e in product((-1,1), repeat=3)
            for i,c in enumerate(coefs)]

def first_octant_vertices(s):
    s=Q(s)
    U=vec(s/2 if s<2 else 1,0,0)
    V=vec(0,1/(1+s),0)
    W=vec(0,0,1/(1+s))
    VW=vec(0,1/(2+s),1/(2+s))
    ans={'U':U,'V':V,'W':W,'VW':VW}
    if s<2:
        a=s*s/(s+2)
        b=(2-s)/(s+2)
        ans.update(UV=vec(a,b,0),UW=vec(a,0,b),
                   T=vec(s*s/4,(2-s)/4,(2-s)/4))
    return ans

def signed_vertices(s):
    out=set()
    for p in first_octant_vertices(s).values():
        for e in product((-1,1),repeat=3):
            out.add(tuple(p[i]*e[i] for i in range(3)))
    return out

def volume_ratio_from_tetrahedra(s):
    s=Q(s)
    v=first_octant_vertices(s)
    if s<2:
        faces=[('U','UV','T','UW'),('V','VW','T','UV'),
               ('W','UW','T','VW')]
        triangles=[(q[0],q[1],q[2]) for q in faces]+[(q[0],q[2],q[3]) for q in faces]
    else:
        triangles=[('U','V','VW'),('U','VW','W')]
    octant_volume=sum(abs(det3(*(v[k] for k in t))) for t in triangles)/6
    return 6*octant_volume

def predicted_ratio(s):
    s=Q(s)
    if s<=2:
        return s*(s**3-5*s*s+6*s+4)/(4*(s+1)*(s+2))
    return Q(2)/((s+1)*(s+2))

def is_facet(form,vertices):
    a,_=form
    on=[x for x in vertices if sum(a[i]*x[i] for i in range(3))==1]
    if len(on)<3:return False
    return any(det3(tuple(y[i]-x[i] for i in range(3)),
                    tuple(z[i]-x[i] for i in range(3)), a) !=0
               for x,y,z in combinations(on,3))

def all_projection_feet_inside(t,x):
    # All nonvertex faces; all coordinates and dot products remain exact.
    axes=(Q(t),ONE,ONE)
    for rank in (2,3):
        for I in combinations(range(3),rank):
            for e in product((-1,1),repeat=rank):
                H=sum(ONE/(axes[i]*axes[i]) for i in I)
                M=ONE-sum(Q(e[j])*x[i]/axes[i] for j,i in enumerate(I))
                for j,i in enumerate(I):
                    foot=x[i]+M*e[j]/(axes[i]*H)
                    if e[j]*foot<=0:
                        return False
    return True

def inequality_test(t,x):
    a=(Q(t),ONE,ONE)
    return all(sum(abs(x[j])/a[j]+a[i]*abs(x[i])/(a[j]*a[j])
                   for j in range(3) if j!=i)<1 for i in range(3))

def main():
    count=0
    for s in map(Q,('1/16','1/4','1/2','3/4','1','5/4','3/2','7/4','199/100','2','201/100','9/4','3','4','9','16')):
        verts=signed_vertices(s)
        requiredV=26 if s<2 else 10
        requiredF=24 if s<2 else 16
        assert len(verts)==requiredV,(s,len(verts))
        forms=supporting_forms(s)
        assert all(sum(a[i]*x[i] for i in range(3))<=1 for x in verts
                   for a,_ in forms)
        facets=[f for f in forms if is_facet(f,verts)]
        assert len(facets)==requiredF,(s,len(facets))
        assert volume_ratio_from_tetrahedra(s)==predicted_ratio(s)
        deficit=Q(1,4)-predicted_ratio(s)
        if s<=2:
            expected=(s-1)**2*(2+3*s-s*s)/(4*(s+1)*(s+2))
        else:
            expected=(s*s+3*s-6)/(4*(s+1)*(s+2))
        assert deficit==expected and deficit>=0
        count+=1
    # Direct face-projection criterion at rational physical aspect ratios.
    checked=0
    for t in (Q(1,2),Q(1),Q(2)):
        for x0,x1,x2 in product((Q(j,8) for j in range(-8,9)),repeat=3):
            x=(x0*t,x1,x2)
            if abs(x0)+abs(x1)+abs(x2)>=1:
                continue
            assert all_projection_feet_inside(t,x)==inequality_test(t,x), (t,x)
            checked+=1
    print('PASS: 16 exact-rational polytope cases; volume, deficits, vertices and facets')
    print('PASS:',checked,'all-face projection equivalence tests')

if __name__=='__main__':main()
