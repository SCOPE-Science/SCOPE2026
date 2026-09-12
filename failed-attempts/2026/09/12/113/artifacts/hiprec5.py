from mpmath import mp, mpc, log
mp.dps = 300
lam = mp.mpc(0, 2*mp.pi)
def tm_digit(i): return bin(i-1).count('1') & 1
M=6000
s=[tm_digit(i) for i in range(1,M+6)]
def tip(s,T,N):
    w = mp.mpc(T, 2*mp.pi*s[N])
    for k in range(N,0,-1):
        w = log(w/lam) + 2*mp.pi*mpc(0,1)*s[k-1]
    return w
E=lambda z: lam*mp.e**z
w0=tip(s,mp.mpf('10.0'),400)
z=w0; bad=None
for i in range(1,3001):
    z=E(z)
    k=int(mp.nint(z.imag/(2*mp.pi)))
    if k!=s[i]:
        print("first itinerary mismatch at n=",i,"got",k,"want",s[i], "Im/2pi=",mp.nstr(z.imag/(2*mp.pi),25),"|z|=",mp.nstr(abs(z),10)); bad=i; break
print("clean length:", (bad or 3001)-1)
# error growth: compare dps=150 w0 vs dps=300 w0
