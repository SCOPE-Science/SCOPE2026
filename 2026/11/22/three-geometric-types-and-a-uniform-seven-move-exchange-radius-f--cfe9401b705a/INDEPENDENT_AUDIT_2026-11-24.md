# Independent mathematical audit

## correctness

PASS

The mixed selected/unselected condition supplies a witness other than the selected endpoint. All pairs with a selected endpoint already have a separator at an endpoint; the remaining condition is injectivity of the distance code on the unselected vertices. The property is upward closed: a newly selected landmark separated from any remaining unselected vertex has a witness in the old set by resolution. Thus checking immediate deletions suffices for inclusion-minimality. I rebuilt the graph, used Floyd–Warshall for distances and evaluated the literal witness and outside-code conditions on all 65,536 subsets. I reproduced every coefficient in RESULT.md, inclusion-minimal counts 192, 1080, 192, 2, fault-tolerant minimum six (336 sets), and the eight pure two-sets (exactly the distance-four pairs). Exhaustive distance-preserving bijection search gave all 96 automorphisms; the 192 five-sets split into orbits 48, 48, 96 with induced edges as in the finding. Adjacency on intersecting in four vertices and a breadth-first search from each of the 192 states gave the common profile (1,5,14,40,74,42,14,2), hence 480 edges and radius and diameter seven. Replay: python3 /workspace/reproductions/graph2.py. The uploaded checkers were inspected, not executed.

## originality

PASS

The closest corpus match is the identical frozen record, not independent corroboration of priority. Distinct close corpus records concern ordinary metric or vertex–edge domination/resolution bases, and the examined weak-total literature supplies the definition and bounds, not the orbit/relocation classification. The pass concerns the complete resolving weak-total classification and exchange geometry, not the definitions, host graph, or its automorphism order.

## value

PASS

The Möbius–Kantor graph is a natural small symmetric cubic benchmark, and the resolving notion's backup constraint changes the optimum state space. The complete orbit types and sharp relocation guarantee identify what all optimal landmark layouts can do rather than merely giving a minimum. In particular, a single all-states distance profile across the three distinct host orbits is usable structural information not implied by host symmetry or the minimum alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
