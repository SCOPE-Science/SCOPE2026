#!/usr/bin/env python3
"""Exact brute-force checks for geodesic multiplicity in free inverse monoids.

Enumerates all words over two generators and inverses up to length 8,
independently computing their Munn vertex sets and endpoints. Compares
counts for every endpoint pair in eleven nonidentical test presentations.
"""
from collections import Counter, deque
from itertools import product
from math import factorial

ALPHABET = (-2,-1,1,2)


def multiply(u,v):
    z=list(u)
    for a in v:
        if z and z[-1]==-a:
            z.pop()
        else:
            z.append(a)
    return tuple(z)


def inverse(u):
    return tuple(-a for a in u[::-1])


def evaluate(word):
    vertex=()
    vertices={vertex}
    for a in word:
        vertex=multiply(vertex,(a,))
        vertices.add(vertex)
    return frozenset(vertices),vertex


def graph(T):
    A={v:set() for v in T}
    for v in T:
        for a in ALPHABET:
            w=multiply(v,(a,))
            if w in A:
                A[v].add(w)
    return A


def path(A,s,t):
    Q=deque([s]); parent={s:None}
    while Q and t not in parent:
        u=Q.popleft()
        for v in A[u]:
            if v not in parent:
                parent[v]=u;Q.append(v)
    assert t in parent
    out=[];v=t
    while v is not None:
        out.append(v);v=parent[v]
    return out[::-1]


def count_predicted(A,s,t):
    if s==t:
        value=factorial(len(A[s]))
        for v in A:
            if v!=s:
                value*=factorial(len(A[v])-1)
        return value
    interior=set(path(A,s,t)[1:-1])
    value=1
    for v in A:
        value*=factorial(len(A[v])-2 if v in interior else len(A[v])-1)
    return value


def rebase(T,s):
    si=inverse(s)
    return frozenset(multiply(si,v) for v in T)


def verify():
    by_length=Counter()
    for n in range(9):
        for w in product(ALPHABET,repeat=n):
            T,t=evaluate(w)
            by_length[(n,T,t)]+=1
    assert sum(by_length.values())==sum(4**n for n in range(9))

    samples=[(),(1,), (1,2), (1,2,-1), (1,2,-1,-2),
             (1,-1,2,-2), (1,2,-2,-1,-2), (1,2,-2,-1,-2,2),
             (1,2,-2,-1,-2,1), (1,-1,2,-2,-1,1,-2,2),
             (1,2,-2,-1,-1,1,2,-2,-1)]
    complete_checks=0
    for word in samples:
        T,_=evaluate(word);A=graph(T);m=len(T)-1
        lengths={(s,t):2*m-(len(path(A,s,t))-1) for s in T for t in T}
        multiplicities={}
        for (s,t),ell in lengths.items():
            target=rebase(T,s)
            endpoint=multiply(inverse(s),t)
            expected=count_predicted(A,s,t)
            actual=by_length[(ell,target,endpoint)]
            assert actual==expected,('H',word,s,t,actual,expected)
            assert sum(by_length[(k,target,endpoint)] for k in range(ell))==0
            multiplicities[(s,t)]=expected
            complete_checks+=1
        diameter=max(2*m-ell for ell in lengths.values())
        D_expected=sum(multiplicities[s,t] for (s,t),ell in lengths.items() if 2*m-ell==diameter)
        D_actual=0
        for (ell,normal,end),count in by_length.items():
            if ell==2*m-diameter and any(normal==rebase(T,s) for s in T):
                D_actual+=count
        assert D_expected==D_actual,('D',word,D_expected,D_actual)
        for s in T:
            ecc=max(2*m-lengths[s,t] for t in T)
            expected=sum(multiplicities[s,t] for t in T if 2*m-lengths[s,t]==ecc)
            rooted=rebase(T,s)
            actual=sum(count for (ell,normal,end),count in by_length.items()
                       if ell==2*m-ecc and normal==rooted)
            assert expected==actual,('R',word,s,expected,actual)
        for t in T:
            ecc=max(2*m-lengths[s,t] for s in T)
            expected=sum(multiplicities[s,t] for s in T if 2*m-lengths[s,t]==ecc)
            actual=sum(count for (ell,normal,end),count in by_length.items()
                       if ell==2*m-ecc and frozenset(multiply(inverse(end),v) for v in normal)==rebase(T,t))
            assert expected==actual,('L',word,t,expected,actual)
        print('tree',len(T),'vertices, degree multiset',sorted(map(len,A.values())),
              'D-geodesic multiplicity',D_actual)
    print('VERIFY_OK trees=11 endpoint_pairs=%d enumerated_words=%d' %
          (complete_checks,sum(4**n for n in range(9))))

if __name__=='__main__':verify()


def rooted_code(A,root,parent=-1):
    return '('+''.join(sorted(rooted_code(A,v,root) for v in A[root] if v!=parent))+')'


def tree_code(A):
    return min(rooted_code(A,v) for v in A)


def all_unlabeled_trees(max_edges=10):
    trees=[{0:set()}]
    for m in range(max_edges+1):
        yield m,trees
        new={}
        for A in trees:
            for at in A:
                B={v:neigh.copy() for v,neigh in A.items()}
                index=len(B);B[index]={at};B[at].add(index)
                k=tree_code(B)
                if k not in new:new[k]=B
        trees=list(new.values())


def expected_max(m):
    if m<=1:return 1
    if m==2:return 2
    if m==3:return 6
    q,r=divmod(m-1,3)
    return 4*(6**q)*(2 if r==2 else 1)


def verify_extremal():
    for m,trees in all_unlabeled_trees(10):
        admissible=[A for A in trees if max(map(len,A.values()))<=4]
        actual=0
        for A in admissible:
            for s in A:
                for t in A:
                    actual=max(actual,count_predicted(A,s,t))
        predicted=expected_max(m)
        assert actual==predicted,('extremal',m,actual,predicted)
        print('MAX_OK edges=%d tree_shapes=%d max_geodesics=%d'%(m,len(admissible),actual))
    print('EXTREMAL_VERIFY_OK m=0..10')


if __name__=='__main__':verify_extremal()
