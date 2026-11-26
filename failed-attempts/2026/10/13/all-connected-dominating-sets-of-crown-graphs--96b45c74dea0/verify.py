from itertools import combinations
from math import comb


def graph(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                u=i; v=n+j
                adj[u].add(v); adj[v].add(u)
    return adj

def is_dom(adj,S):
    S=set(S)
    return all(v in S or (adj[v] & S) for v in range(len(adj)))

def is_conn(adj,S):
    S=set(S)
    if not S: return False
    seen={next(iter(S))}; stack=list(seen)
    while stack:
        u=stack.pop()
        for v in adj[u] & S:
            if v not in seen:
                seen.add(v); stack.append(v)
    return seen==S

def criterion(n,S):
    S=set(S)
    P={i for i in range(n) if i in S}
    Q={j for j in range(n) if n+j in S}
    return len(P)>=2 and len(Q)>=2 and not (len(P)==len(Q)==2 and P==Q)

def verify():
    subset_checks=criterion_checks=poly_checks=minimal_checks=0
    for n in range(3,10):
        adj=graph(n); N=2*n
        coeff=[0]*(N+1); mins=[]; minimal=[]
        for mask in range(1<<N):
            S={v for v in range(N) if mask>>v &1}
            actual=is_dom(adj,S) and is_conn(adj,S)
            pred=criterion(n,S)
            subset_checks+=1; criterion_checks+=1
            if actual!=pred:
                raise AssertionError((n,S,actual,pred))
            if actual:
                coeff[len(S)]+=1
                # inclusion-minimal connected dominating
                if all(not (is_dom(adj,S-{v}) and is_conn(adj,S-{v})) for v in S):
                    minimal.append(S)
        # predicted coeff
        predc=[0]*(N+1)
        for p in range(2,n+1):
            for q in range(2,n+1):
                predc[p+q]+=comb(n,p)*comb(n,q)
        predc[4]-=comb(n,2)
        if coeff!=predc: raise AssertionError(('poly',n,coeff,predc))
        poly_checks += N+1
        nz=[k for k,c in enumerate(coeff) if c]
        if nz[0]!=4: raise AssertionError(('gamma',n,nz[0]))
        if coeff[4] != comb(n,2)*(comb(n,2)-1):
            raise AssertionError(('bases',n,coeff[4]))
        # minimal sets are exactly all size-4 connected dominating sets
        if any(len(S)!=4 for S in minimal) or len(minimal)!=coeff[4]:
            raise AssertionError(('minimal',n,len(minimal),coeff[4],[len(s) for s in minimal[:10]]))
        minimal_checks += len(minimal)+2
        # total count
        total=sum(coeff)
        expected=(2**n-n-1)**2-comb(n,2)
        if total!=expected: raise AssertionError(('total',n,total,expected))
    print(f'VERIFY_OK n_range=3..9 subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={poly_checks} minimal_checks={minimal_checks} max_order=18')
if __name__=='__main__': verify()
