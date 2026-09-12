"""Phase 1: S3-smooth enumeration (consistency) + bounded extremal-witness search (falsification).
S3 = {2,3,7,11,50069}. x+y=1, x,y S3-units. ord_p(x(1-x)) with p=50069.
Since x+(1-x)=1: per-prime valuations are (v,0),(0,v),(-v,-v),(0,0).
Cap<=3  <=>  no solution with v>=4 in a (v,0)/(0,v) configuration.
Case (v,0): x = e*p^v*m/n, y = s/n with m,n {2,3,7,11}-smooth, s=(n-e*p^v*m) S3-smooth.
So search: S'-smooth n (S'={2,3,7,11}), small S'-smooth m, s=n-e*p^v*m trial-divided.
"""
import math, time
t0=time.time()
P = 50069
SP = [2,3,7,11]

def gen_smooth(primes, limit):
    out=[]
    def rec(i, cur):
        if i==len(primes):
            out.append(cur); return
        p=primes[i]; v=cur
        while v<=limit:
            rec(i+1, v)
            if v>limit//p: break
            v*=p
    rec(0,1)
    out.sort()
    return out

def is_smooth(n, primes):
    if n<=0: return False
    for p in primes:
        while n%p==0: n//=p
    return n==1

def ord_p(n, p):
    if n==0: return None
    c=0
    while n%p==0: n//=p; c+=1
    return c

# ---- A. integer solutions: c, c-1 both S3-smooth (x=c,y=1-c), c <= H ----
H=10**12
S3=[2,3,7,11,50069]
sm=gen_smooth(S3,H)
print(f"#S3-smooth <={H}: {len(sm)}  ({time.time()-t0:.1f}s)")
sols=[]
mx=0
sset=set(sm)
for c in sm:
    if c>=2 and (c-1) in sset:
        for x,y in ((c,1-c),(1-c,c)):
            o=ord_p(abs(x*(1-x)),P)
            mx=max(mx,o)
            sols.append((x,o))
print(f"integer solutions x+y=1 (x,y S3-units), x=c<=H: {len(sols)}, max ord_p={mx}")
print("examples:", sols[:12])

# ---- C. extremal witness search v in {4,5}: n S'-smooth <= Nmax, m S'-smooth <= Mmax ----
for Nmax,Mmax,vs in ((10**22,50,(4,)),):
    t1=time.time()
    nlist=gen_smooth(SP,Nmax)
    mlist=[m for m in gen_smooth(SP,Mmax) ]
    print(f"witness search: Nmax={Nmax:.0e} #n={len(nlist)} Mmax={Mmax} #m={len(mlist)} vs={vs}", flush=True)
    hits=0
    checked=0
    pows={v:P**v for v in vs}
    for n in nlist:
        if n<2: continue
        for v in vs:
            pv=pows[v]
            for m in mlist:
                for e in (1,-1):
                    s=n-e*pv*m
                    if s==0: continue
                    checked+=1
                    if is_smooth(abs(s),S3):
                        print(f"  WITNESS v={v} e={e} m={m} n={n} s={s}", flush=True)
                        hits+=1
                        if hits>5: break
                if hits>5: break
            if hits>5: break
        if hits>5: break
    print(f"  checked={checked} hits={hits} ({time.time()-t1:.1f}s)")
print(f"TOTAL {time.time()-t0:.1f}s")
