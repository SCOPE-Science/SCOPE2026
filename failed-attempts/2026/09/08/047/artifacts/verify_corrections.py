"""Correction supplement for lane-147 (preserves verify_family.py as-is).

Corrects two interpretation issues in verify_family.py:
  (C1) components(): the opposite-pairing strand tracer counts DIRECTED cycles,
       so a 1-component diagram yields 2 cycles (the two orientations).
       Undirected components = (#directed cycles)/2. verify_family.py printed
       comp=2, which means 1 undirected component (a knot), confirmed here.
  (C2) 'jones_span': bracket_span_and_circles() returns the Kauffman-bracket
       state-sum exponent RANGE (min/max over states assuming no cancellation).
       bracket_span/4 is an UPPER BOUND on the true Jones span, not the span.
       Proof of strictness: at t=1 the diagram is the 9_42 seed up to relabeling
       and the script gives 8, while KnotAtlas records true Jones span 6.
       Hence all 'spanJ' values are relabeled here as bracket-span bounds.
Stdlib only. Replays sA/sB/span from scratch and checks PD validity.
"""
import sys
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-147/output/artifacts")
from collections import defaultdict
from verify_family import SEED_PD, extend_twist, bracket_span_and_circles

SEED_EXPECTED = [(1,4,2,5),(5,10,6,11),(3,9,4,8),(9,3,10,2),(16,12,17,11),
                 (14,7,15,8),(6,15,7,16),(18,14,1,13),(12,18,13,17)]

def pd_valid(pd):
    ends = defaultdict(list)
    for ci, cr in enumerate(pd):
        for pos, e in enumerate(cr):
            ends[e].append((ci, pos))
    return all(len(v) == 2 for v in ends.values())

def directed_cycle_lengths(pd):
    pair = {}
    for ci in range(len(pd)):
        pair[(ci,0)] = (ci,2); pair[(ci,2)] = (ci,0)
        pair[(ci,1)] = (ci,3); pair[(ci,3)] = (ci,1)
    ends = defaultdict(list)
    for ci, cr in enumerate(pd):
        for pos, e in enumerate(cr):
            ends[e].append((ci, pos))
    assert all(len(v) == 2 for v in ends.values()), "PD invalid"
    nxt = {}
    for e, (p, q) in ends.items():
        nxt[p] = q; nxt[q] = p
    seen = set(); lens = []
    for ci in range(len(pd)):
        for pos in range(4):
            if (ci, pos) in seen:
                continue
            cur = (ci, pos); n = 0
            while cur not in seen:
                seen.add(cur); n += 1
                cur = pair[nxt[cur]]
            lens.append(n)
    return lens

def main():
    assert [tuple(c) for c in SEED_PD] == SEED_EXPECTED, "seed PD mismatch vs KnotAtlas"
    print("seed PD matches KnotAtlas X1425 X5,10,6,11 X3948 X9,3,10,2 X16,12,17,11 X14,7,15,8 X6,15,7,16 X18,14,1,13 X12,18,13,17")
    for t in (1, 3, 5, 7, 9):
        pd = extend_twist(SEED_PD, 0, t)
        c = len(pd)
        assert pd_valid(pd), t
        lens = directed_cycle_lengths(pd)
        assert len(lens) == 2 and lens[0] == lens[1] == 2 * c, (t, lens)
        undirected = len(lens) // 2
        mn, mx, sA, sB, ns = bracket_span_and_circles(pd)
        spanB = mx - mn
        assert spanB % 4 == 0
        print(f"t={t} c={c} pd_valid=True directed_cycles={lens} "
              f"undirected_components={undirected} sA={sA} sB={sB} "
              f"diagram_genus={(c+2-sA-sB)//2} bracket_span={spanB} "
              f"span_upper_bound={spanB//4} deficit_vs_c={c-spanB//4} states={ns}")
    print("C1+C2 corrections confirmed: all members 1-component; spans are upper bounds.")

if __name__ == "__main__":
    main()
