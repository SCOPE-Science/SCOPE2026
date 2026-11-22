"""Self-contained finite checks for a two-radius finite-field Fourier moment identity.
Standard Python 3; run: python check_even_shells.py
Tests do not replace the all-field proof supplied with the result.
"""
from itertools import product
from functools import reduce
from collections import Counter
from math import isqrt


class Field:
    def __init__(self, p, degree=1, nonsquare=None):
        self.p, self.degree, self.q = p, degree, p ** degree
        assert degree in (1, 2) and p % 2
        if degree == 2:
            if nonsquare is None:
                nonsquare = next(k for k in range(2, p) if pow(k, (p - 1) // 2, p) == p - 1)
            assert pow(nonsquare, (p-1)//2, p) == p-1
            self.delta = nonsquare
        self.add = [[0] * self.q for _ in range(self.q)]
        self.mul = [[0] * self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                if degree == 1:
                    self.add[a][b] = (a + b) % p
                    self.mul[a][b] = (a * b) % p
                else:
                    a0, a1 = a % p, a // p
                    b0, b1 = b % p, b // p
                    self.add[a][b] = ((a0 + b0) % p) + p * ((a1 + b1) % p)
                    self.mul[a][b] = ((a0*b0 + nonsquare*a1*b1) % p) + p * ((a0*b1+a1*b0) % p)
        self.neg = [next(b for b in range(self.q) if self.add[a][b] == 0) for a in range(self.q)]
        self.chi = [0] * self.q
        for a in range(1,self.q):
            z = 1
            for _ in range((self.q-1)//2): z = self.mul[z][a]
            self.chi[a] = 1 if z == 1 else -1
        self.one = 1

    def elem(self, z): return z % self.p
    def plus(self, a, b): return self.add[a][b]
    def minus(self, a, b): return self.add[a][self.neg[b]]
    def times(self, *args):
        out=1
        for a in args: out=self.mul[out][a]
        return out
    def sq(self,a): return self.mul[a][a]


def calculate_traces(F,a,b):
    plus,minus,times,sq = F.plus,F.minus,F.times,F.sq
    four=F.elem(4)
    D=lambda t: minus(sq(minus(minus(t,a),b)),times(four,a,b))
    Ta=sum(F.chi[times(t, minus(t,times(four,a)),D(t))] for t in range(F.q))
    Tb=sum(F.chi[times(t, minus(t,times(four,b)),D(t))] for t in range(F.q))
    return Ta,Tb


def analytic_energy(F,d,diag,a,b):
    q=F.q;m=d//2
    det=F.times(*diag)
    eps=F.chi[F.times(F.elem(-1 if m%2 else 1),det)]
    A=q**(d-2); B=eps*q**(m-1)
    U=q**(d-1)-B; V=q**(d-1)+(q-1)*B
    Ta,Tb=calculate_traces(F,a,b)
    c=F.chi[F.times(a,b)]
    energy=4*U*U+(V-1)*(4*A-2*B)**2+U*(16*(q-1)*A*A-48*A*B+B*B*(6*q-14-6*c+4*(Ta+Tb)))
    return energy


def check_trace_family(F):
    q=F.q; a=1
    sum_a=sum_b=0
    failures=[]
    for b in range(2,q):
        Ta,Tb=calculate_traces(F,a,b)
        # The only possible singular ratios are b=9a or a=9b.
        nine=F.elem(9)
        if b==nine:
            assert Ta==-1-F.chi[F.elem(-3)], (q,b,Ta)
        if F.times(b,nine)==a:
            assert Tb==-1-F.chi[F.elem(-3)], (q,b,Tb)
        sum_a+=Ta;sum_b+=Tb
        # Smooth quartics yield elliptic traces |-(1+T)| <= 2 sqrt(q).
        assert abs(Ta+1) <= 2*isqrt(q)+2
        assert abs(Tb+1) <= 2*isqrt(q)+2
    target=4-q+F.chi[F.elem(-3)]
    assert sum_a==target and sum_b==target,(q,sum_a,sum_b,target)
    # The explicit mean-energy law is also checked independently by averaging
    # every individual rational formula; no elliptic library is required.
    d=4
    U=q**(d-1)-q
    L=q**(d-2)
    B=q
    Nzero=q**(d-1)+(q-1)*B
    mean_H2_num=(q-2)*(6*q-14)+(38-8*q+8*F.chi[F.elem(-3)])
    predicted_total=(q-2)*(4*U**2+(Nzero-1)*(4*L-2*B)**2+U*(16*(q-1)*L**2-48*L*B)) + U*B**2*mean_H2_num
    actual_total=sum(analytic_energy(F,d,(1,1,1,1),a,b) for b in range(2,q))
    assert predicted_total==actual_total,(q,predicted_total,actual_total)
    return q-2


def check_direct_energy(F,d,diag,a,b):
    q=F.q
    plus,times=F.plus,F.times
    tuples=product(range(q),repeat=d)
    points=[v for v in tuples
            if reduce(plus, (times(diag[i],F.sq(v[i])) for i in range(d)), 0) in (a, b)]
    hist=Counter(tuple(plus(x[i],y[i]) for i in range(d)) for x in points for y in points)
    actual=sum(h*h for h in hist.values())
    expected=analytic_energy(F,d,diag,a,b)
    assert actual==expected,(q,d,diag,a,b,actual,expected)
    return len(points),len(points)**2


def main():
    trace_tests=0
    for p,degree in [(3,1),(5,1),(7,1),(11,1),(13,1),(17,1),(3,2),(5,2)]:
        F=Field(p,degree)
        trace_tests+=check_trace_family(F)
    cases=[(3,1,2,(1,1),1,2),
           (3,1,2,(1,2),1,2),
           (5,1,2,(1,1),1,3),
           (5,1,2,(1,2),1,4),
           (7,1,2,(1,1),1,3),
           (7,1,2,(1,2),1,4),
           (5,2,2,(1,1),1,5),
           (5,2,2,(1,5),1,5),
           (5,2,2,(1,1),1,9),
           (5,2,2,(1,5),1,9),
           (3,1,4,(1,1,1,1),1,2),
           (3,1,4,(1,1,1,2),1,2),
           (3,1,6,(1,1,1,1,1,1),1,2),
           (3,1,6,(1,1,1,1,1,2),1,2),
           (5,1,4,(1,1,1,1),1,2),
           (5,1,4,(1,1,1,1),2,3),
           (5,1,4,(1,1,1,2),1,4),
           (7,1,4,(1,1,1,1),1,3),
           (7,1,4,(1,1,1,1),1,2),
           (3,2,4,(1,1,1,1),1,2),
           (3,2,4,(1,1,1,1),1,3)]
    pairs=0
    for p,deg,d,diag,a,b in cases:
        F=Field(p,deg)
        n,count=check_direct_energy(F,d,diag,a,b)
        pairs+=count
        print('verified q=%d d=%d detclass=%+d a=%d b=%d |S|=%d pairs=%d'%(F.q,d,F.chi[F.times(*diag)],a,b,n,count))
    print('PASS: %d family-level trace checks, %d complete direct convolution checks, %d ordered pairs.'%(trace_tests,len(cases),pairs))


if __name__=='__main__':main()
