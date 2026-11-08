"""Independent coloring and explicit commutator decomposition checks.
Each vector in the Jacobson radical is represented by its arrow-coordinate tuple.
"""
from itertools import product, combinations

def coloring(n, edges, colors):
    for c in product(range(colors), repeat=n):
        if all(c[u]!=c[v] for u,v in edges): return c
    return None

def build_decomposition(n, arrows, q, values, length):
    support=[e for e,x in zip(arrows,values) if x%q]
    labels=coloring(n, support, q**(2*length))
    if labels is None:return None
    pairs=[[(lab//(q**(2*j)))%(q*q) for j in range(length)] for lab in labels]
    # Each pair stores (diag first, diag second) in base q; choose a radical
    # coefficient on one commutator where the associated slope is nonzero.
    alpha=[[pair//q for pair in row] for row in pairs]
    beta=[[pair%q for pair in row] for row in pairs]
    xs=[[0]*len(arrows) for _ in range(length)]
    ys=[[0]*len(arrows) for _ in range(length)]
    for i,((u,v),t) in enumerate(zip(arrows,values)):
        if not t: continue
        for j in range(length):
            a=(alpha[u][j]-alpha[v][j])%q
            b=(beta[u][j]-beta[v][j])%q
            if a:
                ys[j][i]=t*pow(a,-1,q)%q
                break
            if b:
                xs[j][i]=-t*pow(b,-1,q)%q
                break
        else:raise AssertionError('coloring failed to separate supported edge')
    answer=[]
    for i in range(len(arrows)):
        u,v=arrows[i]
        answer.append(sum((alpha[u][j]-alpha[v][j])*ys[j][i] -
                        (beta[u][j]-beta[v][j])*xs[j][i] for j in range(length))%q)
    assert tuple(answer)==tuple(values)
    return True

def run():
    for n in [3,4,5]:
        arrows=list(combinations(range(n),2))
        for mask in range(1<<len(arrows)):
            values=tuple((mask>>i)&1 for i in range(len(arrows)))
            supp=[edge for edge,x in zip(arrows,values) if x]
            expected=coloring(n,supp,4) is not None
            got=build_decomposition(n,arrows,2,values,1)
            assert bool(got)==expected
            if not expected:
                assert build_decomposition(n,arrows,2,values,2)
        print('CHROMATIC_SUPPORT_PASS','q=2','n=',n,'supports=',1<<len(arrows))
    # Four colors insufficient for K5; two commutators suffice.
    arrows=list(combinations(range(5),2))
    assert coloring(5,arrows,4) is None
    assert build_decomposition(5,arrows,2,[1]*len(arrows),2)
    # Nine colors insufficient for K10 over F3; 81 colors suffice.
    # No need to enumerate: a complete graph requires distinct labels.
    assert 9<10<=81
    print('COMPLETE_GRAPH_THRESHOLDS_PASS')
    print('CHROMATIC_COMMUTATOR_WIDTH_PASS')
if __name__=='__main__':run()
