#!/usr/bin/env python3
"""Independent verifier for the spiked-7 dps census fragment + maximal-volume dps witness.
Stdlib only. Rebuilds the 29 size-7 spiked candidates from Blanco-Santos Thms 3.2/3.3
(vertex data in CANDS below), recounts lattice points by exact facet enumeration,
runs the 21-pair-sum dps test, checks pairwise unimodular inequivalence, checks the
census totals, and replays the maximal-volume dps witness certificate.
Exit 0 with VERIFY_OK on success.
"""
import itertools
from fractions import Fraction as F

CANDS = [
 ('T3.2(a00)',[(1,0,0),(0,1,0),(-1,0,0),(0,-1,4)]),
 ('T3.2(a01)',[(1,0,0),(0,1,0),(-1,0,0),(0,-1,5)]),
 ('T3.2(a11)',[(1,0,0),(0,1,0),(-1,0,-1),(0,-1,5)]),
 ('T3.3(1)',[(1,-1,-1),(-1,1,1),(-1,-1,0),(0,0,3)]),
 ('T3.3(2)',[(1,-1,0),(-1,1,-1),(-1,-1,0),(0,0,2)]),
 ('T3.3(4)',[(2,-1,-1),(-1,2,1),(-1,-1,0),(0,0,3)]),
 ('T3.3(5a-1)',[(1,-1,-1),(0,1,-1),(-1,-1,0),(0,0,3)]),
 ('T3.3(5a0)',[(1,-1,-1),(0,1,0),(-1,-1,0),(0,0,3)]),
 ('T3.3(7a-5)',[(2,1,0),(-1,1,-5),(-1,-1,0),(0,0,3)]),
 ('T3.3(7a-1)',[(2,1,0),(-1,1,-1),(-1,-1,0),(0,0,3)]),
 ('T3.3(8,a-1b-1)',[(1,0,0),(0,1,0),(-1,0,-1),(0,-1,-1),(0,0,2)]),
 ('T3.3(8,a-1b0)',[(1,0,0),(0,1,0),(-1,0,-1),(0,-1,0),(0,0,2)]),
 ('T3.3(8,a-1b1)',[(1,0,0),(0,1,0),(-1,0,-1),(0,-1,1),(0,0,2)]),
 ('T3.3(8,a-1b2)',[(1,0,0),(0,1,0),(-1,0,-1),(0,-1,2),(0,0,2)]),
 ('T3.3(8,a-1b3)',[(1,0,0),(0,1,0),(-1,0,-1),(0,-1,3),(0,0,2)]),
 ('T3.3(8,a0b0)',[(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,2)]),
 ('T3.3(8,a0b1)',[(1,0,0),(0,1,0),(-1,0,0),(0,-1,1),(0,0,2)]),
 ('T3.3(8,a0b2)',[(1,0,0),(0,1,0),(-1,0,0),(0,-1,2),(0,0,2)]),
 ('T3.3(8,a0b3)',[(1,0,0),(0,1,0),(-1,0,0),(0,-1,3),(0,0,2)]),
 ('T3.3(9,a-2b0)',[(1,0,0),(0,1,0),(-1,-1,-2),(1,1,6)]),
 ('T3.3(9,a-2b1)',[(1,0,0),(0,1,0),(-1,-1,-2),(1,1,7)]),
 ('T3.3(9,a-1b0)',[(1,0,0),(0,1,0),(-1,-1,-1),(1,1,5)]),
 ('T3.3(9,a-1b1)',[(1,0,0),(0,1,0),(-1,-1,-1),(1,1,6)]),
 ('T3.3(9,a0b0)',[(1,0,0),(0,1,0),(-1,-1,0),(1,1,4)]),
 ('T3.3(9,a0b1)',[(1,0,0),(0,1,0),(-1,-1,0),(1,1,5)]),
 ('T3.3(10a,a-1)',[(1,0,-1),(0,2,-1),(-1,0,0),(0,0,2)]),
 ('T3.3(10a,a0)',[(1,0,0),(0,2,-1),(-1,0,0),(0,0,2)]),
 ('T3.3(10b,a-1)',[(1,0,0),(0,2,-1),(-1,0,0),(0,1,2)]),
 ('T3.3(10b,a0)',[(1,0,0),(0,2,0),(-1,0,0),(0,1,2)]),
]
EXPECT_DPS = {'T3.2(a00)':1,'T3.2(a01)':1,'T3.2(a11)':1,'T3.3(1)':0,'T3.3(2)':1,
 'T3.3(4)':0,'T3.3(5a-1)':0,'T3.3(5a0)':0,'T3.3(7a-5)':0,'T3.3(7a-1)':0,
 'T3.3(8,a-1b-1)':0,'T3.3(8,a-1b0)':1,'T3.3(8,a-1b1)':0,'T3.3(8,a-1b2)':0,'T3.3(8,a-1b3)':0,
 'T3.3(8,a0b0)':0,'T3.3(8,a0b1)':0,'T3.3(8,a0b2)':0,'T3.3(8,a0b3)':0,
 'T3.3(9,a-2b0)':1,'T3.3(9,a-2b1)':1,'T3.3(9,a-1b0)':1,'T3.3(9,a-1b1)':1,'T3.3(9,a0b0)':1,'T3.3(9,a0b1)':1,
 'T3.3(10a,a-1)':1,'T3.3(10a,a0)':1,'T3.3(10b,a-1)':1,'T3.3(10b,a0)':1}

