"""Independent finite-prime-field spot checks of the Frobenius-twisted cubic system.
Run: python3 verify_members.py. Standard library only.
"""
from itertools import product

class GF3:
    def __init__(self,p):
        self.p=p; self.N=p**3
        for C,B,A in product(range(p),repeat=3):
            if all((t**3+A*t*t+B*t+C)%p for t in range(p)):
                self.mod=(C,B,A); break
        else: raise AssertionError('no irreducible polynomial')
        self.addtab=None
    def digits(self,a):
        p=self.p; return [a%p,(a//p)%p,(a//(p*p))%p]
    def pack(self,d):
        p=self.p;return sum((d[i]%p)*p**i for i in range(3))
    def embed(self,a):return a%self.p
    def add(self,a,b):return self.pack([x+y for x,y in zip(self.digits(a),self.digits(b))])
    def neg(self,a):return self.pack([-x for x in self.digits(a)])
    def mul(self,a,b):
        p=self.p;v=[0]*5;u=self.digits(a);w=self.digits(b)
        for i in range(3):
            for j in range(3):v[i+j]+=u[i]*w[j]
        C,B,A=self.mod
        for i in (4,3):
            z=v[i];v[i]=0;v[i-3]-=C*z;v[i-2]-=B*z;v[i-1]-=A*z
        return self.pack(v)
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def trace(self,a):
        b=self.add(self.add(a,self.power(a,self.p)),self.power(a,self.p*self.p))
        assert self.digits(b)[1:]==[0,0]
        return b%self.p
    def norm(self,a):
        b=self.mul(self.mul(a,self.power(a,self.p)),self.power(a,self.p*self.p))
        assert self.digits(b)[1:]==[0,0]
        return b%self.p

MONS=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]

def pp(g,a,b):
    c=dict(a)
    for k,v in b.items():c[k]=g.add(c.get(k,0),v)
    return c

def pm(g,a,b):
    o={}
    for k,x in a.items():
        for h,y in b.items():
            z=tuple(k[i]+h[i] for i in range(3))
            o[z]=g.add(o.get(z,0),g.mul(x,y))
    return o

def prep(p):
    g=GF3(p)
    def det(A):
        # determinant over Fp of three 3-vectors
        v=A;return (v[0][0]*(v[1][1]*v[2][2]-v[1][2]*v[2][1]) -v[0][1]*(v[1][0]*v[2][2]-v[1][2]*v[2][0])+v[0][2]*(v[1][0]*v[2][1]-v[1][1]*v[2][0]))%p
    theta=next(a for a in range(1,g.N) if det([g.digits(g.power(a,p**i)) for i in range(3)])!=0)
    t=[g.power(theta,p**i) for i in range(3)]
    L={ (1,0,0):t[0],(0,1,0):t[1],(0,0,1):t[2]}
    B=[{k:g.power(v,p**i) for k,v in L.items()} for i in range(3)]
    cubic=pm(g,pm(g,B[0],B[0]),B[1])
    prod=pm(g,pm(g,B[0],B[1]),B[2])
    # Trace construction: f = Tr(a * l0^2*l1) + d*Norm(l0).
    # Since l0^q=l1 and l1^q=l2, the traced cubic is over Fp.
    def coeffs(a,d):
        C={}
        for mon in MONS:
            val=g.add(g.trace(g.mul(a,cubic.get(mon,0))),g.mul(d,prod.get(mon,0)))
            x=g.digits(val)
            assert x[1]==x[2]==0,(mon,a,d,x)
            C[mon]=x[0]
        return C
    return g,theta,coeffs

def projective_points(p):
    return [(1,y,z) for y in range(p) for z in range(p)]+[(0,1,z) for z in range(p)]+[(0,0,1)]

def projective_parameters(p):
    for c in product(range(p),repeat=4):
        if not any(c):continue
        if next(x for x in c if x)!=1:continue
        yield c

def run(p):
    g,theta,coeff=prep(p);pts=projective_points(p)
    counts={'smooth':0,'irreducible_singular':0,'reducible':0}
    point_counts=set();nodecounts=set();cuspcounts=set()
    for a0,a1,a2,d in projective_parameters(p):
        a=g.pack((a0,a1,a2)); cc=coeff(a,d)
        singular=[];zeros=[]
        for xyz in pts:
            f=sum(c*xyz[0]**m[0]*xyz[1]**m[1]*xyz[2]**m[2] for m,c in cc.items())%p
            if f:continue
            zeros.append(xyz)
            grad=[sum(m[i]*c*xyz[0]**(m[0]-(i==0))*xyz[1]**(m[1]-(i==1))*xyz[2]**(m[2]-(i==2)) for m,c in cc.items() if m[i])%p for i in range(3)]
            if grad==[0]*3:singular.append(xyz)
        if a==0:
            counts['reducible']+=1
            assert d!=0 and len(zeros)==0
        elif (d**3+27*g.norm(a))%p==0:
            counts['irreducible_singular']+=1
            assert len(singular)==1,(p,a,d,singular)
            target=p+1 if p==3 else (p if p%3==1 else p+2)
            assert len(zeros)==target,(p,a,d,len(zeros),target)
            point_counts.add(len(zeros))
        else:
            counts['smooth']+=1
            assert not singular
    assert counts=={'smooth':p**3-1,'irreducible_singular':p*p+p+1,'reducible':1},counts
    print('FROBENIUS_CUBIC_STRATA_PASS',p,g.mod,theta,counts,'singular_point_counts',sorted(point_counts))
if __name__=='__main__':
    for p in (2,3,5,7):run(p)
