#!/usr/bin/env python3
"""Independent checks for four-edge geodesic avoidance on spiders."""
from itertools import product
from math import comb
from collections import Counter, deque


def tree(arms):
    adj=[[]]
    edges=[]
    for length in arms:
        prev=0
        for _ in range(length):
            u=len(adj); adj.append([])
            eid=len(edges); edges.append((prev,u))
            adj[prev].append((u,eid)); adj[u].append((prev,eid)); prev=u
    return adj,edges


def path_masks(adj):
    masks=[]
    for start in range(len(adj)):
        seen={start:(-1,-1)}; q=deque([start])
        while q:
            x=q.popleft()
            for y,e in adj[x]:
                if y not in seen:
                    seen[y]=(x,e); q.append(y)
        for end in range(start+1,len(adj)):
            z=end; mask=0
            while z!=start:
                p,e=seen[z]; mask|=1<<e; z=p
            masks.append(mask)
    return masks


def expected(arms):
    d=len(arms); A=[1]
    for a in arms:
        B=[0]*(len(A)+1)
        for i,v in enumerate(A): B[i]+=v; B[i+1]+=a*v
        A=B
    maxk=max(sum(arms),d+1,3)
    face=A+[0]*(maxk+1-len(A))
    def add(k,v): face[k]+=v
    for i,a in enumerate(arms):
        if a>=2:
            Q=[1]
            for j,b in enumerate(arms):
                if j==i:continue
                R=[0]*(len(Q)+1)
                for t,v in enumerate(Q):R[t]+=v; R[t+1]+=b*v
                Q=R
            for t,v in enumerate(Q):add(t+2,comb(a,2)*v)
        if a>=3:add(3,comb(a,3))
    facet=[0]*(maxk+1)
    if max(arms)==1:facet[d]=1
    else:
        facet[d+1]=sum(comb(a,2)*__import__('math').prod(arms[:i]+arms[i+1:]) for i,a in enumerate(arms))
        facet[3]+=sum(comb(a,3) for a in arms)
    return face,facet


def inspect(arms):
    adj,edges=tree(arms); paths=path_masks(adj); n=len(edges)
    valid=[False]*(1<<n); face=Counter(); facet=Counter()
    for mask in range(1<<n):
        # independent of branch-count derivation: test every unique vertex geodesic
        good=all((mask & pm).bit_count()<=3 for pm in paths)
        valid[mask]=good
        if good:face[mask.bit_count()]+=1
    for mask,good in enumerate(valid):
        if good and all(not valid[mask | (1<<i)] for i in range(n) if not mask>>i&1):
            facet[mask.bit_count()]+=1
    exp_f,exp_m=expected(list(arms))
    assert all(face[k]==exp_f[k] for k in range(len(exp_f))),(arms,face,exp_f)
    assert all(facet[k]==exp_m[k] for k in range(len(exp_m))),(arms,facet,exp_m)
    return valid


def rank_mod(columns,p):
    # Sparse column vectors over finite field, indexed by row
    piv={}; r=0
    for c0 in columns:
        c=dict(c0)
        while c:
            k=max(c)
            if k not in piv:
                inv=pow(c[k],-1,p)
                piv[k]={i:(v*inv)%p for i,v in c.items()}
                r+=1;break
            x=c[k]
            for i,v in piv[k].items():
                value=(c.get(i,0)-x*v)%p
                if value:c[i]=value
                else:c.pop(i,None)
    return r


def betti(arms,p):
    n=sum(arms); good=inspect(arms)
    faces={k:[] for k in range(n+1)}
    for mask in range(1,1<<n):
        if good[mask]:faces[mask.bit_count()-1].append(mask)
    dims=[k for k in range(n+1) if faces[k]]
    out={}; ranks={}
    for k in dims:
        rowind={m:i for i,m in enumerate(faces[k-1])} if k else {}
        columns=[]
        for mask in faces[k]:
            if k==0:columns.append({});continue
            v=[i for i in range(n) if mask>>i&1]
            columns.append({rowind[mask^(1<<i)]: (1 if j%2==0 else p-1) for j,i in enumerate(v)})
        boundary_rank=rank_mod(columns,p)
        ranks[k]=boundary_rank
    for k in dims:
        out[k]=len(faces[k])-ranks[k]-ranks.get(k+1,0)
    # remove the ordinary connected H_0 generator
    out[0]-=1
    return {k:v for k,v in out.items() if v}



def oriented_top_cell(d,i):
    """Top relative chain for the i-th filled-arm ball, boundary the shared sphere."""
    out={}
    for states in product((0,1),repeat=d-1):
        vertices=[]; sign=(-1)**i
        t=iter(states)
        for j in range(d):
            if j==i:vertices.extend((2*j,2*j+1))
            else:
                state=next(t);vertices.append(2*j+state)
                if state:sign=-sign
        out[tuple(vertices)]=sign
    return out


def permuted_chain(chain,d,perm):
    result={}
    for face,coeff in chain.items():
        new=[2*perm[v//2]+v%2 for v in face]
        inversions=sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
        key=tuple(sorted(new))
        result[key]=result.get(key,0)+coeff*((-1)**inversions)
    return result


def check_symmetry(d):
    cells=[oriented_top_cell(d,i) for i in range(d)]
    for t in range(d-1):
        perm=list(range(d));perm[t],perm[t+1]=perm[t+1],perm[t]
        for i in range(d):
            lhs=permuted_chain(cells[i],d,perm)
            rhs={face:-c for face,c in cells[perm[i]].items()}
            assert lhs==rhs,(d,t,i,'signed action mismatch')

def main():
    cases=[]
    for d in range(2,6):
        for a in product(range(1,5),repeat=d):
            if sum(a)<=9 and tuple(sorted(a))==a:cases.append(a)
    for a in cases:inspect(a)
    for d in range(2,6):
        check_symmetry(d)
        a=(2,)*d
        for p in (2,3,101):
            got=betti(a,p)
            assert got=={d:d-1},(a,p,got)
    print('VERIFY_OK', 'spider_cases='+str(len(cases)), 'homology_F2_F3_F101_and_integral_signed_permutation_d=2..5')

if __name__=='__main__':main()
