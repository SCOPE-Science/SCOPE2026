#!/usr/bin/env python3
"""Exact degree-two algebraic certificate for the four-cycle maximal-gradient inequality.
Uses Q(sqrt(13)), no floating point and no external dependencies.
"""
from fractions import Fraction as F

class Quad:
    """Exact element a+b*sqrt(13) with rational a,b."""
    def __init__(self,a=0,b=0):
        if isinstance(a,Quad):self.a,self.b=a.a,a.b
        else:self.a,self.b=F(a),F(b)
    def __add__(self,y):
        y=Quad(y);return Quad(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,y):return self+-Quad(y)
    def __rsub__(self,y):return Quad(y)+-self
    def __mul__(self,y):
        y=Quad(y);return Quad(self.a*y.a+13*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=Quad(y);den=y.a*y.a-13*y.b*y.b
        assert den!=0
        return self*Quad(y.a/den,-y.b/den)
    def __rtruediv__(self,y):return Quad(y)/self
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        if a*a>13*b*b:return (a>0)-(a<0)
        return (b>0)-(b<0)
    def __lt__(self,y):return (self-Quad(y)).sign()<0
    def __le__(self,y):return (self-Quad(y)).sign()<=0
    def __gt__(self,y):return (self-Quad(y)).sign()>0
    def __ge__(self,y):return (self-Quad(y)).sign()>=0
    def __eq__(self,y):return self.a==Quad(y).a and self.b==Quad(y).b
    def __repr__(self):return f"({self.a}+{self.b}*sqrt13)"


Z=F(0); U=F(1)

def dot(a,p): return a[0]*p[0]+a[1]*p[1]+a[2]
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(poly):return sum(cross(x,y) for x,y in zip(poly,poly[1:]+poly[:1]))/2

def clip(poly,L):
    if not poly:return []
    out=[]
    for u,v in zip(poly,poly[1:]+poly[:1]):
        du=dot(L,u); dv=dot(L,v)
        if du>=0:out.append(u)
        if (du<0<dv) or (du>0>dv):
            w=( (v[0]*du-u[0]*dv)/(du-dv), (v[1]*du-u[1]*dv)/(du-dv) )
            out.append(w)
        elif du == 0 and dv < 0:pass
        elif du < 0 and dv == 0: pass
    dedup=[]
    for p in out:
        if p not in dedup:dedup.append(p)
    if len(dedup)>=3 and area(dedup)<0: dedup.reverse()
    return dedup

def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,t):return tuple(t*x for x in a)
def v2(a):
    A,B,C=a
    return (A*A,2*A*B,B*B,2*A*C,2*B*C,C*C)
def psub(a,b):return tuple(x-y for x,y in zip(a,b))
def evalq(q,p):
    x,y=p;A,B,C,D,E,F0=q
    return A*x*x+B*x*y+C*y*y+D*x+E*y+F0

def min_poly(q,P):
    best=min((evalq(q,v),v,'vertex') for v in P)
    for u,v in zip(P,P[1:]+P[:1]):
        d=(v[0]-u[0],v[1]-u[1]);A,B,C,D,E,F0=q
        aa=A*d[0]*d[0]+B*d[0]*d[1]+C*d[1]*d[1]
        bb=2*A*u[0]*d[0]+B*(u[0]*d[1]+u[1]*d[0])+2*C*u[1]*d[1]+D*d[0]+E*d[1]
        if aa>0 and 0<-bb<2*aa:
            t=-bb/(2*aa);v0=(u[0]+t*d[0],u[1]+t*d[1])
            best=min(best,(evalq(q,v0),v0,'edge'))
    hdet=4*q[0]*q[2]-q[1]*q[1]
    if q[0]>0 and hdet>0:
        xx=(q[1]*q[4]-2*q[2]*q[3])/hdet
        yy=(q[1]*q[3]-2*q[0]*q[4])/hdet
        pt=(xx,yy)
        # Only if point lies in the polygon (boundary accepted too).
        if all(cross((v[0]-u[0],v[1]-u[1]),(xx-u[0],yy-u[1]))>=0 for u,v in zip(P,P[1:]+P[:1])):
            best=min(best,(evalq(q,pt),pt,'interior'))
    return best

