import numpy as np, math
from fractions import Fraction as F

# Exact rational arithmetic in units of 3^-8.
P = 3**8  # 6561
def Fc(a, b, n=None):
    """Cantor level-n cells as integer intervals [A,B] in units of P (n<=8)."""
    ivs = [(0, P)]
    for _ in range(n):
        n0 = []
        for (A, B) in ivs:
            L = (B-A)//3
            n0.append((A, A+L)); n0.append((B-L, B))
        ivs = n0
    return ivs

def intlog_rigorous(w, K=200000):
    """Rigorous enclosure of log(w), w>0 rational-ish float, via interval Taylor at 1.
    Uses scaling w = 2^e * m, m in [1,2), and log m = 2*atanh((m-1)/(m+1)) series."""
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    wD = Decimal(str(w))
    e = int(math.floor(math.log2(w)))
    m = wD / (Decimal(2) ** e)
    if m < 1 or m >= 2:
        e2 = int(m.ln() / Decimal(2).ln()) if m >= 1 else 0
        m = m / (Decimal(2) ** e2); e += e2
    z = (m-1)/(m+1)
    # 2*sum z^{2k+1}/(2k+1), alternating-free positive terms; tail bound geometric
    s = Decimal(0); t = z
    k = 0
    while True:
        term = t/(2*k+1)
        s += term
        k += 1
        t = t*z*z
        if abs(float(t)) < 1e-55:
            tail = abs(float(t))/(1-float(z*z))/(2*k+1)
            break
    s = 2*s
    tail2 = 2*tail
    ln2 = Decimal(2).ln()
    v = s + e*ln2
    return float(v)-tail2-1e-15, float(v)+tail2+1e-15

def Fs_int(A, B):
    """Rigorous interval for G(B)-G(A) with G(w)=(w^2/2)(log|w|-3/2),
    A,B integers in units of P (coords A/P,B/P), A,B>=0 small.
    Compute h(w)=w^2 log w and w^2/2*1.5 parts with directed rounding margins."""
    import struct
    def w2logw(wint):
        # w = wint/P; w^2 log w = w^2 (log wint - log P)
        if wint == 0: return (0.0, 0.0)
        w = wint/P
        lo, hi = intlog_rigorous(w)
        # interval: w^2*[lo,hi]; widen for float error in w^2 (margin 4 ulp-ish 1e-14 rel)
        c = w*w
        m = 1e-13*(1+c)
        return (c*lo-m if lo < 0 else c*lo-m, c*hi+m if hi > 0 else c*hi+m)
    def w2(wint):
        w = wint/P
        return (w*w*(1-1e-15), w*w*(1+1e-15))
    # G(w) = (w^2 log|w|)/2 - 3 w^2/4 ; for w>=0
    def G(wint):
        if wint == 0: return (0.0, 0.0)
        a, b = w2logw(wint); c, d = w2(wint)
        return (a/2-3*d/4-1e-14, b/2-3*c/4+1e-14)
    GA = G(A); GB = G(B)
    return (GB[0]-GA[1], GB[1]-GA[0])

def Dlog_int(A1, B1, A2, B2):
    # int int log|x-y| over cells [A1,B1]x[A2,B2]/P, non-overlapping (or general via formula)
    t1 = Fs_int(abs(B1-A2), abs(B1-A2))  # placeholder replaced below
    # F(b-c)-F(b-d)-F(a-c)+F(a-d), F(w)=G(|w|)
    def G(wint):
        return Fs_int(0, 0) if wint == 0 else _G(wint)
    def _G(wint):
        return Gpos(wint)
    Fbc = Gpos(abs(B1-A2)); Fbd = Gpos(abs(B1-B2)); Fac = Gpos(abs(A1-A2)); Fad = Gpos(abs(A1-B2))
    sgn = lambda X, Y: 1 if (X-Y) >= 0 else 1  # G takes |.|
    # log|x-y| antiderivative uses signed F with F(-w)=F(w) since even
    lo = Fbc[0]-Fbd[1]-Fac[1]+Fad[0]
    hi = Fbc[1]-Fbd[0]-Fac[0]+Fad[1]
    return (lo, hi)

def Gpos(wint):
    return Fs_int(0, 0) and _Gpos(wint)

def _Gpos(wint):
    # G(w) for w>0
    if wint == 0: return (0.0, 0.0)
    w = wint/P
    lo, hi = intlog_rigorous(w)
    c = w*w
    m = 1e-13*(1+c)
    a, b = (c*lo-m, c*hi+m)
    c2, d2 = (c*(1-1e-15), c*(1+1e-15))
    return (a/2-3*d2/4-1e-14, b/2-3*c2/4+1e-14)

# unit tests
print("log2 in", intlog_rigorous(2.0), "true", math.log(2.0))
print("log(1/9) in", intlog_rigorous(1/9), "true", math.log(1/9))
print("Gpos(729)=", Gpos(729))  # w=1/9
w = 1/9
print("true G(1/9)=", (w*w/2)*(math.log(w)-1.5))
print("Dlog self cell n=8:", Dlog_int(0, 1, 0, 1))  # 3^-8 cell self
h = 1/P
trueD = h*h*(math.log(h)-1.5)
print("true self D=", trueD)
