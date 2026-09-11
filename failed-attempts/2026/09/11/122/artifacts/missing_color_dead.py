"""Decisive test: does the Grebik-Pikhurko / Csoka-Lippner-Pikhurko measurable
Vizing machinery give 4 on E3, and -- critically -- is there any route to
Borel 4 via the same machinery? Key literature fact to verify from the
abstracts: Grebik-Pikhurko 'Measurable versions of Vizing's theorem' (Adv
Math 2020): every Borel graph of max degree d with... admits measurable
edge coloring with d+1 colors under mild conditions? Actually their theorem:
measurable Vizing holds for graphings (d+1?) -- need to check what I know:
Grebik-Pikhurko proved that for every d there is... the measurable chromatic
index of a graphing of max degree d is at most d+O(1)? And Csoka-Lippner-
Pikhurko: bipartite graphing needs d+1? Hmm, actually for bipartite
graphings measurable edge chromatic = d+1 in general? No -- bipartite finite
graphs need exactly d (Konig). For graphings, CLP proved d+O(sqrt d)? and
conjectured d+1?

Since I cannot fetch full texts, the honest auditable position:
- Measurable <=4 on E3: plausible via published measurable Vizing theorems
  (cite), but adapting them to E3 within this session = reproving a paper.
- Borel >=5 (no Borel 4): requires a NEW determinacy argument; finite-depth
  games provably cannot force it (finite_game_no_force.py); the blocking
  lemma kills only the naive transfer.

Recovery test outcome (bounded, honest): attempt the ONE concrete Borel
lower-bound route available in-session -- a Marks-style game on the
Gamma-tree where a hypothetical Borel 4-edge-coloring c induces a vertex
label, and check whether strategy-stealing yields contradiction. Formalize:
assume Borel c: E -> {0,1,2,3}. At each vertex, the missing color
m(v) in {0,1,2,3} (one of 4 colors missing among 3 incident edges, possibly
multiple missing -> pick least). This gives a Borel vertex map m: X -> 4-set.
Marks games rule out Borel maps X -> 3-set with constraints... but a map to
a 4-set with NO constraint is always possible (constant). The edge constraint
'c(e)!=c(f) for adjacent' translates to a constraint on m-values of adjacent
vertices that is WEAK (many m-pairs compatible). So no direct Marks
contradiction: the missing-color map carries too little information.
CONCLUSION: the natural strategy-stealing route fails structurally; a genuine
lower bound needs the full infinite edge-game determinacy analysis which is
a multi-day project, not a one-hour adaptation.

Verdict: TARGET BLOCKED in-session. File target-exit request.
This script just records the missing-color analysis formally.
"""
import json
import itertools

# At a vertex with incident colors {i,j,k} subset of {0,1,2,3}, missing set:
# how many (m(u), m(v)) pairs across an edge are compatible with a proper coloring?
# Edge e=(u,v) has color c. m(u) in Missing(u) [could be 1 or 2 values], similarly.
# Count: over all proper colorings of two adjacent stars (centers u,v joined by
# edge), what pairs (m(u),m(v)) occur? If ALL 16 pairs occur, the vertex map
# carries zero information and Marks route is dead.
seen_pairs = set()
count = 0
for cu in range(4):      # color of central edge at u side (same edge, same color)
    c = cu
    # star at u: central edge color c, other two distinct and != c
    for ou in itertools.permutations([x for x in range(4) if x != c], 2):
        Su = {c, ou[0], ou[1]}
        miss_u = [x for x in range(4) if x not in Su]
        # star at v: central edge color c, other two distinct != c
        for ov in itertools.permutations([x for x in range(4) if x != c], 2):
            Sv = {c, ov[0], ov[1]}
            miss_v = [x for x in range(4) if x not in Sv]
            count += 1
            for mu in miss_u:
                for mv in miss_v:
                    seen_pairs.add((mu, mv))
res = {"adjacent_star_colorings": count,
       "realized_missing_pairs": sorted(seen_pairs),
       "num_realized": len(seen_pairs),
       "route_dead": len(seen_pairs) == 16,
       "conclusion": ("All 16 missing-color pairs occur across properly colored "
        "adjacent stars: the induced Borel vertex map m:X->{0,1,2,3} is unconstrained, "
        "so no Marks-style vertex-game contradiction follows from a Borel 4-edge-coloring. "
        "The strategy-stealing route is structurally dead; Borel>=5 needs a genuinely "
        "new infinite edge-game analysis beyond one-hour scope.")}
print(json.dumps(res, indent=1))
with open("output/artifacts/missing_color_dead.json", "w") as f:
    json.dump(res, f, indent=1)
print("WROTE output/artifacts/missing_color_dead.json")
