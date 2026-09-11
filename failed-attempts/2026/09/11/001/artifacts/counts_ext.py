"""Point counts #X(F_q) via G-trick: F=G(x,y)-G(z,w), G=a^4+b^4+a^2b^2.
#aff = sum_v N_v^2, N_v=#{pairs with G=v}; #proj=(#aff-1)/(q-1).
Works for prime powers q=p^2 with GF(p^2)=Fp[t]/(t^2+c)."""
def add_rep(a,b,p): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def mul_rep(a,b,p,c): return ((a[0]*b[0]-c*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def pow_rep(a,e,p,c):
    r=(1%p,0)
    for _ in range(e):
        r=mul_rep(r,a,p,c)
    return r

def find_irred_c(p):
    sq=set((i*i)%p for i in range(p))
    for c in range(1,p):
        # t^2+c irred <=> -c nonsquare
        if ((-c)%p) not in sq:
            return c
    raise Exception("none")

def count_q(p,c=None,deg=2):
    if deg==1:
        q=p
        elems=list(range(p))
        def G(a,b): return (pow(a,4,p)+pow(b,4,p)+pow(a,2,p)*pow(b,2,p))%p if p>1 else 0
        from collections import Counter
        # need pow with mod
        hist=Counter()
        for a in elems:
            for b in elems:
                hist[(pow(a,4,p)+pow(b,4,p)+(pow(a,2,p)*pow(b,2,p))%p)%p]+=1
        N=sum(v*v for v in hist.values())
        return q,N,(N-1)//(q-1)
    else:
        assert deg==2
        if c is None: c=find_irred_c(p)
        q=p*p
        elems=[(i,j) for i in range(p) for j in range(p)]
        def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
        def mul(a,b): return ((a[0]*b[0]-c*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
        def pw(a,e):
            r=(1,0)
            for _ in range(e): r=mul(r,a)
            return r
        def G(a,b):
            a4=pw(a,4); b4=pw(b,4); a2=pw(a,2); b2=pw(b,2)
            return add(add(a4,b4),mul(a2,b2))
        from collections import Counter
        hist=Counter()
        for a in elems:
            for b in elems:
                hist[G(a,b)]+=1
        N=sum(v*v for v in hist.values())
        return q,N,(N-1)//(q-1),c

for p in [5,7]:
    q,N,nproj,c=count_q(p,deg=2)
    t=nproj-1-q*q
    print(f"p={p} c={c} q={q} #aff={N} #proj={nproj} trace={t}")
# prime check cross-validate
for p in [5,7,11]:
    q,N,nproj=count_q(p,deg=1)
    print(f"prime p={p} #proj={nproj} trace={nproj-1-p*p}")
print("COUNTS_EXT_OK")
