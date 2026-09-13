import numpy as np, math

P = 3**10
def intlog(w):
    from decimal import Decimal, getcontext
    getcontext().prec = 60
    wD = Decimal(str(w))
    e = int(math.floor(math.log2(w)))
    m = wD / (Decimal(2) ** e)
    z = (m-1)/(m+1)
    s = Decimal(0); t = z; k = 0
    while True:
        s += t/(2*k+1); k += 1; t = t*z*z
        if abs(float(t)) < 1e-55:
            tail = abs(float(t))/(1-float(z*z))/(2*k+1); break
    s = 2*s; tail2 = 2*tail
    v = s + e*Decimal(2).ln()
    return float(v)-tail2-1e-15, float(v)+tail2+1e-15

def Gpos(wint):
    if wint == 0: return (0.0, 0.0)
    w = wint/P
    lo, hi = intlog(w)
    c = w*w
    m = 1e-13*(1+c)
    a, b = (c*lo-m, c*hi+m)
    c2, d2 = (c*(1-1e-15), c*(1+1e-15))
    return (a/2-3*d2/4-1e-14, b/2-3*c2/4+1e-14)

def Dlog_cell(A1, B1, A2, B2):
    Fbc = Gpos(abs(B1-A2)); Fbd = Gpos(abs(B1-B2)); Fac = Gpos(abs(A1-A2)); Fad = Gpos(abs(A1-B2))
    return (Fbc[0]-Fbd[1]-Fac[1]+Fad[0], Fbc[1]-Fbd[0]-Fac[0]+Fad[1])

def cantor_int(n):
    ivs = [(0, P)]
    for _ in range(n):
        n0 = []
        for (A, B) in ivs:
            L = (B-A)//3
            n0.append((A, A+L)); n0.append((B-L, B))
        ivs = n0
    return ivs

def Kpoint_avg(xn, A2, B2):
    # (1/h) int_{cell2} K(xn,y) dy, xn int coord possibly inside cell2
    h = (B2-A2)/P
    F = lambda d: d*math.log(d)-d if d > 0 else 0.0
    if xn <= A2:
        d1 = (A2-xn)/P; d2 = (B2-xn)/P
        return (F(d2)-F(d1))/h * -1.0 * -1.0  # check sign below
    return None

# sign check: int_{c}^{d} -log|x-y| dy for x<=c: substitute t=y-x: -int_{c-x}^{d-x} log t dt = -(F(d2)-F(d1))
for (xn, c, d) in [(0, 10, 20)]:
    h = (d-c)/P
    F = lambda t: t*math.log(t)-t
    print("formula:", -(F((d-xn)/P)-F((c-xn)/P))/h)
    import scipy.integrate as I if False else None
