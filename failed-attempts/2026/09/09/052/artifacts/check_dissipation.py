"""Lane 409 — part 5: dissipation-vs-energy superlinearity (orbit-blowup <=> E->inf route).

Verifies on a lattice proxy (su(2)~R^3-valued 1-form on periodic grid):
 E(A) = 1/2 Σ_faces |F|^2 dx^3,  F = dA + g[A,A] (lattice exterior derivative).
 grad E via AD-free analytic formula; dissipation D = ||grad E||_2^2 (dx^3-weighted).
Tests:
 1. Concentration family A^{(λ)}(x) = λ φ(λx) (bump 1-form): fit E ~ λ^1, D ~ λ^3 => D ~ E^3.
 2. Amplitude family A^{(λ)} = λ φ (fixed profile): fit E ~ λ^4, D ~ λ^6 => D ~ E^{1.5}.
 3. Abelian-constant ray: E = 0, D = 0 at all λ (orbit-compact flat direction, harmless).
 4. Ito-trace coefficient: fit of Σ_{0<|k|<=N} |k|^{-2} = 4πN + b; check c vs 4π.
Writes results5.json.
"""
import json, math, os
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results5.json")
rng = np.random.default_rng(40905)
res = {}

N = 48  # grid per dim (period 2π)
L = 2 * math.pi
dx = L / N
xs = np.linspace(0, L - dx, N)

# Bump 1-form profile: A_1^3 = exp(-r^2/2σ^2)-type bump centered, others 0 (non-abelian color fixed so [A,A]=0 here;
# add second component A_2^1 = 0.7*bump shifted to generate nonzero [A,A]).
SIG = 0.6
C = np.array([L/2]*3)
def bump(ix, iy, iz, shift=(0,0,0)):
    X = xs[ix]-C[0]-shift[0]; Y = xs[iy]-C[1]-shift[1]; Z = xs[iz]-C[2]-shift[2]
    # periodize distance
    X = (X + L/2) % L - L/2; Y = (Y + L/2) % L - L/2; Z = (Z + L/2) % L - L/2
    return math.exp(-(X*X+Y*Y+Z*Z)/(2*SIG*SIG))

I1, I2, I3 = np.meshgrid(range(N), range(N), range(N), indexing='ij')
B1 = np.vectorize(lambda a,b,c: bump(a,b,c))(I1,I2,I3)
B2 = np.vectorize(lambda a,b,c: bump(a,b,c,(0.5,0,0)))(I1,I2,I3)
# base profile: A[i,a] arrays
Abase = np.zeros((3,3,N,N,N))
Abase[0,2] = B1           # A_1^3
Abase[1,0] = 0.7*B2        # A_2^1  (non-commuting colors => [A1,A2]~cross != 0)

def curl_F(A, g):
    # F_ij^a = ∂i Aj - ∂j Ai + g ε^abc Ai^b Aj^c ; central differences
    F = np.zeros((3,3,3)+A.shape[2:])
    def d(idx, Fld):
        return (np.roll(Fld,-1,axis=idx+1)-np.roll(Fld,1,axis=idx+1))/(2*dx)
    for i in range(3):
        for j in range(3):
            F[i,j] = d(i,A[j])-d(j,A[i])
            cr = np.cross(A[i].transpose(1,2,3,0), A[j].transpose(1,2,3,0)).transpose(3,0,1,2)
            F[i,j] = F[i,j] + g*cr
    return F

def energy(A, g):
    F = curl_F(A,g)
    return 0.5*np.sum(F**2)*dx**3

def grad_energy(A, g):
    # δE/δA_k^a = -(∂i F_ik^a) + g ε^abc Ai^b F_ic... : adjoint of d + ad.
    F = curl_F(A,g)
    G = np.zeros_like(A)
    def d(idx, Fld):
        return (np.roll(Fld,-1,axis=idx+1)-np.roll(Fld,1,axis=idx+1))/(2*dx)
    for k in range(3):
        acc = np.zeros_like(A[k])
        for i in range(3):
            acc = acc - d(i, F[i,k])
            # ad term: g [A_i, F_ik] (color cross)
            acc = acc + g*np.cross(A[i].transpose(1,2,3,0), F[i,k].transpose(1,2,3,0)).transpose(3,0,1,2)
        G[k] = acc
    return G

def dissipation(A, g):
    G = grad_energy(A,g)
    return float(np.sum(G**2)*dx**3)

