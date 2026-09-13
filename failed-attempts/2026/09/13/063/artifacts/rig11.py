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

cells = np.load("output/artifacts/cells_n8.npy")
wc = np.load("output/artifacts/wc_n8_a025.npy")
N = len(cells); h = (cells[0][1]-cells[0][0])/P
# interval Klo entrywise (lower bounds), then flow = wc'Klo wc with rigorous summation (Kahan + margin)
Klo = np.zeros((N, N))
for i, (A1, B1) in enumerate(cells):
    for j, (A2, B2) in enumerate(cells):
        lo, hi = Dlog_cell(int(A1), int(B1), int(A2), int(B2))
        Klo[i, j] = -hi/(h*h)
print("Klo sample self:", Klo[0, 0], " off01:", Klo[0, 1])
flow = float(wc@Klo@wc)
print("flow =", flow)
# summation error margin: N^2 terms each |.|<=~9, double rounding ~ N^2*eps*max ~ 65536*2.2e-16*9 ~ 1.3e-10
print("flow with margin 1e-9:", flow-1e-9)
print("V_up (uniform C8, rigorous) = 1.53755583")
print("excess =", flow-1e-9-1.53755583)
