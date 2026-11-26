# Independent mathematical audit

## correctness

PASS

The frozen proof incorrectly describes ranks (1,19,141,300) as coming from dimensions 1–4. A four-element face is three-dimensional and there is no 4-chain space. The full replacement repairs the paragraph: the ranks are for degrees 0–3, with the degree-0 augmentation included and the degree-4 map zero. It also states the learning separation as a difference of dimensions rather than query-identification complexity. Independent reproduction using set-inclusion neighborhoods and literal intersections, row rather than column elimination over F2, and branch-by-branch certificate replay: counts by cardinalities 0–6 for dominating sets (0,0,0,0,0,0,130); faces (1,20,190,560,360,0); facet counts 30/80/360 at sizes 2/3/4; degree-0–4 ranks (1,19,141,300,0) yield reduced Betti (0,30,119,60,0). The supplied permutation matches all 30 GP(10,3) edges and the supplied tree has 64 distinct valid leaf witnesses. Every vertex has 39 positive concepts, so depth seven is impossible (root-positive branch would require 64). The independent replay was `python3 /tmp/opencode/desargues-review.py /workspace/source/2026/11/22/exact-static-and-adaptive-shattering-of-minimum-dominating-sets--51fdae664688`; inputs are the frozen depth6_tree.json and vertex_isomorphism.json. The frozen finite algorithms and unaffected certificate files were inspected, not executed. The corrected result is for one graph, with homology over F2 only.

## originality

PASS

Credit the known domination-number antecedent; the supported contribution is the exact Desargues minimum-set/shattering census, dimensions and topology, not gamma=6 or the general method. Same-day learning results on Pappus and Heawood are substantive conceptual overlaps but compute different graph-specific invariants; dates do not establish relative order. The same-graph dominance complex uses a different face rule. The replacement makes these distinctions explicit. Best-of-knowledge only.

## value

PASS

The object is a standard symmetric cubic graph and the ordinary minimum-set concept class separates VC dimension four from adaptive depth six with an explicit tree and a tight first-split obstruction. The polynomial alone cannot determine the nonpure facet profile or the three nonzero homology ranks. The package is a precise benchmark for conjectures about dominance, static versus adaptive shattering, and the topology of shattered supports on symmetric graphs, not just recovery of its known domination number. The replacement limits interpretation to those actual invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
