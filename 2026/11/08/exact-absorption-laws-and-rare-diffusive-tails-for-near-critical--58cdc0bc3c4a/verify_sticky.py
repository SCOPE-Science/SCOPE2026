"""Exact-rational verification for a near-critical sticky random walk.

Run: python3 verify_sticky.py. Uses only the Python 3 standard library.
The finite checks complement, and do not replace, the analytic proofs.
"""
from collections import Counter, deque
from fractions import Fraction


def transition(state):
    """The full many-player chain, not the derived two-state reduction."""
    r = len(state)
    if r == 1:
        return {state: Fraction(1)}
    counts = Counter()
    for winner in range(r):
        nxt = tuple(sorted(x + (r - 1 if i == winner else -1)
                           for i, x in enumerate(state)))
        nxt = tuple(x for x in nxt if x > 0)
        counts[nxt] += 1
    return {v: Fraction(c, r) for v, c in counts.items()}


def survival_chain(m, k, horizon):
    current = {tuple(sorted([1]*(m-k) + [2]*k)): Fraction(1)}
    values = []
    for t in range(horizon+1):
        values.append(sum((p for s,p in current.items() if len(s)>1), Fraction(0)))
        following = {}
        for s,p in current.items():
            for v,q in transition(s).items():
                following[v] = following.get(v, Fraction(0)) + p*q
        current = following
    return values


def ruin_survival(N, a, horizon):
    if a == 0 or a == N:
        return [Fraction(0)]*(horizon+1)
    states = {a: Fraction(1)}
    result = []
    for t in range(horizon+1):
        result.append(sum(states.values(), Fraction(0)))
        new = {}
        for x,p in states.items():
            for y in (x-1, x+1):
                if 0 < y < N:
                    new[y] = new.get(y, Fraction(0)) + p/2
        states = new
    return result


def predicted_survival(m, k, horizon):
    if k == 0:
        return [Fraction(1)] + [Fraction(0)]*horizon
    N = m+k
    a = ruin_survival(N,k,max(0,horizon-2))
    b = ruin_survival(N,k+1,max(0,horizon-2)) if k<m else None
    result=[]
    for t in range(horizon+1):
        if t==0:
            result.append(Fraction(1))
        elif t==1:
            result.append(Fraction(1) if k>=2 else Fraction(m-1,m))
        else:
            value=Fraction(k-1,m)*a[t-2]
            if k<m:
                value+=Fraction(k*(m-k),m*(k+1))*b[t-2]
            result.append(value)
    return result


def reach(m,k):
    start=tuple(sorted([1]*(m-k)+[2]*k))
    states={start};pending=deque([start])
    while pending:
        state=pending.popleft()
        if len(state)==1:
            continue
        for nxt in transition(state):
            if len(nxt)>1 and nxt not in states:
                states.add(nxt);pending.append(nxt)
    return start, sorted(s for s in states if len(s)>1)


def solve(a,b):
    """Exact Gaussian elimination with pivot search (full-rank systems only)."""
    n=len(b)
    mat=[[Fraction(x) for x in row]+[Fraction(b[i])]
         for i,row in enumerate(a)]
    for j in range(n):
        r=next((i for i in range(j,n) if mat[i][j]),None)
        assert r is not None, ('singular',j)
        mat[j],mat[r]=mat[r],mat[j]
        p=mat[j][j]
        for l in range(j,n+1):
            mat[j][l]/=p
        for i in range(n):
            if i==j or not mat[i][j]:continue
            factor=mat[i][j]
            for l in range(j,n+1):
                mat[i][l]-=factor*mat[j][l]
    return [mat[i][n] for i in range(n)]


def full_markov_resolvent(m,k,z,mean=False):
    start,states=reach(m,k)
    n=len(states);index={s:i for i,s in enumerate(states)}
    A=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    b=[Fraction(1) if mean else Fraction(0) for _ in states]
    for state,i in index.items():
        for nxt,p in transition(state).items():
            if len(nxt)==1:
                if not mean: b[i]+=z*p
            else:
                A[i][index[nxt]]-= (1 if mean else z)*p
    return solve(A,b)[index[start]]


def ruin_resolvent(N,a,z):
    if a==0 or a==N:return Fraction(1)
    A=[[Fraction(int(x==y)) for y in range(1,N)] for x in range(1,N)]
    b=[Fraction(0) for _ in range(N-1)]
    for x in range(1,N):
        for y in (x-1,x+1):
            if y in (0,N):b[x-1]+=z/2
            else:A[x-1][y-1]-=z/2
    return solve(A,b)[a-1]


def proposed_pgf(m,k,z):
    if k==0:return z
    N=m+k
    if k==1:
        return z/Fraction(m)+(Fraction(m-1,m)*z*ruin_resolvent(N,1,z))
    ans=Fraction(1,m)*(1+(k-1)*ruin_resolvent(N,k,z))
    if k<m:
        ans+=Fraction(m-k,m*(k+1))*(1+k*ruin_resolvent(N,k+1,z))
    return z*z*ans


def predicted_mean(m,k):
    if k==0:return Fraction(1)
    if k==1:return Fraction(m)
    return Fraction(2+k*(m-2),1)+Fraction(k*k,m)


def run():
    comparisons=0
    for m in range(2,11):
        for k in range(0,m+1):
            a=survival_chain(m,k,32)
            b=predicted_survival(m,k,32)
            for t,(x,y) in enumerate(zip(a,b)):
                assert x==y,(m,k,t,x,y)
                comparisons+=1
    for m in range(2,9):
        for k in range(m+1):
            for z in (Fraction(1,2),Fraction(2,3)):
                assert full_markov_resolvent(m,k,z)==proposed_pgf(m,k,z),(m,k,z)
                comparisons+=1
            assert full_markov_resolvent(m,k,Fraction(1),mean=True)==predicted_mean(m,k),(m,k)
            comparisons+=1
    print('EXACT_CHECKS_OK',comparisons,'survival m<=10, t<=32; pgf and mean m<=8')

if __name__=='__main__':
    run()