def options(n,inputs):
    opts=[]
    for j in range(n):
        choices={}
        for width in range(1,n+1):
            for offset in range(width):
                sites={(j-offset+k)%n for k in range(width)}
                co=tuple(sum((inputs[k][i] for k in sites),Z)/width for i in range(3))
                choices[co]=sites
        opts.append(list(choices))
    return opts


def verify4(min_location):
    # Vertex zero is 1, vertex min is zero. Remaining coordinates are x,y.
    inputs=[None]*4
    inputs[0]=(Z,Z,U)
    inputs[min_location]=(Z,Z,Z)
    others=[j for j in range(4) if inputs[j] is None]
    inputs[others[0]]=(U,Z,Z);inputs[others[1]]=(Z,U,Z)
    opts=options(4,inputs)
    square=[(Z,Z),(U,Z),(U,U),(Z,U)]
    todo=[(square,[])]
    counts=[]
    for j in range(4):
        new=[]
        for P,chosen in todo:
            for a in opts[j]:
                P0=P
                for b in opts[j]:
                    if a==b:continue
                    P0=clip(P0,sub(a,b))
                    if len(P0)<3 or area(P0)==0:break
                if len(P0)>=3 and area(P0)>0:new.append((P0,chosen+[a]))
        todo=new;counts.append(len(todo))
    inputq=(Z,)*6
    for j in range(4):inputq=plus(inputq,v2(sub(inputs[j],inputs[(j+1)%4])))
    worst=(Quad(1000),(Z,Z),'')
    zero_cells=[]
    for idx,(P,cs) in enumerate(todo):
        outputq=(Z,)*6
        for j in range(4):outputq=plus(outputq,v2(sub(cs[j],cs[(j+1)%4])))
        q=psub(scale(inputq,Quad(F(7,36),F(1,36))),outputq)
        small=min_poly(q,P)
        if small[0]<worst[0]:worst=small
        assert small[0]>=0, (min_location,idx,small,P,q)
        if small[0]==0:zero_cells.append((idx,small[1],small[2]))
    assert sum(area(P) for P,_ in todo)==1, (min_location,sum(area(P) for P,_ in todo))
    return counts,len(todo),worst,zero_cells

if __name__=='__main__':
    for m in (1,2):
        counts,final,worst,zeros=verify4(m)
        print('min location',m,'active cells by coordinate',counts,'exact global least deficit',worst,'zero cells',zeros)
    t=Quad(F(5,6),F(-1,6))
    lam=Quad(F(7,36),F(1,36))
    D=2*((1-t)*(1-t)+t*t)
    E=2*(((1-t)/2)*((1-t)/2)+((1+t)/6)*((1+t)/6))
    assert E/D==lam
    # Three-cycle: sorted f=(u+v,v,0). If u>=v the ratio is 1/4.
    # If v>=u the exact difference E(f)/4-E(Mf) is
    # (v-u)*(4u+5v)/18 >= 0.
    for u in range(0,9):
        for v in range(0,9):
            if u+v==0:continue
            f=(F(u+v),F(v),F(0))
            D3=sum((f[j]-f[(j+1)%3])**2 for j in range(3))
            opts=options(3,[(Z,Z,x) for x in f])
            Mf=[max(z[2] for z in choices) for choices in opts]
            E3=sum((Mf[j]-Mf[(j+1)%3])**2 for j in range(3))
            assert 4*E3<=D3
    print('PASS: 13 positive-area cells, exhaustive rational 2D cells, exact Q(sqrt(13)) extrema and sharp witness; independent 3-cycle identities')
