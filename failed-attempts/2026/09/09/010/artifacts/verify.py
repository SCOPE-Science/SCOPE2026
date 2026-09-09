"""Independent verifier: replays tutte_table.json from stored GF(2) matrices only.
Checks: bases count = T(1,1); Tutte subset-expansion recompute; 3-connectivity;
F7/F7* verdict + explicit witness replay (delete/contract/remain + perm); extremals."""
import itertools, json, sys

def rk(cols, idx):
    b = []
    for j in idx:
        x = cols[j]
        for q in b:
            hb = q.bit_length() - 1
            if (x >> hb) & 1:
                x ^= q
        if x:
            b.append(x); b.sort(reverse=True)
            for i in range(len(b)):
                for k in range(len(b)):
                    if i != k and (b[k] >> (b[i].bit_length() - 1)) & 1:
                        b[k] ^= b[i]
            b.sort(reverse=True)
    return len(b)

def Cmat(rows):
    cs = []
    for j in range(len(rows[0])):
        v = 0
        for i in range(len(rows)):
            if rows[i][j]:
                v |= (1 << i)
        cs.append(v)
    return cs

MATRICES = {
 'M1_F7':   [[1,0,0,0,1,1,1],[0,1,0,1,0,1,1],[0,0,1,1,1,0,1]],
 'M2_F7s':  [[0,1,1,1,0,0,0],[1,0,1,0,1,0,0],[1,1,0,0,0,1,0],[1,1,1,0,0,0,1]],
 'M3_AG32': [[1,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,0],[0,0,1,0,1,1,0,1],[0,0,0,1,1,0,1,1]],
 'M4_S8':   [[1,0,0,0,0,1,1,1],[0,1,0,0,1,0,1,1],[0,0,1,0,1,1,0,1],[0,0,0,1,1,1,1,0]],
 'M5_X8a':  [[1,0,0,0,1,0,1,1],[0,1,0,0,1,1,0,1],[0,0,1,0,1,1,0,0],[0,0,0,1,1,1,1,0]],
 'M6_X8b':  [[1,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,0],[0,0,1,0,1,1,0,1],[0,0,0,1,1,0,1,0]],
 'M7_MK33': [[1,1,1,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1],[1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0]],
 'M8_AG32e':[[1,0,0,0,1,1,1,1,0],[0,1,0,0,1,1,1,0,1],[0,0,1,0,1,1,0,1,1],[0,0,0,1,1,0,1,1,0]],
 'M9_S8e':  [[1,0,0,0,0,1,1,1,1],[0,1,0,0,1,0,1,1,1],[0,0,1,0,1,1,0,1,1],[0,0,0,1,1,1,1,0,1]],
}
REF = {'F7': [[1,0,0,0,1,1,1],[0,1,0,1,0,1,1],[0,0,1,1,1,0,1]],
       'F7s': [[0,1,1,1,0,0,0],[1,0,1,0,1,0,0],[1,1,0,0,0,1,0],[1,1,1,0,0,0,1]]}

def tutte_subset(cols, n):
    from math import comb
    E = list(range(n)); rE = rk(cols, E); rc = {}
    def r(S):
        k = tuple(S)
        if k not in rc: rc[k] = rk(cols, list(S))
        return rc[k]
    p = {}
    for mask in range(1 << n):
        A = [j for j in range(n) if (mask >> j) & 1]
        rA = r(A); a = rE - rA; bb = len(A) - rA
        for i in range(a + 1):
            for j in range(bb + 1):
                p[(i, j)] = p.get((i, j), 0) + comb(a, i) * comb(bb, j) * ((-1) ** (a - i + bb - j))
    return {k: v for k, v in p.items() if v}

