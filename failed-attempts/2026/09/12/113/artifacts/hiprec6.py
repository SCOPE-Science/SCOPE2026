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
for N in [400, 1000, 2000, 4000]:
    w0=tip(s,mp.mpf('10.0'),N)
    z=w0; bad=None
    for i in range(1,3001):
        z=E(z)
        k=int(mp.nint(z.imag/(2*mp.pi)))
        if abs(k)>2 or k!=s[i]:
            bad=(i,k,s[i],z); break
    print(f"N={N}: first bad={bad[0] if bad else None} got={bad[1] if bad else None} want={bad[2] if bad else None}")
