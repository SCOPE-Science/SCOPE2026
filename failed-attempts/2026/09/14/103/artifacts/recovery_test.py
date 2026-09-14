"""Bounded recovery test: exhaustive neighbor search + gap/height certificates."""
import numpy as np

def lam_sorted(n):
    return np.array(sorted(np.roots([1,-(n-1),-(n+2),-1]).real))

def eta_all(n):
    L = lam_sorted(n); lam0 = max(L)
    def sig(t): return -1-1/t
    lam = [lam0, sig(lam0)]; lam.append(sig(lam[1]))
    assert abs(sig(lam[2])-lam[0]) < 1e-6
    return np.array([lam[i]*(lam[(i+1)%3]**2) for i in range(3)])

def e12(n,s):
    A = n*n+n+4
    S={0:3,1:3,2:9+2*A}; T={0:3,1:-A,2:A*A-6}
    for j in range(3,s+1):
        S[j]=3*S[j-1]+A*S[j-2]+S[j-3]
        T[j]=-A*T[j-1]-3*T[j-2]+T[j-3]
    return S[s],T[s]

def Gval(n,s,x,y):
    e1,e2=e12(n,s); return x**3-e1*x**2*y+e2*x*y**2-y**3

# Test 1: exhaustive smart search n<=30, s=1..3, |y| in [2,2000]
sols=[]
for n in range(3,31):
    for s in [1,2,3]:
        th=eta_all(n)**s
        e1,e2=e12(n,s)
        for y in list(range(2,2001))+list(range(-2000,-1)):
            for t in th:
                xc=int(round(t*y))
                for x in (xc-2,xc-1,xc,xc+1,xc+2):
                    if x**3-e1*x**2*y+e2*x*y**2-y**3 in (1,-1):
                        sols.append((n,s,x,y)); print(f"SOL n={n} s={s} x={x} y={y}", flush=True)
print("TEST1 count:",len(sols))

# Test 2: gap certificate n=3..200, s=1: min root gap / n
import math
for n in [3,5,10,50,200]:
    th=sorted(eta_all(n))
    gaps=[th[i+1]-th[i] for i in range(2)]
    print(f"n={n} gaps={gaps} mingap/n={min(gaps)/n:.4f}")
# Test 3: height growth in s: log|e1|,log|e2| for n=5
for s in [1,2,3,4,5,6]:
    e1,e2=e12(5,s);print(f"s={s} log|e1|={math.log(abs(e1)):.3f} log|e2|={math.log(abs(e2)):.3f}")
# Test 4: discriminant identity
for n in [3,4,5,10,100]:
    D=n**4+2*n**3+15*n**2+14*n+49
    print(n, D==(n*n+n+7)**2)
