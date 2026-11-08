"""Independent exact small-tree checks for the rooted full-outbreak law.

Requires Python 3.9+ standard library. Run: python CHECKER.py
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import factorial


def h_exp(d, lam, mu):
    return Fraction(factorial(d), 1) * lam**d / __import__('functools').reduce(lambda a, j: a*(mu + j*lam), range(1, d+1), Fraction(1))


def exact_sir_full(n, edges, root, lam, mu):
    full = (1 << n) - 1
    nbrs = [[] for _ in range(n)]
    for u,v in edges:
        nbrs[u].append(v); nbrs[v].append(u)

    @lru_cache(None)
    def f(I, R):
        if I | R == full:
            return Fraction(1)
        if not I:
            return Fraction(0)
        S = full ^ (I | R)
        moves=[]
        for u in range(n):
            if (I >> u) & 1:
                moves.append((mu, I ^ (1 << u), R | (1 << u)))
            elif (S >> u) & 1:
                infected = sum((I >> v) & 1 for v in nbrs[u])
                if infected:
                    moves.append((lam*infected, I | (1 << u), R))
        total=sum((m[0] for m in moves), Fraction(0))
        return sum((rate*f(I1,R1) for rate,I1,R1 in moves), Fraction(0))/total
    return f(1 << root, 0)


def formula(n, edges, root, moments):
    deg=[0]*n
    for u,v in edges:
        deg[u]+=1;deg[v]+=1
    p=Fraction(1)
    for v,d in enumerate(deg):
        p*=moments[d if v==root else d-1]
    return p


def two_point_moment(d):
    return (Fraction(1,4)**d+Fraction(3,4)**d)/2


def check_two_point_direct(n, edges, root):
    children=[[] for _ in range(n)]
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    stack=[(root,-1)]
    while stack:
        v,parent=stack.pop()
        for w in adj[v]:
            if w!=parent:
                children[v].append(w);stack.append((w,v))
    # Explicitly enumerate all environmental infectivities and all directed edge outcomes.
    # In a tree full infection is equivalent to success of every child-directed edge.
    edges_dir=[(v,w) for v in range(n) for w in children[v]]
    ans=Fraction(0)
    for env in product((Fraction(1,4),Fraction(3,4)), repeat=n):
        envprob=Fraction(1,2)**n
        for mask in range(1 << len(edges_dir)):
            edgeprob=Fraction(1)
            for j,(v,w) in enumerate(edges_dir):
                edgeprob*=env[v] if (mask >> j)&1 else (1-env[v])
            if mask == (1 << len(edges_dir))-1:
                ans += envprob*edgeprob
    return ans


def main():
    # Two nonisomorphic tree shapes with the same vertex-degree multiset.
    graphs=[
        (6,((0,1),(0,2),(0,3),(1,4),(2,5))),
        (6,((0,1),(0,2),(0,3),(1,4),(4,5))),
        (5,((0,1),(1,2),(2,3),(3,4))),
        (5,((0,1),(0,2),(0,3),(3,4))),
        (4,((0,1),(0,2),(0,3))),
        (4,((0,1),(1,2),(2,3)))
    ]
    tests=0
    for n, edges in graphs:
        for lam,mu in ((Fraction(1),Fraction(1)),(Fraction(2),Fraction(3)),(Fraction(3),Fraction(1))):
            moments=[h_exp(d,lam,mu) for d in range(n)]
            for root in range(n):
                truth=exact_sir_full(n,edges,root,lam,mu)
                predicted=formula(n,edges,root,moments)
                assert truth == predicted, (n,edges,root,lam,mu,truth,predicted)
                tests+=1
        moments=[two_point_moment(d) for d in range(n)]
        for root in range(n):
            assert check_two_point_direct(n,edges,root) == formula(n,edges,root,moments)
            tests+=1
    trees=graphs[:2]
    for n,edges in trees:
        degrees=[sum(u==v or w==v for u,w in edges) for v in range(n)]
        hs=[h_exp(d,Fraction(1),Fraction(1)) for d in range(n)]
        for degree,expected in ((1,Fraction(1,24)),(2,Fraction(1,18)),(3,Fraction(1,16))):
            root=degrees.index(degree)
            assert formula(n,edges,root,hs)==expected
    print('PASS:',tests,'exact Markov-chain or explicit-transmission checks; six-vertex invariant degree profile passed')

if __name__ == '__main__':
    main()
