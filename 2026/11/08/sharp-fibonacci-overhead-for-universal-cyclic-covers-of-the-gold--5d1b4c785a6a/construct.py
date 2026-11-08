"""Independent brute-force check of short lengths and direct arc-cover construction."""
from collections import Counter
from itertools import product

def fibonacci(k):
    a,b=0,1
    for i in range(k):a,b=b,a+b
    return a

def words(n):
    return {''.join(p) for p in product('01',repeat=n) if '11' not in ''.join(p)}

def all_windows(s,n):
    return Counter(''.join(s[(i+j)%len(s)] for j in range(n)) for i in range(len(s)))

def build(n):
    # Integer encoded Euler tour of the directed constrained de Bruijn multigraph.
    size=n-1
    edges=sorted(words(n))
    extras=sorted('0'+u+'0' for u in words(n-2) if '1' in u)
    outgoing={v:[] for v in words(size)}
    for e in edges+extras:
        outgoing[e[:size]].append((e[1:],e))
    v='0'*size
    todo=[(v,'')]
    circuit=[]
    while todo:
        z=todo[-1][0]
        if outgoing[z]:todo.append(outgoing[z].pop())
        else:
            _,e=todo.pop()
            if e:circuit.append(e)
    circuit.reverse()
    s=''.join(e[-1] for e in circuit)
    assert all_windows(s,n)==Counter(edges+extras)
    return s

def main():
    for n in range(2,6):
        witness=build(n)
        assert len(witness)==fibonacci(n+2)+fibonacci(n)-1
        for length in range(1,len(witness)):
            for bits in product('01',repeat=length):
                s=''.join(bits)
                if '11' in s+s[0]:continue
                if words(n).issubset(all_windows(s,n)):
                    raise AssertionError(('shorter covering',n,s))
        print('small exact',n,len(witness))
    print('CONSTRUCT_OK')
if __name__=='__main__': main()
