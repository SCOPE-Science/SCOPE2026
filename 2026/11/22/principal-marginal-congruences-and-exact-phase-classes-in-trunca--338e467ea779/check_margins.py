"""Finite exact test for phase margins and congruence classes of partial monomial maps.
No external dependencies. Run: python check_margins.py
"""
from itertools import combinations
from math import comb

ZERO = ((), (), 0)

def elements(m, n):
    out=[ZERO]
    for r in range(1,min(m,n)+1):
        sets=list(combinations(range(m),r))
        for D in sets:
            for R in sets:
                for e in range(n):out.append((D,R,e))
    return out

def multiply(a,b,n):
    if a==ZERO or b==ZERO:return ZERO
    da,ra,ea=a; db,rb,eb=b
    am=dict(zip(da,ra)); bm=dict(zip(db,rb))
    surv=[(x,am[y]) for x,y in bm.items() if y in am]
    if not surv:return ZERO
    D=tuple(x for x,y in surv); R=tuple(y for x,y in surv)
    e=(ea*(bm[D[0]]==da[0]) + eb*(D[0]==db[0]))%n
    # nonfirst coefficients must be zero by increasing-map property
    assert all((ea*(bm[x]==da[0])+eb*(x==db[0]))%n==0 for x,_ in surv[1:])
    return (D,R,e)

def inverse(a,n):
    if a==ZERO:return ZERO
    D,R,e=a
    return R,D,(-e)%n

def power(a,n):
    x=a
    for _ in range(1,n):x=multiply(x,a,n)
    return x

def expected_equiv(a,b,m,n):
    if a==ZERO or b==ZERO:return a==b
    D,R,e=a; D2,R2,e2=b
    if D!=D2 or R!=R2:return False
    if e==e2 or len(D)<n:return True
    return D[0]==0 and D[-1]==m-1 and R[0]==0 and R[-1]==m-1

def expected_marginal(a,m,n):
    if a==ZERO:return True
    D,R,e=a
    if D!=R:return False
    return e==0 or len(D)<n or (D[0]==0 and D[-1]==m-1)

def test(m,n):
    S=elements(m,n)
    P={(x,y):power(multiply(x,y,n),n) for x in S for y in S}
    support_groups={}
    for a in S: support_groups.setdefault(a[:2],[]).append(a)
    num_relation=0; num_marginal=0
    for a in S:
        if a==ZERO:
            ida=ZERO
        else:
            ida=(a[0],a[0],0)
        marginal=all(P[a,x]==P[ida,x] and P[x,a]==P[x,ida] for x in S)
        assert marginal==expected_marginal(a,m,n),(m,n,'margin',a,marginal)
        num_marginal+=marginal
    for A in support_groups.values():
        for a in A:
            for b in A:
                eq=all(P[a,x]==P[b,x] and P[x,a]==P[x,b] for x in S)
                assert eq==expected_equiv(a,b,m,n),(m,n,'same support',a,b,eq)
                num_relation+=eq
    # Distinct supports separated by a rank-one test.
    for i,a in enumerate(S):
        for b in S[i+1:]:
            if a[:2]!=b[:2]:
                found=False
                for x in elements(m,n):
                    if len(x[0])==1 and (P[a,x]!=P[b,x] or P[x,a]!=P[x,b]):
                        found=True;break
                assert found,(m,n,'non-separated',a,b)
    # All support-matched pairs lie in generated congruence: rank<n directly,
    # full-rank by conjugating a marginal pair based on one endpoint-supported I.
    if m>n:
        I=tuple([0]+list(range(1,n-1))+[m-1])
        assert len(I)==n
        for K in combinations(range(m),n):
            K=tuple(K)
            u=(I,I,1); e=(I,I,0)
            assert expected_marginal(u,m,n)
            x=(I,K,0)
            assert multiply(multiply(x,u,n),inverse(x,n),n)==(K,K,1)
            assert multiply(multiply(x,e,n),inverse(x,n),n)==(K,K,0)
    t=comb(m,n) if m>=n else 0
    h=comb(m-2,n-2) if m>=n else 0
    # exact classes of ~: all supports rank<n one class; eligible rank-n
    # supports one class, ineligible rank-n supports n singleton classes.
    c=sum(comb(m,r)**2 for r in range(min(m,n)+1))
    eq_classes=c+(n-1)*(t*t-h*h)
    found_eq_classes=1
    for key,A in support_groups.items():
        if key==((),()):continue
        if all(expected_equiv(a,A[0],m,n) for a in A):found_eq_classes+=1
        else:found_eq_classes+=len(A)
    assert eq_classes==found_eq_classes
    return (m,n,len(S),num_marginal,c,eq_classes)

if __name__=='__main__':
    for m,n in [(1,2),(2,2),(3,2),(3,3),(4,2),(4,3),(5,2)]:
        print('TEST',*test(m,n))
    print('VERIFY_OK')


def principal_closure_test(m,n):
    from collections import deque
    S=elements(m,n)
    idx={a:i for i,a in enumerate(S)}
    parent=list(range(len(S)))
    def root(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    queue=deque()
    def join(a,b):
        ra,rb=root(a),root(b)
        if ra==rb:return
        parent[ra]=rb
        queue.append((a,b))
    if m>n:
        I=tuple([0]+list(range(1,n-1))+[m-1])
    else:
        I=tuple(range(m))
    a=(I,I,1)
    assert expected_marginal(a,m,n)
    join(idx[a],idx[(I,I,0)])
    while queue:
        a,b=queue.popleft()
        A,B=S[a],S[b]
        join(idx[inverse(A,n)],idx[inverse(B,n)])
        for x in S:
            join(idx[multiply(A,x,n)],idx[multiply(B,x,n)])
            join(idx[multiply(x,A,n)],idx[multiply(x,B,n)])
    roots={root(i) for i in range(len(S))}
    support_count=1+sum(comb(m,r)**2 for r in range(1,min(n,m)+1))
    assert len(roots)==support_count,(m,n,len(roots),support_count)
    for aa in S:
        for bb in S:
            assert (root(idx[aa])==root(idx[bb]))==(aa[:2]==bb[:2])
    return m,n,len(S),len(roots)

if __name__=='__main__':
    for m,n in [(1,2),(2,2),(3,2),(3,3),(4,2),(4,3),(5,2)]:
        print('PRINCIPAL',*principal_closure_test(m,n))
    print('PRINCIPAL_OK')
