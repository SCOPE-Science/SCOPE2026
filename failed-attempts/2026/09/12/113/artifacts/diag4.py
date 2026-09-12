import cmath, math
lam = 2j*math.pi
def E(z):
    try: return lam*cmath.exp(z)
    except OverflowError: return complex(float('inf'),float('inf'))
def tm_digit(i): return bin(i-1).count('1') & 1
M=800
s_tm=[tm_digit(i) for i in range(1,M+4)]
def tip(s, T, N):
    w = complex(T, 2*math.pi*s[N])
    for k in range(N, 0, -1):
        w = cmath.log(w/lam) + 2j*math.pi*s[k-1]
    return w
w0=tip(s_tm,5.0,500)
print("w0=",w0)
z=w0; mn=1e9; hist=[]
for i in range(60):
    z=E(z)
    if not math.isfinite(z.real+z.imag): print("escape at",i); break
    hist.append(z)
    mn=min(mn,abs(z-w0))
print("min return:",mn)
print("first 12:",[f"({p.real:.4f},{p.imag:.4f})" for p in hist[:12]])
print("strips:",[round(p.imag/(2*math.pi)) for p in hist[:20]])
# For landing at repelling preperiodic point, shifts of address should be eventually periodic.
# But the orbit strips IS sigma-shift of address only if ray lands; numeric orbit of w0 should have strips = TM[1],TM[2]...?
print("TM head:", s_tm[:20])
