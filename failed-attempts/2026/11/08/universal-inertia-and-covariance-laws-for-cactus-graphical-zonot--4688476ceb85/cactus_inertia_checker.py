"""Exact, standalone tests of uniform-volume second moments for cactus graphical zonotopes.
Uses only the Python standard library; run with python3 cactus_inertia_checker.py.
The cycle moments are integrated independently over all permutation simplices.
"""
from fractions import Fraction as F
from itertools import permutations, combinations, product
from math import factorial


def blank(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def outer_add(m, v, w=F(1)):
    for i, vi in enumerate(v):
        for j, vj in enumerate(v):
            m[i][j] += w * vi * vj


def cycle_chamber_covariance(n, edges):
    """Actual simplicial integration on the projected edge coefficient cube."""
    k = len(edges)
    total = blank(n)
    means = [F(0)] * n
    for perm in permutations(range(k)):
        vertices = []
        for j in range(1, k):
            low = set(perm[:j])
            y = [F(j, k) if h not in low else F(j-k, k) for h in range(k)]
            v = [F(0)] * n
            for h, (u, w) in enumerate(edges):
                v[u] += y[h]
                v[w] -= y[h]
            vertices.append(v)
        vs = [sum((v[i] for v in vertices), F(0)) for i in range(n)]
        for i in range(n):
            means[i] += vs[i] / (k * factorial(k))
        weight = F(1, factorial(k) * k * (k+1))
        outer_add(total, vs, weight)
        for v in vertices:
            outer_add(total, v, weight)
    assert all(m == 0 for m in means)
    return total


def cov_cactus(n, bridges, cycles):
    m = blank(n)
    for a, b in bridges:
        v = [F(0)] * n; v[a]=1; v[b]=-1
        outer_add(m, v, F(1,12))
    for cycle in cycles:
        cm = cycle_chamber_covariance(n, cycle)
        for i in range(n):
            for j in range(n):
                m[i][j] += cm[i][j]
    return m


def laplace_pred(n, bridges, cycles):
    m = blank(n)
    for a,b in bridges:
        v=[F(0)]*n;v[a]=1;v[b]=-1
        outer_add(m,v,F(1,12))
    for cycle in cycles:
        k=len(cycle)
        for a,b in cycle:
            v=[F(0)]*n;v[a]=1;v[b]=-1
            outer_add(m,v,F(k+2,12*k))
    return m


def det(a):
    m=[list(row) for row in a]; n=len(m); p=F(1)
    for j in range(n):
        t=next((i for i in range(j,n) if m[i][j]),None)
        if t is None:return F(0)
        if t!=j:m[t],m[j]=m[j],m[t];p=-p
        q=m[j][j];p*=q
        for i in range(j+1,n):
            z=m[i][j]/q
            for h in range(j+1,n):m[i][h]-=z*m[j][h]
            m[i][j]=F(0)
    return p


def tree_count(n, es):
    count=0
    for eds in combinations(es,n-1):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for u,v in eds:
            ru,rv=root(u),root(v)
            if ru!=rv:parent[ru]=rv
        count+=len({root(i) for i in range(n)})==1
    return count


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))


def diff(x,y):return tuple(a-b for a,b in zip(x,y))


