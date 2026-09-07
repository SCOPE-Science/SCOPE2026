#!/usr/bin/env python3
"""Deterministic independent replay for [[12,2]] d*=4 claim. Stdlib only.
Verifies from tableau strings + integer dual certificates only:
 1. rank/commutation, stabilizer/normalizer enumeration, distance 4, non-CSS, weight tables.
 2. Singleton/Hamming from scratch.
 3. MacWilliams+shadow LP infeasibility for d=5 (exact ints) and d=6 (exact ints).
Usage: python3 replay.py
"""
import math
from fractions import Fraction

N=12; CSIZE=1024
CAND=["IXXXZXXYXIXX","YXZZYYIZXIZX","ZXYIYZZZXXYX","XYYIIXIXZXYZ","YYXZIYIYIYYX","IZYYYXYIXYXZ","ZYXXIIYYXZXI","YYZIXYZYZZIX","ZIZXYYIYZYYY","IYZZZXIYXXZI"]

def str_to_int(s):
    xa=za=0
    for i,ch in enumerate(s):
        if ch=='X': xa|=(1<<i)
        elif ch=='Z': za|=(1<<i)
        elif ch=='Y': xa|=(1<<i); za|=(1<<i)
        elif ch=='I': pass
        else: raise ValueError(ch)
    return xa|(za<<12)

def comm(a,b):
    xa=a&0xFFF; za=(a>>12)&0xFFF
    xb=b&0xFFF; zb=(b>>12)&0xFFF
    return (bin(xa&zb).count('1')+bin(za&xb).count('1'))&1

def rank24(rows):
    A=list(rows); r=0
    for col in range(24):
        bit=1<<col
        piv=None
        for i in range(r,len(A)):
            if A[i]&bit: piv=i;break
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(len(A)):
            if i!=r and (A[i]&bit): A[i]^=A[r]
        r+=1
    return r

def nullspace24(mat):
    r=len(mat); A=list(mat); where=[-1]*24
    for col in range(24):
        bit=1<<col; sel=-1
        # find pivot at or below current row count
        nrows_done=sum(1 for w in where if w!=-1)
        for i in range(nrows_done,r):
            if A[i]&bit: sel=i;break
        if sel==-1: continue
        A[nrows_done],A[sel]=A[sel],A[nrows_done]
        where[col]=nrows_done
        for i in range(r):
            if i!=nrows_done and (A[i]&bit): A[i]^=A[nrows_done]
    basis=[]
    for f in range(24):
        if where[f]==-1:
            v=(1<<f)
            for c in range(24):
                if where[c]!=-1 and (A[where[c]]>>f &1): v|=(1<<c)
            basis.append(v)
    return basis

def weight24(v):
    return bin((v&0xFFF)|((v>>12)&0xFFF)).count('1')

def rank12(lst):
    A=list(lst); r=0
    for col in range(12):
        bit=1<<col; piv=None
        for i in range(r,len(A)):
            if A[i]&bit: piv=i;break
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        for i in range(len(A)):
            if i!=r and (A[i]&bit): A[i]^=A[r]
        r+=1
    return r

def Kmat(n):
    K=[[0]*(n+1) for _ in range(n+1)]
    for j in range(n+1):
        for i in range(n+1):
            s=0
            for t in range(max(0,j-(n-i)), min(j,i)+1):
                s+=((-1)**t)*(3**(j-t))*math.comb(i,t)*math.comb(n-i,j-t)
            K[j][i]=s
    return K

def Ksmat(n):
    Ks=[[0]*(n+1) for _ in range(n+1)]
    for jj in range(n+1):
        for ii in range(n+1):
            s=0
            for a in range(max(0,jj-ii), min(n-ii,jj)+1):
                b=a+ii-jj
                if 0<=b<=ii:
                    s+=math.comb(n-ii,a)*(3**a)*math.comb(ii,b)*((-1)**b)
            Ks[jj][ii]=s
    return Ks

def build_int(d, K, Ks, use_shadow):
    Aub=[];bub=[];Aeq=[];beq=[]
    Aeq.append([1]*12);beq.append(1023)
    for j in range(1,d):
        Aub_eq=[K[j][i]-(CSIZE if i==j else 0) for i in range(1,13)]
        Aeq.append(Aub_eq);beq.append(-K[j][0])
    for i in range(12):
        row=[0]*12;row[i]=-1;Aub.append(row);bub.append(0)
    for j in range(13):
        Aub.append([-K[j][i] for i in range(1,13)]);bub.append(K[j][0])
    for j in range(d,13):
        Aub.append([-(K[j][i]-(CSIZE if i==j else 0)) for i in range(1,13)]);bub.append(K[j][0])
    if use_shadow:
        for jj in range(13):
            Aub.append([-Ks[jj][i] for i in range(1,13)]);bub.append(Ks[jj][0])
    return Aub,bub,Aeq,beq

