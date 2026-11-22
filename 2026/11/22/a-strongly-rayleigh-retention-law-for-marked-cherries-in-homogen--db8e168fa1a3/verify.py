"""Independent, standard-library checks of marked old-cherry survival under PDA leaf grafting."""
from collections import Counter
from fractions import Fraction
from math import comb


def falling(x, k):
    y = Fraction(1)
    for j in range(k):
        y *= x-j
    return y


def law(n, c, r):
    a = Fraction(2*n-3, 2)
    return tuple(Fraction(comb(c,s)) * falling(a,s) * falling(r,c-s)
                 / falling(a+r,c) for s in range(c+1))


def moments(n, c, r, j):
    a = Fraction(2*n-3, 2)
    return falling(a,j) / falling(a+r,j)


def transition(n, r, old):
    alpha = Fraction(2, 2*(n+r)-1)
    nxt=[Fraction(0) for _ in old]
    for s,p in enumerate(old):
        nxt[s] += p*(1-alpha*s)
        if s:
            nxt[s-1] += p*alpha*s
    return tuple(nxt)


def tree_key(tree):
    if isinstance(tree,int): return f'{tree:04d}'
    return '('+tree_key(tree[0])+','+tree_key(tree[1])+')'


def node(a,b):
    return (a,b) if tree_key(a)<tree_key(b) else (b,a)


def paths(tree, path=()):
    out=[path]
    if not isinstance(tree,int):
        out += paths(tree[0],path+(0,))
        out += paths(tree[1],path+(1,))
    return out


def graft(tree, path, new_leaf):
    if not path: return node(tree, new_leaf)
    q=list(tree)
    q[path[0]]=graft(q[path[0]],path[1:],new_leaf)
    return node(q[0],q[1])


def cherries(tree):
    if isinstance(tree,int): return set()
    a,b=tree
    found={(a,b)} if isinstance(a,int) and isinstance(b,int) else set()
    return found|cherries(a)|cherries(b)


def direct_law(base, n, r):
    old_cherries=cherries(base)
    current={base}
    for k in range(n,n+r):
        following={graft(t,path,k) for t in current for path in paths(t)}
        assert len(following)==len(current)*(2*k-1), 'Grafting not bijective'
        current=following
    hist=Counter(len(cherries(t)&old_cherries) for t in current)
    return tuple(Fraction(hist[s],len(current)) for s in range(len(old_cherries)+1))


def main():
    families=0
    for n in range(2,19):
        for c in range(0,n//2+1):
            p=law(n,c,0)
            assert p==tuple([Fraction(0)]*c+[Fraction(1)])
            for r in range(0,10):
                p=law(n,c,r)
                assert sum(p)==1 and all(v>=0 for v in p)
                for j in range(c+1):
                    actual=sum(comb(s,j)*p[s] for s in range(j,c+1)) / comb(c,j) if j else Fraction(1)
                    assert actual==moments(n,c,r,j), ('moment',n,c,r,j)
                assert transition(n,r,p)==law(n,c,r+1), ('Markov',n,c,r)
                families+=1
    # Each tree is unordered: canonicalized nodes ensure distinct labeled extensions.
    examples=[
        (2,node(0,1),3),
        (3,node(node(0,1),2),3),
        (4,node(node(0,1),node(2,3)),4),
        (4,node(node(node(0,1),2),3),3),
        (5,node(node(0,1),node(2,node(3,4))),3),
        (5,node(node(node(node(0,1),2),3),4),3),
    ]
    actual_tests=0
    for n,base,maxr in examples:
        for r in range(maxr+1):
            result=direct_law(base,n,r)
            assert result==law(n,len(cherries(base)),r), ('direct',n,base,r,result)
            actual_tests+=1
    n,c,r=4,2,2
    assert law(n,c,r)==(Fraction(8,63),Fraction(40,63),Fraction(5,21))
    print('exact-Markov-and-moment-cases:',families)
    print('independent-exhaustive-tree-comparisons:',actual_tests)
    print('representative n=4, c=2, r=2:',','.join(map(str,law(4,2,2))))
    print('ALL_MARKED_CHERRY_EXTENSION_CHECKS_OK')

if __name__=='__main__':
    main()
