"""Direct independent incidence-algebra census and Tutte state-sum check.
Python 3 standard library. Execute: python checker.py
"""
from itertools import product


def algebra(n, pairs, q):
    # pairs must contain every strict comparable ordered pair, not merely covers.
    basis = [(i,i) for i in range(n)] + list(pairs)
    index = {ij:j for j,ij in enumerate(basis)}
    products = [[] for _ in basis]
    for j,(u,v) in enumerate(basis):
        for k,(a,b) in enumerate(basis):
            if v==a:
                assert (u,b) in index, 'Not a transitively closed poset'
                products[j].append((k,index[u,b]))
    def mul(x,y):
        result=[0]*len(basis)
        for j,xx in enumerate(x):
            if xx:
                for k,l in products[j]:
                    result[l]+=xx*y[k]
        return tuple(z%q for z in result)
    identity=(1,)*n+(0,)*len(pairs)
    invol=[]
    for diagonal in product((1,q-1),repeat=n):
        for off in product(range(q),repeat=len(pairs)):
            x=diagonal+off
            if mul(x,x)==identity:
                invol.append(x)
    return mul,invol


def direct(n,pairs,q,r):
    mul,inv=algebra(n,pairs,q)
    table=[[mul(x,y)==mul(y,x) for y in inv] for x in inv]
    answer=sum(all(table[t[i]][t[j]] for i in range(r) for j in range(i+1,r))
               for t in product(range(len(inv)),repeat=r))
    return len(inv),answer


def potts(n,pairs,q,r):
    Q=2**r
    return sum(q**sum(c[i]!=c[j] for i,j in pairs)
               for c in product(range(Q),repeat=n))


def random_cluster(n,pairs,q,r):
    Q=2**r; m=len(pairs); total=0
    for subset in product((0,1),repeat=m):
        parent=list(range(n))
        def root(a):
            while parent[a]!=a:
                a=parent[a]
            return a
        for take,(i,j) in zip(subset,pairs):
            if take:parent[root(i)]=root(j)
        s=sum(subset)
        total+=Q**len({root(i) for i in range(n)}) * q**(m-s) * (1-q)**s
    return total


def test(name,n,pairs,q,r):
    nr,actual=direct(n,pairs,q,r)
    spin=potts(n,pairs,q,r)
    fk=random_cluster(n,pairs,q,r)
    assert actual==spin==fk, (name,n,pairs,q,r,actual,spin,fk)
    if r==1:assert actual==nr
    print(f'PASS {name}: q={q} r={r} involutions={nr} commuting_tuples={actual}')

if __name__=='__main__':
    test('chain-2',2,[(0,1)],3,3)
    test('chain-2',2,[(0,1)],5,2)
    test('chain-3',3,[(0,1),(0,2),(1,2)],3,1)
    test('chain-3',3,[(0,1),(0,2),(1,2)],3,2)
    test('chain-3',3,[(0,1),(0,2),(1,2)],3,3)
    test('fork-3',3,[(0,1),(0,2)],3,2)
    test('diamond-4',4,[(0,1),(0,2),(0,3),(1,3),(2,3)],3,2)
    test('disconnected-3',3,[(0,1)],3,2)
    print('INCIDENCE_TUPLE_POTTS_DIRECT_PASS')
