"""Lane-56 census builder: explicit 2-generated nonabelian groups, orders 48-64.
Stdlib + numpy only. Emits CSV table + words.json certificates + console run log."""
import json, math, csv, sys, os
import numpy as np

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)))

def finalize(els, mul, pres, struct, order_expect):
    """els: list of hashables (identity FIRST). mul(p,q)->element. Returns G dict."""
    n = len(els)
    assert n == order_expect, (struct, n, order_expect)
    idx = {v: i for i, v in enumerate(els)}
    assert len(idx) == n
    T = [[0]*n for _ in range(n)]
    for i, p in enumerate(els):
        for j, q in enumerate(els):
            T[i][j] = idx[mul(p, q)]
    e = 0
    for i in range(n):
        assert T[e][i] == i and T[i][e] == i, struct
    for i in range(n):
        Ti = T[i]
        for j in range(n):
            ij = Ti[j]
            Tij = T[ij]
            Tj = T[j]
            for k in range(n):
                if Tij[k] != Ti[Tj[k]]:
                    raise AssertionError((struct, i, j, k))
    inv = [None]*n
    for i in range(n):
        for j in range(n):
            if T[i][j] == e and T[j][i] == e:
                inv[i] = j
                break
        assert inv[i] is not None, (struct, i)
    wit = None
    for i in range(n):
        for j in range(n):
            if T[i][j] != T[j][i]:
                wit = (i, j)
                break
        if wit:
            break
    assert wit is not None, struct
    return {"els": els, "T": T, "inv": inv, "e": e, "n": n,
            "pres": pres, "struct": struct, "wit": wit}

def build_twisted(m, t, name, pres):
    """<r,s | r^m=s^2=1, srs=r^t>; requires t^2=1 mod m. Dihedral t=m-1."""
    assert (t*t) % m == 1, (m, t)
    els = [(ee, k) for ee in (0, 1) for k in range(m)]
    def mul(p, q):
        e1, k1 = p
        e2, k2 = q
        if e1 == 0 and e2 == 0:
            return (0, (k1+k2) % m)
        if e1 == 0:
            return (1, (t*k1+k2) % m)
        if e2 == 0:
            return (1, (k1+k2) % m)
        return (0, (t*k1+k2) % m)
    return finalize(els, mul, pres, name, 2*m)

def build_dihedral(m):
    return build_twisted(m, m-1, f"Dihedral_2x{m}",
                         f"<r,s|r^{m}=s^2=1,srs=r^-1> dihedral order {2*m}")

