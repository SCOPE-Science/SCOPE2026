#!/usr/bin/env python3
"""Defect + Haagerup for bordered BH(6,3) solution vs Fourier F6 reference.
Exact integer arithmetic only (Fractions). No floats.
Defect convention: d(H) = dim_R ker(linearized unitarity) - (2n-1).
Dephased defect = nullity of 30x25 restricted matrix (should equal d).
Haagerup Lambda(H) = {h_ij h_kl conj(h_il h_kj)} as exponent sets.
Usage: python3 defect_haagerup.py -> writes defect_lambda.json + prints table.
"""
import json, os
from fractions import Fraction
from collections import Counter

N=6
ROWS=[[0,0,0,0,0,0],[0,0,1,1,2,2],[0,1,0,2,1,2],[0,1,2,0,2,1],[0,2,1,2,0,1],[0,2,2,1,1,0]]
F6=[[ (i*j)%6 for j in range(6)] for i in range(6)]

def build_M_mu3(rows):
    n=len(rows); M=[]
    for i in range(n):
        for j in range(i+1,n):
            e=[(rows[i][k]-rows[j][k])%3 for k in range(n)]
            r=[2 if x==0 else -1 for x in e]
            s=[0 if x==0 else (1 if x==1 else -1) for x in e]
            rr=[0]*(n*n); ii=[0]*(n*n)
            for k in range(n):
                rr[i*n+k]+=r[k]; rr[j*n+k]-=r[k]
                ii[i*n+k]+=s[k]; ii[j*n+k]-=s[k]
            M.append(rr); M.append(ii)
    return M

def build_M_F6(F):
    n=6
    remap={0:2,1:1,2:-1,3:-2,4:-1,5:1}
    smap={0:0,1:1,2:1,3:0,4:-1,5:-1}
    M=[]
    for i in range(n):
        for j in range(i+1,n):
            e=[(F[i][k]-F[j][k])%6 for k in range(n)]
            r=[remap[x] for x in e]; s=[smap[x] for x in e]
            rr=[0]*(n*n); ii=[0]*(n*n)
            for k in range(n):
                rr[i*n+k]+=r[k]; rr[j*n+k]-=r[k]
                ii[i*n+k]+=s[k]; ii[j*n+k]-=s[k]
            M.append(rr); M.append(ii)
    return M

def rank_frac(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if m else 0
    pivrow=0
    for c in range(n):
        sel=-1
        for i in range(pivrow,m):
            if A[i][c]!=0:
                sel=i; break
        if sel<0: continue
        A[pivrow],A[sel]=A[sel],A[pivrow]
        pv=A[pivrow][c]
        for i in range(m):
            if i!=pivrow and A[i][c]!=0:
                f=A[i][c]/pv
                for j in range(c,n):
                    A[i][j]-=f*A[pivrow][j]
        pivrow+=1
        if pivrow==m: break
    return pivrow

def defect_of(M,n):
    r=rank_frac(M)
    null=n*n-r
    d=null-(2*n-1)
    cols=[i*n+k for i in range(1,n) for k in range(1,n)]
    Mdep=[[row[c] for c in cols] for row in M]
    r2=rank_frac(Mdep)
    ddep=(n-1)*(n-1)-r2
    return {"rank":r,"null":null,"defect":d,"dephased_rank":r2,"dephased_null":ddep}

def haagerup_mu3(rows):
    c=Counter(); s=set()
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    v=(rows[i][j]+rows[k][l]-rows[i][l]-rows[k][j])%3
                    s.add(v); c[v]+=1
    return sorted(s), {str(k):c[k] for k in sorted(c)}

def haagerup_F6(F):
    c=Counter(); s=set()
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    v=(F[i][j]+F[k][l]-F[i][l]-F[k][j])%6
                    s.add(v); c[v]+=1
    return sorted(s), {str(k):c[k] for k in sorted(c)}

def main():
    base=os.path.dirname(os.path.abspath(__file__))
    M=build_M_mu3(ROWS)
    dO=defect_of(M,6)
    MF=build_M_F6(F6)
    dF=defect_of(MF,6)
    Ls,cO=haagerup_mu3(ROWS)
    Lf,cF=haagerup_F6(F6)
    out={"solution":{"matrix_exp":ROWS,"linear_system":"30x36 integer (r=2/-1,s=0/+1/-1)",
            "rank":dO["rank"],"null":dO["null"],"defect":dO["defect"],
            "dephased_rank":dO["dephased_rank"],"dephased_null":dO["dephased_null"],
            "haagerup_exp_mod3":Ls,"haagerup_counts":cO,"haagerup_size":len(Ls),
            "haagerup_as_roots":"{1,omega,omega^2}"},
         "fourier_F6":{"rank":dF["rank"],"null":dF["null"],"defect":dF["defect"],
            "dephased_rank":dF["dephased_rank"],"dephased_null":dF["dephased_null"],
            "haagerup_exp_mod6":Lf,"haagerup_counts":cF,"haagerup_size":len(Lf),
            "haagerup_as_roots":"all 6th roots zeta^e, zeta=exp(pi*i/3)"},
         "comparison":{"defect_distinguishes":dO["defect"]!=dF["defect"],
            "haagerup_distinguishes":len(Ls)!=len(Lf),
            "verdict":"solution defect 0 (isolated, Tao-type), Fourier defect 4; Lambda 3 vs 6 -> inequivalent to Fourier"}}
    with open(os.path.join(base,"defect_lambda.json"),"w") as f:
        json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
