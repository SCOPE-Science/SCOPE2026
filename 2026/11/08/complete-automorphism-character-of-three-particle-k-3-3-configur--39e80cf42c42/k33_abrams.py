"""Independent subdivided Abrams cell complex for unordered three-point configurations on K3,3."""
from itertools import combinations,permutations
from collections import defaultdict
from math import comb
from functools import reduce
V=list(range(6))
ORIG=[(a,b) for a in range(3) for b in range(3,6)]
EDGES=sorted(tuple(sorted(edge)) for i,(a,b) in enumerate(ORIG) for edge in ((a,6+i),(6+i,b)))
EDGEINDEX={e:i for i,e in enumerate(EDGES)}

def cells():
    C=[[] for _ in range(4)]
    for d in range(4):
        for ed in combinations(range(len(EDGES)),d):
            used=[v for ei in ed for v in EDGES[ei]]
            if len(set(used))<2*d:continue
            for vs in combinations((v for v in range(15) if v not in used),3-d):
                C[d].append((vs,ed))
    return C

def boundaries(C):
    col=[]
    for d in (1,2,3):
        idx={cell:i for i,cell in enumerate(C[d-1])}
        matrix=[]
        for vs,ed in C[d]:
            v={}
            for i,e in enumerate(ed):
                a,b=EDGES[e]
                for x,c in ((a,-1), (b,1)):
                    tgt=(tuple(sorted(vs+(x,))),ed[:i]+ed[i+1:]);r=idx[tgt]
                    v[r]=v.get(r,0)+c*(-1)**i
            matrix.append({r:x for r,x in v.items() if x})
        col.append(matrix)
    return col

def rank_mod(cols,p):
    piv={}
    for cc in cols:
        c={i:a%p for i,a in cc.items() if a%p}
        while c:
            r=min(c)
            if r not in piv:
                inv=pow(c[r],-1,p);piv[r]={i:a*inv%p for i,a in c.items()};break
            a=c[r]
            for i,v in piv[r].items():
                x=(c.get(i,0)-a*v)%p
                if x:c[i]=x
                else:c.pop(i,None)
    return len(piv)

def chain_comp_zero(A,B):
    for col in B:
        acc=defaultdict(int)
        for idx,v in col.items():
            for r,w in A[idx].items():acc[r]+=v*w
        assert not any(acc.values())

def automorphisms():
    out=[]
    for sw in (False,True):
        for p in permutations(range(3)):
            for q in permutations(range(3)):
                g0=[0]*6
                if not sw:
                    for a in range(3):g0[a]=p[a];g0[a+3]=q[a]+3
                else:
                    for a in range(3):g0[a]=p[a]+3;g0[a+3]=q[a]
                mid={tuple(sorted(edge)):i for i,edge in enumerate(ORIG)}
                eper=[mid[tuple(sorted((g0[a],g0[b])))] for a,b in ORIG]
                g=tuple(g0)+(tuple(6+j for j in eper))
                out.append(g)
    return out

def sign_perm(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def chain_trace(C,g):
    result=[]
    for d in range(4):
        t=0
        for vs,ed in C[d]:
            if tuple(sorted(g[v] for v in vs))!=vs:continue
            x=[];sg=1
            for e in ed:
                a,b=EDGES[e];u,v=g[a],g[b]
                if u>v:u,v=v,u;sg=-sg
                x.append(EDGEINDEX[(u,v)])
            if tuple(sorted(x))==ed:t+=sg*sign_perm(x)
        result.append(t)
    return result

if __name__=='__main__':
    C=cells();print('cube cell counts',[len(c) for c in C],flush=True)
    B=boundaries(C)
    chain_comp_zero(B[0],B[1]);chain_comp_zero(B[1],B[2]);print('boundary square zero',flush=True)
    for p in (2,3,101):
        R=[0]+[rank_mod(m,p) for m in B]+[0]
        print('field',p,'boundary ranks',R,'betti',[len(C[i])-R[i]-R[i+1] for i in range(4)],flush=True)
    from k33_sym import AUT
    from k33_classes import chi
    for gi,g in enumerate(automorphisms()):
        tc=chain_trace(C,g)
        L=sum((-1)**j*tc[j] for j in range(4))
        L2=1-chi[gi][1]+chi[gi][2]
        assert L==L2,(gi,L,L2)
    print('independent Lefschetz all 72 PASS')
