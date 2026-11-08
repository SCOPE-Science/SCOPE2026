from fractions import Fraction as Q
from collections import defaultdict

# Exact convex cells in the initial square, with torus coordinates canonicalized to [0,1).
init=((Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1)))

def dot(a,v):return a[0]*v[0]+a[1]*v[1]
def clip(poly,a,b,less):
    # a.p<=b if less else >= b
    if not less:a=(-a[0],-a[1]);b=-b
    if not poly:return ()
    out=[]
    for pp,qq in zip(poly, poly[1:]+poly[:1]):
        fp=dot(a,pp)-b; fq=dot(a,qq)-b
        if fp<=0:out.append(pp)
        if (fp<0 and fq>0) or (fp>0 and fq<0):
            out.append(tuple((fq*pp[i]-fp*qq[i])/(fq-fp) for i in (0,1)))
    # remove consecutive duplicates
    out2=[]
    for p in out:
        if not out2 or p!=out2[-1]:out2.append(p)
    if len(out2)>=2 and out2[-1]==out2[0]:out2.pop()
    return tuple(out2)

def cross(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
def area(poly):return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])))/2

def mkmap(A,b,a,c):
    # affine expression a dot state +c
    return (tuple(a[0]*A[0][i]+a[1]*A[1][i] for i in (0,1)),a[0]*b[0]+a[1]*b[1]+c)
def nexts(A,b,P):
    # F first: u=x+f(y)-k; G: v=y+f(u)-l
    for signy in (+1,-1):
        p=clip(P,A[1], Q(1,2)-b[1], signy==+1)
        if not p:continue
        ay=2*signy; cy=0 if signy==1 else 2
        U0,uc0=mkmap(A,b,(1,ay),cy)
        for k in (0,1):
            q=clip(clip(p,U0,k+1-uc0,True),U0,k-uc0,False)
            if not q:continue
            U=U0;uc=uc0-k
            for signu in (+1,-1):
                s=clip(q,U,Q(1,2)-uc,signu==+1)
                if not s:continue
                au=2*signu;cu=0 if signu==1 else 2
                V0,vc0=mkmap((U,A[1]),(uc,b[1]),(au,1),cu)
                for l in (0,1):
                    z=clip(clip(s,V0,l+1-vc0,True),V0,l-vc0,False)
                    if z: yield ((U,V0),(uc,vc0-l),z,(signy,k,signu,l))


def branches(n):
    cells=[(((1,0),(0,1)),(0,0),init,())]
    counts=[]
    for _ in range(n):
        children=[]
        for A,b,P,w in cells:
            for A1,b1,P1,branch in nexts(A,b,P):
                if area(P1)>0:children.append((A1,b1,P1,w+(branch,)))
        cells=children
        counts.append(len(cells))
    return cells,counts

def h(p):
    x,y=p
    u=(x+2*min(y,1-y))%1
    v=(y+2*min(u,1-u))%1
    return u,v

def iterate(p,n):
    for _ in range(n):p=h(p)
    return p

def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def jac4(p):
    A=((1,0),(0,1))
    for _ in range(4):
        x,y=p;u=(x+2*min(y,1-y))%1
        if y in (0,Q(1,2)) or u in (0,Q(1,2)):return None
        a=2 if y<Q(1,2) else -2
        b=2 if u<Q(1,2) else -2
        A=mm(((1,a),(b,1+a*b)),A)
        p=h(p)
    return A

def line_poly(P,a,b):
    hits=[]
    for u,v in zip(P,P[1:]+P[:1]):
        gu=dot(a,u)-b;gv=dot(a,v)-b
        if gu==0:hits.append(u)
        if gv==0:hits.append(v)
        if gu*gv<0:hits.append(tuple((gv*u[i]-gu*v[i])/(gv-gu) for i in (0,1)))
    return sorted(set(hits))