def sub(a,b): return (a[0]-b[0],a[1]-b[1],a[2]-b[2])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(M):
    (a,b,c),(d,e,f),(g,h,i)=M
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def facets(pts):
    n=len(pts); seen={}
    for i,j,k in itertools.combinations(range(n),3):
        nv=cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if nv==(0,0,0): continue
        vals=[dot(nv,p) for p in pts]
        if dot(nv,pts[i])==max(vals): key=(nv,max(vals))
        elif dot(nv,pts[i])==min(vals): key=((-nv[0],-nv[1],-nv[2]),-min(vals))
        else: continue
        seen[key]=seen.get(key,0)+1
    plains=list(seen)
    res=[]
    for idx,(nv,rhs) in enumerate(plains):
        copl={i for i,p in enumerate(pts) if dot(nv,p)==rhs}
        if any(copl<({i for i,p in enumerate(pts) if dot(m,p)==t}) for j,(m,t) in enumerate(plains) if j!=idx):
            continue
        res.append((nv,rhs))
    return res

def lpts(verts):
    fs=facets(verts)
    xs=[v[0] for v in verts]; ys=[v[1] for v in verts]; zs=[v[2] for v in verts]
    S=[(x,y,z) for x in range(min(xs),max(xs)+1) for y in range(min(ys),max(ys)+1) for z in range(min(zs),max(zs)+1)
       if all(dot(nv,(x,y,z))<=rhs for nv,rhs in fs)]
    return sorted(S),fs

def dps21(S):
    sums={}
    for i,j in itertools.combinations(range(len(S)),2):
        s=(S[i][0]+S[j][0],S[i][1]+S[j][1],S[i][2]+S[j][2])
        if s in sums: return False,(s,sums[s],(i,j))
        sums[s]=(i,j)
    return True,None

