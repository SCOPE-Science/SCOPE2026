import cmath, math
lam = 2j*math.pi
def E(z): return lam*cmath.exp(z)
def tm_digit(i): return bin(i-1).count('1') & 1
M=3000
s_tm=[tm_digit(i) for i in range(1,M+6)]
def F(x): return math.exp(x)-1.0
def Finv(y): return math.log1p(y)
def ray(s, t, Ttop=10.0):
    # lift t by F until >= Ttop; top approx w=T+2pi i s_{N+1}; pull back along s_1..s_N
    x=t; N=0
    while x<Ttop:
        x=F(x); N+=1
        if N>M-2: raise ValueError("depth exceeded")
    w=complex(x, 2*math.pi*s[N])
    for k in range(N,0,-1):
        w=cmath.log(w/lam)+2j*math.pi*s[k-1]
    return w, N
w0ref=complex(0.08803199956471025,0.014704204392486712)
print("TM ray honest computation:")
for t in [1.0,0.5,0.2,0.1,0.05,0.02,0.01,0.005,0.002,0.001]:
    w,N=ray(s_tm,t)
    print(f"t={t:<7} N={N:<4} g=({w.real:.10f},{w.imag:.10f}) |g-w0|={abs(w-w0ref):.2e}")
print()
print("Periodic controls (should tend to known landing points as t->0):")
s_zero=[0]*(M+6)
for t in [0.5,0.1,0.02,0.005]:
    w,N=ray(s_zero,t)
    print(f"zero t={t}: g=({w.real:.10f},{w.imag:.10f}) N={N}")
# fixed point of L_0:
wfix=complex(-1.340406207609493,0.9528262730678185)
print("zero-landing fixed pt:",wfix,"|E(w)-w|=",abs(E(wfix)-wfix))
