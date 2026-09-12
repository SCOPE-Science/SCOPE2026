import cmath, math
lam = 2j*math.pi
def tm_digit(i):  # 1-indexed c_i = parity(popcount(i-1))
    return bin(i-1).count('1') & 1
def tip(s, T, N):
    # s: list 0-indexed digits; pull back w=T+2pi i s[N] along s[N-1]..s[0]
    w = complex(T, 2*math.pi*s[N])
    for k in range(N, 0, -1):
        w = cmath.log(w/lam) + 2j*math.pi*s[k-1]
    return w
def run(s, T, Ns):
    return [(N, tip(s, T, N)) for N in Ns]
# controls: periodic address 0^infty and period-2 (01)^infty
Nmax = 400
s_zero = [0]*(Nmax+2)
s_01 = [(i%2) for i in range(Nmax+2)]  # 0,1,0,1... (1-indexed: c1=0,c2=1,...)
s_tm = [tm_digit(i) for i in range(1, Nmax+3)]
Ns = list(range(10, Nmax+1, 10))
for name, s in [("zero", s_zero), ("01", s_01), ("TM", s_tm)]:
    for T in [3.0, 5.0]:
        pts = run(s, T, Ns)
        tail = [p for _, p in pts[-10:]]
        rs = [p.real for _, p in pts]; ms = [p.imag for _, p in pts]
        succ = [abs(pts[i+1][1]-pts[i][1]) for i in range(len(pts)-1)]
        print(f"{name} T={T}: tailRe=[{min(p.real for p in tail):.4f},{max(p.real for p in tail):.4f}] "
              f"tailIm=[{min(p.imag for p in tail):.4f},{max(p.imag for p in tail):.4f}] "
              f"lastSucc={succ[-1]:.2e} maxSucc_tail={max(succ[-10:]):.2e} maxAbs={max(abs(p) for _,p in pts):.3f}")
    print()
# fixed-point residual check for zero-address limit
w = tip(s_zero, 5.0, 400)
print("zero-limit w=", w, " |E(w)-w|=", abs(lam*cmath.exp(w)-w))
w2 = tip(s_tm, 5.0, 400)
print("TM N=400 tip=", w2)
