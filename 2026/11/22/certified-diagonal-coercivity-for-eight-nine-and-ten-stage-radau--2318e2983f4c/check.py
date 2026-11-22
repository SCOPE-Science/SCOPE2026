"""Exact rational certificate for positive stage diagonals of Radau IIA orders 8--10.

Python 3 standard library only; all comparisons and sign tests use integers/Fraction.
"""
from fractions import Fraction as F
from math import comb

NODE_BRACKETS = {
    8: [22479386438,114679053160,265789822784,452846373669,647375282886,819759308263,943737439463],
    9: [17779915147,91323607899,214308479395,371932164583,545186684803,713175242855,855633742957,955366044710],
    10: [14412409648,74387389709,176116656162,309667579927,461970401081,618117234695,762823015185,881921021210,963742187116],
}
WEIGHT_NUMERATORS = {
    8: [11631,19596,20636,18091,14101,9725,5356,865],
    9: [9292,16551,18497,17283,14532,11191,7711,4255,688],
    10: [7580,14096,16509,16200,14383,11864,9087,6262,3460,560],
}

class Interval:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def get(x): return x if isinstance(x, Interval) else Interval(x)
    def __add__(self,b):
        b=self.get(b);return Interval(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,b):return self+-self.get(b)
    def __rsub__(self,b):return self.get(b)+-self
    def __mul__(self,b):
        b=self.get(b); x=[i*j for i in (self.lo,self.hi) for j in (b.lo,b.hi)]
        return Interval(min(x),max(x))
    __rmul__=__mul__
    def reciprocal(self):
        assert not (self.lo<=0<=self.hi), 'zero in divisor interval'
        return Interval(1/self.hi,1/self.lo)
    def __truediv__(self,b):return self*self.get(b).reciprocal()
    def __rtruediv__(self,b):return self.get(b)*self.reciprocal()

def jacobi_right_rad_poly(m,x):
    # J_m(x) = P_m^{(1,0)}(2x-1)
    # Jacobi binomial formula: integral coefficients, no floating point.
    return sum(comb(m+1,k)*comb(m,m-k)*(x-1)**(m-k)*x**k for k in range(m+1))

def round_nearest(q,denom):
    n=q*denom
    return F((n.numerator*2+n.denominator)//(2*n.denominator),denom)

def positive_by_LDL(A):
    n=len(A);L=[[F(0) for j in range(n)] for i in range(n)];d=[]
    for i in range(n):
        for j in range(i):
            L[i][j]=(A[i][j]-sum(L[i][k]*d[k]*L[j][k] for k in range(j)))/d[j]
        piv=A[i][i]-sum(L[i][k]*L[i][k]*d[k] for k in range(i))
        assert piv>0,('nonpositive LDL pivot',i,piv)
        d.append(piv);L[i][i]=F(1)
    return [float(v) for v in d]

def verify(s):
    n=s
    starts=NODE_BRACKETS[s]
    assert len(starts)==s-1
    # Disjoint intervals each containing a zero; degree s-1 implies these are all roots.
    den=10**12
    c=[Interval(F(t,den),F(t+1,den)) for t in starts]+[Interval(1)]
    for i in range(n-1):
        assert F(0)<c[i].lo<c[i].hi<c[i+1].lo<=F(1)
        pl=jacobi_right_rad_poly(s-1,c[i].lo)
        pr=jacobi_right_rad_poly(s-1,c[i].hi)
        assert pl*pr<0,('root bracket failed',i)
    assert c[-1].lo==1
    w=[F(x,10**5) for x in WEIGHT_NUMERATORS[s]]
    assert len(w)==n and min(w)>0
    # B = A^{-1} = differentiation at c_i of degree-s polynomial q
    # interpolating q(0)=0 and q(c_j)=v_j.
    B=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                val=1/c[j]+sum((1/(c[j]-c[k]) for k in range(n) if k!=j),Interval(0))
            else:
                val=(c[i]/c[j])/(c[j]-c[i])
                for k in range(n):
                    if k!=i and k!=j:
                        val=val*((c[i]-c[k])/(c[j]-c[k]))
            row.append(val)
        B.append(row)
    # Symmetrized stage operator. Exact interval enclosures are rounded outward
    # only through selecting a small rational central matrix, with errors
    # verified against BOTH exact interval endpoints.
    C=[[ (w[i]*B[i][j]+w[j]*B[j][i])/2 for j in range(n)] for i in range(n)]
    C0=[[round_nearest((C[i][j].lo+C[i][j].hi)/2,10**5) for j in range(n)] for i in range(n)]
    assert all(C0[i][j]==C0[j][i] for i in range(n) for j in range(n))
    row_errors=[]
    for i in range(n):
        row_errors.append(sum(max(abs(C[i][j].lo-C0[i][j]),abs(C[i][j].hi-C0[i][j])) for j in range(n)))
    assert max(row_errors)<F(1,20000),('too large interval error (>=1/20000)',s,float(max(row_errors)))
    # Since C0-0.001 I is SPD by exact rational LDL, true C is SPD:
    # ||C-C0||_2 <= ||C-C0||_infty < 0.00005, yielding lambda_min(C)>0.00095.
    shifted=[[C0[i][j]-(F(1,1000) if i==j else F(0)) for j in range(n)] for i in range(n)]
    pivots=positive_by_LDL(shifted)
    print('s',s,'exact root enclosures',s-1,'weights',WEIGHT_NUMERATORS[s],
          'max row error',float(max(row_errors)), 'min LDL pivot',min(pivots),
          'verified C strictly positive')

if __name__=='__main__':
    for s in (8,9,10):verify(s)
    print('PASS: exact-rational Jacobi-root and matrix definiteness certificates')
