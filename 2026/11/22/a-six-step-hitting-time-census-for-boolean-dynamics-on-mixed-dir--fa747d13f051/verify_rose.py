"""Standalone exact checks for synchronous AND dynamics on directed 2/3-cycle roses.

No external libraries required. Run: python verify_rose.py
"""
from collections import Counter


def rose_edges(m, k):
    # Vertex 0 is the common root; m two-cycles 0->a->0;
    # k three-cycles 0->b->c->0. Distinct non-root vertices are labelled.
    edges = []
    for a in range(1, m + 1):
        edges += [(0, a), (a, 0)]
    for j in range(k):
        b, c = m + 1 + 2 * j, m + 2 + 2 * j
        edges += [(0, b), (b, c), (c, 0)]
    return edges


def histogram_formula(m, k):
    a, b = 2 ** (m+k) - 1, 2**k
    return [1, a-1, a*(b-1), a*(b-1), b, a, b-1]


def brute_and(m, k):
    n=1+m+2*k
    ins=[[] for _ in range(n)]
    for u,v in rose_edges(m,k):
        ins[v].append(u)
    incoming=[sum(1 << u for u in ps) for ps in ins]
    full=(1<<n)-1
    def step(x):
        ans=0
        for v,mask in enumerate(incoming):
            if x & mask == mask:
                ans |= 1 << v
        return ans
    count=Counter()
    for x in range(1<<n):
        if x == full:
            count['never'] += 1
            continue
        y=x
        for t in range(7):
            if y == 0:
                count[t]+=1
                break
            y=step(y)
        else:
            raise AssertionError(('no extinction',m,k,x))
    assert count['never']==1
    return [count[t] for t in range(7)]


def sum_rows(reach, indices):
    out = 0
    for u in indices:
        out |= reach[u]
    return out

def via_walk_sets(m,k):
    # Independent reachability test: complement (OR dynamics) at t
    # propagates a source iff a directed walk of length t exists.
    n=1+m+2*k
    reach=[1<<u for u in range(n)]
    mask=(1<<n)-1
    ins=[[] for _ in range(n)]
    for u,v in rose_edges(m,k):ins[v].append(u)
    h=[]
    for t in range(7):
        # Rows reach[v] encode the time-t predecessor set of v.
        nfull=0
        for y in range(1<<n):
            if all(row & y for row in reach):nfull+=1
        h.append(nfull)
        reach=[sum_rows(reach, ps) for ps in ins]
    return [h[0]]+[h[t]-h[t-1] for t in range(1,7)]


def main():
    cases=[]
    total_states=0
    for m in range(1,8):
        for k in range(1,6):
            n=1+m+2*k
            if n>16:
                continue
            expected=histogram_formula(m,k)
            got=brute_and(m,k)
            assert got==expected,(m,k,got,expected)
            total_states+=1<<n
            if n<=13:
                walk=via_walk_sets(m,k)
                assert walk==expected,(m,k,walk,expected)
            cases.append((m,k,n,expected))
    for m,k in [(1,1),(2,2),(4,3),(7,4)]:
        print('m=%d k=%d n=%d counts=%s'%(m,k,1+m+2*k,histogram_formula(m,k)))
    for m,k in [(1,1),(2,3),(50,70),(200,300)]:
        assert sum(histogram_formula(m,k)) == 2**(1+m+2*k)-1
    print('PASS: %d parameter pairs, %d exhaustively checked states; independent walk-set checks for n<=13.'%(len(cases),total_states))


if __name__ == '__main__':main()
