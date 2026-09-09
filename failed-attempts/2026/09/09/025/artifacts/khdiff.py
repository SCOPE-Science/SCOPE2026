"""Khovanov differentials + homology over F_p (and Z via SNF for small blocks).
Differential construction: for each edge (state s0, flip A->B at crossing j):
  determine merge/split from circle partitions; tensor-slot maps from canonical
  circle orderings; sign (-1)^{#{B-smoothings before j}}.
Homology per (i,j): build sparse matrix over F_p, rank via dict-based elimination.
Also builds integer matrices for SNF (sympy) on small blocks.
"""
from cube import CONV
from kh import build_state, state_circles, chain_basis

def differential_blocks(word, nstrands, basis, orders, p):
    """Returns dict ((i,q)src -> list of (src_idx, tgt_block, tgt_idx, coef_mod_p)).
    We build per-source-block matrices as dict rows."""
    m = len(word)
    A = tuple(CONV[s] for _, s in word)
    # index maps
    idx = {key: {e: k for k, e in enumerate(v)} for key, v in basis.items()}
    # group edges by source block
    mats = {}  # (src_key, tgt_key) -> dict (r, c) -> val
    n_plus = sum(1 for _, s in word if s == 1)
    n_minus = sum(1 for _, s in word if s == -1)
    for src_key, elts in basis.items():
        si, sq = src_key
        for c, (bits, signs) in enumerate(elts):
            # B-count before j: #{jj<j : bits[jj] != A[jj]}
            for j in range(m):
                if bits[j] != A[j]:
                    continue  # already B; edge flips A->B only
                prej = sum(1 for jj in range(j) if bits[jj] != A[jj])
                sign = -1 if prej % 2 else 1
                bits2 = list(bits); bits2[j] = 1 - bits2[j]; bits2 = tuple(bits2)
                o0 = orders[bits]; o1 = orders[bits2]
                # Kind of the edge from the circle-count change (ground truth):
                # ka==kb alone is NOT sufficient for split (redundant joins can flip
                # into a merge with an adjacent circle). Verified on K1 2026-09-09.
                dc = len(o1) - len(o0)
                assert dc in (1, -1), ("count change", bits, j, len(o0), len(o1))
                # find circles through ports of crossing j in state bits
                _, _, ports0 = build_state(word, nstrands, bits)
                ta, tb, ba, bb = ports0[j]
                # node->circle index in o0
                n2k = {}
                for k, circ in enumerate(o0):
                    for v in circ:
                        n2k[v] = k
                ka = n2k[ta]; kb = n2k[tb]
                # target block key: height h+1 -> i+1, same q (d has q-degree 0).
                # If the target (i+1,sq) block is empty the component is zero: skip.
                tgt_key = (si + 1, sq)
                if tgt_key not in idx:
                    continue
                r = len(o0)
                if dc == 1:
                    # SPLIT: single o0 circle S through ports; outputs = the two o1
                    # circles meeting S's nodes.
                    assert ka == kb, ("split needs ka==kb", bits, j)
                    S = set(o0[ka])
                    outs = [l for l, circ in enumerate(o1) if S & set(circ)]
                    assert len(outs) == 2, ("split outputs", bits, j, outs)
                    lt, lb = outs
                    # Delta on slot ka with sign value v = signs[ka]
                    # positions: remove slot ka, insert (lt, lb) in canonical order
                    others = [signs[t] for t in range(r) if t != ka]
                    lo, hi2 = (lt, lb) if lt < lb else (lb, lt)
                    v = signs[ka]
                    terms = []
                    if v == 1:
                        # v+ -> v+_lo v-_hi + v-_lo v+_hi
                        terms = [({lo: 1, hi2: -1}, 1), ({lo: -1, hi2: 1}, 1)]
                    else:
                        terms = [({lo: -1, hi2: -1}, 1)]
                    for slotvals, coef in terms:
                        newsigns = []
                        for l in range(len(o1)):
                            if l == lo:
                                newsigns.append(slotvals[lo])
                            elif l == hi2:
                                newsigns.append(slotvals[hi2])
                            else:
                                # map: slots of o1 other than lo,hi correspond to o0 slots other than ka, in canonical order
                                # build mapping via shared nodes: circle in o1 (not lo/hi) equals circle in o0 (not ka)? verify by node-set equality where possible
                                newsigns.append(None)
                        # fill others by matching circles: o1 circle that shares nodes with o0 circle t
                        for l in range(len(o1)):
                            if newsigns[l] is None:
                                c1 = o1[l]
                                # find o0 circle (not ka) with max overlap
                                best = None
                                for t in range(r):
                                    if t == ka:
                                        continue
                                    if o0[t] & c1:
                                        best = t
                                        break
                                assert best is not None, ("nomatch", src_key, bits, j)
                                newsigns[l] = signs[best]
                        tgt = idx[tgt_key][(bits2, tuple(newsigns))]
                        key = (src_key, tgt_key)
                        mats.setdefault(key, {})
                        d = mats[key]
                        d[(tgt, c)] = (d.get((tgt, c), 0) + sign * coef) % p
                else:
                    # MERGE: the merged o1 circle T through ports; inputs = the two
                    # o0 circles meeting T's nodes. (Normally {ka,kb}; in the
                    # redundant-join case ka==kb and the partner is the adjacent
                    # circle absorbed by the flip.)
                    n2l = {}
                    for l, circ in enumerate(o1):
                        for v in circ:
                            n2l[v] = l
                    T = n2l[ta]
                    assert n2l[tb] == T and n2l[ba] == T and n2l[bb] == T, \
                        ("merge ports", bits, j)
                    Tnodes = set(o1[T])
                    ins = [t for t in range(r) if Tnodes & set(o0[t])]
                    assert len(ins) == 2, ("merge inputs", bits, j, ins)
                    ka2, kb2 = ins
                    lm = T  # merged circle's canonical slot
                    # m symmetric on (+,-) pairs; order irrelevant.
                    a, b = signs[ka2], signs[kb2]
                    if a == -1 and b == -1:
                        continue
                    out = 1 if (a == 1 and b == 1) else -1
                    newsigns = []
                    for l in range(len(o1)):
                        if l == lm:
                            newsigns.append(out)
                        else:
                            c1 = o1[l]
                            best = None
                            for t in range(r):
                                if t == ka2 or t == kb2:
                                    continue
                                if o0[t] & c1:
                                    best = t
                                    break
                            assert best is not None, ("nomatch-m", src_key, bits, j)
                            newsigns.append(signs[best])
                    tgt = idx[tgt_key][(bits2, tuple(newsigns))]
                    key = (src_key, tgt_key)
                    mats.setdefault(key, {})
                    d = mats[key]
                    d[(tgt, c)] = (d.get((tgt, c), 0) + sign) % p
    # clean zeros
    for key in list(mats):
        mats[key] = {k: v % p for k, v in mats[key].items() if v % p}
        if not mats[key]:
            del mats[key]
    return mats, idx

