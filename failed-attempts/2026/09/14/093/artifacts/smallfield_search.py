"""Small-field numerics: F_25 and F_49.
- Verify reduction embedding (cap holds for B subset F_p inside F_{p^2}).
- Check GP initial segments: sizes of A+A, AA, cap compliance, ratio R=max/|A|^1.25.
- Heuristic search (simulated annealing) for cap-compliant sets minimizing max(|A+A|,|AA|).
Goal: bounded recovery test — look for any small-field refutation pattern; none expected
(small arcs force large sums). Disproof would need ratio->0 asymptotically, untestable here.
"""
import random, math, itertools

def make_field(p, poly_c):
    # F_p[t]/(t^2 - c), c nonresidue. elt = a + b t <-> (a,b)
    q = p * p
    def add(x, y): return ((x[0]+y[0]) % p, (x[1]+y[1]) % p)
    def mul(x, y):
        return ((x[0]*y[0] + poly_c*x[1]*y[1]) % p, (x[0]*y[1] + x[1]*y[0]) % p)
    def eq(x, y): return x[0]==y[0] and x[1]==y[1]
    N = [(a,b) for a in range(p) for b in range(p)]
    NZ = [x for x in N if not (x[0]==0 and x[1]==0)]
    return p, q, add, mul, N, NZ

def sumset(A, add):
    S=set()
    for x in A:
        for y in A: S.add(add(x,y))
    return S

def prodset(A, mul):
    S=set()
    for x in A:
        for y in A: S.add(mul(x,y))
    return S

def cap_ok(A, p, q, add, mul, N, NZ):
    Aset=set(A); G=[(a,0) for a in range(p)]  # F_p subfield
    bound=math.sqrt(p)
    # all F_p-affine lines aG+b
    for a in NZ:
        aG=[mul(a,g) for g in G]
        for b in N:
            line=set(add(x,b) for x in aG)
            if len(Aset & line) > bound + 1e-9: return False, (a,b,len(Aset&line))
    return True, None

def ratio(A, add, mul):
    m=len(A); M=max(len(sumset(A,add)), len(prodset(A,mul)))
    return M/(m**1.25), len(sumset(A,add)), len(prodset(A,mul))

random.seed(0)
for (p,c) in [(5,2),(7,3)]:
    p,q,add,mul,N,NZ = make_field(p,c)
    print(f"===== F_{q} (p={p}) =====")
    # (a) embedding check: random B subset F_p^x, |B|=floor(sqrt p)
    m=min(int(math.sqrt(p)), p-1)
    B=[(a,0) for a in random.sample(range(1,p), m)]
    ok,info=cap_ok(B,p,q,add,mul,N,NZ)
    r,sp,pr=ratio(B,add,mul)
    print(f"embed B=F_p-subset size {m}: cap_ok={ok} {info}, |A+A|={sp},|AA|={pr}, R={r:.3f}")
    # full F_p^x (violates cap for p>3? |B|=p-1 > sqrt p) -- confirm excluded
    Bfull=[(a,0) for a in range(1,p)]
    ok2,info2=cap_ok(Bfull,p,q,add,mul,N,NZ)
    print(f"full F_p^x size {p-1}: cap_ok={ok2} (expect False for p>3) {info2}")
    # (b) GP initial segment: find primitive-ish g, N terms
    # find element of large order
    def order(g):
        x=(1,0); o=0
        for i in range(q):
            x=mul(x,g); o+=1
            if x==(1,0): return o
        return o
    g=max(NZ,key=order); print(f"g order={order(g)} (q-1={q-1})")
    for Nlen in [min(p,order(g)), min(2*p-1,order(g))]:
        A=[]; x=(1,0)
        for i in range(Nlen): A.append(x); x=mul(x,g)
        ok3,info3=cap_ok(A,p,q,add,mul,N,NZ)
        r3,sp3,pr3=ratio(A,add,mul)
        print(f"GP len {Nlen}: cap_ok={ok3} {info3}, |A+A|={sp3},|AA|={pr3}, R={r3:.3f}")
    # (c) annealing: minimize max(|A+A|,|AA|) s.t. cap, fixed size m
    for m in ([4,6] if p==5 else [5,8]):
        A=random.sample(NZ,m)
        def energy(A):
            Aset=set(A)
            ok,_=cap_ok(Aset,p,q,add,mul,N,NZ)
            M=max(len(sumset(Aset,add)),len(prodset(Aset,mul)))
            return M + (0 if ok else 10*q), ok, M
        best=list(A); be,okb,Mb=energy(best)
        cur=list(A); ce=be
        for it in range(4000):
            i=random.randrange(m); cand=list(cur)
            cand[i]=random.choice(NZ)
            if len(set(cand))<m: continue
            e,ok,M=energy(cand)
            T=2.0*(1-it/4000)+0.01
            if e<ce or random.random()<math.exp(-(e-ce)/T):
                cur=cand; ce=e
                if e<be: best=list(cand); be,okb,Mb=e,ok,M
        rB=Mb/(m**1.25)
        print(f"anneal m={m}: best M={Mb} cap_ok={okb} R={rB:.3f} set={sorted(best)}")
print("done.")
