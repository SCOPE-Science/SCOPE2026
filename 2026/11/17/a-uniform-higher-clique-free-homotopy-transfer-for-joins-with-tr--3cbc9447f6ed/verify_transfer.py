"""Independent finite tests for clique-free join homotopy transfer.
Pure Python 3, integer bit-vector boundary ranks over F_2.
"""
import itertools, math

def matrix_rank(columns):
    pivots={}
    for col in columns:
        v=col
        while v:
            p=v.bit_length()-1
            if p in pivots:v^=pivots[p]
            else:pivots[p]=v;break
    return len(pivots)

def betti_from_faces(faces):
    bylen={}
    for f in faces:
        bylen.setdefault(f.bit_count(),[]).append(f)
    maxsize=max(bylen)
    ranks={}
    # augmented chain C_{-1} includes {empty}, rank d0=1 when vertices exist
    for s in range(1,maxsize+1):
        ids={f:i for i,f in enumerate(bylen.get(s-1,[]))}
        cols=[]
        for f in bylen.get(s,[]):
            mask=0;v=f
            while v:
                b=v&-v;v-=b
                mask^=1<<ids[f^b]
            cols.append(mask)
        ranks[s]=matrix_rank(cols)
    betti={}
    for s in range(0,maxsize+1):
        b=len(bylen.get(s,[]))-ranks.get(s,0)-ranks.get(s+1,0)
        if b:betti[s-1]=b
    return betti

def all_faces_on_graph(n,edges,threshold):
    # Exclusion by t-cliques (graph on n vertices)
    tcliques=[]
    for cc in itertools.combinations(range(n), threshold):
        if all((min(i,j),max(i,j)) in edges for i,j in itertools.combinations(cc,2)):
            tcliques.append(sum(1<<i for i in cc))
    return [u for u in range(1<<n) if all((u & c)!=c for c in tcliques)]

def check(n,edge_mask,s,t):
    edgelist=list(itertools.combinations(range(n),2))
    hedges={e for j,e in enumerate(edgelist) if edge_mask>>j&1}
    if any(all((min(x,y),max(x,y)) in hedges for x,y in itertools.combinations(tri,2)) for tri in itertools.combinations(range(n),3)):
        return None
    joined=set(hedges)
    joined.update(itertools.combinations(range(n,n+s),2))
    joined.update((i,j) for i in range(n) for j in range(n,n+s))
    actual=betti_from_faces(all_faces_on_graph(n+s,joined,t))
    ind=betti_from_faces(all_faces_on_graph(n,hedges,2))
    k=t-2
    predicted={d+k: v*math.comb(s,k) for d,v in ind.items()} if s>=k else {}
    if s>=k+1:predicted[k]=predicted.get(k,0)+math.comb(s,k+1)
    predicted={d:v for d,v in predicted.items() if v}
    return actual,predicted

def main():
    cases=0
    counts={4:0,5:0,6:0,7:0,8:0}
    for n in range(1,5):
        for em in range(1<<(n*(n-1)//2)):
            for s in range(2,6):
                for t in range(4,7):
                    if n+s>9: continue
                    res=check(n,em,s,t)
                    if res is None:continue
                    actual,pred=res
                    cases+=1
                    counts[t]+=1
                    if actual!=pred:
                        raise RuntimeError(f'FAIL n={n}, e={em}, s={s}, t={t}, actual={actual}, predicted={pred}')
    for n in range(1,4):
        for em in range(1 << (n*(n-1)//2)):
            for s in range(5,8):
                for t in (7,8):
                    if n+s>10: continue
                    res=check(n,em,s,t)
                    if res is None:continue
                    actual,pred=res
                    cases+=1
                    counts[t]+=1
                    if actual!=pred:raise RuntimeError(f'HIGH_THRESHOLD_FAIL {n,em,s,t,actual,pred}')
    for (n,edges,s,t) in [
        (6,{(i,(i+1)%6) if i<(i+1)%6 else ((i+1)%6,i) for i in range(6)},3,4),
        (6,{(i,(i+1)%6) if i<(i+1)%6 else ((i+1)%6,i) for i in range(6)},3,5),
        (6,{(i,(i+1)%6) if i<(i+1)%6 else ((i+1)%6,i) for i in range(6)},4,5),
    ]:
        edgelist=list(itertools.combinations(range(n),2))
        em=sum(1<<j for j,e in enumerate(edgelist) if e in edges)
        actual,pred=check(n,em,s,t)
        cases+=1
        counts[t]+=1
        if actual!=pred:raise RuntimeError(f'CYCLE_FAIL {n,s,t,actual,pred}')
    print(f'CLIQUES_JOIN_TRANSFER_FINITE_PASS cases={cases} target_t_ge_5={sum(counts[x] for x in (5,6,7,8))} known_t4_benchmark={counts[4]} coefficient=F2 n<=6')

if __name__=='__main__':main()
