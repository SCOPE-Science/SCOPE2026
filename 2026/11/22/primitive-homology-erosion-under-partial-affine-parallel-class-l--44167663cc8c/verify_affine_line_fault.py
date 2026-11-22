#!/usr/bin/env python3
"""Independent finite checks of affine incidence Rips radius-two line erasures.
Standard Python 3, no third-party dependencies.
"""
from collections import deque, defaultdict
from itertools import combinations


def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4:
        return a*b%q
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a&4: a^=7 # GF(4), t^2+t+1
    return z

def build(q,erasures=0):
    pts=list((a,b) for a in range(q) for b in range(q))
    lines=[]
    for m in range(q):
        for c in range(q):
            lines.append(('slope',m,c))
    for c in range(q):
        lines.append(('vertical',c))
    for c in range(erasures):
        lines.remove(('vertical',c))
    nv=len(pts)+len(lines)
    adj=[set() for _ in range(nv)]
    for i,(a,b) in enumerate(pts):
        for j,ls in enumerate(lines,len(pts)):
            kind=ls[0]
            hit=(b==add(mul(ls[1],a,q),ls[2],q)) if kind=='slope' else (a==ls[1])
            if hit:
                adj[i].add(j)
                adj[j].add(i)
    dist=[]
    for i in range(nv):
        d=[1000]*nv; d[i]=0; Q=deque([i])
        while Q:
            v=Q.popleft()
            for w in adj[v]:
                if d[w]==1000:
                    d[w]=d[v]+1; Q.append(w)
        assert max(d)<1000
        dist.append(d)
    return pts,lines,adj,dist

def clique_faces(dist):
    n=len(dist)
    nbr=[sum(1<<j for j in range(i+1,n) if dist[i][j]<=2) for i in range(n)]
    faces=defaultdict(list)
    def extend(t,candidates):
        if t: faces[len(t)-1].append(t)
        while candidates:
            bit=candidates&(-candidates)
            i=bit.bit_length()-1
            candidates^=bit
            extend(t+(i,),candidates & nbr[i])
    extend((),(1<<n)-1)
    return faces

def rank2(columns):
    piv={}
    for col in columns:
        x=col
        while x:
            bit=x.bit_length()-1
            if bit in piv: x^=piv[bit]
            else: piv[bit]=x; break
    return len(piv)

def betti(faces):
    ranks={}; fvec={d:len(xs) for d,xs in faces.items()}
    for k in range(1,max(fvec)+1):
        idx={s:i for i,s in enumerate(faces[k-1])}
        cols=[]
        for cell in faces[k]:
            mask=0
            for j in range(len(cell)):
                face=cell[:j]+cell[j+1:]
                mask^=1<<idx[face]
            cols.append(mask)
        ranks[k]=rank2(cols)
    return {k:v-ranks.get(k,0)-ranks.get(k+1,0) for k,v in fvec.items()},ranks

def basis_add(v,piv):
    while v:
        h=v.bit_length()-1
        if h not in piv:
            piv[h]=v
            return True
        v^=piv[h]
    return False

def boundary_columns(faces,k):
    if k==0: return [0]*len(faces[0])
    idx={f:i for i,f in enumerate(faces[k-1])}
    return [sum(1<<idx[f[:j]+f[j+1:]] for j in range(len(f)))
            for f in faces[k]]

def kernel_basis(cols):
    piv={}; pre={}; ker=[]
    for j,a in enumerate(cols):
        x=a; combo=1<<j
        while x:
            h=x.bit_length()-1
            if h not in piv:
                piv[h]=x; pre[h]=combo; break
            x^=piv[h]; combo^=pre[h]
        else:
            ker.append(combo)
    return ker

def homology_inclusion(q,s,k):
    pts,ls,_,d=build(q,s)
    tpts,tls,_,td=build(q,s-1)
    a=clique_faces(d); b=clique_faces(td)
    old={f:i for i,f in enumerate(b.get(k,[]))}
    verts=list(range(len(pts)))+[len(pts)+tls.index(x) for x in ls]
    src=kernel_basis(boundary_columns(a,k))
    piv={}
    for col in boundary_columns(b,k+1): basis_add(col,piv)
    base=len(piv)
    for z in src:
        col=0
        while z:
            bit=z&-z
            j=bit.bit_length()-1
            z^=bit
            f=a[k][j]
            mapped=tuple(verts[x] for x in f)
            col^=1<<old[mapped]
        basis_add(col,piv)
    return len(piv)-base

def verify(q,erasures,exhaustive):
    s=erasures
    pts,lines,adj,d=build(q,s)
    P=len(pts); L=len(lines); E=sum(len(x) for x in adj)//2
    assert (P,L,E)==(q*q,q*(q+1)-s,q*q*(q+1)-s*q)
    for i,(a,b) in enumerate(pts):
        for j,(c,e) in enumerate(pts[:i]):
            assert (d[i][j]>2)==(a==c and a<s)
    for i,u in enumerate(lines):
        for j,v in enumerate(lines[:i]):
            parallel=(u[0]==v[0] and (u[0]=='vertical' or u[1]==v[1]))
            assert (d[P+i][P+j]>2)==parallel
    for i in range(P):
        for j in range(P,P+L):
            assert (d[i][j]<=2)==(j in adj[i])
    beta2=E-P-L+1
    assert beta2==(q-1)**2*(q+1)-s*(q-1)
    if s<q:
        # A is conical; one retained class may be a singleton when s=q-1.
        predicted={2:beta2}
        beta_top=(q-s-1)*(q-1)**q
        if beta_top: predicted[q]=predicted.get(q,0)+beta_top
    else:
        # Both pure-shore complexes are a q-fold join of q-point sets.
        predicted={2:beta2}
        beta_top=2*(q-1)**q
        predicted[q-1]=predicted.get(q-1,0)+beta_top
    if exhaustive:
        f=clique_faces(d)
        h,r=betti(f)
        actual={k:v for k,v in h.items() if k>=1 and v}
        assert actual==predicted,(q,s,actual,predicted)
        assert h[0]==1
        print(f'q={q} removed={s}: vertices={P+L}, fvector={[len(f[k]) for k in range(max(f)+1)]}, Hpositive={actual}, OK')
    else:
        print(f'q={q} removed={s}: vertices={P+L}, edges={E}, distances OK, predicted Hpositive={predicted}')
    if s:
        _,prev_lines,prev_adj,prev_d=build(q,s-1)
        kept=list(range(P))+[P+j for j,ls in enumerate(prev_lines) if ls in lines]
        assert all((d[i][j]<=2)<= (prev_d[kept[i]][kept[j]]<=2) for i in range(len(kept)) for j in range(len(kept)))
        assert sum(len(x) for x in prev_adj)//2-E==q
        assert (sum(len(x) for x in prev_adj)//2-(P+len(prev_lines))+1)-beta2==q-1
    print(f'q={q} removed={s}: inclusion and combinatorial invariants OK')

if __name__=='__main__':
    for s in range(3): verify(2,s,True) if s<=1 else None
    for s in range(4): verify(3,s,True)
    for s in range(5): verify(4,s,False)
    for s in range(1,4):
        for k in (2,3):
            r=homology_inclusion(3,s,k)
            expected=({1:14,2:12,3:10}[s] if k==2 else {1:8,2:0,3:0}[s])
            assert r==expected,(s,k,r,expected)
            print(f'q=3 induced map removed={s} -> removed={s-1}, H{k} image rank={r}, OK')
    print('VERIFY_OK')
