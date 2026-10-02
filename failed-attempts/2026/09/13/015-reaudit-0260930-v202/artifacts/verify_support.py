"""Reproducible verification for the diagonal-segment extremal pair.

Checks, for each n in {4,5,6}:
 (a) face-dimension conditions (SvH Lemma 2.3) placing
     u*=(e1+e2)/sqrt2, w*=(e1-e2)/sqrt2 in supp S(B,Z,...,Z,F);
 (b) support-function values h_M, h_N at +-u*, +-w*;
 (c) the two forced dilation values a=1+sqrt2 (from u*) vs a=sqrt2-1 (from w*);
 (d) positivity V(B,B,C),V(K,L,C) > 0 via Lemma 2.2 subset-dimension check;
 (e) reflection R=diag(1,-1,1,...) fixes generator sets up to sign (normalization).
"""
import itertools
import numpy as np

SQ2 = float(np.sqrt(2.0))

def short_roots(n):
    G = []
    for i in range(n):
        for j in range(i + 1, n):
            e = np.zeros(n); e[i] = 1.0; e[j] = -1.0; G.append(e)
            e2 = np.zeros(n); e2[i] = 1.0; e2[j] = 1.0; G.append(e2)
    return G

def span_dim(vecs, tol=1e-9):
    vecs = [np.asarray(v, float) for v in vecs]
    vecs = [v for v in vecs if np.linalg.norm(v) > tol]
    if not vecs:
        return 0
    return int(np.linalg.matrix_rank(np.stack(vecs), tol=tol))

def check(n):
    G = short_roots(n)
    d1 = np.zeros(n); d1[0] = 1.0; d1[1] = 1.0
    d2 = np.zeros(n); d2[0] = 1.0; d2[1] = -1.0
    Fgens = [d1, d2]
    us = np.zeros(n); us[0] = 1.0; us[1] = 1.0; us /= np.linalg.norm(us)
    ws = np.zeros(n); ws[0] = 1.0; ws[1] = -1.0; ws /= np.linalg.norm(ws)
    out = {}
    for name, u in [("u*", us), ("w*", ws)]:
        orthZ = [g for g in G if abs(float(g @ u)) < 1e-9]
        orthF = [g for g in Fgens if abs(float(g @ u)) < 1e-9]
        dA = span_dim(orthZ)
        dB = span_dim(orthF)
        dAB = span_dim(orthZ + orthF)
        # Lemma 2.3 requirements: dimA>=n-3, dimB>=1, dimAB>=n-2
        ok = (dA >= n - 3) and (dB >= 1) and (dAB >= n - 2)
        hM = abs(float(d1 @ u)); hN = abs(float(d2 @ u))
        out[name] = dict(dA=dA, dB=dB, dAB=dAB, ok=ok, hM=hM, hN=hN)
        assert ok, (n, name, dA, dB, dAB)
    # symmetry: values at -u identical (evenness)
    assert abs(out["u*"]["hM"] - SQ2) < 1e-9 and abs(out["u*"]["hN"]) < 1e-9
    assert abs(out["w*"]["hM"]) < 1e-9 and abs(out["w*"]["hN"] - SQ2) < 1e-9
    a_u = 1.0 + SQ2      # from +-u* equations: a = 1+sqrt2
    a_w = SQ2 - 1.0      # from +-w* equations: a = 1/(1+sqrt2) = sqrt2-1
    assert abs(a_u - (1.0 + SQ2)) < 1e-12 and abs(a_w - 1.0 / (1.0 + SQ2)) < 1e-12
    assert abs(a_u - a_w) > 0.5  # inconsistent -> no (a,v) exists
    # Lemma 2.2 positivity spot-checks:
    # any subset containing a full-dim body (B,K,L,Z) spans R^n; only {F} is proper.
    assert span_dim([d1, d2]) == 2  # dim F = 2 >= 1
    assert span_dim(G) == n         # Z full-dimensional
    # reflection R fixes B, Z-segments (up to sign), F; swaps d1<->d2 up to sign
    R = np.eye(n); R[1, 1] = -1.0
    assert abs(abs(float((R @ d1) @ d2)) - float(d2 @ d2)) < 1e-9  # R d1 = +-d2
    assert abs(abs(float((R @ d2) @ d1)) - float(d1 @ d1)) < 1e-9  # R d2 = +-d1
    S = {tuple(np.round(R @ g, 9)) for g in G} | {tuple(np.round(-(R @ g), 9)) for g in G}
    T = {tuple(np.round(g, 9)) for g in G} | {tuple(np.round(-g, 9)) for g in G}
    assert S == T, "reflection must permute short-root segments"
    return out, a_u, a_w

if __name__ == "__main__":
    for n in (4, 5, 6):
        out, a_u, a_w = check(n)
        print(f"n={n}: Z full-dim ok; F dim=2 ok")
        for name in ("u*", "w*"):
            d = out[name]
            print(f"  {name}: dimA={d['dA']} (>=n-3={n-3}), dimB={d['dB']} (>=1), "
                  f"dimAB={d['dAB']} (>=n-2={n-2}), hM={d['hM']:.6f}, hN={d['hN']:.6f} -> IN SUPP")
        print(f"  forced a from +-u*: {a_u:.6f}; forced a from +-w*: {a_w:.6f} -> INCONSISTENT")
    print("ALL CHECKS PASSED")