def census():
    cells,counts=branches(4)
    assert counts==[15,97,515,2337],counts
    assert sum((area(P) for A,b,P,w in cells),Q(0))==1
    fixed_candidates=[];rank_deficient=[]
    for A,b,P,w in cells:
        D=((1-A[0][0],-A[0][1]),(-A[1][0],1-A[1][1]))
        determinant=D[0][0]*D[1][1]-D[0][1]*D[1][0]
        if determinant:
            x=Q(b[0]*D[1][1]-b[1]*D[0][1],determinant)
            y=Q(D[0][0]*b[1]-D[1][0]*b[0],determinant)
            p=(x,y)
            if all(cross(a,z,p)>=0 for a,z in zip(P,P[1:]+P[:1])):
                fixed_candidates.append(p)
        else:
            rank_deficient.append((D,b,P))
    assert len(fixed_candidates)==574
    assert len(rank_deficient)==9
    # Canonical representatives remove right/top edges and directly verify the
    # actual mod-one dynamics, including on polygon-switching boundaries.
    points={tuple(z%1 for z in p) for p in fixed_candidates}
    assert all(iterate(p,4)==p for p in points)
    assert len(points)==336,len(points)
    primitive={p for p in points if iterate(p,2)!=p}
    assert len(primitive)==320,len(primitive)
    assert all(iterate(p,4)==p and iterate(p,2)!=p for p in primitive)
    # Every zero determinant cell either has no fixed points or its fixed
    # line intersects the polygon in a (possibly degenerate) period-two set.
    segments=[]
    for D,b,P in rank_deficient:
        a=D[0]; c=b[0]
        consistent=(a[0]*b[1]==D[1][0]*c and a[1]*b[1]==D[1][1]*c)
        if not consistent:continue
        hits=line_poly(P,a,c)
        if len(hits)>=2:
            lo,hi=hits[0],hits[-1]
            mid=tuple((lo[i]+hi[i])/2 for i in range(2))
            assert iterate(lo,2)==tuple(z%1 for z in lo)
            assert iterate(hi,2)==tuple(z%1 for z in hi)
            assert iterate(mid,2)==mid
            segments.append((lo,hi))
        elif hits:
            assert iterate(hits[0],2)==tuple(z%1 for z in hits[0])
    assert len(segments)==4,segments
    # A continuous affine return on each rank-deficient cell, and three
    # collinear samples, prove every fixed segment has period dividing two.
    assert {frozenset((a,b)) for a,b in segments}=={
       frozenset(((Q(1,2),Q(1,4)),(Q(3,4),Q(0)))),
       frozenset(((Q(3,4),Q(1,2)),(Q(1),Q(1,4)))),
       frozenset(((Q(0),Q(3,4)),(Q(1,4),Q(1)))),
       frozenset(((Q(1,4),Q(1,2)),(Q(1,2),Q(3,4))))}
    # Independently solve the return equations on the two canonical torus
    # edges. These include lifted return values 1 that represent 0 mod 1.
    edge_points=set()
    for edge in ('x','y'):
        normal=(1,0) if edge=='x' else (0,1)
        for A,b,P,w in cells:
            hit=line_poly(P,normal,Q(0))
            if len(hit)<2 or hit[0]==hit[-1]:continue
            lo,hi=hit[0],hit[-1]
            for shift_x in (0,1):
                for shift_y in (0,1):
                    target=(shift_x,shift_y)
                    end_vals=[(dot(A[i],lo)+b[i]-lo[i]-target[i],
                               dot(A[i],hi)+b[i]-hi[i]-target[i]) for i in (0,1)]
                    roots=[]
                    for left,right in end_vals:
                        if left==right:
                            roots.append('all' if left==0 else None)
                        else:roots.append(-left/(right-left))
                    if None in roots:continue
                    nonconstant=[r for r in roots if r!='all']
                    assert nonconstant, 'An uncounted full fixed interval on a boundary'
                    if len(set(nonconstant))!=1:continue
                    t=nonconstant[0]
                    if 0<=t<=1:
                        p=tuple((lo[i]+t*(hi[i]-lo[i]))%1 for i in (0,1))
                        if iterate(p,4)==p:edge_points.add(p)
    assert len(edge_points)==23 and edge_points<=points
    cycles={frozenset(iterate(p,j) for j in range(4)) for p in primitive}
    assert len(cycles)==80 and all(len(orbit)==4 for orbit in cycles) and all(orbit<=primitive for orbit in cycles)
    from collections import Counter
    traces=Counter()
    for p in primitive:
        A=jac4(p)
        traces['switching' if A is None else A[0][0]+A[1][1]]+=1
    assert traces==Counter({-574:128,578:64,178:64,'switching':64}),traces
    for orbit in cycles:
        labels={('switching' if jac4(p) is None else sum(jac4(p)[i][i] for i in range(2))) for p in orbit}
        assert len(labels)==1,labels
    print('four-step convex cells',len(cells))
    print('rank-deficient affine cells',len(rank_deficient),'existing two-periodic segments',len(segments))
    print('fourth-iterate points',len(points),'primitive-four points',len(primitive),'primitive-four cycles',len(cycles))
    print('point traces',dict(traces))
    print('cycle counts', {str(k):v//4 for k,v in traces.items()})

if __name__=='__main__':census()
