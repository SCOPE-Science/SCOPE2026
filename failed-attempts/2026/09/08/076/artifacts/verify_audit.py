"""Independent verifier: replays artifact tables from logged pairings only."""
import json, math, cmath, sys
import numpy as np

def polygon_data(n):
    a = math.pi / n
    d = math.acosh(1.0 / math.tan(a))
    r_mid = math.tanh(d / 2.0)
    phi = [2.0 * math.pi * j / n for j in range(n)]
    mids = [r_mid * complex(math.cos(p), math.sin(p)) for p in phi]
    tang = [1j * complex(math.cos(p), math.sin(p)) for p in phi]
    return mids, tang

def Tmat(m):
    s = 1.0 / math.sqrt(1 - abs(m) ** 2)
    return s * np.array([[1, -m], [-np.conj(m), 1]], dtype=complex)

def Rmat(theta):
    e = cmath.exp(0.5j * theta)
    return np.array([[e, 0], [0, 1 / e]], dtype=complex)

def gen_frame(mj, tj, mi, ti):
    th = cmath.phase(-ti) - cmath.phase(tj)
    G = Tmat(-mi) @ Rmat(th) @ Tmat(mj)
    return G / np.sqrt(np.linalg.det(G))

def build(n, pairing):
    mids, tang = polygon_data(n)
    pi = {}
    for a, b in pairing: pi[a] = b; pi[b] = a
    pairs = sorted(tuple(sorted(p)) for p in pairing)
    A = [gen_frame(mids[j], tang[j], mids[i], tang[i]) for j, i in pairs]
    def frame_of(s):
        t = tuple(sorted((s, pi[s]))); k = pairs.index(t); lo, hi = t
        return (k, +1) if s == lo else (k, -1)
    def vimage(V, s):
        j = s; i = pi[s]
        if V == (j + 1) % n: return i
        elif V == j: return (i + 1) % n
        else: raise ValueError
    V = 0; s_arr = None; W = np.eye(2, dtype=complex)
    for _ in range(n):
        cand = [(V - 1) % n, V]
        s_out = [s for s in cand if s != s_arr][0] if s_arr is not None else V
        k, e = frame_of(s_out)
        W = (A[k] if e == 1 else np.linalg.inv(A[k])) @ W
        V = vimage(V, s_out); s_arr = pi[s_out]
    closed = (V == 0)
    res = min(np.linalg.norm(W - np.eye(2)), np.linalg.norm(W + np.eye(2))) / 2.0
    return A, res, closed

def word_matrix(A, w):
    M = np.eye(2, dtype=complex)
    Ainv = [np.linalg.inv(G) for G in A]
    for k, e in w:
        M = (A[k] if e == 1 else Ainv[k]) @ M
    return M

def check_file(fn, Wmax, tol=1e-9):
    data = json.load(open(fn))
    n = 8 if "_n8_" in fn else 12
    fails = 0
    # vertex-class smoothness recheck via union-find
    for rec in data:
        pairs = [tuple(p) for p in rec["pairs"]]
        pi = {}
        for a, b in pairs: pi[a] = b; pi[b] = a
        parent = list(range(n))
        def find(x):
            while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for a in range(n):
            b = pi[a]
            ra, rb = find(a), find((b + 1) % n)
            if ra != rb: parent[ra] = rb
            ra, rb = find((a + 1) % n), find(b)
            if ra != rb: parent[ra] = rb
        if len(set(find(v) for v in range(n))) != 1:
            print(f"FAIL smoothness idx={rec['idx']}"); fails += 1
        A, res, closed = build(n, pairs)
        if not closed or res > 1e-6:
            print(f"FAIL relation idx={rec['idx']} res={res}"); fails += 1
        M = word_matrix(A, [tuple(x) for x in rec["word"]])
        L = 2.0 * math.acosh(abs(np.trace(M)) / 2.0)
        if abs(L - rec["sys"]) > 1e-9:
            print(f"FAIL sys idx={rec['idx']} {L} vs {rec['sys']}"); fails += 1
        # W-ball minimality: exhaustive reduced-word scan, assert nothing smaller by >tol
        r = len(A); Ainv = [np.linalg.inv(G) for G in A]
        from collections import deque
        dq = deque()
        for k in range(r):
            for e in (+1, -1):
                M2 = A[k] if e == 1 else Ainv[k]
                dq.append((M2, k, e, ((k, e),)))
        while dq:
            M2, lk, le, w = dq.popleft()
            if len(w) > Wmax: continue
            t = abs(np.trace(M2)) / 2.0
            if t >= 1 + 1e-12:
                (fk, fe), (ek2, ee) = w[0], w[-1]
                if not (fk == ek2 and fe == -ee):
                    L2 = 2.0 * math.acosh(t)
                    if L2 < rec["sys"] - tol:
                        print(f"FAIL minimality idx={rec['idx']}: {L2} < {rec['sys']} at {w}"); fails += 1
                        dq.clear(); break
            if len(w) < Wmax:
                for k in range(r):
                    for e in (+1, -1):
                        if k == lk and e == -le: continue
                        dq.append(((A[k] if e == 1 else Ainv[k]) @ M2, k, e, w + ((k, e),)))
    print(f"{fn}: {'VERIFY_OK' if fails == 0 else 'VERIFY_FAIL'} ({len(data)} rows, {fails} fails)")
    return fails == 0

if __name__ == "__main__":
    ok = True
    ok &= check_file("census_n8_W6.json", 6)
    ok &= check_file("census_n12_W4.json", 4)
    sys.exit(0 if ok else 1)
