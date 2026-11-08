"""Finite-field checks of the graph orthogonality state-sum motivic identity.
No finite check is offered as proof of the unrestricted identity.
"""
from itertools import combinations,product
from math import comb


def bip_data(vertices, edges):
    support=set(vertices)
    adj={v:set() for v in support}
    for a,b in edges:
        if a in support and b in support:
            adj[a].add(b);adj[b].add(a)
    seen=set(); bip=0; nonbip=0
    for root in vertices:
        if root in seen: continue
        color={root:0};stack=[root];seen.add(root); good=True
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w not in color:
                    color[w]=color[v]^1;seen.add(w);stack.append(w)
                elif color[w]==color[v]:good=False
        if good:bip+=1
        else:nonbip+=1
    return bip, nonbip


def state_sum(n,edges,q,eps):
    out=0
    for mask in range(1<<n):
        s=[i for i in range(n) if mask>>i&1]
        b,c=bip_data(s,edges)
        out+=(q-1)**len(s)*(q+1)**b*(1+eps)**c
    return out


def direct(n,edges,q):
    vs=list(product(range(q), repeat=2))
    # DFS enumerate all q^(2n) tuples with early-pruned orthogonality.
    def rec(i,prev):
        if i==n:return 1
        ans=0
        for v in vs:
            if all((v[0]*prev[j][0]+v[1]*prev[j][1])%q==0 for j in range(i) if (j,i) in edges):
                ans+=rec(i+1,prev+[v])
        return ans
    return rec(0,[])


def main():
    nchecks=0
    for q in (3,5,7):
        eps=1 if q%4==1 else -1
        for n in (1,2,3,4):
            pairs=list(combinations(range(n),2))
            # all labeled graphs through n=3, and representative graphs through n=4.
            if n<=3: masks=range(1<<len(pairs))
            else:masks=(0,1,3,7,15,21,31,63)
            for mask in masks:
                e={p for j,p in enumerate(pairs) if mask>>j&1}
                a=direct(n,e,q)
                b=state_sum(n,e,q,eps)
                assert a==b,(n,q,mask,a,b)
                nchecks+=1
    # Exact complete-graph specialization for 3 <= h <= 40 and both signs.
    spec_checks=0
    for h in range(3,41):
        for q in (3,5,7,9,11):
            for eps in (-1,1):
                graph=1+h*(q*q-1)+comb(h,2)*(q*q-1)*(q-1)
                graph+=(1+eps)*sum(comb(h,t)*(q-1)**t for t in range(3,h+1))
                A=q**h+h*q*(q-1)+comb(h,2)*q*(q-1)**2
                C=q**h-1-h*(q-1)-comb(h,2)*(q-1)**2
                assert graph==A+eps*C
                spec_checks+=1
    print('DIRECT_LABELED_GRAPH_ENUMERATIONS_OK',nchecks)
    print('COMPLETE_GRAPH_SPECIALIZATION_OK',spec_checks)
    print('UNRESTRICTED_RESULT_FROM_PROJECTIVE_LINE_SUPPORT_STRATIFICATION')

if __name__=='__main__':main()
