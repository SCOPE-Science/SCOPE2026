"""Phase 3c: exact integer LLL + exact SVP, Smart VI.4.2 reduction loop for K=Q case.
Lattice: dim d=n+m=5. Basis rows of A (integer matrix):
  r_i = e_i (i=0..3), r_4 = (B1,B2,B3,B4, p^u), Bi = (log_p(mu_i)/lam) mod p^u as integers.
lam = p^c8, c8 = min valuation = 1 (computed). So Bi = log_i / p (exact p-adic division:
  log_i = p * ui => Bi = ui mod p^u). y = 0 (b0=0 since log(mu0)=0).
SVP: shortest nonzero vector of row-lattice. LLL-reduce then enumerate exactly.
If shortest^2 > n*B0^2 (=4*B0^2): reduced bound B2 = (u + c9)/c5, c9 = c8 = 1.
Iterate u = 1,2,... until success. Precision needed: prec > u + c8.
Also FIRST: rigorous global B0. Smart pipeline: B0 = max over places via K0_func:
  K0_l per place l, then B0 ~ K0 (archimedean+finite combined). Implement K0_l formula
  from Sage K0_func: K0_l = (2 c8_l)/(e_l c5_l) * log(c8_l/(e_l c5_l)) with c5_l=c3/(e_l log Nl).
  For K=Q: places 2,3,7,11,50069 (+inf? K0 loops over SUK.primes() = finite only).
  Need c8_l per place (Yu_bound at each small place) — compute with same exact formula
  (condition (1.15) per place; quadratic-extension branch if fails).
Then B0glob = K0 (documented AKMRVW/Smart: initial B0 from archimedean Baker + K0 max).
We compute K0 and take B0 = max(K0, small). Then run LLL loop at v=(50069).
"""
import math
from math import factorial
# ---------- Yu c8 per place (faithful formula, K=Q) ----------
def yu_c8(p, mus_list, dK=1, ep=1, fp=1, w=2):
    q=2; u=1
    if p==2: a1,k1,c1=32,40,160
    elif p==3: a1,k1,c1=(16,20,537)
    elif p==5: a1,k1,c1=(8*4/3,10,1473)
    elif p%4==1: a1,k1,c1=(8*(p-1)/(p-2),10,1473)
    else: a1,k1,c1=(8*(p-1)/(p-2),10,1288)
    def cond115():
        if p==2: return (w%3==0)
        if (p**fp)%4==1: return True
        return (w%4==0)
    n=1+len(mus_list)
    hs=[math.log(a) for a in mus_list]
    h1=fp*math.log(p)/(k1*(n+4)*dK)
    Om=max(0.0,h1)*math.prod(hs)
    C1=c1*(a1**n)*(n**n*(n+1)**(n+1)/factorial(n))*(p**fp/q**u)
    C1*=(dK/(fp*math.log(p)))**(n+2)
    C1*=math.log(max(dK,math.e))
    C1*=max(math.log(math.exp(4)*(n+1)*dK),ep,fp*math.log(p))
    C1star=(n+1)*C1
    return max(math.exp(2)/math.log(2),Om*C1star),cond115()
S=[2,3,7,11,50069]
for pl in S:
    mus=[q for q in S if q!=pl]
    c8,ok=yu_c8(pl,mus)
    print(f"v=({pl}): cond115={ok} mus={mus} c8={c8:.4e}")
# K0 per place: c5_l = c3/(e log N), e=1,N=pl; K0_l=(2c8/c5)log(c8/c5)
c3_cert=0.027
for pl in S:
    mus=[q for q in S if q!=pl]
    c8,_=yu_c8(pl,mus)
    c5=c3_cert/math.log(pl)
    K0=(2*c8/c5)*math.log(c8/c5)
    print(f"v=({pl}): c5={c5:.4e} K0_l={K0:.4e}")
