from mpmath import mp, mpc, log
for dps in [80, 150, 300]:
    mp.dps = dps
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
    for N in [400, 2000]:
        w0=tip(s,mp.mpf('10.0'),N)
        z=w0
        for i in range(1,332):
            z=E(z)
        print(f"dps={dps} N={N}: n=329 |z|={mp.nstr(abs(z),10)} Im/2pi={mp.nstr(z.imag/(2*mp.pi),20)}")
