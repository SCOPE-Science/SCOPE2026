"""Exact, dependency-free check of second-image entropy separation for Rules 22 and 104.
Run: python3 verify.py (with spectral_witnesses.json in the same directory).
The inequalities are over arbitrary-precision integers; no floating point is used.
"""
import json
from collections import deque
from pathlib import Path


def local_value(rule, window, size, steps):
    bits = [(window >> (size-1-i)) & 1 for i in range(size)]
    for _ in range(steps):
        bits = [(rule >> (4*bits[i]+2*bits[i+1]+bits[i+2])) & 1
                for i in range(len(bits)-2)]
    assert len(bits) == 1
    return bits[0]


def subset_dfa(rule, steps):
    k = 2*steps
    n = 1 << k
    single = [[0, 0] for _ in range(n)]
    for s in range(n):
        for b in (0, 1):
            w = (s << 1) | b
            label = local_value(rule, w, k+1, steps)
            single[s][label] |= 1 << (w & (n-1))
    start = (1 << n) - 1
    states, seen, edges = [start], {start: 0}, []
    for mask in states:
        row = [-1, -1]
        for label in (0, 1):
            new_mask = 0
            m = mask
            while m:
                bit = m & -m
                s = bit.bit_length()-1
                new_mask |= single[s][label]
                m -= bit
            if new_mask:
                if new_mask not in seen:
                    seen[new_mask] = len(states)
                    states.append(new_mask)
                row[label] = seen[new_mask]
        edges.append(row)
    return states, edges


def sccs(edges):
    index = 0
    stack, onstack, indices, low, components = [], set(), {}, {}, []
    def visit(v):
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in edges[v]:
            if w < 0:
                continue
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            component=[]
            while True:
                w=stack.pop()
                onstack.remove(w)
                component.append(w)
                if w == v: break
            components.append(sorted(component))
    for v in range(len(edges)):
        if v not in indices:
            visit(v)
    return components


def reachable_word(edges, word):
    state = 0
    for c in word:
        if state < 0:
            return False
        state=edges[state][int(c)]
    return state >= 0


def dfa_difference_witness(A, B):
    """Find a word admitted by A and rejected by B, or prove none exists."""
    todo=deque([(0,0,'')])
    seen={(0,0)}
    while todo:
        i,j,prefix=todo.popleft()
        for symbol in (0,1):
            u=A[i][symbol] if i>=0 else -1
            v=B[j][symbol] if j>=0 else -1
            if u>=0 and v<0:
                return prefix+str(symbol), len(seen)
            if u<0:
                continue
            pair=(u,v)
            if pair not in seen:
                seen.add(pair)
                todo.append((u,v,prefix+str(symbol)))
    return None, len(seen)


def word_count(edges, n):
    values=[0]*len(edges)
    values[0]=1
    for _ in range(n):
        update=[0]*len(edges)
        for s,value in enumerate(values):
            if value:
                for nxt in edges[s]:
                    if nxt>=0:
                        update[nxt]+=value
        values=update
    return sum(values)


def direct_language(rule, steps, n):
    ninput=n+2*steps
    outputs=set()
    for x in range(1 << ninput):
        cells=[(x >> (ninput-1-i)) & 1 for i in range(ninput)]
        for _ in range(steps):
            cells=[(rule >> (4*cells[i]+2*cells[i+1]+cells[i+2])) & 1
                   for i in range(len(cells)-2)]
        outputs.add(tuple(cells))
    return outputs


def exact_spectrum_check(edges, bounds, coeffs, required_component_size, required_total):
    assert len(edges)==required_total
    components=sccs(edges)
    largest=max(components,key=len)
    assert len(largest)==required_component_size
    # All other components are singleton with at most one loop: their
    # adjacency spectral radius is therefore <= 1, below either bound.
    for comp in components:
        if comp != largest:
            assert len(comp)==1
            v=comp[0]
            assert sum(int(target==v) for target in edges[v])<=1
    lo_num,hi_num,den=bounds
    assert 1*den<lo_num<hi_num
    assert len(coeffs)==len(largest) and all(type(x)==int and x>0 for x in coeffs)
    position={state:i for i,state in enumerate(largest)}
    for i,state in enumerate(largest):
        image=sum(coeffs[position[target]] for target in edges[state] if target in position)
        # Collatz-Wielandt positive-vector sandwich for an irreducible
        # nonnegative matrix: lo < rho < hi.
        assert den*image > lo_num*coeffs[i], (state,'lower')
        assert den*image < hi_num*coeffs[i], (state,'upper')
    return (len(components),len(largest))


def conjugate(rule):
    return sum((1-((rule>>(4*(1-a)+2*(1-b)+1-c))&1)) <<(4*a+2*b+c)
               for a in (0,1) for b in (0,1) for c in (0,1))


def main():
    certificate=json.loads(Path(__file__).with_name('spectral_witnesses.json').read_text())
    assert conjugate(22)==151 and conjugate(104)==233
    one,twostep={},{}
    for r in (22,104):
        _,one[r]=subset_dfa(r,1)
        _,twostep[r]=subset_dfa(r,2)
        assert len(one[r])==15
    # Exact all-length language equivalence for the first images.
    a,_=dfa_difference_witness(one[22],one[104])
    b,_=dfa_difference_witness(one[104],one[22])
    assert a is None and b is None
    # Both strict differences for second images: no inclusion either way.
    a,_=dfa_difference_witness(twostep[22],twostep[104])
    b,_=dfa_difference_witness(twostep[104],twostep[22])
    assert a=='10111101' and b=='1010111', (a,b)
    targets={22:(360,350,(186746,186748,100000)),
             104:(418,418,(183426,183428,100000))}
    for r in (22,104):
        total,principal,bounds=targets[r]
        data=certificate[str(r)]
        assert data['rule']==r and data['bounds']==list(bounds)
        result=exact_spectrum_check(twostep[r],bounds,data['positive_vector'],principal,total)
        print('exact Perron sandwich',r,result,f'{bounds[0]}/{bounds[2]} < rho < {bounds[1]}/{bounds[2]}')
    assert 183428<186746
    # Full finite-block independent reconstruction, no DFA code shared.
    for rule in (22,104):
        for step in (1,2):
            E=one[rule] if step==1 else twostep[rule]
            for n in range(0,12):
                direct=direct_language(rule,step,n)
                assert len(direct)==word_count(E,n), (rule,step,n)
                for word in direct:
                    assert reachable_word(E,''.join(map(str,word)))
    for r in (22,104):
        for n in range(1,8 if r==22 else 9):
            if n<(7 if r==22 else 8):
                assert word_count(one[r],n)==word_count(twostep[r],n)
        n=7 if r==22 else 8
        assert word_count(one[r],n)==(128 if r==22 else 254)
        assert word_count(twostep[r],n)==(126 if r==22 else 252)
    assert word_count(twostep[22],11)==1788
    assert word_count(twostep[104],11)==1770
    # Check all-length source image equality and specific short-language losses.
    for r,n,expected in [(22,7,{'1010111','1110101'}),
                         (104,8,{'10111101','11011011'})]:
        diff=direct_language(r,1,n)-direct_language(r,2,n)
        assert {''.join(map(str,word)) for word in diff}==expected
    print('PASS all-length first-image equality, incomparable second images,')
    print('     exact rational spectral bounds, independent finite enumeration through length 11')

if __name__=='__main__':
    main()
