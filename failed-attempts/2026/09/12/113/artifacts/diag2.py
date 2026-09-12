import cmath, math
lam = 2j*math.pi
E = lambda z: lam*cmath.exp(z)
def tm_digit(i): return bin(i-1).count('1') & 1
def tip(s, T, N):
    w = complex(T, 2*math.pi*s[N])
    for k in range(N, 0, -1):
        w = cmath.log(w/lam) + 2j*math.pi*s[k-1]
    return w
Nmax=60
s_tm=[tm_digit(i) for i in range(1,Nmax+3)]
# check the shift property: sigma^k(TM) addresses
print("TM prefix:", ''.join(map(str,s_tm[:32])))
for k in range(8):
    print(k, ''.join(map(str,s_tm[k:k+24])))
# Fixed-point-free check? test w0 orbit long: does it escape/return near w0?
w0=tip(s_tm,5.0,150)
z=w0; mn=1e9
for i in range(200):
    z=E(z)
    if abs(z)>1e6: print("escape at",i); break
    mn=min(mn,abs(z-w0))
else:
    print("no escape; min return |z_n-w0|:", mn)
# check tail-digits: s_tm[N] for N near 150.. deterministic
# Orbit address test: track imag-strip index of E^n(w0) along actual numeric orbit
z=w0
idx=[]
for i in range(30):
    z=E(z)
    k=round(z.imag/(2*math.pi))
    idx.append(k)
print("orbit strip indices:", idx)
print("TM tail shifted? TM[1..30]:", s_tm[:30])
# Address of ray should satisfy: E(g_s(t)) = g_{sigma s}(F(t)); landing point orbit strips follow sigma shifts