def diamond_direct_tetrahedra():
    """Independent exhaustive exact 3D face enumeration and radial tetrahedral integration."""
    n=4;es=[(0,1),(1,2),(2,0),(1,3),(2,3)]
    pts=set()
    for sigs in product((-1,1), repeat=len(es)):
        v=[0]*n
        for (u,w),sg in zip(es,sigs):v[u]+=sg;v[w]-=sg
        pts.add(tuple(F(z,2) for z in v))
    pts=sorted(pts)
    fs={}
    for aa,bb,cc in combinations(range(len(pts)),3):
        a,b,c=[pts[i][:3] for i in (aa,bb,cc)]
        N=cross(diff(b,a),diff(c,a))
        if not any(N):continue
        d=dot(N,a)
        vals=[dot(N,p[:3])-d for p in pts]
        if max(vals)>0 and min(vals)<0:continue
        if max(vals)>0:N=tuple(-x for x in N);d=-d;vals=[-x for x in vals]
        # all vertices now satisfy N*p<=d; origin strict interior implies d>0
        assert d>0
        face=frozenset(i for i,v in enumerate(vals) if v==0)
        if len(face)>=3:fs[face]=N
    assert len(fs)==12,(len(fs), [len(f) for f in fs])
    vol=F(0);moment=F(0);ntet=0
    for face, normal in fs.items():
        # Exactly project the face to two independent coordinates and take its planar convex hull.
        coords = (0,1) if normal[2] else ((0,2) if normal[1] else (1,2))
        nodes=sorted((pts[i][coords[0]],pts[i][coords[1]],i) for i in face)
        def cross2(a,b,c):
            return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        lo=[]
        for p in nodes:
            while len(lo)>=2 and cross2(lo[-2],lo[-1],p)<=0:lo.pop()
            lo.append(p)
        up=[]
        for p in reversed(nodes):
            while len(up)>=2 and cross2(up[-2],up[-1],p)<=0:up.pop()
            up.append(p)
        ordered=[p[2] for p in (lo[:-1]+up[:-1])]
        for h in range(1,len(ordered)-1):
            selected=[pts[idx] for idx in [ordered[0],ordered[h],ordered[h+1]]]
            a,b,c=[p[:3] for p in selected]
            tvol=abs(dot(a,cross(b,c)))/6
            if not tvol:continue
            S=[sum((p[j] for p in selected),F(0)) for j in range(4)]
            quad=sum((dot(p,p) for p in selected),F(0))+dot(S,S)
            vol+=tvol
            moment+=tvol*quad/20
            ntet+=1
    assert vol==8 and moment/vol==F(13,8),(vol,moment/vol)
    return len(pts),len(fs),ntet,vol,moment/vol


def main():
    examples=[
        ('tree-4',4,[(0,1),(1,2),(1,3)],[]),
        ('triangle',3,[],[[(0,1),(1,2),(2,0)]]),
        ('triangle-with-branch',4,[(2,3)],[[(0,1),(1,2),(2,0)]]),
        ('square-with-two-branches',6,[(0,4),(4,5)],[[(0,1),(1,2),(2,3),(3,0)]]),
        ('bowtie',5,[],[[(0,1),(1,2),(2,0)],[(0,3),(3,4),(4,0)]]),
        ('two-triangles-joined',6,[(2,3)],[[(0,1),(1,2),(2,0)],[(3,4),(4,5),(5,3)]]),
        ('triangle-square-cactus',6,[],[[(0,1),(1,2),(2,0)],[(0,3),(3,4),(4,5),(5,0)]]),
        ('pentagon-bridge-triangle',8,[(4,5)],[[(0,1),(1,2),(2,3),(3,4),(4,0)],[(5,6),(6,7),(7,5)]]),
    ]
    checked=0;entries=0
    for name,n,bridges,cycles in examples:
        actual=cov_cactus(n,bridges,cycles)
        predicted=laplace_pred(n,bridges,cycles)
        assert actual==predicted,(name, actual,predicted)
        assert sum(actual[i][i] for i in range(n))==F(n-1+3*len(cycles),6)
        minor=det([row[:-1] for row in actual[:-1]])
        expected=F(1,12**(n-1))
        for c in cycles:
            k=len(c)
            expected*=F(k)*F(k+2,k)**(k-1)
        assert minor==expected,(name,minor,expected)
        es=bridges+[e for c in cycles for e in c]
        assert tree_count(n,es)==__import__('math').prod(len(c) for c in cycles),name
        print(name,'n',n,'cycles',len(cycles),'trace',sum(actual[i][i] for i in range(n)),'det_cofactor',minor)
        checked+=1;entries+=n*n
    diamond=diamond_direct_tetrahedra()
    print('diamond_non_cactus',diamond)
    print('CACTUS_UNIFORM_INERTIA_EXACT_CHECKS_PASSED',checked,entries,diamond)

if __name__=='__main__':main()
