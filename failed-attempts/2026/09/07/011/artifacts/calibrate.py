import sys
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-07/output/artifacts")
from braid_toolkit import *

def show(name, s, w):
    print("=" * 60)
    print(name, "s=", s, "word=", w)
    print("  comps:", closure_components(s, w), "n=", n_components(s, w), "writhe=", writhe(w))
    br = bracket_poly(s, w)
    print("  bracket:", sorted(br.items()))
    if n_components(s, w) == 1:
        jp = jones_poly(s, w)
        print("  jones:", sorted(jp.items()), "span=", jones_span(jp))
        try:
            ap = alexander_poly(s, w)
            print("  alex:", sorted(ap.items()))
        except Exception as e:
            print("  alex ERR:", e)
    print("  alternating:", is_alternating_diagram(s, w))
    try:
        ed = pd_edges(s, w)
        print("  #pdedges:", len(ed), "expected:", 2 * len(w), "ends ok:", all(len(x["ends"]) == 2 for x in ed))
    except Exception as e:
        print("  pdedges ERR:", e)

# unknot, 0 crossings (1 strand, empty word)
show("unknot", 1, [])
# unknot with +kink: 2 strands, single crossing
show("unknot kink+", 2, [(1, 1)])
show("unknot kink-", 2, [(1, -1)])
# Hopf link: 2 strands, two + crossings
print("--- Hopf (2-comp link, jones may fail div-by-4) ---")
try:
    show("hopf", 2, [(1, 1), (1, 1)])
except Exception as e:
    print("hopf ERR:", e)
# trefoil
show("trefoil", 2, [(1, 1)] * 3)
show("trefoil mirror", 2, [(1, -1)] * 3)
# RII: 2 strands [+,-] closure (2-comp unlink) bracket should equal d = {-2: -1, 2: -1}? as A-poly {2:-1,-2:-1}
print("--- RII test ---")
b1 = bracket_poly(2, [(1, 1), (1, -1)])
print("RII closure bracket:", sorted(b1.items()), "expected d = [(2,-1),(-2,-1)]:", b1 == {2: -1, -2: -1})
# RIII: 3 strands
b2 = bracket_poly(3, [(1, 1), (2, 1), (1, 1)])
b3 = bracket_poly(3, [(2, 1), (1, 1), (2, 1)])
print("RIII brackets equal:", b2 == b3, sorted(b2.items())[:5], "...")
# figure-8 candidate: (s1 s2^-1)^2
show("fig8?", 3, [(1, 1), (2, -1), (1, 1), (2, -1)])
# 5_1 torus (2-strand, 5 +)
show("5_1", 2, [(1, 1)] * 5)
