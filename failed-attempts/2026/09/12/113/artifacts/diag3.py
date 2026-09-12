import cmath, math
lam = 2j*math.pi
E = lambda z: lam*cmath.exp(z)
def tm_digit(i): return bin(i-1).count('1') & 1
M=800
s_tm=[tm_digit(i) for i in range(1,M+4)]
def tip(s, T, N):
    w = complex(T, 2*math.pi*s[N])
    for k in range(N, 0, -1):
        w = cmath.log(w/lam) + 2j*math.pi*s[k-1]
    return w
for N in [50,100,200,300,500,700]:
    for T in [3.0,5.0]:
        print(f"N={N} T={T}: {tip(s_tm,T,N)}")
w0=tip(s_tm,5.0,500)
z=w0; mn=1e9
for i in range(200):
    z=E(z)
    if abs(z)>1e6: print("escape at",i); break
    mn=min(mn,abs(z-w0))
else:
    print("no escape; min return |z_n-w0| over 200:", mn)
z=w0; idx=[]
for i in range(30):
    z=E(z)
    k=round(z.imag/(2*math.pi))
    idx.append(k)
print("orbit strip indices:", idx)
print("sigma-shifts of TM:", ["".join(map(str,s_tm[k:k+12])) for k in range(6)])
