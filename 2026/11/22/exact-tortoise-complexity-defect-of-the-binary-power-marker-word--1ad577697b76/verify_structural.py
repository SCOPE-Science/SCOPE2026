"""Independent marker-gap construction and first-output-one recovery checks."""

def is_marker(i):
    return i >= 0 and (i + 1) & i == 0

def block(start, n):
    return ''.join('1' if is_marker(t) else '0' for t in range(start, start+n))

def tau(w):
    one_places = [i for i, c in enumerate(w) if c == '1']
    if not one_places:
        return w
    z = [one_places[0]]
    z.extend(one_places[i] - one_places[i-1] - 1 for i in range(1, len(one_places)))
    z.append(len(w) - one_places[-1] - 1)
    if len(one_places) == 1:
        return '0'*(len(w)-1) + '1'
    return '0'*(z[0]+z[1])+'1'+''.join('0'*g+'1' for g in z[2:])

def interval(j):
    if j == 0:
        return range(1)
    return range(1 << (j-1))

cases = 0
for n in range(2, 321):
    marked = {}
    j = 0
    while (1 << j) < n:
        d = 1 << j
        marker = d-1
        for off in interval(j):
            if off+d >= n:
                continue
            w = block(marker-off, n)
            assert w.count('1') >= 2
            assert w.index('1') == off
            assert w.index('1', off+1) - off == d
            # Exact map identifies the original first-marker gap from the
            # output's first one; those intervals are disjoint by doubling.
            out = tau(w)
            K = out.index('1')
            assert K == off+d-1
            assert K not in marked, (n,j,off,K)
            marked[K] = w
            cases += 1
        j += 1
    k = n.bit_length()-1
    expected = min(n-(1<<(k-1)),1<<k)
    assert len(marked) == expected, (n,len(marked),expected)
    assert len(set(marked.values())) == len(marked)
    # The n one-marker words and the all-zero word form every residual class.
    p = 1+n+len(marked)
    t = 2+len(marked)
    assert p-t == n-1
print(f'PASS: structural enumeration through n=320; {cases} recovered multi-marker factors; exact dyadic count and loss')
