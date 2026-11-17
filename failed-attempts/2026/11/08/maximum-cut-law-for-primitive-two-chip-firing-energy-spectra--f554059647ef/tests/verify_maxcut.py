"""Independent construction and endpoint multiplicity checks for the max-cut mass theorem."""
from random import Random

def fire_step(chips, neighbors):
    fired=[int(chips[i]>=len(neighbors[i])) for i in range(len(chips))]
    return tuple(chips[i]+sum(fired[j] for j in neighbors[i])-len(neighbors[i])*fired[i] for i in range(len(chips)))

def connected(neighbors):
    seen={0};todo=[0]
    while todo:
        for v in neighbors[todo.pop()]:
            if v not in seen:seen.add(v);todo.append(v)
    return len(seen)==len(neighbors)

def check(edges,n):
    N=[[] for _ in range(n)]
    for i,j in edges:N[i].append(j);N[j].append(i)
    assert connected(N)
    E=len(edges)
    cm=[]
    for bits in range(1<<n):
        cut=sum(((bits>>i)&1)!=((bits>>j)&1) for i,j in edges)
        cm.append((cut,bits))
    M=max(x for x,_ in cm)
    maximizing=[bits for c,bits in cm if c==M]
    extreme_states=set()
    for bits in maximizing:
        cross=[sum(((bits>>v)&1)!=((bits>>j)&1) for j in N[v]) for v in range(n)]
        assert min(cross)>=1
        lo=[len(N[v]) if bits>>v&1 else len(N[v])-cross[v] for v in range(n)]
        width=[x-1 for x in cross]
        assert sum(lo)==2*E-M
        assert sum(width)==2*M-n
        extreme_states.add(tuple(lo))
        for target in range(sum(width)+1):
            remain=target; current=list(lo)
            for v,w in enumerate(width):
                k=min(remain,w);current[v]+=k;remain-=k
            assert remain==0
            assert sum(current)==2*E-M+target
            nxt=fire_step(current,N)
            assert nxt!=tuple(current) and fire_step(nxt,N)==tuple(current)
    assert len(extreme_states)==len(maximizing)
    return len(maximizing),M

def main():
    rng=Random(20261105)
    examples=0;witnesses=0
    for n in range(2,12):
        candidates=[]
        candidates.append([(i,i+1) for i in range(n-1)])
        candidates.append([(i,j) for i in range(n) for j in range(i+1,n)])
        for _ in range(16):
            p=rng.randrange(20,81)/100
            edges=[(i,j) for i in range(n) for j in range(i+1,n) if rng.random()<p]
            candidates.append(edges)
        for edges in candidates:
            A=[[] for _ in range(n)]
            for i,j in edges:A[i].append(j);A[j].append(i)
            if not connected(A):continue
            mult,M=check(edges,n)
            witnesses+=mult
            examples+=1
    print(f'CONSTRUCTIVE_OK connected_graphs={examples} maximum_cut_orientations={witnesses}')
if __name__=='__main__':main()
