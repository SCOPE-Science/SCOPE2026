import cmath, math
lam = 2j*math.pi
def E(z): return lam*cmath.exp(z)
def tm_digit(i): return bin(i-1).count('1') & 1
M=60000
s_tm=[tm_digit(i) for i in range(1,M+6)]
def F(x): return math.exp(x)-1.0
def ray(s, t, Ttop=10.0):
    x=t; N=0
    while x<Ttop:
        x=F(x); N+=1
        if N>M-2: raise ValueError("depth exceeded at t=%r"%t)
    w=complex(x, 2*math.pi*s[N])
    for k in range(N,0,-1):
        w=cmath.log(w/lam)+2j*math.pi*s[k-1]
    return w, N, x
wref=complex(0.08803199956471025,0.014704204392486712)
print("Ttop sensitivity at t=0.01:")
for Ttop in [6.0,8.0,10.0,14.0]:
    w,N,x=ray(s_tm,0.01,Ttop=Ttop)
    print(f"  Ttop={Ttop}: N={N} g=({w.real:.12f},{w.imag:.12f}) |g-wref|={abs(w-wref):.2e}")
print("dense t sweep (Ttop=10):")
ts=[0.05,0.03,0.02,0.015,0.01,0.007,0.005,0.003,0.002,0.001,5e-4,2e-4,1e-4]
prev=None
for t in ts:
    w,N,x=ray(s_tm,t)
    d=abs(w-wref)
    step="" if prev is None else f" step={abs(w-prev):.1e}"
    print(f"  t={t:<8} N={N:<6} g=({w.real:.12f},{w.imag:.12f}) |g-wref|={d:.2e}{step}")
    prev=w
