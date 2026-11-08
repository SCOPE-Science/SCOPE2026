#!/usr/bin/env python3
"""Independent finite-field and intersection check for the D8-Ciani pencil in characteristic 7."""
P=7
# F_49 = F_7[t]/(t^2+1). Pair (u,v) represents u+v*t.
class K:
    def __init__(self,u,v=0):self.u,self.v=u%P,v%P
    def __add__(self,o):
        o=conv(o);return K(self.u+o.u,self.v+o.v)
    __radd__=__add__
    def __neg__(self):return K(-self.u,-self.v)
    def __sub__(self,o):return self+-conv(o)
    def __rsub__(self,o):return conv(o)+-self
    def __mul__(self,o):
        o=conv(o);return K(self.u*o.u-self.v*o.v,self.u*o.v+self.v*o.u)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        x=K(1)
        while n:
            if n&1:x=x*self
            self=self*self;n>>=1
        return x
    def __eq__(self,o):
        o=conv(o);return (self.u,self.v)==(o.u,o.v)
    def __hash__(self):return hash((self.u,self.v))
    def __repr__(self):return f'({self.u},{self.v})'
def conv(o):return o if isinstance(o,K) else K(o)
ALL=[K(i,j) for i in range(P) for j in range(P)]
assert len(set(ALL))==49
assert all(z==0 or z**48==1 for z in ALL)

# Independent elliptic-quotient quartics obtained by completing squares.
def quartic_hasse(A,C,B):
    # [T^6](A T^4+C T^2+B)^3 = C^3+6 A B C.
    return C**3+6*A*B*C

def smooth(a,b):return (a*a-4)*(b*b-4)*(a*a+2*b*b-a*b*b-4)!=0

def haar(a,b):
    A=a*a-4; B=b*b-4
    c=2*b*(a-2);d=2*(b*b-2*a)
    return quartic_hasse(A,c,B),quartic_hasse(B,d,B)

def factors(a,b):
    v=b*b
    return 2*b*(a-2)**2*((3*v+4)*a+4*v+1),4*(v-2*a)*(a+v+1)*(a-2*v-1)

counts={(0,3):0,(1,2):0,(2,1):0,(3,0):0}
zeros=[]
for a in ALL:
    for b in ALL:
        h1,h3=haar(a,b)
        assert (h1,h3)==factors(a,b)
        if not smooth(a,b):continue
        nonzero=int(h1!=0)*2+int(h3!=0)
        counts[(nonzero,3-nonzero)]+=1
        if h1==h3==0: zeros.append((a,b))
assert len(zeros)==7,zeros
expected={(K(0),K(0)),(K(1),K(0)),(K(6),K(0))}
expected|={(K(4),b) for b in ALL if b*b==2}
expected|={(K(3),b) for b in ALL if b*b==6}
assert set(zeros)==expected,(zeros,expected)
# Gradient transversality of the two Hasse polynomials, at every superspecial point.
def deriv(a,b):
    # lambda = 2b(a-2)^2 L, mu = 4(v-2a)(a+v+1)(a-2v-1)
    v=b*b;L=(3*v+4)*a+4*v+1
    La=3*v+4;Lb=2*b*(3*a+4)
    lam_a=2*b*(2*(a-2)*L+(a-2)**2*La)
    lam_b=2*(a-2)**2*(L+b*Lb)
    U=v-2*a;V=a+v+1;W=a-2*v-1
    mu_a=4*((-2)*V*W+U*W-U*V)
    mu_b=4*((2*b)*V*W+U*(2*b)*W+U*V*(-4*b))
    return lam_a,lam_b,mu_a,mu_b
for a,b in zeros:
    la,lb,ma,mb=deriv(a,b)
    assert la*mb-lb*ma!=0,(a,b)
print('PASS F49 exhaustive smooth parameters:',sum(counts.values()),'strata',sorted(counts.items()))
print('PASS superspecial seven points:',zeros)
print('PASS all seven Hasse-divisor intersections transverse.')
