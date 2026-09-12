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
# itinerary to length 2000
w0=tip(s,mp.mpf('10.0'),400)
z=w0; dig=[]
OK=True
for i in range(2000):
    z=E(z)
    k=int(mp.nint(z.imag/(2*mp.pi)))
    dig.append(k)
    if k!=s[i+1]:
        print("MISMATCH at",i,"got",k,"want",s[i+1]); OK=False; break
print("itinerary 2000 match:",OK)
# multiplier along orbit: product of E(z_n), and |.| growth; also distance from postsingular set
prods=[]; p=mp.mpc(1)
z=w0
mn=mp.mpf('1e300')
for i in range(200):
    z=E(z)
    p*=z  # E'(z)=E(z)
    d1=abs(z); d2=abs(z-lam)
    mn=min(mn,d1,d2)
    if (i+1)%40==0: print(f"n={i+1} |prod|={mp.nstr(abs(p),6)} log|prod|/n={mp.nstr(log(abs(p))/(i+1),6)} minDistPS={mp.nstr(mn,4)}")
print("final minDistPS over 200:", mp.nstr(mn,6))
