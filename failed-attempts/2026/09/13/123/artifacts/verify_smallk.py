"""Verify DP machinery at small k against hand/direct computations + try longdouble eigensolve."""
import numpy as np, math, itertools

def build(k, wmax=6, dmax=3, rset=None):
    if rset is None: rset = [0]+list(range(2, 2*dmax+3))
    def enum_vecs(W, J=9):
        vecs = []
        def rec(j, rem, cur):
            if j > J:
                vecs.append(tuple(cur)); return
            for e in range(rem // j + 1):
                cur.append(e); rec(j+1, rem - j*e, cur); cur.pop()
        rec(1, W, [])
        return vecs
    vecsW = enum_vecs(wmax); vecsD = enum_vecs(dmax)
    Eidx = {v:i for i,v in enumerate(vecsW)}
    E=len(vecsW); B=len(vecsD)
    W = np.array([sum((j+1)*v[j] for j in range(9)) for v in vecsW])
    from math import comb
    rows,cols,Cs,AAs,WFs=[],[],[],[],[]
    for ei,e in enumerate(vecsW):
        for f in itertools.product(*[range(x+1) for x in e]):
            c=1
            for j in range(9): c*=comb(e[j],f[j])
            A=sum(e[j]-f[j] for j in range(9))
            rows.append(ei);cols.append(Eidx[f]);Cs.append(c);AAs.append(A);WFs.append(W[Eidx[f]])
    rows=np.array(rows);cols=np.array(cols);Cs=np.array(Cs);AAs=np.array(AAs);WFs=np.array(WFs)
    lg=np.vectorize(math.lgamma)
    v={s:np.zeros(E) for s in rset}
    for s in rset: v[s][Eidx[(0,)*9]]=1.0
    snap=None
    for kk in range(1,k+1):
        vn={}
        for s in rset:
            A1=AAs+1;B1=(kk-1)+WFs+s+1
            co=Cs*np.exp(lg(A1)+lg(B1)-lg(A1+B1))
            out=np.zeros(E); np.add.at(out,rows,co*v[s][cols]); vn[s]=out
        v=vn
        if kk==k-1: snap={s:x.copy() for s,x in v.items()}
    return vecsW, vecsD, Eidx, v, snap

# k=2 checks: F=1 and F=p1
vecsW, vecsD, Eidx, v2, v1 = build(2)
e0=Eidx[(0,)*9]; e1=Eidx[tuple([1]+[0]*8)]; e2=Eidx[tuple([2]+[0]*8)]
print("k=2: vol =",v2[0][e0],"expect",1/2)
print("k=2: int p1 =",v2[0][e1],"expect",1/6)
print("k=2: int p1^2 =",v2[0][e2],"expect",2/24)
# J_1 for F=p1 at k=2: hand value 2/15. DP: J1 = sum over subs of p1: subs (f,e): t-expansion of p1=x+y in x: a=1,c=1 (term x) and a=0,c=y (term 1*y).
# formula: J1 = sum_{f,g} c1c2 v1[a+b+2][f+g]/((a+1)(b+1)); basis element p1: subs: (f=0,c=1,a=1),(f=e1,c=1,a=0)
s=0.0
subs=[(e0,1,1),(e1,1,0)]
for (ff,c1,a) in subs:
    for (gg,c2,b) in subs:
        h=tuple([vecsW[ff][t]+vecsW[gg][t] for t in range(9)])
        s+=c1*c2*v1[a+b+2][Eidx[h]]/((a+1)*(b+1))
print("k=2: J1(p1) =",s,"expect",2/15, " match:", abs(s-2/15)<1e-12)
# J_1 for F=1: int_0^1 (1-y)^2 dy=1/3
print("k=2: J1(1) =",v1[2][e0],"expect",1/3)
# k=3: F=1: J1 = int_{x+y<=1}(1-x-y)^2 = 1/12? int Dx_2(1) (1-S)^2 dS-area = B: 2!... = 2!/(4!)*2! hmm: int=S_2 simplex (1-S)^2 = 2!*2!/4! = 1/12... (2*2/24=1/6?) compute: prod factorials: for Dx_2: int (1-S)^2 = 0!0!2!/(0+0+2+2)! *... Dirichlet: int_{Dx_k} prod t_i^{a_i}(1-S)^b = prod(a_i!) b!/(|a|+b+k)!. k=2,a=0,b=2: 2!/4!=1/12. 
vecsW3, vecsD3, Eidx3, v3, v2b = build(3)
print("k=3: J1(1) =",v2b[2][Eidx3[(0,)*9]],"expect",1/12)
print("k=3: vol =",v3[0][Eidx3[(0,)*9]],"expect",1/6)
# F=p1 at k=3, J1 by hand: inner int_0^{1-S}(x+S)dx with S=y+z: =(1-S)^2/2+S(1-S)=(1-S)(1+S)/2. square/outer: int_{Dx_2(1)} (1-S)^2(1+S)^2/4 = (1/4)*int(1-2S^2+S^4)... moments: use DP values: int 1=1/2, int S^2? S^2=(y+z)^2=y^2+z^2+2yz: Dirichlet k=2: int y^2=2! /4! =1/12 each, int yz=1/24... wait (0!..): int y^2 z^0 (1-S)^0: 2!0!0!/(2+0+2)!=2/24=1/12. int yz: 1!1!/(1+1+0+2)!=1/24. so int S^2=1/12+1/12+2/24=1/4. int S^4: expand (y+z)^4: y^4+z^4+4y^3z+4yz^3+6y^2z^2: ints: 4!/6!=1/30 each y^4; 3!1!/6!=1/120 each y^3z; 2!2!/6!=1/180 y^2z^2*6=1/30. total 1/30+1/30+4/120+4/120+1/30 = (4+4+2+2+4)/120=16/120=2/15? let me just: 1/30*2=1/15; 8/120=1/15; 1/30. total=1/15+1/15+1/30=5/30=1/6. So J1=(1/4)(1/2-2*(1/4)+1/6)=(1/4)(1/2-1/2+1/6)=1/24.
subs3=[(Eidx3[(0,)*9],1,1),(Eidx3[tuple([1]+[0]*8)],1,0)]
s=0.0
for (ff,c1,a) in subs3:
    for (gg,c2,b) in subs3:
        h=tuple([vecsW3[ff][t]+vecsW3[gg][t] for t in range(9)])
        s+=c1*c2*v2b[a+b+2][Eidx3[h]]/((a+1)*(b+1))
print("k=3: J1(p1) =",s,"expect",1/24," match:",abs(s-1/24)<1e-12)
