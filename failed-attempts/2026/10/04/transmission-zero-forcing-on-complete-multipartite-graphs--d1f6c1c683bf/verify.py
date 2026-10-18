from fractions import Fraction
from itertools import combinations, product


def graph(parts):
    part_of=[]
    for p,n in enumerate(parts):
        part_of += [p]*n
    N=len(part_of)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if part_of[u]!=part_of[v]:
                adj[u].add(v); adj[v].add(u)
    return adj


def succeeds(parts, alpha, beta, initial):
    adj=graph(parts)
    N=len(adj)
    weights=[Fraction(0) for _ in range(N)]
    filled=set(initial)
    for v in filled: weights[v]=Fraction(1)
    used=set()  # a filled vertex may transmit at most once total
    while True:
        unfilled=set(range(N))-filled
        contributions={u:Fraction(0) for u in unfilled}
        transmitters=[]
        for v in sorted(filled-used):
            targets=adj[v] & unfilled
            if len(targets)==1:
                u=next(iter(targets))
                contributions[u]+=alpha*weights[v]
                transmitters.append(v)
        used.update(transmitters)
        newly=set()
        for u,inc in contributions.items():
            weights[u]+=inc
            if weights[u] >= beta:
                newly.add(u)
        if not newly:
            return len(filled)==N
        filled.update(newly)


def brute(parts, alpha, beta):
    N=sum(parts)
    for k in range(N+1):
        for S in combinations(range(N),k):
            if succeeds(parts,alpha,beta,S):
                return k
    raise RuntimeError


def formula(parts, alpha, beta):
    parts=sorted(parts)
    N=sum(parts)
    assert len(parts)>=3 and parts[-1]>=2
    qs=[]
    for s in parts[1:]:
        qs.append(min((s-1)*alpha,(N-s-1)*alpha+(s-1)*alpha*alpha))
    Q=max(qs)
    Delta=N-parts[0]
    if beta <= Q:
        return N-2
    if beta <= Delta*alpha:
        return N-1
    return N


def main():
    alphas=[Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1,1)]
    betas=[Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1,1)]
    part_tuples=set()
    for r,sizes in [(3,range(1,4)),(4,range(1,3))]:
        for ps in product(sizes,repeat=r):
            ps=tuple(sorted(ps))
            if ps[-1]>=2:
                part_tuples.add(ps)
    cases=0
    for parts in sorted(part_tuples):
        for a in alphas:
            for b in betas:
                got=brute(parts,a,b)
                want=formula(parts,a,b)
                if got!=want:
                    raise AssertionError((parts,a,b,got,want))
                cases+=1
    # direct checks of the pair threshold formula on an asymmetric family
    for parts in [(1,2,4),(2,3,4),(1,1,3,4)]:
        N=sum(parts)
        offsets=[]
        k=0
        vertices=[]
        for i,n in enumerate(parts):
            vertices.append(list(range(k,k+n))); k+=n
        for i in range(len(parts)):
            for j in range(i+1,len(parts)):
                x=vertices[i][0]; y=vertices[j][0]
                s=max(parts[i],parts[j])
                for a in alphas:
                    threshold=min((s-1)*a,(N-s-1)*a+(s-1)*a*a)
                    for b in betas:
                        S=[v for v in range(N) if v not in (x,y)]
                        if succeeds(parts,a,b,S)!=(b<=threshold):
                            raise AssertionError(('pair',parts,i,j,a,b,threshold))
                        cases+=1
    print(f'ALL CHECKS PASSED; exact_fraction_cases={cases}; graph_profiles={len(part_tuples)}')

if __name__=='__main__': main()
