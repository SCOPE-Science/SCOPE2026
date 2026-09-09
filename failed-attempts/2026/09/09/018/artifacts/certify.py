"""Certify record endpoints (deterministic Miller-Rabin bases 2,7,61 + BPSW)
and log smallest prime factor for every interior in-class integer.
Reads output/artifacts/records.json. Writes certs.json, spf_logs.json."""
import json, math

REC = json.load(open("output/artifacts/records.json"))

def mr_bases(n, bases):
    if n < 2: return False, []
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return (n == p), [{"small": p}]
    d, s = n-1, 0
    while d % 2 == 0: d//=2; s+=1
    log=[]
    for a in bases:
        if a % n == 0: continue
        x = pow(a, d, n)
        seq=[x]
        if x in (1, n-1):
            log.append({"a":a,"ok":True,"x0":x}); continue
        ok=False
        for _ in range(s-1):
            x = x*x % n; seq.append(x)
            if x == n-1: ok=True; break
        log.append({"a":a,"ok":ok or seq[-1]==n-1,"seq":seq})
        if not (ok or seq[-1]==n-1): return False, log
    return True, log

def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def lucas_spsp(n):
    # Strong Lucas-Selfridge test: D in 5,-7,9,-11,... with (D/n)=-1, P=1, Q=(1-D)/4
    if n == 2: return True
    if n % 2 == 0: return False
    for p in (3,5,7,11,13,17,19,23,29,31):
        if n % p == 0: return n == p
    D = 5
    while True:
        j = jacobi(D, n)
        if j == 0: return False
        if j == -1: break
        D = -(D+2) if D > 0 else -D+2
    P, Q = 1, (1-D)//4
    inv2 = (n+1)//2
    def add1(U, V, Qk):
        Un = ((P*U + V)*inv2) % n
        Vn = ((D*U + P*V)*inv2) % n
        return Un, Vn, (Qk*Q) % n
    def dbl(U, V, Qk):
        return (U*V) % n, (V*V - 2*Qk) % n, (Qk*Qk) % n
    delta = n + 1  # since (D/n) = -1
    d = delta
    s = 0
    while d % 2 == 0: d //= 2; s += 1
    U, V, Qk = 0, 2, 1  # U_0, V_0, Q^0
    for b in bin(d)[2:]:
        U, V, Qk = dbl(U, V, Qk)
        if b == '1':
            U, V, Qk = add1(U, V, Qk)
    # now (U,V) = (U_d, V_d)
    if U % n == 0: return True
    for _ in range(s):
        if V % n == 0: return True
        V = (V*V - 2*Qk) % n
        Qk = (Qk*Qk) % n
    return False

def bpsw(n):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    # MR base 2
    d,s = n-1,0
    while d%2==0: d//=2;s+=1
    x=pow(2,d,n)
    if x not in (1,n-1):
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return lucas_spsp(n)

def spf(n):
    if n % 2 == 0: return 2
    r=int(n**0.5)
    f=3
    while f<=r:
        if n%f==0: return f
        f+=2
    return n

certs={}; spf_logs={}
for cls,info in REC.items():
    q,r = map(int,cls.split("_"))
    certs[cls]=[]; spf_logs[cls]=[]
    for (g,a,b) in info["records"]:
        for p in (a,b):
            ok,log = mr_bases(p,[2,7,61])
            bl = bpsw(p)
            certs[cls].append({"p":p,"mr_ok":ok,"bpsw_ok":bl,"mr_log":log})
            assert ok and bl, (p,ok,bl)
        # interior in-class integers strictly between a and b congruent r mod q
        m = a+q if False else None
        start = a+((r-a)%q)
        if start<=a: start+=q
        run=[]
        t=start
        while t<b:
            f=spf(t)
            assert f<t, (t,)  # must be composite
            run.append([t,f])
            t+=q
        # run length must equal (b-a)/q - 1
        assert len(run)==(b-a)//q-1,(cls,a,b,len(run))
        spf_logs[cls].append({"gap":g,"a":a,"b":b,"run":run})

json.dump(certs,open("output/artifacts/certs.json","w"))
json.dump(spf_logs,open("output/artifacts/spf_logs.json","w"))
n_end=sum(len(v) for v in certs.values())
n_in=sum(len(e["run"]) for v in spf_logs.values() for e in v)
print(f"CERT_OK endpoints={n_end} interior_inclass_composites={n_in}")