def check_cert(d, use_shadow, y_dict, zp_dict, scale, label):
    K=Kmat(12); Ks=Ksmat(12)
    Aub,bub,Aeq,beq=build_int(d,K,Ks,use_shadow)
    m_ub=len(Aub); m_eq=len(Aeq)
    y=[0]*m_ub
    for k,v in y_dict.items(): y[int(k)]=v
    z=[0]*m_eq
    for k,v in zp_dict.items(): z[int(k)]=v
    # check y>=0
    assert all(v>=0 for v in y), f"{label}: y negative"
    # residual per x-col
    for kk in range(12):
        s=sum(y[i]*Aub[i][kk] for i in range(m_ub))+sum(z[e]*Aeq[e][kk] for e in range(m_eq))
        assert s==0, f"{label}: residual col {kk}={s}"
    s=sum(y[i]*bub[i] for i in range(m_ub))+sum(z[e]*beq[e] for e in range(m_eq))
    assert s==-scale, f"{label}: norm {s} != {-scale}"
    assert s<0
    print(f"[PASS] {label}: exact Farkas verified (scale {scale}, norm {s})")
    return True

def main():
    print("=== 1. Tableau checks ===")
    rows=[str_to_int(s) for s in CAND]
    assert len(rows)==10
    for i in range(10):
        for j in range(i+1,10):
            assert comm(rows[i],rows[j])==0, f"commute fail {i},{j}"
    print("[PASS] pairwise symplectic orthogonality (45 pairs)")
    r=rank24(rows); assert r==10, r
    print("[PASS] rank 10 over GF(2)")
    GJ=[(((v>>12)&0xFFF))|((v&0xFFF)<<12) for v in rows]
    basis=nullspace24(GJ)
    assert len(basis)==14, len(basis)
    print("[PASS] normalizer dim 14")
    stab=set()
    for mask in range(1<<10):
        v=0
        for i in range(10):
            if mask>>i &1: v^=rows[i]
        stab.add(v)
    assert len(stab)==1024
    print("[PASS] |S|=1024")
    from collections import Counter
    cN=Counter();cS=Counter();cL=Counter()
    minL=13
    for mask in range(1<<14):
        v=0
        for i in range(14):
            if mask>>i &1: v^=basis[i]
        w=weight24(v)
        cN[w]+=1
        if v in stab: cS[w]+=1
        else:
            cL[w]+=1
            if w<minL: minL=w
    assert sum(cN.values())==16384 and sum(cS.values())==1024 and sum(cL.values())==15360
    print(f"[PASS] |N|=16384; distance (min N\\S) = {minL}")
    assert minL==4, minL
    expN={0:1,4:35,5:212,6:652,7:1668,8:3195,9:4220,10:3796,11:2092,12:513}
    expS={0:1,5:7,6:37,7:123,8:210,9:245,10:231,11:137,12:33}
    expL={4:35,5:205,6:615,7:1545,8:2985,9:3975,10:3565,11:1955,12:480}
    assert dict(cN)==expN, dict(cN)
    assert dict(cS)==expS, dict(cS)
    assert dict(cL)==expL, dict(cL)
    print("[PASS] weight distributions match published tables")
    # non-CSS
    xrows=[(v&0xFFF) for v in stab if ((v>>12)&0xFFF)==0 and (v&0xFFF)!=0]
    zrows=[((v>>12)&0xFFF) for v in stab if (v&0xFFF)==0 and ((v>>12)&0xFFF)!=0]
    dx=rank12(xrows); dz=rank12(zrows)
    assert dx==0 and dz==0 and dx+dz!=10, (dx,dz)
    print(f"[PASS] genuinely non-CSS (dx={dx},dz={dz},sum!=10); X-only count {len(xrows)}, Z-only {len(zrows)}")
    # pure: stabilizer min weight
    minS=min(k for k in cS if k>0)
    assert minS==5 and minS>=4
    print(f"[PASS] pure code (stabilizer min weight {minS}>=4)")
    print("=== 2. Singleton/Hamming from scratch ===")
    assert 2*7-2>10 and 2*6-2<=10
    print("[PASS] Singleton: d<=6 (10>=2d-2)")
    def Hs(n,t): return sum((3**j)*math.comb(n,j) for j in range(t+1))
    assert Hs(12,1)==37<=1024 and Hs(12,2)==631<=1024 and Hs(12,3)==6571>1024
    print(f"[PASS] Hamming: t=1 sum 37, t=2 sum 631<=1024, t=3 sum 6571>1024 => d<=6")
    print("=== 3. LP infeasibility ===")
    # d5 shadow cert
    check_cert(5, True, {"0":21504,"1":11264,"2":9216,"3":3072,"4":2048,"33":24,"34":4,"35":4}, {"0":39,"1":19,"2":9,"3":3,"4":1}, 21504, "[[12,2,5]] shadow LP")
    # d6 no-shadow cert
    check_cert(6, False, {"0":985600,"1":593920,"2":311296,"3":139264,"4":48640,"5":10240,"8":512}, {"0":1760,"1":770,"2":320,"3":116,"4":32,"5":5}, 1351680, "[[12,2,6]] MacWilliams LP")
    print("=== ALL CHECKS PASS: d*=4 (attain d=4, no d>=5) ===")

if __name__=="__main__":
    main()