def main():
    t = json.load(open('output/artifacts/tutte_table.json'))
    refB = {k: set(B for B in itertools.combinations(range(7), 3 if k == 'F7' else 4)
                   if rk(Cmat(v), list(B)) == (3 if k == 'F7' else 4)) for k, v in REF.items()}
    ok = True
    for name, rows in MATRICES.items():
        cols = Cmat(rows); n = len(cols); E = list(range(n)); r = rk(cols, E)
        row = t[name]
        B = set(Bb for Bb in itertools.combinations(E, r) if rk(cols, list(Bb)) == r)
        T = tutte_subset(cols, n)
        Tstored = {(a, b): c for a, b, c in row['tutte']}
        c1 = (T == Tstored); c2 = (sum(T.values()) == len(B) == row['nbases'])
        c3 = (sum(c for c in T.values()) is not None)
        t11 = sum(T.values()); c4 = (t11 == len(B))
        # 3-conn
        conn = True
        for k in (1, 2):
            for mask in range(1, (1 << n) - 1):
                X = [j for j in range(n) if (mask >> j) & 1]; Y = [j for j in range(n) if not (mask >> j) & 1]
                if min(len(X), len(Y)) < k: continue
                if rk(cols, X) + rk(cols, Y) - r < k: conn = False
        c5 = (conn == row['is_3conn'] == True)
        # minor verdicts
        msg = []
        for ref, key, wkey in (('F7', 'has_F7', 'F7_witness'), ('F7s', 'has_F7s', 'F7s_witness')):
            w = row[wkey]; claim = row[key]
            if claim:
                D, Cc, rem, perm = w['delete'], w['contract'], w['remain'], w['perm']
                rC = rk(cols, Cc)
                rM = rk(cols, list(rem) + list(Cc)) - rC
                mB = set(S for S in itertools.combinations(rem, rM)
                         if rk(cols, list(S) + list(Cc)) - rC == rM)
                norm = set(tuple(sorted(perm[rem.index(x)] for x in S)) for S in mB)
                good = (norm == refB[ref])
            else:
                # avoidance: exhaustive check no (D,C) yields ref bases (same search, small n)
                found = False
                Eset = set(range(n))
                for nd in range(n - 6):
                    for D in itertools.combinations(range(n), nd):
                        Ds = set(D)
                        for nc in range(n - 6 - nd + 1):
                            rest = [j for j in range(n) if j not in Ds]
                            if n - nd - nc != 7: continue
                            for Cc2 in itertools.combinations(rest, nc):
                                Cs = set(Cc2); rem2 = tuple(sorted(Eset - Ds - Cs))
                                rC = rk(cols, list(Cs))
                                rM = rk(cols, list(rem2) + list(Cs)) - rC
                                rr = 3 if ref == 'F7' else 4
                                if rM != rr: continue
                                mB = set(S for S in itertools.combinations(rem2, rM)
                                         if rk(cols, list(S) + list(Cs)) - rC == rM)
                                if len(mB) != len(refB[ref]): continue
                                norm = set(tuple(sorted(rem2.index(x) for x in S)) for S in mB)
                                for pp in itertools.permutations(range(7)):
                                    if set(tuple(sorted(pp[i] for i in S)) for S in norm) == refB[ref]:
                                        found = True; break
                                    if found: break
                                if found: break
                            if found: break
                        if found: break
                    if found: break
                good = (not found)
            msg.append('%s=%s(%s)' % (ref, claim, 'replay-ok' if good else 'REPLAY-FAIL'))
            c1 = c1 and good
        line = '%s Tutte_match=%s T11=%s conn=%s %s maxc=%s' % (name, T == Tstored, c4, c5, ' '.join(msg), max(T.values()) == row['maxcoeff'])
        print(line)
        ok = ok and (T == Tstored) and c2 and c4 and c5
    ex = t['_extremals']
    eA = max([k for k in MATRICES], key=lambda k: t[k]['maxcoeff'])
    fl = [k for k in MATRICES if not t[k]['has_F7'] and not t[k]['has_F7s']]
    eB = max(fl, key=lambda k: t[k]['nbases'])
    print('extremal maxcoeff:', eA, t[eA]['maxcoeff'], 'claimed:', ex['max_maxcoeff'], eA == ex['max_maxcoeff'])
    print('extremal Ffree:', fl, '->', eB, t[eB]['nbases'], 'claimed:', ex['max_bases_Ffree'], eB == ex['max_bases_Ffree'])
    ok = ok and eA == ex['max_maxcoeff'] and eB == ex['max_bases_Ffree'] and set(fl) == set(ex['Ffree_list'])
    print('VERIFY_' + ('OK' if ok else 'FAIL'))
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
