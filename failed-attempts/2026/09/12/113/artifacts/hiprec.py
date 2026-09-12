from mpmath import mp, mpc, log, matrix
mp.dps = 60
lam = mp.mpc(0, 2*mp.pi)
def tm_digit(i): return bin(i-1).count('1') & 1
M=3000
s=[tm_digit(i) for i in range(1,M+6)]
def tip(s,T,N):
    w = mp.mpc(T, 2*mp.pi*s[N])
    for k in range(N,0,-1):
        w = log(w/lam) + 2*mp.pi*mpc(0,1)*s[k-1]
    return w
for N in [100,200,400]:
    for T in ['10.0','25.0']:
        w=tip(s,mp.mpf(T),N)
        print(f"N={N} T={T}: Re={mp.nstr(w.real,25)} Im={mp.nstr(w.imag,25)}")
w1=tip(s,mp.mpf('10.0'),400); w2=tip(s,mp.mpf('25.0'),400)
print("T-independence |diff| =", mp.nstr(abs(w1-w2),5))
w3=tip(s,mp.mpf('10.0'),100)
print("N=100 vs 400 |diff| =", mp.nstr(abs(w3-w1),5))
# functional equation: E(w0) should equal landing of shifted ray; check itinerary digits to 30
w0=w1
z=w0
E=lambda z: lam*mp.e**z
digits=[]
for i in range(30):
    z=E(z)
    k=int(mp.nint(z.imag/(2*mp.pi)))
    digits.append(k)
print("fwd itinerary:",digits)
print("sigma-TM     :",s[1:31])
print("match:",digits==s[1:31])
