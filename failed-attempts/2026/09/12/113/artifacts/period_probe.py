import cmath, math
from fractions import Fraction
lam=2j*math.pi
def E(z): return lam*cmath.exp(z)
def dE(z): return E(z)
# candidate w0
w0=complex(0.08803199956471025,0.014704204392486712)
# orbit
orb=[w0]
z=w0
for i in range(40):
    z=E(z); orb.append(z)
# find near-returns of orb[?] to detect preperiod/period: compute pairwise distances among first 30 (skip escape? check magnitudes)
print("magnitudes:",[f"{abs(p):.3f}" for p in orb[:15]])
D={}
n=len(orb)
for i in range(n):
    for j in range(i+1,n):
        if abs(orb[i])<50 and abs(orb[j])<50:
            d=abs(orb[i]-orb[j])
            if d<1e-3: D[(i,j)]=d
print("close pairs (<1e-3):",D)
# Newton search for repelling cycle near orb tail? Use Newton on E^q - id from seeds along orbit
def Epow(z,q):
    for _ in range(q): z=E(z)
    return z
def Newton(z0,q,it=60):
    z=z0
    h=1e-7
    for _ in range(it):
        f=Epow(z,q)-z
        d=(Epow(z+h,q)-(z+h)-f)/h
        if abs(d)<1e-12: break
        z=z-f/d
        if abs(f)<1e-14: break
    return z
for q in [1,2,3,4,5,6]:
    for seed in orb[1:8]:
        try:
            r=Newton(seed,q)
            if abs(Epow(r,q)-r)<1e-8 and abs(r)<50:
                # multiplier
                h=1e-7
                m=(Epow(r+h,q)-Epow(r-h,q))/(2*h)
                print(f"q={q} seed~({seed.real:.3f},{seed.imag:.3f}) -> root ({r.real:.10f},{r.imag:.10f}) res={abs(Epow(r,q)-r):.1e} mult={m:.4f} |m|={abs(m):.4f}")
                break
        except Exception as ex: pass
