import numpy as np, math

# K(x,y) = log(1/|x-y|), positive on [0,1]^2. F'' = log|.| ; F(w)=(w^2/2)(log|w|-1.5)
def F(w):
    w = np.asarray(w, float)
    out = np.zeros_like(w)
    nz = w != 0
    u = w[nz]
    out[nz] = (u*u/2.0)*(np.log(abs(u))-1.5) if np.isscalar(u) else (u**2/2)*(np.log(np.abs(u))-1.5)
    return out

def Fs(w):
    if w == 0: return 0.0
    return (w*w/2.0)*(math.log(abs(w))-1.5)

def Dlog(a, b, c, d):
    # int_a^b int_c^d log|x-y| dx dy
    return Fs(b-c)-Fs(b-d)-Fs(a-c)+Fs(a-d)

def Kavg(a, b, c, d):
    return -Dlog(a, b, c, d)/((b-a)*(d-c))

def cantor(n):
    ivs = [[0.0, 1.0]]
    for _ in range(n):
        n0 = []
        for (a, b) in ivs:
            L = (b-a)/3
            n0.append([a, a+L]); n0.append([b-L, b])
        ivs = n0
    return ivs

def energy_uniform(cells):
    # normalized Lebesgue on union of cells; energy under K
    tot = sum(b-a for a, b in cells)
    E = 0.0
    for (a, b) in cells:
        for (c, d) in cells:
            E += -Dlog(a, b, c, d)
    return E/(tot*tot)

def Upot(x, cells, rho):
    # U^{nu}(x) = int K(x,y) rho dy over cells (rho = density const per total)
    s = 0.0
    for (c, d) in cells:
        if x < c: s += -((d-x)*math.log(d-x)-(d-x) - ((c-x)*math.log(c-x)-(c-x)))
        elif x > d: s += -(((x-c)*math.log(x-c)-(x-c)) - ((x-d)*math.log(x-d)-(x-d)))
        else:
            s += -(((x-c)*math.log(x-c+1e-300)-(x-c)) if x > c else 0.0) \
                 -(((d-x)*math.log(d-x+1e-300)-(d-x)) if x < d else 0.0)
        # careful: K = -log|x-y|; integral of -log over [c,d]
    return rho*s

def E1(t):
    # int log|t| dt = t log|t| - t ; we need int_c^d -log|x-y| dy pieces
    pass

# check Upot by quadrature on simple case
cells4 = cantor(4)
tot4 = sum(b-a for a, b in cells4)
rho4 = 1.0/tot4
U0 = energy_uniform(cells4)
print("U0 = I(nu0), nu0 uniform on C4:", U0)

# inner cells: those inside I01=[2/9,1/3] or I10=[2/3,7/9]
inner = [(a, b) for (a, b) in cells4 if a >= 2/9-1e-12 and b <= 1/3+1e-12 or a >= 2/3-1e-12 and b <= 7/9+1e-12]
outer = [(a, b) for (a, b) in cells4 if not ((a >= 2/9-1e-12 and b <= 1/3+1e-12) or (a >= 2/3-1e-12 and b <= 7/9+1e-12))]
print("num inner cells:", len(inner), "num outer:", len(outer))
J0 = energy_uniform(inner)
print("J0 = I(nu*), nu* uniform on inner C4 blocks:", J0)
C = (J0+U0)/2
print("C = (J0+U0)/2 =", C)

toti = sum(b-a for a, b in inner)
rhoi = 1.0/toti
# envelopes of U^{nu*} over each level-2 cylinder (sampled finely)
cyls = [(0, 1/9), (2/9, 1/3), (2/3, 7/9), (8/9, 1)]
for k, (a, b) in enumerate(cyls):
    xs = np.linspace(a, b, 2001)
    vals = np.array([Upot(x, inner, rhoi) for x in xs])
    print(f"cyl{k}: min={vals.min():.6f} max={vals.max():.6f} mean~{vals.mean():.6f}")
# lower-bound route: a >= (m1 - C)/(2(m1 - m0)) with m0 outer min, m1 inner min
m0 = min(min(Upot(x, inner, rhoi) for x in np.linspace(0, 1/9, 2001)),
         min(Upot(x, inner, rhoi) for x in np.linspace(8/9, 1, 2001)))
m1 = min(min(Upot(x, inner, rhoi) for x in np.linspace(2/9, 1/3, 2001)),
         min(Upot(x, inner, rhoi) for x in np.linspace(2/3, 7/9, 2001)))
print("m0=", m0, "m1=", m1)
print("implied a >= ", (m1-C)/(2*(m1-m0)))
