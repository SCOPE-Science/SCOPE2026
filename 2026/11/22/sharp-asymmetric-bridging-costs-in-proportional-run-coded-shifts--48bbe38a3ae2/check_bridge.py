"""Finite independent tests of sharp bridging bounds for proportional-run languages.

Constructs a finite generator-cycle automaton directly from the defining words;
no minimal-forbidden-word formula or external dependencies are used.
"""
from itertools import product
from functools import lru_cache


def complete_right(u, k):
    b = len(u) - len(u.rstrip('1'))
    if b == 0:
        a = len(u) - len(u.rstrip('0'))
        return '1' * (k * a)
    q = (b+k-1)//k
    z = u[:-b]
    if z:
        a = len(z) - len(z.rstrip('0'))
        if len(z)>a:  # the zero run begins after a 1 and is fully visible
            q = a
        else:
            q = max(q, a)
    assert k*q >= b
    return '1' * (k*q-b)


def complete_left(v, k):
    a = len(v) - len(v.lstrip('0'))
    if a:
        if a == len(v):
            return ''
        y = v[a:]
        b = len(y)-len(y.lstrip('1'))
        if b<len(y):
            assert b % k == 0 and b//k >= a
            q=b//k
        else:
            q=max(a,(b+k-1)//k)
        return '0' * (q-a)
    b = len(v) - len(v.lstrip('1'))
    q = (b+k-1)//k
    return '0'*q+'1'*(k*q-b)


@lru_cache(None)
def graph(k, B):
    # Shared hub 0, cycles labeled by 0^a1^(ka), 1<=a<=B.
    edges={0:{'0':set(),'1':set()}}
    state=1
    for a in range(1,B+1):
        s='0'*a+'1'*(k*a)
        prev=0
        for j, sym in enumerate(s):
            cur=0 if j==len(s)-1 else state
            if cur!=0:
                edges[cur]={'0':set(),'1':set()}
                state+=1
            edges[prev][sym].add(cur)
            prev=cur
    return edges


def admitted(word,k):
    # For a length-L factor, generator zero-run size <=L suffices:
    # complete its at-most-two boundary generators with observed run lengths.
    g=graph(k, max(len(word),1))
    active=set(g)
    for c in word:
        active={v for u in active for v in g[u][c]}
        if not active: return False
    return True


def witness(k,m,n):
    t=(n-2)//k
    u='0'*(m-1)+'1'
    v='0'+'1'*(k*t)+'0'*(n-k*t-1)
    w='1'*(k*(m-1)-1)+'0'*(t-1)
    return u,v,w


def test():
    count_pairs=count_witness=count_short=0
    for k in range(1,4):
        for m in range(1,6):
            U=[''.join(t) for t in product('01',repeat=m) if admitted(''.join(t),k)]
            for n in range(1,6):
                V=[''.join(t) for t in product('01',repeat=n) if admitted(''.join(t),k)]
                for u in U:
                    p=complete_right(u,k)
                    assert len(p)<=k*m
                    for v in V:
                        q=complete_left(v,k)
                        assert len(q)<= (n+k-1)//k +k
                        assert admitted(u+p+q+v,k),(k,m,n,u,v,p,q)
                        count_pairs+=1
    for k in range(1,5):
        for m in range(2,8):
            for n in range(k+2,10):
                u,v,w=witness(k,m,n)
                assert admitted(u,k) and admitted(v,k) and admitted(u+w+v,k)
                low=k*(m-1)+(n-2)//k-2
                assert len(w)==low
                # Independently test no shorter bridge for the smallest witnesses.
                if len(w)<=10:
                    for s in range(len(w)):
                        for bits in product('01',repeat=s):
                            assert not admitted(u+''.join(bits)+v,k),(k,m,n,s,bits)
                            count_short+=1
                count_witness+=1
    print('VERIFY_OK pairwise_completed',count_pairs,'sharp_witnesses',count_witness,'ruled_out_short_bridges',count_short)

if __name__=='__main__':test()
