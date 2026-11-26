"""Standalone exact checks for circular golden-mean universal superstrings.
Python 3 standard library; run: python verify.py.
"""
from collections import Counter, defaultdict
from itertools import product


def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def allowed(k):
    return [''.join(x) for x in product('01',repeat=k) if '11' not in ''.join(x)]


def target_multiset(k):
    return Counter({w:1+int(w[0]==w[-1]=='0' and '1' in w) for w in allowed(k)})


def rightmost_one(v):
    return v.rfind('1')+1  # 0 for all zeros, otherwise 1-based


def euler_circular(k, mult):
    adj=defaultdict(list)
    for w,c in mult.items():
        adj[w[:-1]].extend([w[-1]]*c)
    start='0'*(k-1)
    stack=[start]
    walk=[]
    while stack:
        u=stack[-1]
        if adj[u]:
            digit=adj[u].pop()
            stack.append(u[1:]+digit)
        else:
            walk.append(stack.pop())
    walk.reverse()
    assert len(walk)==sum(mult.values())+1 and walk[0]==walk[-1]
    # Each transition's appended digit spells one position of circular word.
    C=''.join(v[-1] for v in walk[1:])
    return C


def circular_factor_histogram(C,k):
    return Counter(''.join(C[(i+j)%len(C)] for j in range(k)) for i in range(len(C)))


def brute_small(k,L):
    A=set(allowed(k))
    M=target_multiset(k)
    valid=0
    for digits in product('01',repeat=L):
        C=''.join(digits)
        if '11' in (C+C[:1]):
            continue
        hist=circular_factor_histogram(C,k)
        if set(hist)==A:
            valid+=1
            assert L>=sum(M.values())
            if L==sum(M.values()):
                assert hist==M
    return valid


def main():
    local_edges=0
    local_nodes=0
    total_factors=0
    for k in range(2,15):
        edges=allowed(k)
        assert len(edges)==fib(k+2)
        target=target_multiset(k)
        assert sum(target.values())==fib(k+2)+fib(k)-1
        assert sum(c-1 for c in target.values())==fib(k)-1
        vertices=set(w[:-1] for w in edges) | set(w[1:] for w in edges)
        orig_out=Counter(w[:-1] for w in edges)
        orig_in=Counter(w[1:] for w in edges)
        extra_out=Counter({})
        extra_in=Counter({})
        for w,count in target.items():
            if count>1:
                extra_out[w[:-1]]+=count-1
                extra_in[w[1:]]+=count-1
            du=rightmost_one(w[:-1])-rightmost_one(w[1:])
            assert du<=1
            if count>1:
                assert du==1
        for v in vertices:
            assert orig_out[v]+extra_out[v]==orig_in[v]+extra_in[v]
        # Potential lower bound is exactly the number of extra proposed edges.
        total_potential=sum(rightmost_one(w[:-1])-rightmost_one(w[1:]) for w in edges)
        assert total_potential==-(fib(k)-1)
        C=euler_circular(k,target)
        assert len(C)==sum(target.values())
        assert '11' not in C+C[:1]
        assert circular_factor_histogram(C,k)==target
        # Every candidate with minimum length must use exactly the tight edges.
        local_edges+=len(edges); local_nodes+=len(vertices); total_factors+=len(C)
    exhaustive_lengths=0
    optimal_binary_words=0
    for k in range(2,6):
        L=sum(target_multiset(k).values())
        if k<=4:
            for short_length in range(1,L):
                assert brute_small(k,short_length)==0
                exhaustive_lengths+=1
        candidates=brute_small(k,L)
        assert candidates>0
        optimal_binary_words+=candidates
    print(f'VERIFY_OK k=2..14 factor_edges={local_edges} vertices={local_nodes} produced_positions={total_factors} exhaustive_short_lengths={exhaustive_lengths} optimal_linear_representatives_k2to5={optimal_binary_words}')


if __name__=='__main__':
    main()
