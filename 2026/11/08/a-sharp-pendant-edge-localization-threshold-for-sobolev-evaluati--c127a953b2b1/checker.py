"""Exact, finite validation of rational cases of a mean-zero graph Sobolev formula.
Universal assertions are proved analytically in RESULT.md; this checker is diagnostic.
Requires SymPy. Run: python checker.py
"""
import sympy as s

def graph_resistance(r, h, p, q):
    # p and q are edge-index and distance from its initial vertex.
    # Edges 0..r-1 run u -> v with length 1; edge r runs u -> leaf with length h.
    lens = [s.S.One]*r + [h]
    edges=[]; nodes={'u':0,'v':1,'w':2}
    next_node=3
    positions=[]
    for i,L in enumerate(lens):
        a='u'; b='v' if i<r else 'w'
        internal=sorted(set([z for j,z in [p,q] if j==i and 0<z<L]))
        arr=[(s.S.Zero,nodes[a])]
        for z in internal:
            arr.append((z,next_node)); next_node+=1
        arr.append((L,nodes[b]));positions.append(arr)
        for (t0,u),(t1,v) in zip(arr[:-1],arr[1:]):edges.append((u,v,1/(t1-t0)))
    def locate(a):
        i,t=a
        for z,node in positions[i]:
            if z==t:return node
        raise AssertionError('missing split')
    a=locate(p); b=locate(q)
    if a==b:return s.S.Zero
    lap=s.zeros(next_node)
    for u,v,c in edges:
        lap[u,u]+=c;lap[v,v]+=c;lap[u,v]-=c;lap[v,u]-=c
    # Ground b; inject one unit at a.
    active=[i for i in range(next_node) if i!=b]
    mat=lap.extract(active,active)
    cur=s.zeros(len(active),1);cur[active.index(a)]=1
    potential=mat.inv()*cur
    return s.factor(potential[active.index(a)])

def total_resistance(r,h,p):
    edge_lengths=[s.S.One]*r+[h]
    total=s.S.Zero
    for i, length in enumerate(edge_lengths):
        boundaries=sorted(set([s.S.Zero,length]+([p[1]] if p[0]==i else [])))
        for a,b in zip(boundaries[:-1],boundaries[1:]):
            mid=(a+b)/2
            z=(graph_resistance(r,h,p,(i,a))+4*graph_resistance(r,h,p,(i,mid)) +graph_resistance(r,h,p,(i,b)))*(b-a)/6
            total+=z
    return s.factor(total)

def expected_F(r,h,p):
    Fu=(s.Rational(r+2,6)+h*h/2)
    i,z=p
    if i==r:return s.factor(Fu+z*z+(r-h)*z)
    K=s.Integer(r-2)+s.Rational(r-1,r)*h
    return s.factor(Fu+s.Rational(1,r)*h*z+K*z*(1-z))

checks=0
for r in [3,4,5]:
    for h in [s.Rational(1,12),s.Rational(1,5)]:
        for edge,pos in [(0,s.Rational(1,4)),(0,s.Rational(1,2)),(1,s.Rational(3,4)),(r,h/3),(r,h)]:
            p=(edge,pos)
            got=total_resistance(r,h,p)
            want=expected_F(r,h,p)
            assert got==want,(r,h,p,got,want)
            checks+=1
        K=s.Integer(r-2)+s.Rational(r-1,r)*h
        assert K>0
        xstar=(r-2+h)/(2*K)
        assert s.S.Half<xstar<1
        J=(s.Integer(r)**2+h*(r+2)+3*r*h*h+h**3)/3
        # Independently integrate the two edgewise formulae.
        x=s.Symbol('x')
        J2=r*s.integrate(expected_F(r,h,(0,x)),(x,0,1))+s.integrate(expected_F(r,h,(r,x)),(x,0,h))
        assert s.factor(J-J2)==0
        checks+=1
for r in range(3,70):
    rr=s.Integer(r)
    hc=(rr-2)*(2*s.sqrt(rr*rr-1)-(2*rr-1))/(4*rr-5)
    assert hc>0
    K=rr-2+(rr-1)*hc/rr
    assert s.simplify(4*rr*hc*K-(rr-2+hc)**2)==0
    assert hc<1
    checks+=1
print('ALL_TWIGGED_BANANA_SOB OLEV_CHECKS_PASSED'.replace(' ','') ,checks)
