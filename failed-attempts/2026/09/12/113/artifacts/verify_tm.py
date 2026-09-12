import cmath, math
lam = 2j*math.pi
E = lambda z: lam*cmath.exp(z)
print("E(0) =", E(0), " == 2pi i:", E(0)==lam)
print("E(2pi i) =", E(lam), " diff:", abs(E(lam)-lam))
print("mult =", lam, " |mult| =", abs(lam), " repelling:", abs(lam)>1)

# Thue-Morse: c_n = parity of popcount(n-1), n>=1
def tm(n):  # length-n prefix, 1-indexed c_1..c_n
    return [bin(k).count('1')%2 for k in range(n)]
t = tm(2000)
print("prefix64:", ''.join(map(str,t[:64])))
# bounded
print("alphabet:", sorted(set(t)))
# cube-free check on prefix: no www with |w|>=1 up to some size
def cube_free(seq, wmax):
    n=len(seq)
    for w in range(1,wmax+1):
        for i in range(n-3*w+1):
            if seq[i:i+w]==seq[i+w:i+2*w]==seq[i+2*w:i+3*w]:
                return False,(i,w)
    return True,None
print("cube-free (w<=40, n=2000):", cube_free(t,40))
# eventual periodicity test: for preperiod p0<=20, period q<=40, check consistency on long window
def eventual(seq,p0,q):
    for i in range(p0,len(seq)-q):
        if seq[i]!=seq[i+q]: return False
    return True
hits=[(p0,q) for p0 in range(0,21) for q in range(1,41) if eventual(t[p0:],0,q)]
print("eventual-period hits (should be []):", hits[:10])
# uniform recurrence spot check: every factor of length 8 in first 200 reappears with bounded gap in 2000
from collections import defaultdict
facs=set(tuple(t[i:i+8]) for i in range(200))
gaps=[]
s=''.join(map(str,t))
ok=True
for f in facs:
    fs=''.join(map(str,f))
    idx=s.find(fs); gap=0; mx=0
    while idx!=-1 and idx<1900:
        nxt=s.find(fs,idx+1)
        if nxt==-1: break
        mx=max(mx,nxt-idx); idx=nxt
    gaps.append(mx)
print("max recurrence gap over len-8 factors:", max(gaps))
