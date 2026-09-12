from mpmath import mp, mpc, log
mp.dps = 120
lam = mp.mpc(0, 2*mp.pi)
def tm_digit(i): return bin(i-1).count('1') & 1
M=9000
s=[tm_digit(i) for i in range(1,M+6)]
def tip(s,T,N):
    w = mp.mpc(T, 2*mp.pi*s[N])
    for k in range(N,0,-1):
        w = log(w/lam) + 2*mp.pi*mpc(0,1)*s[k-1]
    return w
E=lambda z: lam*mp.e**z
w0=tip(s,mp.mpf('10.0'),4000)
z=w0
for i in range(1,1216):
    z=E(z)
    if 1195<=i<=1215:
        print(f"n={i} z=({mp.nstr(z.real,20)},{mp.nstr(z.imag,20)}) |z|={mp.nstr(abs(z),12)} want_next={s[i]}")
print("postsigular dist at 1214:", mp.nstr(min(abs(z),abs(z-lam)),12))
