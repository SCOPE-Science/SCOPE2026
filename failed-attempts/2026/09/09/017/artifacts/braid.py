"""Braid closure builder: word on n strands -> fat-graph diagram. Bounded step."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from pbuilder import bracket_of, det_of_bracket, P0, P1


def braid_closure(n, word):
    """word: list of (i, sign) with i in 1..n-1 (sigma_i^sign). Returns cr, edges."""
    cr = {}; edges = {}; eid = [0]; cid = [0]

    def new_edge(a=None):
        eid[0] += 1
        edges[eid[0]] = [] if a is None else [a]
        return eid[0]

    def reg(e, c, p):
        edges[e].append((c, p))

    # strands at levels: live edges at current bottom of each strand position
    # positions 0..n-1; strand segments vertical. Crossing sigma_i: positions i-1,i.
    # Represent crossing with ports W,E (left strand, right strand in), W2,E2 out.
    # Use generic 4-port crossing with over/under along (inL->outR?) For sigma_i^+:
    # left strand over right: left in (WL) exits lower-right (ER); right in (EL)... define
    # ports: NW (left in), NE (right in), SW (left out), SE (right out). sigma_i^+: left over right:
    # over=(NW,SE)?? left strand goes NW->SE (ends lower-right): yes for positive; under=(NE,SW).
    # sigma_i^-: over=(NE,SW), under=(NW,SE).
    live = [new_edge() for _ in range(n)]
    tops = list(live)
    for (i, s) in word:
        a = i - 1; b = i
        eL, eR = live[a], live[b]
        oL = new_edge(); oR = new_edge()
        cid[0] += 1; c = cid[0]
        if s > 0:
            over, under = ('NW', 'SE'), ('NE', 'SW')
        else:
            over, under = ('NE', 'SW'), ('NW', 'SE')
        cr[c] = {'pos': (float(i), -float(cid[0])),
                 'ports': {'NW': eL, 'NE': eR, 'SE': oL, 'SW': oR},
                 'over': over, 'under': under, 'colsign': s}
        reg(eL, c, 'NW'); reg(eR, c, 'NE'); reg(oL, c, 'SE'); reg(oR, c, 'SW')
        # after crossing, strands swap positions: position a holds strand from oR? left strand exits SE(right side)
        live[a], live[b] = oR, oL
    # trace closure: bottom position j to top position j
    def merge(ek, ed):
        if ek == ed:
            return
        for end in edges[ed]:
            edges[ek].append(end)
        del edges[ed]
        for c, d in cr.items():
            for p, e in d['ports'].items():
                if e == ed:
                    d['ports'][p] = ek
    for j in range(n):
        merge(tops[j], live[j])
    return cr, edges


if __name__ == '__main__':
    # T(3,4) = closure of (s1 s2)^4
    word = [(1, 1), (2, 1)] * 4
    cr, edges = braid_closure(3, word)
    B = bracket_of(cr, edges, P0, P1)
    print('T(3,4) det=%.3f' % det_of_bracket(B), dict(sorted((k, v) for k, v in B.items() if v != 0)))
    print('target bracket: {12:1, 4:1, -8:-1}')
    # trefoil: closure of s1^3 on 2 strands
    cr2, e2 = braid_closure(2, [(1, 1)] * 3)
    B2 = bracket_of(cr2, e2, P0, P1)
    print('trefoil det=%.3f' % det_of_bracket(B2), dict(sorted((k, v) for k, v in B2.items() if v != 0)))
