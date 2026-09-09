"""Independent replay: rebuild gaps/records from filtered lists only,
re-prove primality by trial division to sqrt (complete for n<=5e6),
check spf-log minimality, maximality by exhaustive scan,
recompute Kourbatov trend residuals. Prints VERIFY_OK on success."""
import json, math

X = 5000000
REC = json.load(open("output/artifacts/records.json"))
CERTS = json.load(open("output/artifacts/certs.json"))
SPF = json.load(open("output/artifacts/spf_logs.json"))

# small primes up to sqrt(5e6) via sieve
N = int(X**0.5)+1
bs = bytearray(b'\x01')*(N+1); bs[0]=bs[1]=0
for i in range(2,int(N**0.5)+1):
    if bs[i]: bs[i*i:N+1:i]=b'\x00'*(((N-i*i)//i)+1)
SMALL=[i for i in range(2,N+1) if bs[i]]

def is_prime_td(n):
    if n<2: return False
    for p in SMALL:
        if p*p>n: break
        if n%p==0: return n==p
    return True

def spf_td(n):
    for p in SMALL:
        if p*p>n: break
        if n%p==0: return p
    return n

def mr(n,bases):
    if n<2: return False
    for p in SMALL:
        if p*p>n: break
        if n%p==0: return n==p
    d,s=n-1,0
    while d%2==0: d//=2;s+=1
    for a in bases:
        if a % n == 0: continue
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True

def li(x):
    # Simpson with step 1000 on [2,x]
    a,h=2.0,1000.0
    n=int((x-a)/h)
    def f(t): return 1.0/math.log(t)
    s=f(a)+f(a+n*h)
    for i in range(1,n):
        s+= (4.0 if i%2 else 2.0)*f(a+i*h)
    rem=x-(a+n*h)
    s=s*h/3.0
    if rem>1e-12:
        b0=a+n*h
        m=(b0+x)/2
        s+=(x-b0)/6.0*(f(b0)+4*f(m)+f(x))
    return s

def trend(q,x,b=0.0):
    phi=2  # phi(4)=phi(6)=2
    L=li(x)
    return phi*x/L*(2*math.log(L/phi)-math.log(x)+b)

allok=True
trend_tab={}
for cls in ["4_1","4_3","6_1","6_5"]:
    q,r=map(int,cls.split("_"))
    flt=list(map(int,open(f"output/artifacts/filtered_{cls}.txt").read().split()))
    assert flt==sorted(flt) and len(flt)==REC[cls]["count"], cls
    assert all(p<=X and p%q==r for p in flt), cls
    # full trial-division primality of every filtered entry would be ~350k*330 divs ~ 1e8 ops; spot check endpoints fully + audit all via MR base set
    for p in flt:
        assert mr(p,[2,3,5,7,11]), (cls,p)
    gaps=[b-a for a,b in zip(flt,flt[1:])]
    best=0; recs=[]
    for a,b,g in zip(flt,flt[1:],gaps):
        if g>best: best=g; recs.append([g,a,b])
    assert recs==REC[cls]["records"], (cls,recs[-3:],REC[cls]["records"][-3:])
    # maximality: best equals last record gap; exhaustive (all gaps scanned above)
    assert best==recs[-1][0]
    assert all(g<=best for g in gaps)
    # certificates: independent trial-division proof of each endpoint
    seen=[c["p"] for c in CERTS[cls]]
    want=[p for rec in recs for p in rec[1:]]
    assert seen==want, cls
    for c in CERTS[cls]:
        assert c["mr_ok"] and c["bpsw_ok"]
        assert is_prime_td(c["p"]), c["p"]
        assert mr(c["p"],[2,3,5,7,11])
    # spf logs
    assert len(SPF[cls])==len(recs)
    for e,rec in zip(SPF[cls],recs):
        g,a,b=e["gap"],e["a"],e["b"]
        assert [g,a,b]==rec
        assert (b-a)//q-1==len(e["run"])
        t=a+((r-a)%q)
        if t<=a: t+=q
        for (tt,f) in e["run"]:
            assert tt==t,(cls,tt,t); assert tt%q==r
            assert f==spf_td(tt) and tt%f==0 and f<tt,(cls,tt,f)
            assert is_prime_td(f)
            t+=q
        assert t==b
    # trend residuals at each record upper endpoint
    rows=[]
    for (g,a,b) in recs:
        T=trend(q,b)
        Cb=2*math.log(b)**2
        rows.append({"gap":g,"a":a,"b":b,"T0":T,"resid":g-T,"ratio":g/T,"cramer":Cb,"G/C":g/Cb})
        assert g<Cb,(cls,g,Cb)  # Kourbatov empirical bound G<phi log^2 x holds
    trend_tab[cls]=rows
    print(f"{cls}: n={len(flt)} recs={len(recs)} max={recs[-1]} T0_end={rows[-1]['T0']:.2f} resid={rows[-1]['resid']:.2f} G/C={rows[-1]['G/C']:.3f} OK")

json.dump(trend_tab,open("output/artifacts/trend_residuals.json","w"),indent=1)
print("VERIFY_OK")
