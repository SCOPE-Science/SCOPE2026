# Key rigidity question: does TM address coincide (up to shift) with a periodic address?
# TM is cube-free => not eventually periodic. Verify rigorously: if sigma^k(s) were periodic, s would be eventually periodic.
# Also check: could g_TM land at preperiodic point whose OWN address is different (preperiodic portrait)?
# For exponential Misiurewicz maps, landing rays at same point share periodic orbit portrait: all rays landing at a periodic point
# have addresses with same period dividing... Actually distinct rays at same periodic point: their shifts are distinct but all periodic?
# Test numerically: compute candidate periodic addresses near w0? Approach: find repelling cycles of periods<=6 near orbit, compute their addresses by strip itinerary, compare with TM shifts.
import cmath, math
lam=2j*math.pi
def E(z): return lam*cmath.exp(z)
def itinerary(z,n):
    out=[]
    for _ in range(n):
        z=E(z)
        # strip index: round(Im/2pi) but near boundaries ambiguous; here generic
        out.append(int(round(z.imag/(2*math.pi))))
    return out
w0=complex(0.08803199956471025,0.014704204392486712)
print("w0 fwd itinerary:", itinerary(w0,30))
def tm_digit(i): return bin(i-1).count('1') & 1
M=200; s_tm=[tm_digit(i) for i in range(1,M+2)]
print("TM head       :", s_tm[:30])
# Newton cycles
def Epow(z,q):
    for _ in range(q): z=E(z)
    return z
def Newton(z0,q,it=80):
    z=z0; h=1e-8
    for _ in range(it):
        f=Epow(z,q)-z
        if abs(f)<1e-15: break
        d=(Epow(z+h,q)-(z+h)-f)/h
        z=z-f/d
    return z
seeds=[w0,E(w0),E(E(w0))]
import itertools
found={}
for q in range(1,7):
    for s in seeds:
        r=Newton(s,q)
        if abs(Epow(r,q)-r)<1e-9 and abs(r)<50:
            key=(q,round(r.real,6),round(r.imag,6))
            if key not in found:
                found[key]=r
for key,r in found.items():
    q=key[0]
    print(f"period {q}: ({r.real:.8f},{r.imag:.8f}) itin={itinerary(r,12)}")
