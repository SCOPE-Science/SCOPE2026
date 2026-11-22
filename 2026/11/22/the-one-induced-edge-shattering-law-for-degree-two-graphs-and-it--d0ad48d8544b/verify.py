from itertools import combinations,product
from math import comb

def all_concepts(n,edges):
    masks=[]
    for mask in range(1<<n):
        k=sum(1 for u,v in edges if (mask>>u)&1 and (mask>>v)&1)
        if k==1:masks.append(mask)
    return masks

def shattered_by_brute(concepts,S):
    trace={tuple((x>>i)&1 for i in S) for x in concepts}
    return len(trace)==(1<<len(S))

def law(n,edges,S):
    ss=set(S)
    return (sum(u in ss and v in ss for u,v in edges)<=1 and sum(u not in ss and v not in ss for u,v in edges)>=1)


def brute_graph():
    trials=0;graph_cases=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for bits in range(1<<len(pairs)):
            edges=[pairs[j] for j in range(len(pairs)) if (bits>>j)&1]
            if any(sum(v==i or u==i for u,v in edges)>2 for i in range(n)):continue
            graph_cases+=1
            concepts=all_concepts(n,edges)
            for s in range(1<<n):
                S=[i for i in range(n) if (s>>i)&1]
                assert shattered_by_brute(concepts,S)==law(n,edges,S),(n,edges,S)
                trials+=1
    return graph_cases,trials

def gf_counts(n):
    # Count weighted supports with at most one adjacent 11, minus those avoiding adjacent 00.
    def count(forbid00):
        st={(None,0,0):1}  # last bit, number of adjacent-11, number of chosen positions
        for _ in range(n):
            nxt={}
            for (last,r,k),v in st.items():
                for b in (0,1):
                    if forbid00 and last==0 and b==0:continue
                    nr=r+(last==1 and b==1)
                    if nr>1:continue
                    key=(b,nr,k+b)
                    nxt[key]=nxt.get(key,0)+v
            st=nxt
        out=[0]*(n+1)
        for (_,_,k),v in st.items():out[k]+=v
        return out
    a=count(False);b=count(True)
    return [x-y for x,y in zip(a,b)]

def main():
    ng,ns=brute_graph()
    assert shattered_by_brute(all_concepts(4,[(0,2),(0,3),(1,2),(1,3),(2,3)]),(0,1))==False
    assert law(4,[(0,2),(0,3),(1,2),(1,3),(2,3)],(0,1))==True
    ncases=0
    for n in range(2,13):
        edges=[(i,i+1) for i in range(n-1)]
        concepts=all_concepts(n,edges)
        coeff=[0]*(n+1)
        for mask in range(1<<n):
            S=[i for i in range(n) if (mask>>i)&1]
            ok=shattered_by_brute(concepts,S)
            assert ok==law(n,edges,S), (n,S)
            if ok:coeff[len(S)]+=1
            ncases+=1
        assert coeff==gf_counts(n),(n,coeff,gf_counts(n))
        expected=0 if n==2 else (1 if n==3 else (n+1)//2)
        assert max(i for i,x in enumerate(coeff) if x)==expected,(n,coeff)
        for k in range(n+1):
            if n>=2*k+2 and k>=1:
                v=comb(n-k+1,k)+(k-1)*comb(n-k+1,k-1)
                assert coeff[k]==v,(n,k,coeff[k],v)
    print(f'SINGLE_INDUCED_EDGE_SHATTERING_PASS graphs={ng} graph_supports={ns} path_supports={ncases}; verified n<=12')

if __name__=='__main__':main()
