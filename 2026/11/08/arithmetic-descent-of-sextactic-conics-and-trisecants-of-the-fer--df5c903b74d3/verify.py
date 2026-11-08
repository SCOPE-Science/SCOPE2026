"""Independent finite-field check for the 81-line sextactic configuration.

Only uses Python standard library. For p=5,7,31 it builds splitting fields,
constructs all 6-torsion points on E:y^2=x^3-432, forms the 81 trisecants,
and tests rationality by coefficient Frobenius and point-line incidence.
"""
from itertools import product

class Field:
    def __init__(self,p,poly):
        self.p=p
        self.poly=poly  # coefficients low-to-high, monic
        self.d=len(poly)-1
        self.elems=[tuple(c) for c in product(range(p),repeat=self.d)]
        self.zero=(0,)*self.d
        self.one=(1,)+(0,)*(self.d-1)
    def const(self,n):return (n%self.p,)+(0,)*(self.d-1)
    def add(self,a,b):return tuple((x+y)%self.p for x,y in zip(a,b))
    def neg(self,a):return tuple(-x%self.p for x in a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        n=self.d; c=[0]*(2*n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%self.p
        for k in range(2*n-2,n-1,-1):
            t=c[k]
            for j in range(n):c[k-n+j]=(c[k-n+j]-t*self.poly[j])%self.p
        return tuple(c[:n])
    def power(self,a,n):
        if n<0:return self.power(self.inv(a),-n)
        z=self.one
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n>>=1
        return z
    def inv(self,a):
        assert a!=self.zero
        return self.power(a,self.p**self.d-2)
    def div(self,a,b):return self.mul(a,self.inv(b))


def check(p,poly):
    F=Field(p,poly);add=F.add;sub=F.sub;mul=F.mul;power=F.power
    z=F.zero;o=F.one;cv=F.const
    const432=cv(432)
    roots2=[x for x in F.elems if power(x,3)==const432]
    assert len(roots2)==3
    tors2=[(x,z) for x in roots2]
    eps=[x for x in F.elems if add(add(power(x,2),x),o)==z and x!=o]
    assert len(eps)==2
    # Fermat cubic flexes transported by the integral projective equivalence.
    tors3=[None]
    for e in eps:
        tors3.append((z,F.div(mul(cv(36),add(o,e)),sub(o,e))))
    for e in [o]+eps:
        tors3.append((mul(cv(12),e),cv(36)))
        tors3.append((mul(cv(12),e),cv(-36)))
    assert len(tors3)==9 and len(set(tors3))==9
    for P in tors3[1:]:
        x,y=P
        assert power(y,2)==sub(power(x,3),const432)
    def neg(P):return None if P is None else (P[0],F.neg(P[1]))
    def eadd(P,Q):
        if P is None:return Q
        if Q is None:return P
        x,y=P;u,v=Q
        if x==u:
            if add(y,v)==z:return None
            slope=F.div(mul(cv(3),power(x,2)),mul(cv(2),y))
        else:slope=F.div(sub(v,y),sub(u,x))
        xx=sub(sub(power(slope,2),x),u)
        yy=sub(mul(slope,sub(x,xx)),y)
        return (xx,yy)
    for P in tors3:
        assert eadd(eadd(P,P),P) is None
    all_pts={(i,j):eadd(T,Q) for i,T in enumerate(tors2) for j,Q in enumerate(tors3)}
    assert len(set(all_pts.values()))==27
    def homogeneous(P):return (z,o,z) if P is None else (P[0],P[1],o)
    def cross(P,Q):
        a,b,c=P;u,v,w=Q
        return (sub(mul(b,w),mul(c,v)),sub(mul(c,u),mul(a,w)),sub(mul(a,v),mul(b,u)))
    def normalize(L):
        assert L!=(z,z,z)
        idx=next(i for i,a in enumerate(L) if a!=z)
        return tuple(F.div(a,L[idx]) for a in L)
    lines={}
    # all points in each of the three nonzero 2-torsion cosets
    for j in range(9):
        for k in range(9):
            a=all_pts[(0,j)];b=all_pts[(1,k)]
            c=eadd(neg(a),neg(b))
            assert c in [all_pts[(2,t)] for t in range(9)]
            L=normalize(cross(homogeneous(a),homogeneous(b)))
            assert L not in lines
            lines[L]=(a,b,c)
    assert len(lines)==81
    def on(L,P):
        x,y,w=homogeneous(P)
        return add(add(mul(L[0],x),mul(L[1],y)),mul(L[2],w))==z
    assert set(sum((list(Ps) for Ps in lines.values()),[]))==set(all_pts.values())
    assert all(sum(on(L,P) for P in all_pts.values())==3 for L in lines)
    def fixed(a):return power(a,p)==a
    def frob_pt(P):return None if P is None else (power(P[0],p),power(P[1],p))
    def frob_line(L):return normalize(tuple(power(a,p) for a in L))
    assert {frob_pt(P) for P in all_pts.values()}==set(all_pts.values())
    assert {frob_line(L) for L in lines}==set(lines)
    def cycles(objects,frob):
        unseen=set(objects);cs={}
        while unseen:
            a=next(iter(unseen));b=frob(a);n=1
            unseen.remove(a)
            while b!=a:
                assert b in unseen
                unseen.remove(b);b=frob(b);n+=1
            cs[n]=cs.get(n,0)+1
        return cs
    point_cycles=cycles(all_pts.values(),frob_pt)
    line_cycles=cycles(lines,frob_line)
    rat_points={P for P in all_pts.values() if frob_pt(P)==P}
    rat_lines=[L for L in lines if frob_line(L)==L]
    incidence=[sum(on(L,P) for P in rat_points) for L in rat_lines]
    if p==5:expect=(3,9,{1:9},{1:3,2:12},{1:9,2:36})
    elif p==7:expect=(0,9,{0:9},{3:9},{1:9,3:24})
    else:expect=(27,81,{3:81},{1:27},{1:81})
    from collections import Counter
    actual=(len(rat_points),len(rat_lines),dict(Counter(incidence)),point_cycles,line_cycles)
    assert actual==expect,(p,actual,expect)
    print('FIELD_OK',p,'degree',F.d,'sextactic_cycles',point_cycles,
          'line_cycles',line_cycles,'rational_line_incidence',dict(Counter(incidence)))

if __name__=='__main__':
    check(5,(2,0,1))    # x^2+2 irreducible over F_5
    check(7,(-2,0,0,1)) # x^3-2 irreducible over F_7
    check(31,(0,1))     # prime field; 2=4^3 and a third root of unity exists
    print('VERIFY_SEXTACTIC_LINES_OK')