g = 0.5
# --- Test 2 first (cheap): amplitude scaling (no resampling) ---
lams = [0.5, 1.0, 2.0, 4.0]
Es, Ds = [], []
for lam in lams:
    A = lam*Abase
    Es.append(energy(A,g)); Ds.append(dissipation(A,g))
res["amplitude_E"] = dict(zip(map(str,lams),Es))
res["amplitude_D"] = dict(zip(map(str,lams),Ds))
# fit log-log slopes
le, ld = np.log(Es), np.log(Ds)
se, _ = np.polyfit(np.log(lams), le, 1)
sd, _ = np.polyfit(np.log(lams), ld, 1)
res["amplitude_E_exponent"] = float(se)   # expect ~4 (quartic-dominated at large λ) ; small λ ~2
res["amplitude_D_exponent"] = float(sd)   # expect ~6
res["amplitude_D_vs_E"] = float(sd/se)    # expect ~1.5
# large-λ only fit (last 3 points)
se2,_ = np.polyfit(np.log(lams[-2:]), le[-2:], 1)
sd2,_ = np.polyfit(np.log(lams[-2:]), ld[-2:], 1)
res["amplitude_E_exp_large"] = float(se2)
res["amplitude_D_exp_large"] = float(sd2)
res["amplitude_D_vs_E_large"] = float(sd2/se2)

# --- Test 3: abelian constants ---
for lam in [1.0, 50.0]:
    A = np.zeros_like(Abase); A[0,2] = lam  # constant abelian
    res[f"abelian_E_lam{lam}"] = energy(A,g)
    res[f"abelian_D_lam{lam}"] = dissipation(A,g)

# --- Test 1: concentration scaling via analytic formula (no resampling error) ---
# E(λ) = λ^{4-d}E1 with d=3 -> λ^1; D(λ) = λ^{6-d}... D scales as λ^3 (derived); verify RATIO on lattice:
# emulate by noting F^λ(x) = λ^2 F(λx): E ratio exact λ^1 by change of variables (continuum).
# On lattice, verify change-of-variables factor directly: sum over refined/coarse not available;
# instead verify the ALGEBRAIC identity D/E^3 = const along amplitude family at large λ (from test 2)
# and E-linearity in λ along a dilation implemented by Fourier rescaling of the bump width.
widths = [0.9, 0.6, 0.4]
Er, Dr = [], []
for s in widths:
    Bb = np.vectorize(lambda a,b,c,s=s: math.exp(-((( (xs[a]-C[0]+L/2)%L-L/2)**2+((xs[b]-C[1]+L/2)%L-L/2)**2+((xs[c]-C[2]+L/2)%L-L/2)**2)/(2*s*s))))(I1,I2,I3)
    lam = SIG/s  # concentration factor λ = σ/s keeps L^2-ish mass: A^λ = λ φ(λ·) with φ width σ
    A = np.zeros_like(Abase); A[0,2] = lam*Bb; A[1,0] = 0.7*lam*np.roll(Bb,3,axis=0)
    Er.append(energy(A,g)); Dr.append(dissipation(A,g))
res["concentr_widths"] = widths
res["concentr_E"] = Er
res["concentr_D"] = Dr
lams_c = [SIG/s for s in widths]
cle,_ = np.polyfit(np.log(lams_c), np.log(Er), 1)
cld,_ = np.polyfit(np.log(lams_c), np.log(Dr), 1)
res["concentr_E_exponent"] = float(cle)  # expect ~1
res["concentr_D_exponent"] = float(cld)  # expect ~3
res["concentr_D_vs_E"] = float(cld/cle)  # expect ~3

# --- Test 4: 4π coefficient ---
Ns = [5,10,15,20,30]
S = {}
for Nn in Ns:
    s = 0.0
    for k1 in range(-Nn,Nn+1):
        for k2 in range(-Nn,Nn+1):
            for k3 in range(-Nn,Nn+1):
                r2 = k1*k1+k2*k2+k3*k3
                if r2 == 0 or r2 > Nn*Nn: continue
                s += 1.0/r2
    S[Nn] = s
A = np.vstack([Ns, np.ones(len(Ns))]).T
c, b = np.linalg.lstsq(A, [S[n] for n in Ns], rcond=None)[0]
res["ito_trace_fit_c"] = float(c)
res["ito_trace_4pi"] = 4*math.pi
res["ito_trace_relerr"] = abs(c-4*math.pi)/(4*math.pi)
res["ito_trace_b"] = float(b)

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