def equiv(S1,S2):
    s2=set(S2)
    p0=S1[0]; E=None
    for q in itertools.permutations(range(len(S1)),4):
        M=tuple(sub(S1[q[i]],S1[q[0]]) for i in (1,2,3))
        if det3(M)!=0: p0=S1[q[0]]; E=(q,M); break
    q,E=E; d1=det3(E)
    (a,b,c),(d,e,f),(g,h,i)=E
    C=[[(e*i-f*h),-(d*i-f*g),(d*h-e*g)],[-(b*i-c*h),(a*i-c*g),-(a*h-b*g)],[(b*f-c*e),-(a*f-c*d),(a*e-b*d)]]
    Adj=((C[0][0],C[1][0],C[2][0]),(C[0][1],C[1][1],C[2][1]),(C[0][2],C[1][2],C[2][2]))
    for r in itertools.permutations(range(len(S2)),4):
        s0=S2[r[0]]; M2=tuple(sub(S2[r[i]],s0) for i in (1,2,3))
        if abs(det3(M2))!=abs(d1): continue
        A=[]; ok=True
        for rr in range(3):
            row=[]
            for cc in range(3):
                num=sum(M2[rr][kk]*Adj[kk][cc] for kk in range(3))
                if num%d1!=0: ok=False; break
                row.append(num//d1)
            if not ok: break
            A.append(tuple(row))
        if not ok or abs(det3(tuple(A)))!=1: continue
        t=tuple(s0[j]-sum(A[j][k]*p0[k] for k in range(3)) for j in range(3))
        if {tuple(sum(A[j][k]*p[k] for k in range(3))+t[j] for j in range(3)) for p in S1}==s2:
            return True
    return False

def main():
    sets={}
    for name,V in CANDS:
        S,fs=lpts(V)
        assert len(S)==7,(name,len(S))
        sets[name]=(S,fs,V)
    for name,(S,fs,V) in sets.items():
        ok,_=dps21(S)
        assert int(ok)==EXPECT_DPS[name],(name,ok)
    assert sum(EXPECT_DPS.values())==15 and len(EXPECT_DPS)==29
    names=list(sets)
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            assert not equiv(sets[names[i]][0],sets[names[j]][0]),(names[i],names[j])
    # witness replay
    S,fs,V=sets['T3.3(9,a-2b1)']
    assert S==[(-1,-1,-2),(0,0,0),(0,0,1),(0,0,2),(0,1,0),(1,0,0),(1,1,7)],S
    ok,_=dps21(S)
    assert ok
    assert len({(S[i][0]+S[j][0],S[i][1]+S[j][1],S[i][2]+S[j][2]) for i,j in itertools.combinations(range(7),2)})==21
    # facet list + volume fan from interior lattice point (0,0,0)
    assert sorted(fs)==sorted([((2,2,-3),2),((7,7,-1),7),((5,-14,2),5),((-14,5,2),5)]),fs
    tot=F(0)
    for (nv,rhs) in fs:
        fp=[p for p in S if dot(nv,p)==rhs]
        assert len(fp)>=3
        f0=(sum(F(p[0]) for p in fp)/len(fp),sum(F(p[1]) for p in fp)/len(fp),sum(F(p[2]) for p in fp)/len(fp))
        import math
        ax=max(range(3),key=lambda i:abs(nv[i])); ot=[i for i in range(3) if i!=ax]
        fx=sum(F(p[ot[0]]) for p in fp)/len(fp); fy=sum(F(p[ot[1]]) for p in fp)/len(fp)
        fp=sorted(fp,key=lambda p:math.atan2(float(F(p[ot[1]])-fy),float(F(p[ot[0]])-fx)))
        for x,y in zip(fp,fp[1:]+fp[:1]):
            tot+=abs(det3(((F(x[0]),F(x[1]),F(x[2])),(F(y[0]),F(y[1]),F(y[2])),f0)))/F(6)
    assert tot==F(19,6),tot
    # width: (-1,0,0) achieves 2; no width-1 functional in certified box
    vals=[-p[0] for p in S]
    assert max(vals)-min(vals)==2
    p0=S[1]; M=None
    import itertools as _it
    for q in _it.combinations(range(7),3):
        Mc=tuple(sub(S[i],p0) for i in q)
        if det3(Mc)!=0: M=Mc; break
    assert det3(M)!=0
    (a,b,c),(d,e,f),(g,h,i)=M
    C=[[(e*i-f*h),-(d*i-f*g),(d*h-e*g)],[-(b*i-c*h),(a*i-c*g),-(a*h-b*g)],[(b*f-c*e),-(a*f-c*d),(a*e-b*d)]]
    Adj=((C[0][0],C[1][0],C[2][0]),(C[0][1],C[1][1],C[2][1]),(C[0][2],C[1][2],C[2][2]))
    D=abs(det3(M)); rs=max(sum(abs(x) for x in r) for r in Adj)
    import math as m
    R=m.ceil(1*rs/D)+1
    best=min(max(dot(u,p) for p in S)-min(dot(u,p) for p in S)
             for u in itertools.product(range(-R,R+1),repeat=3)
             if u!=(0,0,0) and m.gcd(m.gcd(abs(u[0]),abs(u[1])),abs(u[2]))==1)
    assert best==2,(best,R)
    print('VERIFY_OK 29 classes, 15 dps / 14 non-dps; witness vol 19/6 width 2')
if __name__=='__main__': main()