def build_frob(q, p, r, name):
    assert pow(r, p, q) == 1 and (r % q) != 1, (q, p, r)
    els = [(x, y) for x in range(q) for y in range(p)]
    pw = [pow(r, y, q) for y in range(p)]
    def mul(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return ((x1 + pw[y1]*x2) % q, (y1+y2) % p)
    return finalize(els, mul, f"<x,y|x^{q}=y^{p}=1,yxy^-1=x^{r}> frob {name}",
                    name, q*p)

def build_f63():
    q, p, r = 7, 9, 2
    assert pow(r, 3, q) == 1
    els = [(x, y) for x in range(q) for y in range(p)]
    pw = [pow(r, y, q) for y in range(p)]
    def mul(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return ((x1 + pw[y1]*x2) % q, (y1+y2) % p)
    return finalize(els, mul, "<x,y|x^7=y^9=1,yxy^-1=x^2> C7xC9 via C3 quotient",
                    "Frob_C7_C9", 63)

def build_dic(M, name):
    assert M % 2 == 0
    half = M//2
    els = [(k, j) for j in (0, 1) for k in range(M)]
    def mul(p1, p2):
        k1, j1 = p1
        k2, j2 = p2
        if j1 == 0 and j2 == 0:
            return ((k1+k2) % M, 0)
        if j1 == 0:
            return ((k1+k2) % M, 1)
        if j2 == 0:
            return ((k1-k2) % M, 1)
        return ((k1-k2+half) % M, 0)
    return finalize(els, mul, f"<a,x|a^{M}=1,x^2=a^{half},x^-1ax=a^-1> dicyclic {name}",
                    name, 2*M)

def build_gl23():
    mats = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a*d-b*c) % 3 != 0:
                        mats.append((a, b, c, d))
    assert len(mats) == 48
    mats.sort(key=lambda m: (0 if m == (1, 0, 0, 1) else 1, m))
    def mul(p, q):
        a, b, c, d = p
        w, x, y, z = q
        return ((a*w+b*y) % 3, (a*x+b*z) % 3, (c*w+d*y) % 3, (c*x+d*z) % 3)
    return finalize(mats, mul, "GL(2,3) 2x2 matrices/F3 det!=0, order 48",
                    "GL23", 48)

def perm_mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def build_S3():
    import itertools
    els = sorted(itertools.permutations(range(3)))
    els.sort(key=lambda m: (0 if m == (0, 1, 2) else 1, m))
    return els

def build_A5():
    import itertools
    def sign(p):
        inv = sum(1 for i in range(5) for j in range(i+1, 5) if p[i] > p[j])
        return 1 if inv % 2 == 0 else -1
    els = sorted([p for p in itertools.permutations(range(5)) if sign(p) == 1])
    assert len(els) == 60
    els.sort(key=lambda m: (0 if m == (0, 1, 2, 3, 4) else 1, m))
    return finalize(els, perm_mul, "A5 even permutations of 5, order 60",
                    "A5", 60)

def build_heis(p):
    els = [(x, y, z) for x in range(p) for y in range(p) for z in range(p)]
    def mul(p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return ((x1+x2) % p, (y1+y2) % p, (z1+z2+x1*y2) % p)
    return els, mul

def build_direct(elsA, mulA, elsB, mulB, pres, struct):
    els = [(a, b) for a in elsA for b in elsB]
    def mul(p1, p2):
        return (mulA(p1[0], p2[0]), mulB(p1[1], p2[1]))
    return finalize(els, mul, pres, struct, len(elsA)*len(elsB))

def closure_set(T, e, gens):
    seen = {e}
    stack = [e]
    while stack:
        g = stack.pop()
        for s in gens:
            h = T[g][s]
            if h not in seen:
                seen.add(h)
                stack.append(h)
    return seen

def find_canonical(T, e):
    n = len(T)
    for i in range(n):
        if i == e:
            continue
        for j in range(n):
            if j == e or j == i:
                continue
            if len(closure_set(T, e, (i, j))) == n:
                return (i, j)
    return None

def bfs_from(T, src, S):
    n = len(T)
    dist = [-1]*n
    par = [-1]*n
    pe = [-1]*n
    dist[src] = 0
    q = [src]
    qi = 0
    while qi < len(q):
        g = q[qi]
        qi += 1
        for s in S:
            h = T[g][s]
            if dist[h] == -1:
                dist[h] = dist[g]+1
                par[h] = g
                pe[h] = s
                q.append(h)
    return dist, par, pe

def analyze(G, a, b, pair_kind):
    T, e, n, inv = G["T"], G["e"], G["n"], G["inv"]
    assert len(closure_set(T, e, (a, b))) == n, "generators must generate"
    ai, bi = inv[a], inv[b]
    S = []
    for g in (a, ai, b, bi):
        if g not in S:
            S.append(g)
    assert e not in S
    d = len(S)
    lmap = {}
    lmap[a] = 'a'
    if ai != a:
        lmap[ai] = 'A'
    if b not in lmap:
        lmap[b] = 'b'
    if bi != b and bi not in lmap:
        lmap[bi] = 'B'
    assert a in lmap and b in lmap, (a, b, ai, bi)
    back = {v: k for k, v in lmap.items()}
    A = np.zeros((n, n))
    for g in range(n):
        Tg = T[g]
        for s in S:
            A[g, Tg[s]] = 1.0
    for g in range(n):
        assert abs(A[g].sum()-d) < 1e-12
    dist0, par0, pe0 = bfs_from(T, e, S)
    assert all(x >= 0 for x in dist0), "disconnected!"
    words = ['']*n
    words[e] = ''
    order = sorted(range(n), key=lambda g: dist0[g])
    for g in order:
        if g == e:
            continue
        words[g] = words[par0[g]] + lmap[pe0[g]]
        assert len(words[g]) == dist0[g]
    for g in range(n):
        cur = e
        for ch in words[g]:
            cur = T[cur][back[ch]]
        assert cur == g, (g, words[g])
    D = 0
    for src in range(n):
        dd, _, _ = bfs_from(T, src, S)
        assert all(x >= 0 for x in dd)
        D = max(D, max(dd))
    assert D == max(dist0)
    wit = next(g for g in range(n) if dist0[g] == D)
    w, V = np.linalg.eigh(A)
    mu = w
    lam1, lam2, lam3 = mu[-1], mu[-2], mu[-3]
    assert abs(lam1-d) < 1e-6, (lam1, d)
    res = []
    for j in (n-1, n-2, n-3):
        v = V[:, j]
        r = float(np.linalg.norm(A@v-mu[j]*v))
        res.append(r)
    rho = max(res)
    w2 = np.linalg.eig(A)[0]
    desc = sorted((complex(z).real for z in w2), reverse=True)
    lam2b = desc[1]
    agree = abs(lam2-lam2b)
    tr = float(mu.sum())
    tr2 = float((mu**2).sum())
    assert abs(tr) < 1e-6, tr
    assert abs(tr2-n*d) < 1e-4, (tr2, n*d)
    sep12 = lam1-lam2
    sep23 = lam2-lam3
    # Top separation pins the nearby true eigenvalue below d (d simple by
    # connectedness/Perron); lower spectrum may have multiplicity (sep23~0).
    top_sep_ok = bool(res[0]+res[1] < sep12)
    mult2 = int(sum(1 for x in mu if abs(x-lam2) < 1e-6))
    gap = d-lam2
    rho_rep = max(rho, 5e-10)  # inflated: covers all fp slop by ~5 orders
    glo, ghi = gap-2*rho_rep, gap+2*rho_rep
    return {
        "a": a, "b": b, "S": S, "degree": d, "letters": lmap,
        "diameter": D, "witness": wit, "witness_word": words[wit],
        "dist0": dist0, "words": words,
        "lambda2_eigh": float(lam2), "lambda2_eig": float(lam2b),
        "agree": float(agree), "resid": [float(x) for x in res],
        "rho": float(rho),         "gap": float(gap),
        "gap_lo": float(glo), "gap_hi": float(ghi),
        "sep12": float(sep12), "sep23": float(sep23), "sep_ok": bool(top_sep_ok),
        "mult2": int(mult2),
        "trace": float(tr), "trace2": float(tr2),
        "spectrum": [round(float(x), 6) for x in mu],
        "pair_kind": pair_kind,
    }

def label(G, i):
    return repr(G["els"][i])

def main():
    groups = []
    for m in (24, 25, 26, 27, 28, 29, 30, 31, 32):
        groups.append(build_dihedral(m))
    groups.append(build_frob(11, 5, 3, "Frob_C11_C5_55"))
    groups.append(build_frob(19, 3, 7, "Frob_C19_C3_57"))
    groups.append(build_f63())
    groups.append(build_frob(13, 4, 5, "Frob_C13_C4_52"))
    groups.append(build_dic(24, "Dic12_48"))
    groups.append(build_dic(28, "Dic14_56"))
    groups.append(build_gl23())
    S3 = build_S3()
    C8 = list(range(8))
    groups.append(build_direct(S3, perm_mul, C8, lambda p, q: (p+q) % 8,
                "S3 x C8 direct product, order 48", "S3xC8_48"))
    H3, mH3 = build_heis(3)
    groups.append(build_direct(H3, mH3, [0, 1], lambda p, q: (p+q) % 2,
                "Heis(F3) x C2 direct product, order 54", "Heis3xC2_54"))
    groups.append(build_A5())
    U4, mU4 = build_heis(4)
    groups.append(finalize(U4, mU4, "<X,Y|X^4=Y^4=1,[X,Y]=Z central> UT3(Z4) order 64",
                    "UT3Z4_64", 64))
    D8 = build_dihedral(4)
    D8els = D8["els"]
    D8T = D8["T"]
    D8idx = {v: i for i, v in enumerate(D8els)}
    def d8mul(p, q):
        return D8els[D8T[D8idx[p]][D8idx[q]]]
    # D8xC8 is NOT 2-generated (abelianization C2xC2xC8 needs 3 gens): record the
    # complete lex-pair search failure as the 2-generation filter certificate.
    G_d8c8 = build_direct(D8els, d8mul, C8, lambda p, q: (p+q) % 8,
                "D8 x C8 direct product, order 64 (NOT 2-generated)", "D8xC8_64")
    assert find_canonical(G_d8c8["T"], G_d8c8["e"]) is None, "D8xC8 unexpectedly 2-gen"
    print("D8xC8_64: certified NOT 2-generated (all 4096 ordered pairs fail closure)",
          flush=True)
    # Classic order-64 2-groups instead: semidihedral + modular (t^2=1 mod 32).
    groups.append(build_twisted(32, 15, "Semidihedral_64",
                "<r,s|r^32=s^2=1,srs=r^15> semidihedral order 64"))
    groups.append(build_twisted(32, 17, "Modular_64",
                "<a,b|a^32=b^2=1,bab=a^17> modular 2-group order 64"))
    groups.append(build_dic(32, "Q64_Dic16"))
    print(f"built {len(groups)} groups", flush=True)

    rows = []
    gid = 0
    for G in groups:
        n = G["n"]
        ab = find_canonical(G["T"], G["e"])
        assert ab is not None, G["struct"]
        a, b = ab
        R = analyze(G, a, b, "canonical")
        R.update({"id": f"R{gid:02d}", "struct": G["struct"], "order": n,
                  "pres": G["pres"], "gen": f"{label(G,a)} ; {label(G,b)}",
                  "nonab_wit": [int(x) for x in G["wit"]]})
        rows.append((G, R))
        print(f"{R['id']} {G['struct']:16s} n={n:3d} gen=({a},{b}) d={R['degree']} "
              f"D={R['diameter']:3d} lam2={R['lambda2_eigh']:.6f} gap={R['gap']:.6f} "
              f"agree={R['agree']:.1e} rho={R['rho']:.1e} sep_ok={R['sep_ok']}", flush=True)
        gid += 1
    for G, R in list(rows):
        if G["struct"] in ("Dihedral_2x24", "Dihedral_2x32"):
            m = G["n"]//2
            els = G["els"]
            s = els.index((1, 0))
            rs = els.index((1, 1))
            R2 = analyze(G, s, rs, "alternate-bireflection")
            R2.update({"id": f"R{gid:02d}", "struct": G["struct"]+":alt", "order": G["n"],
                       "pres": G["pres"], "gen": f"{label(G,s)} ; {label(G,rs)}",
                       "nonab_wit": [int(x) for x in G["wit"]]})
            rows.append((G, R2))
            print(f"{R2['id']} {R2['struct']:16s} n={G['n']:3d} gen=({s},{rs}) d={R2['degree']} "
                  f"D={R2['diameter']:3d} lam2={R2['lambda2_eigh']:.6f} gap={R2['gap']:.6f} "
                  f"agree={R2['agree']:.1e} rho={R2['rho']:.1e} sep_ok={R2['sep_ok']}", flush=True)
            gid += 1

    Dmax = max(R["diameter"] for _, R in rows)
    ext = [R["id"] for _, R in rows if R["diameter"] == Dmax]
    dec = []
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            A1, A2 = rows[i][1], rows[j][1]
            if A1["gap_lo"] > A2["gap_hi"] and A1["diameter"] > A2["diameter"]:
                dec.append((A1["id"], A2["id"], A1["diameter"]-A2["diameter"],
                            A1["gap_lo"]-A2["gap_hi"]))
            elif A2["gap_lo"] > A1["gap_hi"] and A2["diameter"] > A1["diameter"]:
                dec.append((A2["id"], A1["id"], A2["diameter"]-A1["diameter"],
                            A2["gap_lo"]-A1["gap_hi"]))
    dec.sort(key=lambda t: (t[2], t[3]), reverse=True)
    print(f"EXTREMAL Dmax={Dmax} rows={ext}", flush=True)
    print(f"DECOUPLING pairs (bigger-D yet bigger-gap): {len(dec)}; top={dec[:5]}", flush=True)
    Ds = np.array([R["diameter"] for _, R in rows], float)
    Gs = np.array([R["gap"] for _, R in rows], float)
    corr = float(np.corrcoef(Ds, Gs)[0, 1])
    print(f"Pearson corr(diameter,gap)={corr:.4f}", flush=True)

    with open(os.path.join(ART, "cayley_table.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "order", "structure", "presentation", "generators",
                    "pair_kind", "degree", "diameter", "lambda2_eigh", "lambda2_eig",
                    "agree", "gap", "gap_lo", "gap_hi", "sep_ok", "extremal",
                    "witness_idx", "witness_word"])
        for _, R in rows:
            w.writerow([R["id"], R["order"], R["struct"], R["pres"], R["gen"],
                        R["pair_kind"], R["degree"], R["diameter"],
                        f"{R['lambda2_eigh']:.6f}", f"{R['lambda2_eig']:.6f}",
                        f"{R['agree']:.2e}", f"{R['gap']:.6f}",
                        f"{R['gap_lo']:.6f}", f"{R['gap_hi']:.6f}",
                        int(R["sep_ok"]), int(R["id"] in ext),
                        R["witness"], R["witness_word"]])
    J = {"rows": [], "meta": {"Dmax": Dmax, "extremal": ext,
                              "corr_diameter_gap": corr,
                              "decoupling_top": [list(t) for t in dec[:10]],
                              "decoupling_count": len(dec)}}
    for G, R in rows:
        J["rows"].append({
            "id": R["id"], "order": R["order"], "struct": R["struct"],
            "pres": R["pres"], "gen_idx": [int(R["a"]), int(R["b"])],
            "gen": R["gen"], "pair_kind": R["pair_kind"],
            "degree": R["degree"], "S": [int(x) for x in R["S"]],
            "diameter": R["diameter"], "witness": int(R["witness"]),
            "witness_word": R["witness_word"],
            "gap": R["gap"], "gap_lo": R["gap_lo"], "gap_hi": R["gap_hi"],
            "lambda2_eigh": R["lambda2_eigh"], "lambda2_eig": R["lambda2_eig"],
            "agree": R["agree"], "rho": R["rho"],
            "sep12": R["sep12"], "sep23": R["sep23"], "sep_ok": R["sep_ok"],
            "mult2": R["mult2"],
            "extremal": bool(R["id"] in ext),
            "mult": G["T"], "dist0": [int(x) for x in R["dist0"]],
            "words": R["words"], "spectrum": R["spectrum"],
            "nonab_wit": R["nonab_wit"],
        })
    with open(os.path.join(ART, "words.json"), "w") as f:
        json.dump(J, f)
    print(f"wrote cayley_table.csv + words.json ({len(J['rows'])} rows)", flush=True)

if __name__ == "__main__":
    main()
