#!/usr/bin/env python3
"""
Weight-32 level-one Galois-orbit certificate (stdlib only, no Sage).
Computes exact Hecke polynomials for T2,T3,T5 on S_32, discriminant +
mod-29 irreducibility witness, normalized eigenforms to O(q^50) in
Q(sqrt(18295489)), and independent Eichler-Selberg trace cross-check.
All arithmetic exact over ZZ/QQ (Fractions + big ints). No floating point.
Run: python3 s32_certificate.py  (writes sibling .txt files, completes in seconds)
"""
from fractions import Fraction
import math, time, os

K = 32
DSF = 18295489  # squarefree kernel, 67*273067
# Quadratic field Q(sqrt(DSF)) elements as pairs (p,q) = p+q*sqrt(DSF) with Fractions
def f_add(a,b): return (a[0]+b[0], a[1]+b[1])
def f_sub(a,b): return (a[0]-b[0], a[1]-b[1])
def f_mul(a,b):
    # (p1+q1 s)(p2+q2 s) = (p1p2+q1q2 d) + (p1q2+p2q1)s
    return (a[0]*b[0]+a[1]*b[1]*DSF, a[0]*b[1]+a[1]*b[0])
def f_conj(a): return (a[0], -a[1])
def f_norm(a): return a[0]*a[0]-a[1]*a[1]*DSF
def f_inv(a):
    n = f_norm(a)
    assert n != 0, "zero divisor in quadratic field"
    return (a[0]/n, -a[1]/n)
def f_div(a,b): return f_mul(a, f_inv(b))
def f_int(p,q=0): return (Fraction(p), Fraction(q))
def f_eq(a,b): return a[0]==b[0] and a[1]==b[1]
def f_str(a): return f"{a[0]} + ({a[1]})*sqrt({DSF})"

t_start = time.time()
outdir = os.path.dirname(os.path.abspath(__file__))

# ---------- 0. Dimension ----------
# M_32 = C[E4,E6]_{32}: monomials E4^a E6^b, 4a+6b=32 -> (8,0),(5,2),(2,4): 3 monomials.
sols = sorted([(a,b) for a in range(9) for b in range(6) if 4*a+6*b==32], reverse=True)
assert sols==[(8,0),(5,2),(2,4)], sols
print(f"[dim] monomial solutions {sols} => dim M_32 <=3")

# ---------- 1. Eisenstein q-expansions ----------
PREC = 70  # need indices 0..69; O(q^50) output uses 0..50
def sigma(e,n):
    s=0; d=1
    while d*d<=n:
        if n%d==0:
            s+=pow(d,e); d2=n//d
            if d2!=d: s+=pow(d2,e)
        d+=1
    return s
def smul(a,b,prec):
    c=[0]*prec
    for i in range(prec):
        ai=a[i]
        if ai==0: continue
        lim=prec-i
        for j in range(lim):
            bj=b[j]
            if bj: c[i+j]+=ai*bj
    return c
def spow(a,e,prec):
    r=[0]*prec; r[0]=1; base=a[:]
    while e>0:
        if e&1: r=smul(r,base,prec)
        base=smul(base,base,prec); e>>=1
    return r
e4=[0]*PREC; e6=[0]*PREC; e4[0]=1; e6[0]=1
for n in range(1,PREC):
    e4[n]=240*sigma(3,n); e6[n]=-504*sigma(5,n)
m1=spow(e4,8,PREC)
m2=smul(spow(e4,5,PREC),spow(e6,2,PREC),PREC)
m3=smul(spow(e4,2,PREC),spow(e6,4,PREC),PREC)
# independence: det of coeffs at 0,1,2 nonzero
# matrix rows n=0,1,2 cols m1,m2,m3
import copy
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
Dmat=det3([[m1[0],m2[0],m3[0]],[m1[1],m2[1],m3[1]],[m1[2],m2[2],m3[2]]])
print(f"[dim] det(monomials at 0,1,2) = {Dmat}")
assert Dmat==-5159780352 and Dmat!=0
print("[dim] => m1,m2,m3 linearly independent => dim M_32 =3 (structure theorem C[E4,E6] + independence).")
print("[dim] S_32 = ker(a0) has dim 2 (each mi has a0=1, condition c1+c2+c3=0).")
b0=[m1[i]-m2[i] for i in range(PREC)]
b1=[m2[i]-m3[i] for i in range(PREC)]
assert b0[0]==0 and b1[0]==0
assert b0[1]==1728 and b1[1]==1728
# check b0,b1 independent (det at 1,2)
detB=b0[1]*b1[2]-b1[1]*b0[2]
print(f"[dim] det cusp basis at 1,2 = {detB}")
assert detB==-5159780352 and detB!=0