def rank_modp(nrows, ncols, entries, p):
    """Rank of sparse matrix given as dict (r,c)->v over F_p. rows>=... elimination on columns."""
    # pivot per column; work rows as dicts
    rows = {}
    for (r, c), v in entries.items():
        v %= p
        if v:
            rows.setdefault(r, {})[c] = v
    pivots = {}  # col -> row dict (normalized)
    rank = 0
    inv_cache = {}
    def inv(a):
        if a not in inv_cache:
            inv_cache[a] = pow(a, p - 2, p)
        return inv_cache[a]
    for r in sorted(rows):
        row = {c: v % p for c, v in rows[r].items() if v % p}
        # fully reduce: repeat until no pivot column remains
        while True:
            piv = [c for c in row if c in pivots]
            if not piv:
                break
            c = min(piv)
            pr = pivots[c]
            factor = row[c] * inv(pr[c]) % p
            del row[c]
            if factor:
                for cc, vv in pr.items():
                    if cc == c:
                        continue
                    row[cc] = (row.get(cc, 0) - factor * vv) % p
                    if not row[cc]:
                        del row[cc]
        if not row:
            continue
        c0 = min(row)
        s = inv(row[c0])
        row = {c: v * s % p for c, v in row.items()}
        pivots[c0] = row
        rank += 1
    return rank

def homology_modp(word, nstrands, p):
    n_plus = sum(1 for _, s in word if s == 1)
    n_minus = sum(1 for _, s in word if s == -1)
    basis, orders = chain_basis(word, nstrands, n_plus, n_minus)
    mats, idx = differential_blocks(word, nstrands, basis, orders, p)
    # per block: dim Ker(d_in... careful: d: C^{i} -> C^{i+1}. Betti(i,q) = dim C - rank(incoming) - rank(outgoing).
    from collections import defaultdict
    rank_out = defaultdict(int)  # (src) -> rank
    rank_in = defaultdict(int)
    for (src, tgt), entries in mats.items():
        nrows = len(basis[tgt]); ncols = len(basis[src])
        rk = rank_modp(nrows, ncols, entries, p)
        rank_out[src] += rk
        rank_in[tgt] += rk
    betti = {}
    for key, elts in basis.items():
        betti[key] = len(elts) - rank_in.get(key, 0) - rank_out.get(key, 0)
        assert betti[key] >= 0, (key, betti[key])
    return betti, basis, mats
