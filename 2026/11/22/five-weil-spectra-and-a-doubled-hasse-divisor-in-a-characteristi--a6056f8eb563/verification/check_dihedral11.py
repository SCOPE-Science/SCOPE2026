"""Exact arithmetic verification for a genus-four dihedral hyperelliptic pencil.

Runs with Python's standard library only. All calculations are integer modular
arithmetic and exhaustive finite-field counts; the general double-square
cohomological argument is supplied separately in the mathematical proof.
"""
from collections import defaultdict
from math import factorial

P = 11
GOOD = [a for a in range(P) if a not in (2, 9)]
EXPECTED_Q = {
    0: (1,-4,6,-44,121),
    1: (1,6,26,66,121),
    3: (1,1,21,11,121),
    4: (1,1,11,11,121),
    5: (1,-4,26,-44,121),
}

class F121:
    def __init__(self, c, d):
        self.c,self.d=c,d  # t^2+c*t+d
        self.pairs=[(a,b) for a in range(P) for b in range(P)]
        sq=set()
        for v in self.pairs:
            sq.add(self.mul(v,v))
        self.squares=sq
    def add(self,a,b):return ((a[0]+b[0])%P,(a[1]+b[1])%P)
    def mul(self,a,b):
        a0,a1=a;b0,b1=b; z=a1*b1
        return ((a0*b0-self.d*z)%P,(a0*b1+a1*b0-self.c*z)%P)
    def sc(self,a,n):return ((n*a[0])%P,(n*a[1])%P)
    def power(self,a,n):
        r=(1,0)
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def chi(self,a):return 0 if a==(0,0) else (1 if a in self.squares else -1)

def chi11(a):
    a%=P
    if a==0:return 0
    return 1 if pow(a,5,P)==1 else -1

def D5(t, F):
    t2=F.mul(t,t);t3=F.mul(t2,t);t5=F.mul(t3,t2)
    return F.add(F.add(t5,F.sc(t3,-5)),F.sc(t,5))

def genus2_points(a, extension):
    if extension is None:
        return P+2+sum(chi11((t+2)*(t**5-5*t**3+5*t+a)) for t in range(P))
    F=extension
    S=0
    for t in F.pairs:
        val=F.mul(F.add(t,(2,0)),F.add(D5(t,F),(a,0)))
        S+=F.chi(val)
    return P*P+2+S

def genus4_points(a, extension):
    if extension is None:
        return P+2+sum(chi11(x**10+a*x**5+1) for x in range(P))
    F=extension;S=0
    for x in F.pairs:
        v=F.power(x,5); z=F.add(F.add(F.mul(v,v),F.sc(v,a)),(1,0))
        S+=F.chi(z)
    return P*P+2+S

def quadratic_divisor(h, c0,c1):
    # Polynomial ascending coefficients in F11.
    h=[v%P for v in h]
    b=[c0%P,c1%P,1]
    while len(h)>=3:
        m=h[-1]
        for j in range(3):h[len(h)-3+j]=(h[len(h)-3+j]-m*b[j])%P
        while h and h[-1]==0:h.pop()
    return len(h)==0

def verify():
    # Independent irreducible models; discriminants 4^2-8=8, 1-4=8.
    assert 8 not in {i*i%P for i in range(P)}
    models=[F121(4,2),F121(1,1)]
    for F in models:
        assert len(F.squares)==61
        assert all(F.power(v,121)==v for v in F.pairs)
    # Hyperelliptic f(x) is square-free iff a^2 != 4;
    # derivative x^4(10x^5+5a), and f(0)=1.
    assert GOOD==[0,1,3,4,5,6,7,8,10]
    # Expansion f^5, x^{5r} coefficient via multinomial sums.
    coeff=[]
    for r in (2,4,6,8):
        terms=[]
        for i in range(6):
            for j in range(6-i):
                k=5-i-j
                if 2*i+j ==r:
                    terms.append((factorial(5)//(factorial(i)*factorial(j)*factorial(k)),j))
        coeff.append(terms)
    def val(terms,a):return sum(c*pow(a,j,P) for c,j in terms)%P
    for a in range(P):
        h1=(5-a*a)%P
        h2=(5*pow(a,4,P)-3*a*a-1)%P
        assert [val(t,a) for t in coeff]==[h1,h2,h2,h1]
    # h2=5*(a^4-5a^2+2) is irreducible of degree 4 over F11.
    h2=[10,0,8,0,5] # 5 a^4 -3 a^2 -1 modulo 11
    assert all((5*pow(a,4,P)-3*a*a-1)%P for a in range(P))
    assert all(not quadratic_divisor(h2,c0,c1) for c0 in range(P) for c1 in range(P))
    assert [a for a in range(P) if (5-a*a)%P==0]==[4,7]
    assert all((5*pow(a,4,P)-3*a*a-1)%P for a in (4,7))
    assert all((a*a-4)%P for a in (4,7))
    # Verify genus-2 quotient and genus-4 direct counts agree under
    # the group-theoretic predicted relation N_C=2*N_Q-(q+1).
    for F in [None]+models:
        q=P if F is None else P*P
        for a in GOOD:
            nq=genus2_points(a,F)
            nc=genus4_points(a,F)
            assert nc==2*nq-(q+1),(F,a,nq,nc)
    for a in GOOD:
        key=min(a,(-a)%P)
        n1=genus2_points(a,None)
        n2=genus2_points(a,models[0])
        s1=P+1-n1
        s2=P*P+1-n2
        c1=-s1
        c2=(s1*s1-s2)//2
        assert (s1*s1-s2)%2==0
        q=(1,c1,c2,P*c1,P*P)
        assert q==EXPECTED_Q[key],(a,q)
        assert n2==genus2_points(a,models[1])
    assert set(EXPECTED_Q)=={0,1,3,4,5}
    assert len(set(EXPECTED_Q.values()))==5
    # E: y^2=x^3+x+10 has trace 2.
    N_E=1+sum(1+chi11(x**3+x+10) for x in range(P))
    assert N_E==10
    E2=(1,-4,26,-44,121) # (1-2T+11T^2)^2
    assert EXPECTED_Q[5]==E2
    assert all(EXPECTED_Q[a]!=E2 for a in (0,1,3,4))
    # Distinct quadratic twists give L_Q(-T), all ten Weil types distinct.
    types=set()
    for coeffs in EXPECTED_Q.values():
        types.add(coeffs)
        types.add(tuple(c if i%2==0 else -c for i,c in enumerate(coeffs)))
    assert len(types)==10
    print('DIHEDRAL11_WEIL_AND_CARTIER_VERIFIED smooth_marked=9 geometric_hasse_roots=6 F11_rank2=2 F11_weil_types=5 with_quadratic_twists=10 elliptic_fourth_power=1 models_GF121=2')

if __name__=='__main__': verify()
