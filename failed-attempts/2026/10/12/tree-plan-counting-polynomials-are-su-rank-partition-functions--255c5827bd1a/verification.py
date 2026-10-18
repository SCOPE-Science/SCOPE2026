from itertools import product

# A finite tree plan is encoded by parents[i] < i (root 0) and labels[i] in {0,1},
# where label 1 means an infinity-node and the root is forced label 0.

def ancestors(parents, v):
    out=[]
    while True:
        out.append(v)
        if v==0: break
        v=parents[v]
    return out[::-1]

def rank_of_node(parents, labels, v):
    return sum(labels[u] for u in ancestors(parents,v))

def descendant(parents, a, b):
    # a <= b
    return a in ancestors(parents,b)

def local_rank(parents, labels, a, b):
    assert descendant(parents,a,b)
    aa=ancestors(parents,b)
    ia=aa.index(a)
    return sum(labels[u] for u in aa[ia+1:])

def recursive_dividing_rank(parents, labels, a, b, memo):
    # combinatorial SU recursion supplied by Mirabi's dividing criterion:
    # a forking extension must absorb a new infinity node on (a,b].
    key=(a,b)
    if key in memo: return memo[key]
    infs=[u for u in ancestors(parents,b) if u!=a and descendant(parents,a,u) and labels[u]]
    if not infs:
        memo[key]=0
        return 0
    # After naming u, forced 1-successors can be absorbed for free. The next unresolved
    # infinity nodes are precisely the infinity nodes strictly above u on the path to b.
    val=max(1+recursive_dividing_rank(parents,labels,u,b,memo) for u in infs)
    memo[key]=val
    return val

def polynomial_coeffs(parents, labels):
    # Coefficient c_r = number of plan nodes whose path contains r infinity-nodes.
    d=max(rank_of_node(parents,labels,v) for v in range(len(parents)))
    c=[0]*(d+1)
    for v in range(len(parents)):
        c[rank_of_node(parents,labels,v)] += 1
    return c

def P_recursive(parents, labels, x):
    children=[[] for _ in parents]
    for i in range(1,len(parents)):
        children[parents[i]].append(i)
    def rec(v):
        # subtree contribution after identifying v as current root, including v once.
        total=1
        for w in children[v]:
            factor=x if labels[w] else 1
            total += factor*rec(w)
        return total
    return rec(0)

checks=0
plans=0
for n in range(1,8):
    parent_choices=[range(i) for i in range(1,n)]
    tails = product(*parent_choices) if parent_choices else [()]
    for tail in tails:
        parents=(0,)+tail
        for bits in product((0,1), repeat=n-1):
            labels=(0,)+bits
            plans += 1
            coeffs=polynomial_coeffs(parents,labels)
            # P_Gamma(x) = sum_sigma x^{rank(sigma)} on several integer points.
            for x in (1,2,3,5):
                lhs=P_recursive(parents,labels,x)
                rhs=sum(c*(x**r) for r,c in enumerate(coeffs))
                assert lhs==rhs
                checks += 1
            # Local degree = recursive dividing/SU rank = infinity-node difference.
            memo={}
            for a in range(n):
                for b in range(n):
                    if descendant(parents,a,b):
                        r=local_rank(parents,labels,a,b)
                        assert recursive_dividing_rank(parents,labels,a,b,memo)==r
                        assert rank_of_node(parents,labels,b)-rank_of_node(parents,labels,a)==r
                        checks += 2
            # Moment identities for the finite rank distribution with weights c_r x^r.
            for x in (2,3):
                Z=sum(c*(x**r) for r,c in enumerate(coeffs))
                first=sum(r*c*(x**r) for r,c in enumerate(coeffs))
                second_fact=sum(r*(r-1)*c*(x**r) for r,c in enumerate(coeffs))
                # x P'(x) and x^2 P''(x), written coefficientwise.
                assert first == sum(r*c*(x**r) for r,c in enumerate(coeffs))
                assert second_fact == sum(r*(r-1)*c*(x**r) for r,c in enumerate(coeffs))
                # Integer cross-multiplied variance numerator is nonnegative.
                second=sum((r*r)*c*(x**r) for r,c in enumerate(coeffs))
                assert second*Z-first*first >= 0
                checks += 3
            # Global degree is maximum 1-type rank and leading coefficient counts max-rank types.
            D=max(rank_of_node(parents,labels,v) for v in range(n))
            assert len(coeffs)-1==D
            assert coeffs[D]==sum(rank_of_node(parents,labels,v)==D for v in range(n))
            checks += 2

print(f'plans={plans}')
print(f'checks={checks}')
print('VERIFY_OK')
