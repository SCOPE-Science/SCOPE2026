"""Independent exact checks using string-labeled graphs and fraction-free determinants.

Run: python3 verify.py counts.csv
Only the Python standard library is required.
"""
from itertools import product, combinations
from pathlib import Path
import csv
import sys


def admissible(n, cyclic):
    for tup in product('01', repeat=n):
        s = ''.join(tup)
        if '11' in s: continue
        if cyclic and s[0] == s[-1] == '1': continue
        yield s


def determinant(matrix):
    """Integer Bareiss method with row exchanges."""
    a = [list(row) for row in matrix]
    N = len(a)
    if N == 0: return 1
    sign = 1
    previous = 1
    for k in range(N - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, N) if a[i][k]), None)
            if pivot is None: return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, N):
            aik = a[i][k]
            for j in range(k + 1, N):
                numerator = p * a[i][j] - aik * a[k][j]
                value, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][j] = value
            a[i][k] = 0
        previous = p
    return sign * a[-1][-1]


def full_tree_count(n):
    edges = list(admissible(n, True))
    labels = sorted({w[:-1] for w in edges} | {w[1:] for w in edges})
    z = {w: i for i, w in enumerate(labels)}
    L = [[0] * len(labels) for _ in labels]
    for w in edges:
        a, b = z[w[:-1]], z[w[1:]]
        L[a][a] += 1
        L[a][b] -= 1
    assert all(sum(row) == 0 for row in L)
    assert len(labels) == (len(edges) and len(list(admissible(n - 1, False))))
    root = z['0' * (n - 1)]
    return determinant([[row[j] for j in range(len(labels)) if j != root]
                        for i, row in enumerate(L) if i != root])


def compressed_tree_count(n):
    edges = list(admissible(n, True))
    branch = sorted(w for w in admissible(n-1, False)
                    if w.startswith('0') and w.endswith('0'))
    assert branch[0] == '0' * (n - 1)
    z = {w: i for i, w in enumerate(branch)}
    L = [[0] * len(branch) for _ in branch]
    for w in branch:
        for b in '01':
            successor = w[1:] + b
            steps = 0
            while not (successor[0] == successor[-1] == '0'):
                successor = successor[1:] + '0'
                steps += 1
                assert steps <= n
            assert successor in z
            L[z[w]][z[w]] += 1
            L[z[w]][z[successor]] -= 1
    return determinant([r[1:] for r in L[1:]]),len(edges),len(branch)


def max_support_check(n):
    """Exhaustive min-deletion test, independent of the extremal theorem."""
    edges = list(admissible(n, False))
    verts = sorted({w[:-1] for w in edges} | {w[1:] for w in edges})
    z = {v:i for i,v in enumerate(verts)}
    A = [(z[w[:-1]], z[w[1:]]) for w in edges]
    D = [0] * len(verts)
    for a,b in A:
        D[a] += 1;D[b] -= 1
    K = sum(d > 0 for d in D)
    good = []
    for removed in combinations(range(len(edges)), K):
        d = D.copy()
        for j in removed:
            a,b=A[j];d[a]-=1;d[b]+=1
        if all(t==0 for t in d): good.append(removed)
    expected = tuple(i for i,w in enumerate(edges) if w[0] == w[-1] == '1')
    assert good == [expected], (n,len(good),expected,good[:2])
    return len(edges),K


def direct_cycles(n):
    target = set(admissible(n, True))
    length = len(target)
    seen = set()
    for tuple_ in product('01', repeat=length):
        s=''.join(tuple_)
        if '11' in s or s[0] == s[-1] == '1': continue
        windows = {''.join(s[(i+j) % length] for j in range(n)) for i in range(length)}
        if windows != target: continue
        seen.add(min(s[i:] + s[:i] for i in range(length)))
    return len(seen)


def main():
    rows = {int(n):(int(w),int(v),int(k)) for n,w,v,k in list(csv.reader(open(sys.argv[1],encoding='utf-8')))}
    for n in range(2,13):
        result = full_tree_count(n)
        assert result == rows[n][2], (n,result,rows[n][2])
    print('FULL_GRAPH_DETERMINANTS_OK_2_TO_12',flush=True)
    for n in range(3,16):
        r,words,vertices = compressed_tree_count(n)
        assert (words, vertices, r) == rows[n], (n, r, rows[n])
    print('INDEPENDENT_COMPRESSED_BAREISS_OK_3_TO_15',flush=True)
    for n in range(2,8):
        a,k=max_support_check(n)
        assert a-k == rows[n][0]
    print('UNIQUE_MAXIMAL_SUPPORT_ENUMERATION_OK_2_TO_7',flush=True)
    for n in range(2,7):
        assert direct_cycles(n) == rows[n][2]
    print('DIRECT_CIRCULAR_WORDS_OK_2_TO_6',flush=True)
    print('VERIFY_OK',flush=True)

if __name__=='__main__':main()
