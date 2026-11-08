"""Independent finite checks for period-doubling minimal unique substrings."""

def word(k):
    w = '0'
    for _ in range(k):
        w = ''.join('01' if c == '0' else '00' for c in w)
    return w


def complete_mus_by_suffix_lcp(w):
    n = len(w)
    nxt = [0] * (n+1)
    lcp = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if w[i] == w[j]:
                lcp[i][j] = 1 + (lcp[i+1][j+1] if i+1 < n and j+1 < n else 0)
    max_other = [max(lcp[i][j] for j in range(n) if j != i) for i in range(n)]
    answer = []
    for i in range(n):
        ell = max_other[i] + 1
        if ell <= n-i and (ell == 1 or (i+1 < n and ell-1 <= max_other[i+1])):
            answer.append((i, ell))
    return answer


def verify():
    for k in range(3, 11):
        w = word(k)
        m = 1 << (k-2)
        a = word(k-2)
        c = word(k-3)
        b = c+c
        assert w == a+b+a+a
        assert a[:m-1] == b[:m-1]
        assert a[:m//2] == c
        assert a[m//2:-1] == c[:-1]
        assert a[-1] != c[-1]
        target = [(m-1, m+1), (3*m//2-1, m+1), (2*m-1, m+1), (3*m-1, m+1)]
        actual = complete_mus_by_suffix_lcp(w)
        assert actual == target, (k, actual, target)
        for r in range(m-1):
            i,j = r,2*m+r
            q=0
            while j+q < len(w) and w[i+q] == w[j+q]:q+=1
            assert q == 2*m-r-1, ('A',k,r,q)
        for r in range(m//2-1):
            i,j=m+r,3*m//2+r
            q=0
            while j+q < len(w) and w[i+q] == w[j+q]:q+=1
            assert q == 3*m//2-r-1, ('B',k,r,q)
        print(f'k={k}: length={len(w)}, exactly four MUSs at {target}; all pair LCPs verified')
    print('PASS: all finite full-language and companion-divergence checks')

if __name__ == '__main__':
    verify()
