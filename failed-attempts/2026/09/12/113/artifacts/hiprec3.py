from mpmath import mp, mpc, log
mp.dps = 80
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
z=w0
for i in range(320,330):
    z=E(z) if i==320 else z  # placeholder
# redo cleanly: iterate and print window 320..330 with high precision imag/2pi and distance to half-integer boundary
z=w0
for i in range(1,331):
    z=E(z)
    if 318<=i<=330:
        r=z.imag/(2*mp.pi)
        print(f"n={i} Im/2pi={mp.nstr(r,30)} nearest={int(mp.nint(r))} dist_to_half={mp.nstr(abs(r-(mp.floor(r)+mp.mpf('0.5'))),6)} |z|={mp.nstr(abs(z),8)}")
