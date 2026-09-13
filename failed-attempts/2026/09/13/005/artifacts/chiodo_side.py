"""Route (ii): independent intersection-theory evaluation of h_DL at (g,d,mu)=(2,7,(3,2,1,1))
via the DL pushed-forward Chiodo formula (eq ELSVdMgn):
  h = d^{2-g} \int_{Mbar_{2,4}} eps_*Ch^{[d]}(7,7;-3,-2,-1,-1) / prod(1-mu_i psi_i).
We expand with Chiodo's formula + JPPZ stable-graph formula for eps_*Ch, using exact
Bernoulli values, and Witten-Kontsevich (DVV/string) psi-integrals computed from scratch
(base <tau0^3>_0=1, string, dilaton, DVV). No use of the sinh/GJV polynomial input.
Prints every contributing Hodge-type integral (all monomials psi^a kappa^b and boundary pushforwards).
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb

# ---------- Bernoulli ----------
def bernoulli(n):
    # exact via series x/(e^x-1)
    a=[Fraction(0)]*(n+1); a[0]=Fraction(1)
    for m in range(1,n+1):
        s=Fraction(0)
        for k in range(m):
            s+=a[k]*Fraction(factorial(m+1),factorial(k)*factorial(m+1-k))
        # sum_{k=0}^{m} C(m+1,k) a_k = 0 for m>=1  => a_m = -s/(m+1)... careful: C(m+1,m)=m+1
        a[m]=-s/Fraction(m+1)
    return a[n]
def Bpoly(n,x):
    # Bernoulli polynomial exact at rational x
    from math import comb as C
    return sum(Fraction(C(n,k))*bernoulli(k)* (x**(n-k)) for k in range(n+1))

print("B2(1)=",Bpoly(2,1),"B2(6/7)=",Bpoly(2,Fraction(6,7)))

# ---------- psi integrals on Mbar_{g,n} ----------
# cache keyed (g, tuple(a))
from functools import lru_cache
def dim(g,n): return 3*g-3+n
@lru_cache(maxsize=None)
def psi_int(g, a):
    """<prod tau_{a_i}>_{g,n}, exact, via string/dilaton/DVV + base cases. a: tuple length n."""
    a=tuple(a); n=len(a); D=dim(g,n)
    if sum(a)!=D: return Fraction(0)
    if g==0:
        if n<3: return Fraction(0)  # unstable here (we only call stable)
        return Fraction(factorial(n-3),1) * prod_frac([Fraction(1,factorial(x)) for x in a])
    if g==1 and n==1: return Fraction(1,24)  # <tau1>
    # string: if any a_i==0 remove it (n>=1, 2g-2+n>0)
    if 0 in a:
        i=a.index(0)
        b=list(a); b.pop(i)
        return sum( (Fraction(b[j]-1+1,1) if False else Fraction(0)) for j in []) # placeholder
    return _dvv(g,a)
def prod_frac(xs):
    p=Fraction(1)
    for x in xs: p*=x
    return p

# implement string/dilaton/DVV properly with recursion on (g,n,sum)
from functools import lru_cache as lc
@lc(maxsize=None)
def I(g, a):
    a=tuple(a); n=len(a)
    if n==0: return Fraction(0)
    D=3*g-3+n
    if sum(a)!=D: return Fraction(0)
    if g==0:
        if n<3: return Fraction(0)
        return Fraction(factorial(n-3))/prod_frac([Fraction(factorial(x)) for x in a])
    if g==1 and n==1:
        return Fraction(1,24)
    if 0 in a:
        # string equation: <tau_0 prod tau>=sum_j <..tau_{a_j-1}..>
        i=list(a).index(0)
        b=list(a); b.pop(i)
        tot=Fraction(0)
        for j in range(len(b)):
            if b[j]>0:
                c=list(b); c[j]-=1
                tot+=I(g,tuple(c))
        return tot
    # dilaton: all a_i>=1; if some a_i==1 use dilaton to reduce n
    if 1 in a and n>1:
        i=list(a).index(1)
        b=list(a); b.pop(i)
        return Fraction(2*g-2+len(b))*I(g,tuple(b))
    # DVV (Witten): pick first index with a_1>=1... here all>=2
    # <tau_{k+1} prod_{i>=2} tau_{a_i}> = 1/(2k+3)!! [....]. Use standard form:
    k=a[0]-1
    rest=a[1:]
    # term A: sum_j (2a_j+1)!!/(2k+1)!!/(2(a_j-1)+1)!! ... use factorials: (2m+1)!!=(2m+1)!/(2^m m!)
    from math import factorial as F
    def oddfact(m): return Fraction(F(2*m+1), 2**m * F(m))
    tot=Fraction(0)
    for j in range(len(rest)):
        aj=rest[j]
        c=[0]*len(rest); 
        for t in range(len(rest)): c[t]=rest[t]
        c[j]=aj+k
        tot+= oddfact(aj+k-1+1-1+1)*0  # placeholder replaced below
    return _dvv_full(g,a)

def _dvv_full(g,a):
    # Full DVV recursion, exact.
    from math import factorial as F
    def oddfact(m): return Fraction(F(2*m+1), 2**m * F(m)) if m>=0 else Fraction(1)
    def dblodd_ratio(num, den): return oddfact(num)/oddfact(den)
    k=a[0]-1
    rest=list(a[1:])
    tot=Fraction(0)
    # A: sum_{j>=2} (2a_j+1)!!/(2k+1)!! * ... use standard: coefficient (2(a_j+k)+1)!!/((2k+1)!!(2a_j-1)!!)
    for j in range(len(rest)):
        aj=rest[j]
        c=list(rest); c[j]=aj+k
        tot+= dblodd_ratio(aj+k, 0)*0  # placeholder
    raise NotImplementedError("use dvv() below")

def dvv(g, a):
    """Standalone DVV recursion with memo, standard formula:
    <tau_{k+1} T> = 1/(2k+3)!! [ sum_j (2a_j+1)!!/(2(a_j-1)+1)!! ... ] — implement known-good version:
    2k+3)!! <tau_{k+1} prod tau_{a_j}> = sum_j (2(a_j+k)+1)!!/(2a_j-1)!! <..tau_{a_j+k}..>
      + 1/2 sum_{s+t=k-1} (2s+1)!!(2t+1)!! [ <tau_s tau_t T>_{g-1} + sum splits ]."""
    from math import factorial as F
    def of(m): return Fraction(F(2*m+1), 2**m*F(m)) if m>=0 else Fraction(1)
    key=(g,tuple(a))
    return _dvv_memo(g,tuple(a),of)

@lc(maxsize=None)
def _dvv_memo(g,a,of=None):
    from math import factorial as F
    def oddf(m): return Fraction(F(2*m+1), 2**m*F(m)) if m>=0 else Fraction(1)
    a=tuple(a); n=len(a); D=3*g-3+n
    if sum(a)!=D: return Fraction(0)
    if g==0:
        if n<3: return Fraction(0)
        return Fraction(F(n-3))/prod_frac([Fraction(F(x)) for x in a])
    if g==1 and n==1: return Fraction(1,24)
    if 0 in a:
        i=list(a).index(0); b=list(a); b.pop(i); tot=Fraction(0)
        for j in range(len(b)):
            if b[j]>0:
                c=list(b); c[j]-=1; tot+=_dvv_memo(g,tuple(c))
        return tot
    if 1 in a and n>1:
        i=list(a).index(1); b=list(a); b.pop(i)
        return Fraction(2*g-2+len(b))*_dvv_memo(g,tuple(b))
    # all >=2: DVV on first marking
    k=a[0]-1; rest=list(a[1:])
    rhs=Fraction(0)
    for j in range(len(rest)):
        aj=rest[j]; c=list(rest); c[j]=aj+k
        rhs+= oddf(aj+k)/oddf(aj-1)*_dvv_memo(g,tuple([0]*0+([0] if False else [])) if False else tuple(c))
    # B: genus-split terms
    for s in range(k+1):
        t=k-s
        # non-separating
        rhs+= Fraction(1,2)*oddf(s)*oddf(t)*_dvv_memo(g-1,tuple(rest+[s,t]))
        # separating: subsets of rest
        m=len(rest)
        for mask in range(1,(1<<m)-1):
            I1=[rest[j] for j in range(m) if mask>>j &1]; I2=[rest[j] for j in range(m) if not mask>>j &1]
            # avoid double count: fix element 0 in I1
            if 0 not in [rest[j] for j in range(m) if mask>>j &1][:1] and True:
                pass
            # enforce canonical: first rest element in I1
            if not (mask & 1): continue
            for g1 in range(g+1):
                g2=g-g1
                n1=len(I1)+1; n2=len(I2)+1
                if 2*g1-2+n1<=0 or 2*g2-2+n2<=0: continue
                if sum(I1)+s!=3*g1-3+n1 or sum(I2)+t!=3*g2-3+n2: continue
                rhs+= Fraction(1,2)*oddf(s)*oddf(t)*_dvv_memo(g1,tuple(I1+[s]))*_dvv_memo(g2,tuple(I2+[t]))
        # stable range check for g-1 term
        # (memo handles instability by returning 0 via dim mismatch? ensure n>=1 for g=0 etc.)
    return rhs/oddf(k+1)

if __name__=="__main__":
    # validate psi engine against known values
    checks=[
        ((0,(1,1,1,0,0,0)),None),
    ]
    print("g0 7-pt <1^4>:", _dvv_memo(0,(1,1,1,1,0,0,0)))
    print("g1 <1>:", _dvv_memo(1,(1,)))
    print("g1 <1,0>:", _dvv_memo(1,(1,0)))
    print("g2 <4>:", _dvv_memo(2,(4,)))
    print("g2 <3,1>:", _dvv_memo(2,(3,1)))
    print("g2 <2,2>:", _dvv_memo(2,(2,2)))
    print("g2 <2,1,1>:", _dvv_memo(2,(2,1,1)))
    print("g2 <1,1,1,1>:", _dvv_memo(2,(1,1,1,1)))
    # known: <tau4>_2=1/1152, <tau3 tau1>=... check
