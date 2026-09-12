import cmath, math
lam = 2j*math.pi
E = lambda z: lam*cmath.exp(z)
def tm_digit(i): return bin(i-1).count('1') & 1
def tip(s, T, N):
    w = complex(T, 2*math.pi*s[N])
    for k in range(N, 0, -1):
        w = cmath.log(w/lam) + 2j*math.pi*s[k-1]
    return w
Nmax=600
s_tm=[tm_digit(i) for i in range(1,Nmax+3)]
# 1) consecutive-N trace for fixed T
for T in [1.0,3.0,5.0,8.0]:
    seq=[tip(s_tm,T,N) for N in range(1,201)]
    tail=seq[-20:]
    import statistics
    print(f"T={T} last5:", [f"({p.real:.6f},{p.imag:.6f})" for p in seq[-5:]])
    print(f"   spread last50: Re[{min(p.real for p in seq[-50:]):.8f},{max(p.real for p in seq[-50:]):.8f}] Im[{min(p.imag for p in seq[-50:]):.8f},{max(p.imag for p in seq[-50:]):.8f}]")
    print(f"   spread N=1..200: Re[{min(p.real for p in seq):.6f},{max(p.real for p in seq):.6f}] Im[{min(p.imag for p in seq):.6f},{max(p.imag for p in seq):.6f}]")
# 2) candidate landing point orbit
w0=tip(s_tm,5.0,500)
print("candidate w0=",w0)
z=w0
for i in range(10):
    z=E(z)
    print(i+1, f"{z.real:.8f} {z.imag:.8f} |z|={abs(z):.6f}")
# 3) preperiod check: distance to postsingular {0, lam} and to cycles
print("|w0|=",abs(w0),"|w0-lam|=",abs(w0-lam))
