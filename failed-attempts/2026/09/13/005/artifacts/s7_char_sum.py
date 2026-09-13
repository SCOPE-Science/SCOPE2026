"""Route (i): exact GJV character/class-algebra sum for (g,d,nu)=(2,7,(3,2,1,1)), r=7.

Setup: s in S7 fixed of type nu=(3,2,1,1). Count N_fix = #{(t_1..t_7,T): t_i transpositions,
T a 7-cycle, prod(t)*T = s}. Since T is a 7-cycle every tuple is transitive (connected),
so no disconnected subtraction is needed.

Character formula (Frobenius): for conjugacy classes C_1..C_{r+1} and fixed g in class D,
  #{x_i in C_i : prod x_i = g} = (prod|C_i|/d!) * sum_lam chi_lam(g^{-1}) prod chi_lam(C_i)/dim_lam^r.
All classes here self-inverse (7-cycles inverse is a 7-cycle), so chi(g^{-1})=chi(g).
Characters computed exactly via Jacobi-Trudi/Frobenius power-sum expansion in Q[p].

Normalization lemma: each geometric cover f (sheets unlabelled) with sheet-labelings gives
d!/|Aut f| tuples; fixing s selects fraction |cent(s)|/d!. Hence N_fix = |cent(s)| * H,
|cent(s)| = 3*2*2! = 12. Target H = N_fix/12. DL one-part number h_DL = |Aut(nu)|/r! * H
= 2/5040 * H = H/2520. Verified: brute-force S3 analogue in s3_check.log.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial

def partitions(n, maxp=None):
    if n==0: yield (); return
    if maxp is None: maxp=n
    for f in range(min(maxp,n),0,-1):
        for rest in partitions(n-f, f):
            yield (f,)+rest

def char_via_frobenius(lam, mu):
    n = sum(lam)
    h = {}
    for m in range(0, n+1):
        terms = {}
        if m==0:
            terms[(0,)*n]=Fraction(1)
        else:
            for nu in partitions(m):
                e=[0]*n
                for p in nu: e[p-1]+=1
                e=tuple(e)
                z=1
                from collections import Counter
                c=Counter(nu)
                for l,cnt in c.items():
                    z*=(l**cnt)*factorial(cnt)
                terms[e]=terms.get(e,Fraction(0))+Fraction(1,z)
        h[m]=terms
    def add(a,b,s=1):
        c=dict(a)
        for k,v in b.items(): c[k]=c.get(k,Fraction(0))+s*v
        return {kk:vv for kk,vv in c.items() if vv!=0}
    def mul(a,b):
        c={}
        for k1,v1 in a.items():
            for k2,v2 in b.items():
                k=tuple(k1[i]+k2[i] for i in range(n))
                c[k]=c.get(k,Fraction(0))+v1*v2
        return {kk:vv for kk,vv in c.items() if vv!=0}
    import itertools
    l=len(lam)
    M=[[h[lam[i]-i+j] if lam[i]-i+j>=0 else {(0,)*n:Fraction(0)} for j in range(l)] for i in range(l)]
    out={}
    for perm in itertools.permutations(range(l)):
        inv=sum(1 for i in range(l) for j in range(i+1,l) if perm[i]>perm[j])
        sgn=-1 if inv%2 else 1
        t={(0,)*n:Fraction(sgn)}
        for i in range(l):
            t=mul(t,M[i][perm[i]])
        out=add(out,t)
    from collections import Counter
    c=Counter(mu); e=tuple(c.get(k+1,0) for k in range(n))
    z=1
    for part,cnt in c.items(): z*=(part**cnt)*factorial(cnt)
    return out.get(e,Fraction(0))*z

if __name__=="__main__":
    d=7; r=7
    C2=21; C7=720
    tot=Fraction(0)
    log=open("output/artifacts/s7_char_table.log","w")
    for lam in partitions(7):
        dim=int(char_via_frobenius(lam,(1,)*7))
        c2=char_via_frobenius(lam,(2,1,1,1,1,1))
        c7=char_via_frobenius(lam,(7,))
        cnu=char_via_frobenius(lam,(3,2,1,1))
        log.write(f"{lam} dim={dim} chi2={c2} chi7={c7} chinu={cnu}\n")
        assert dim>0
        tot+=Fraction(cnu)*(Fraction(c2)**r)*Fraction(c7)/Fraction(dim**7)
    log.close()
    Nfix=Fraction(C2**r*C7,1)*tot/Fraction(factorial(7))
    assert Nfix.denominator==1, Nfix
    H=Nfix/12
    h_DL=H/2520
    print("char sum =",tot)
    print("Nfix =",Nfix)
    print("H =",H)
    print("h_DL =",h_DL)
    open("output/artifacts/s7_result.txt","w").write(f"charsum={tot}\nNfix={Nfix}\nH={H}\nh_DL={h_DL}\n")