# ---------- 2. Hecke matrices ----------
def divisors(n):
    ds=[]; d=1
    while d*d<=n:
        if n%d==0:
            ds.append(d)
            if d*d!=n: ds.append(n//d)
        d+=1
    return sorted(ds)
def hecke_series(f,n,k,prec_out):
    g=[0]*prec_out
    pd={d:pow(d,k-1) for d in divisors(n)}
    g[0]=sum(pd[d] for d in divisors(n))*f[0]
    for m in range(1,prec_out):
        gg=math.gcd(n,m)
        tot=0
        for d in divisors(gg):
            idx=(m*n)//(d*d)
            tot+=pd[d]*f[idx]
        g[m]=tot
    return g
def hecke_matrix(n):
    T0=hecke_series(b0,n,K,12); T1=hecke_series(b1,n,K,12)
    B11,B12,B21,B22=Fraction(b0[1]),Fraction(b1[1]),Fraction(b0[2]),Fraction(b1[2])
    T11,T12,T21,T22=Fraction(T0[1]),Fraction(T1[1]),Fraction(T0[2]),Fraction(T1[2])
    detBf=B11*B22-B12*B21
    assert detBf!=0
    inv00,inv01,inv10,inv11=B22/detBf,-B12/detBf,-B21/detBf,B11/detBf
    M00=inv00*T11+inv01*T21; M01=inv00*T12+inv01*T22
    M10=inv10*T11+inv11*T21; M11=inv10*T12+inv11*T22
    M=[[M00,M01],[M10,M11]]
    for m in range(12):
        assert Fraction(T0[m])==M00*b0[m]+M10*b1[m], f"verify T{n}b0@{m}"
        assert Fraction(T1[m])==M01*b0[m]+M11*b1[m], f"verify T{n}b1@{m}"
    assert M00.denominator==1 and M01.denominator==1 and M10.denominator==1 and M11.denominator==1
    return [[int(M00),int(M01)],[int(M10),int(M11)]], T0, T1

M2,_,_=hecke_matrix(2)
M3,_,_=hecke_matrix(3)
M5,_,_=hecke_matrix(5)
print(f"[hecke] M2={M2}")
print(f"[hecke] M3={M3}")
print(f"[hecke] M5={M5}")
def tr_det(M):
    tr=M[0][0]+M[1][1]; det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return tr,det,tr*tr-4*det
tr2,det2,D2=tr_det(M2); tr3,det3v,D3=tr_det(M3); tr5,det5,D5=tr_det(M5)
print(f"[hecke] T2 Tr={tr2} det={det2} D={D2}")
print(f"[hecke] T3 Tr={tr3} det={det3v} D={D3}")
print(f"[hecke] T5 Tr={tr5} det={det5} D={D5}")
assert (tr2,det2)==(39960,-2235350016)
assert (tr3,det3v)==(17363160,-416300505539184)
assert (tr5,det5)==(-19391218020,-5207533830370075837500)
# commutativity
def mmul(A,B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]],[A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
assert mmul(M2,M3)==mmul(M3,M2) and mmul(M2,M5)==mmul(M5,M2) and mmul(M3,M5)==mmul(M5,M3)
print("[hecke] pairwise commutativity OK (simultaneously diagonalizable).")

# ---------- 3. Discriminant / irreducibility / field ----------
r2=math.isqrt(D2)
assert r2*r2<D2<(r2+1)*(r2+1), "D2 non-square by bracketing"
print(f"[disc] D2={D2} bracketed: {r2}^2={r2*r2} < D2 < {(r2+1)*(r2+1)}={(r2+1)*(r2+1)} => non-square, non-zero => T2 charpoly irreducible quadratic.")
# factor squarefree kernel by trial division (exact)
def primes_upto(N):
    sieve=[True]*(N+1); sieve[0]=sieve[1]=False
    for i in range(2,int(N**0.5)+1):
        if sieve[i]:
            for j in range(i*i,N+1,i): sieve[j]=False
    return [i for i,ok in enumerate(sieve) if ok]
primes=primes_upto(5000)
def factor_trial(n):
    f={}; tmp=n
    for p in primes:
        if p*p>tmp: break
        c=0
        while tmp%p==0:
            tmp//=p; c+=1
        if c: f[p]=c
    if tmp>1: f[tmp]=1  # tmp prime (no divisor <=5000 and >5000? need proof: if composite, factor <=sqrt; sqrt(18295489)<4278<5000, so tmp prime)
    return f
fac_DSF=factor_trial(DSF)
print(f"[field] DSF={DSF} = {fac_DSF}")
assert fac_DSF=={67:1,273067:1}, fac_DSF
# prove 273067 prime: trial divided by all primes <=522 (isqrt), none divide (done inside factor_trial since primes up to 5000 cover)
assert math.isqrt(273067)==522
# squarefree: exponents all 1
assert all(e==1 for e in fac_DSF.values())
# D ratios are squares
assert D3//D2==432*432 and D3%D2==0
q5=D5//D2; r5=math.isqrt(q5)
assert D5%D2==0 and r5*r5==q5 and r5==1418560
print(f"[field] D3/D2=432^2, D5/D2=1418560^2 => same squarefree kernel => same quadratic field Q(sqrt({DSF})).")
print(f"[field] DSF mod4 = {DSF%4} => field discriminant = {DSF} (since 1 mod4, squarefree).")
# mod-p witness: T2 poly mod29 has no root
p=29
Trm=tr2%p; detm=det2%p
roots=[x for x in range(p) if (x*x-Trm*x+detm)%p==0]
print(f"[witness] T2 charpoly mod{p} roots: {roots}")
assert roots==[]
# Legendre check: D2 non-residue mod29
assert pow(D2,(p-1)//2,p)==p-1
print(f"[witness] D2^((p-1)/2) = {p-1} mod{p} => quadratic non-residue => irreducible mod{p}.")
# also record Legendre table for p<29 for context
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
tab=[(q, (D2%q==0 and "ramified" or leg(D2,q))) for q in primes if q<29 and q>=3]
print(f"[witness] Legendre table p<29: {tab}")

# ---------- 4. Eigenforms O(q^50) ----------
# eigenvalues of T2: lam = 19980 +/- 12 sqrt(DSF)
lam_minus=(Fraction(19980),Fraction(-12))
lam_plus=(Fraction(19980),Fraction(12))
# eigenvectors of M2: v=(b, lam-a), a=M2[0][0], b=M2[0][1]
a00=M2[0][0]; b01=M2[0][1]
def vec_for(lam):
    return [(Fraction(b01),Fraction(0)), (lam[0]-a00, lam[1])]
v_minus=vec_for(lam_minus); v_plus=vec_for(lam_plus)
# check M3,M5 share eigenvectors, extract eigenvalues
def mat_vec(M,v):
    # v=[(p0,q0),(p1,q1)]
    r0=f_add(f_mul(f_int(M[0][0]),v[0]), f_mul(f_int(M[0][1]),v[1]))
    r1=f_add(f_mul(f_int(M[1][0]),v[0]), f_mul(f_int(M[1][1]),v[1]))
    return [r0,r1]
def eigenval(M,v):
    w=mat_vec(M,v)
    # mu = w0/v0 (v0 nonzero: b01=1280664)
    mu=f_div(w[0],v[0])
    # check parallel: w1 == mu*v1
    assert f_eq(w[1], f_mul(mu,v[1])), f"not eigenvector {M}"
    return mu
mu3_minus=eigenval(M3,v_minus); mu3_plus=eigenval(M3,v_plus)
mu5_minus=eigenval(M5,v_minus); mu5_plus=eigenval(M5,v_plus)
print(f"[eigen] mu3- = {f_str(mu3_minus)}, mu3+ = {f_str(mu3_plus)}")
print(f"[eigen] mu5- = {f_str(mu5_minus)}, mu5+ = {f_str(mu5_plus)}")
assert mu3_minus==(Fraction(8681580),Fraction(-5184)) and mu3_plus==(Fraction(8681580),Fraction(5184))
assert mu5_minus==(Fraction(-9695609010),Fraction(17022720)) and mu5_plus==(Fraction(-9695609010),Fraction(-17022720))
# verify charpoly roots: Tr=mu+conj, det=mu*conj
for mu,tr,det in [(mu3_minus,tr3,det3v),(mu5_minus,tr5,det5)]:
    assert mu[0]*2==tr and (mu[0]*mu[0]-mu[1]*mu[1]*DSF)==det
print("[eigen] M3/M5 eigenvalues lie in same field, traces/dets match charpolys.")
# normalize: alpha+beta=1/1728 (since a1=1728 each)
def normalize(v):
    s=f_add(v[0],v[1])
    t=f_div((Fraction(1,1728),Fraction(0)), s)
    return [f_mul(t,v[0]), f_mul(t,v[1])]
ab_minus=normalize(v_minus); ab_plus=normalize(v_plus)
print(f"[eigen] alpha-={f_str(ab_minus[0])} beta-={f_str(ab_minus[1])}")
# build q-exps 0..50
NOUT=51
def build_qexp(ab):
    al,be=ab
    qs=[]
    for m in range(NOUT):
        # al*b0[m]+be*b1[m]
        t0=(al[0]*b0[m], al[1]*b0[m])
        # careful: al=(p,q), b integer: al*b = (p*b, q*b)
        # above: al[0]*b0[m] is Fraction*int=Fraction ok
        t1=(be[0]*b1[m], be[1]*b1[m])
        qs.append((t0[0]+t1[0], t0[1]+t1[1]))
    return qs
q_minus=build_qexp(ab_minus); q_plus=build_qexp(ab_plus)
# checks: a0=0,a1=1, a2=lam, integrality (denominators 1)
for qs,lam,name in [(q_minus,lam_minus,"minus"),(q_plus,lam_plus,"plus")]:
    assert qs[0]==(Fraction(0),Fraction(0)) and qs[1]==(Fraction(1),Fraction(0)), name
    assert f_eq(qs[2],lam), name
    for m,c in enumerate(qs):
        assert c[0].denominator==1 and c[1].denominator==1, f"non-integral {name}@{m}: {c}"
print("[qexp] normalized (a0=0,a1=1), a2 matches eigenvalue, all coeffs in Z[sqrt(DSF)] to O(q^50).")
# Galois conjugacy: plus = conj(minus)
for m in range(NOUT):
    assert q_plus[m]==f_conj(q_minus[m])
print("[qexp] two eigenforms Galois-conjugate => single orbit degree 2.")
# Hecke relations spot-check: a_{mn} etc.? At least check trace sums and multiplicativity for small primes:
# trace form t_n = a_n^- + a_n^+ = 2A_n
traces=[int(q_minus[n][0]*2) for n in range(NOUT)]
assert traces[2]==tr2 and traces[3]==tr3 and traces[5]==tr5
print(f"[qexp] trace form head: {traces[:13]}")
# verify a4 = a2^2 - 2^{31} (Hecke relation for prime square, level1, k=32: a_{p^2}=a_p^2-p^{k-1})
for qs in [q_minus,q_plus]:
    for pr in [2,3,5]:
        ap=qs[pr]; ap2=f_mul(ap,ap); ppow=f_int(pow(pr,K-1))
        expect=f_sub(ap2,ppow)
        assert f_eq(qs[pr*pr],expect), f"prime-square relation fail p={pr}"
print("[qexp] prime-square Hecke relations a_{p^2}=a_p^2-p^{31} hold for p=2,3,5 on both eigenforms.")
# verify a6=a2*a3 (distinct primes multiplicative)
for qs in [q_minus,q_plus]:
    assert f_eq(qs[6], f_mul(qs[2],qs[3]))
print("[qexp] multiplicativity a6=a2*a3 holds.")

# ---------- 5. Eichler-Selberg trace formula (independent) ----------
def S_seq(t,n,m):
    if m==0: return 0
    if m==1: return 1
    s0,s1=0,1
    for _ in range(2,m+1):
        s0,s1=s1,t*s1-n*s0
    return s1
def Pk(t,n,k): return S_seq(t,n,k-1)
def hurwitz(D):
    if D>=0:
        return Fraction(-1,12) if D==0 else Fraction(0)
    if D%4 not in (0,1):  # python mod: allowed 0,1 (i.e. 0 or 1 mod4)
        return Fraction(0)
    if D==-3: return Fraction(1,3)
    if D==-4: return Fraction(1,2)
    tot=Fraction(0)
    bmax=int(math.isqrt(abs(D)//3))+1
    for b in range(-bmax,bmax+1):
        if (b*b-D)%4!=0: continue
        ac=(b*b-D)//4
        if ac<=0: continue
        amax=int(math.isqrt(ac))
        for a in range(1,amax+1):
            if ac%a!=0: continue
            c=ac//a
            if abs(b)>a or a>c: continue
            if (abs(b)==a or a==c) and b<0: continue
            if a==c and b==0: w=Fraction(1,2)
            elif a==c and b==a: w=Fraction(1,3)
            else: w=Fraction(1,1)
            tot+=w
    return tot
def trace_selberg(k,n):
    tmax=int(math.isqrt(4*n-1))
    ell=Fraction(0)
    for t in range(-tmax,tmax+1):
        if t*t>=4*n: continue
        h=hurwitz(t*t-4*n)
        if h!=0: ell+=Pk(t,n,k)*h
    term_ell=Fraction(-1,2)*ell
    divs=divisors(n)
    sdiv=sum(pow(min(d,n//d),k-1) for d in divs)
    term_hyp=Fraction(-1,2)*sdiv
    r=math.isqrt(n); term_id=Fraction(k-1,12)*pow(n,(k-2)//2) if r*r==n else Fraction(0)
    return term_ell+term_hyp+term_id, term_ell, term_hyp, term_id
sel={}
for n in [1,2,3,5]:
    tr,e,h,i=trace_selberg(K,n)
    sel[n]=tr
    print(f"[trace] n={n}: Tr={tr} (ell={e}, hyp={h}, id={i})")
assert sel[1]==2 and sel[2]==tr2 and sel[3]==tr3 and sel[5]==tr5
print("[trace] Eichler-Selberg traces match Hecke-matrix traces for n=1,2,3,5.")

t_end=time.time()
print(f"[done] all checks passed in {t_end-t_start:.2f}s")

# ---------- 6. Write artifacts ----------
def w(path, text):
    with open(os.path.join(outdir,path),"w") as f: f.write(text)
# polys
w("hecke_polys.txt",
f"S_32(SL2Z) exact Hecke characteristic polynomials (T^2 - Tr*T + det)\n"
f"T2: T^2 - ({tr2})*T + ({det2}) = T^2 - 39960*T - 2235350016; D={D2}=576*18295489, 18295489=67*273067\n"
f"T3: T^2 - ({tr3})*T + ({det3v}); D={D3}, D3/D2=432^2\n"
f"T5: T^2 - ({tr5})*T + ({det5}); D={D5}, D5/D2=1418560^2\n"
f"M2={M2}\nM3={M3}\nM5={M5}\n"
f"Irreducible: D2 non-square ({r2}^2 < D2 < {(r2+1)}^2), no root mod29.\n")
# qexps as A,B pairs
lines=["n A_n B_n_minus  (a_n^- = A+B*sqrt(18295489), a_n^+ = A-B*sqrt(18295489))"]
for n in range(NOUT):
    A=int(q_minus[n][0]); B=int(q_minus[n][1])
    lines.append(f"{n} {A} {B}")
w("qexp_Oq50.txt","\n".join(lines)+"\n")
# trace form
w("trace_form.txt","n Tr(T_n)=a_n^-+a_n^+\n"+"\n".join(f"{n} {traces[n]}" for n in range(NOUT))+"\n")
# trace check
w("trace_check.txt",
f"Eichler-Selberg (k=32): Tr(T1)={sel[1]}, Tr(T2)={sel[2]}, Tr(T3)={sel[3]}, Tr(T5)={sel[5]}\n"
f"Hecke matrices: Tr(T2)={tr2}, Tr(T3)={tr3}, Tr(T5)={tr5}\nAgreement: True\n")
w("run_log.txt",f"completed in {t_end-t_start:.2f}s, PREC={PREC}, K={K}, stdlib-only, no floating point.\n")
print("[write] hecke_polys.txt, qexp_Oq50.txt, trace_form.txt, trace_check.txt, run_log.txt")
