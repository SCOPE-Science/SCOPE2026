def f_int(x): return x**6 - 3*x**5 + x**4 + 3*x**2 - x + 1
def N_aff(q):
    # count affine Fp^q points by brute force over integers mod q (q=p or p^2 via GF(p^2) emulation)
    return None
def count_N1(p):
    sq=set((t*t)%p for t in range(p))
    n=0
    for x in range(p):
        v=f_int(x)%p
        n+=sum(1 for t in range(p) if (t*t)%p==v)
    return n
def count_N2(p):
    # GF(p^2) = Fp[t]/(t^2+1) if x^2+1 irred, else need another poly; pick irreducible dynamically
    # find a,b s.t. X^2+aX+b irreducible mod p
    def mul(u,v,a,b):
        # (u0+u1 w)(v0+v1 w), w^2 = -a w - b
        u0,u1=u; v0,v1=v
        c0=(u0*v0+(u1*v1*(-b)))%p
        c1=(u0*v1+u1*v0+u1*v1*(-a))%p
        return (c0,c1)
    def add(u,v): return ((u[0]+v[0])%p,(u[1]+v[1])%p)
    def sub(u,v): return ((u[0]-v[0])%p,(u[1]-v[1])%p)
    def pw(u,n,a,b):
        r=(1,0)
        while n:
            if n&1: r=mul(r,u,a,b)
            u=mul(u,u,a,b); n>>=1
        return r
    irr=None
    for a in range(p):
        for b in range(p):
            if all((t*t+a*t+b)%p!=0 for t in range(p)):
                irr=(a,b); break
        if irr: break
    a,b=irr
    q=p*p
    # squares: brute force q mults
    # count x in GF(q): q values; f(x) via mul/add; test quadratic residuosity via z^((q-1)/2)==1 and count sqrt
    # naive sqrt count: for each y, #sqrt = number of t with t^2=y -> instead precompute all squares multiset
    sqcount={}
    for t0 in range(p):
        for t1 in range(p):
            s=mul((t0,t1),(t0,t1),a,b)
            sqcount[s]=sqcount.get(s,0)+1
    N=0
    for x0 in range(p):
        for x1 in range(p):
            x=(x0,x1)
            # f(x)=x^6-3x^5+x^4+3x^2-x+1
            x2=mul(x,x,a,b); x3=mul(x2,x,a,b); x4=mul(x2,x2,a,b); x5=mul(x4,x,a,b); x6=mul(x3,x3,a,b)
            def sc(k,u): return ((k*u[0])%p,(k*u[1])%p)
            v=add(add(sub(add(x6,sc(-3,x5)),(0,0)),x4),sc(3,x2))
            v=sub(v,x); v=add(v,(1,0))
            N+=sqcount.get(v,0)
    return N, irr
for p in [13,17,31]:
    n1=count_N1(p)
    print(f"p={p} N1_aff={n1} N1_proj={n1+2}")
for p in [13,17]:
    n1=count_N1(p)
    n2,irr=count_N2(p)
    N1=n1+2; N2=n2+2  # both infinities rational, Frobenius fixes each
    s1=p+1-N1; s2=p*p+1-N2
    J=(1-s1+(s1*s1-s2)//2-p*s1+p*p)
    print(f"p={p} irr={irr} N2_aff={n2} N2_proj={N2} s1={s1} s2={s2} #J(Fp)={J} rem={(s1*s1-s2)%2}")
