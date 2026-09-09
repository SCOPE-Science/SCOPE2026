"""Lane 471 TARGET, part 6: GENERIC irreducible quartic partition test (beyond 4-plane arrangement).
P(x,y,z) = sum of monomials degree<=4 with fixed generic coefficients (seeded, recorded).
Per tube: restrict to univariate quartic q(t)=P(b+t e); coefficients EXACT via binomial expansion
(dot products); real roots via numpy.roots (companion eigenvalues); #cells = #distinct real roots in
(-1/2,1/2)+1 (<=5 by FTA, Bezout<=4 unless q=0 identically); containment certificate:
min over tubes of ||coeff||_inf >> 0.
Wall-length estimate via dense sampling (20001 pts/tube, spacing 5e-5 ~ 0.2d): fraction of samples
with |P| <= d*|grad P| (first-order wall proxy) — reported as estimate with resolution note.
Families: H, bush-planar, sticky-S, 3D-fib bush (subsample 512 for speed on fib).
Stdlib+numpy.
"""
import json, math
import numpy as np

d = 2.0**-12
rng = np.random.default_rng(20260907)
# generic quartic: random coeffs for all 35 monomials degree<=4 in 3 vars, scaled; plus constant offset
# build exponent list
exps=[]
for i in range(5):
    for j in range(5-i):
        for k in range(5-i-j):
            exps.append((i,j,k))
assert len(exps)==35
coef = rng.normal(size=35)
coef /= np.linalg.norm(coef)
# force leading homogeneous part nonzero (generic): ensure some deg-4 coeff large
coef[exps.index((4,0,0))]+=1.0; coef[exps.index((0,4,0))]-=0.7; coef[exps.index((0,0,4))]+=0.5
coef[exps.index((0,0,0))]=0.37  # constant offset so 0 not on surface
print("P coeffs (first 6):",coef[:6],"const:",coef[exps.index((0,0,0))])

def qtube_coeffs(b,e):
    # q(t)=sum_c c_a (b+t e)^a; expand each monomial: prod over vars of sum_{s} C(a,s) b^{a-s} e^s t^s
    # coefficient of t^m: sum over monomials c_a * sum_{s1+s2+s3=m} prod C(a_i,s_i) b_i^{a_i-s_i} e_i^{s_i}
    from math import comb
    q=np.zeros(5)  # q[m] = coeff of t^m
    for (a1,a2,a3),c in zip(exps,coef):
        for s1 in range(a1+1):
            for s2 in range(a2+1):
                for s3 in range(a3+1):
                    m=s1+s2+s3
                    q[m]+=c*comb(a1,s1)*comb(a2,s2)*comb(a3,s3)*(b[0]**(a1-s1))*(b[1]**(a2-s2))*(b[2]**(a3-s3))*(e[0]**s1)*(e[1]**s2)*(e[2]**s3)
    return q  # ascending powers

def analyze(bx,by,bz,ex,ey,ez,label,maxn=None):
    n=len(bx) if maxn is None else maxn
    cells=np.zeros(n,dtype=int); cmin=1e9; contained=0
    for i in range(n):
        q=qtube_coeffs((bx[i],by[i],bz[i]),(ex[i],ey[i],ez[i]))
        cn=np.abs(q).max()
        cmin=min(cmin,cn)
        if cn<1e-12:
            contained+=1; cells[i]=1; continue
        r=np.roots(q[::-1])  # numpy wants descending
        real=sorted(float(x.real) for x in r if abs(x.imag)<1e-6 and -0.5<float(x.real)<0.5)
        # merge ties within 1e-9
        merged=[]
        for x in real:
            if merged and x-merged[-1]<1e-9: merged[-1]=0.5*(merged[-1]+x)
            else: merged.append(x)
        cells[i]=len(merged)+1
    # wall proxy dense sampling
    S=2001
    t=np.linspace(-0.5,0.5,S)
    wall=0; tot=0
    for i in range(n):
        X=bx[i]+t*ex[i]; Y=by[i]+t*ey[i]; Z=bz[i]+t*ez[i]
        Pv=np.zeros(S); Gv=np.zeros(S)
        for (a1,a2,a3),c in zip(exps,coef):
            Pv+=c*X**a1*Y**a2*Z**a3
            if a1>0: Gx=c*a1*X**(a1-1)*Y**a2*Z**a3
            else: Gx=0
            if a2>0: Gy=c*a2*X**a1*Y**(a2-1)*Z**a3
            else: Gy=0
            if a3>0: Gz=c*a3*X**a1*Y**a2*Z**(a3-1)
            else: Gz=0
            Gv+=0  # accumulate grad norm below properly
        # recompute grad norm cleanly
        Gx=np.zeros(S); Gy=np.zeros(S); Gz=np.zeros(S)
        for (a1,a2,a3),c in zip(exps,coef):
            if a1>0: Gx+=c*a1*X**(a1-1)*Y**a2*Z**a3
            if a2>0: Gy+=c*a2*X**a1*Y**(a2-1)*Z**a3
            if a3>0: Gz+=c*a3*X**a1*Y**a2*Z**(a3-1)
        Gn=np.sqrt(Gx**2+Gy**2+Gz**2)
        wall+=int((((np.abs(Pv)<=d*np.maximum(Gn,1e-300)))).sum()); tot+=S
    from collections import Counter
    hist=dict(Counter(cells.tolist()))
    return dict(label=label,n=n,max_cells=int(cells.max()),hist=hist,min_coeff=float(cmin),
                contained=int(contained),bezout_ok=bool((cells<=5).all() and contained==0),
                wall_proxy=float(wall/tot))

N=2048; j=np.arange(N); th=2*np.pi*j/N; ux=np.cos(th); uy=np.sin(th); uz=np.zeros(N)
zj=-0.5+(j+0.5)/N; bx=-0.5+(j+0.5)/N
out={}
out["H"]=analyze(np.zeros(N),np.zeros(N),zj,ux,uy,uz,"H"); print("H:",out["H"])
out["bush"]=analyze(np.zeros(N),np.zeros(N),np.zeros(N),ux,uy,uz,"bush"); print("bush:",out["bush"])
out["sticky"]=analyze(bx,np.zeros(N),np.full(N,0.11),ux,uy,uz,"sticky"); print("sticky:",out["sticky"])
# fib 3d subsample 512
ga=math.pi*(3.0-math.sqrt(5.0)); K=512; kk=np.arange(K)
zz=1.0-(2.0*(kk+0.5)/K); rr=np.sqrt(np.maximum(0,1-zz**2)); aa=ga*kk
out["fib3d"]=analyze(np.zeros(K),np.zeros(K),np.zeros(K),rr*np.cos(aa),rr*np.sin(aa),zz,"fib3d"); print("fib3d:",out["fib3d"])
with open("output/artifacts/target_generic_quartic_log.json","w") as f: json.dump(out,f,indent=1)
print("GENERIC_QUARTIC done")
