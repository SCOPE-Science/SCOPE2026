# Independent mathematical audit

## correctness

PASS

For a connected selected k-set in a cubic graph on 2m vertices with nonempty complementary forest, the complement has 3m−3k+e(S)≥3m−2k−1 edges, and at most 2m−k−1. Equality at k=m requires both sides to be trees. The displayed seven-set is an actual witness, so the bound is attained in Heawood. Independent all-subset reconstruction (branches/reproduce-exchanges.py heawood, with .out) used the Fano incidence mask, checked the given LCF isomorphism, and tested the forest identity e=|V|−components for every complementary mask. It returned fvs=4 with 70 choices and cfvs=7 with 770 choices; price 7/4 follows. All 770 complements qualify and give 385 unordered pairs of halves. To recover the full group, enumerate all permutations of the seven points carrying the seven incidence triples to themselves; the image of each line is then forced. The graph is connected bipartite, so all remaining automorphisms are obtained by composing these with the polarity switching the two shores. This gives 336 automorphisms and the five orbit sizes as claimed. Pairwise XOR population two constructs the exact jump graph, and unweighted distances from all 770 sources reproduce the edge and degree counts, seven distance multiplicities, constant eccentricity seven, and 5,460 Johnson-plus-one pairs. Every complement pair has Johnson distance seven, and there are no other distance-seven pairs. This proves uniqueness of each complementary antipode, not a statement about the unrestricted four-set exchange graph.

## originality

PASS

The ordinary optimum and its finite census are prior and explicitly credited. There is also earlier jump-metric work on Heawood's 70 unrestricted four-sets. The surviving claim concerns the very different family of seven-vertex connected optima and its exchange geometry; no checked source supplies or implies that census and metric.

## value

PASS

The Heawood graph is a canonical cubic cage, and requiring a connected set of deletions is a natural distinction from its known ordinary feedback problem. At the optimum every deletion has a paired tree complement, so the classification identifies a concrete geometric space on which the mobility question is distinct from mere feasibility. An exact nearly Johnson metric and a unique farthest complement at every vertex are useful reconfiguration properties not automatic from the degree count or from the known ordinary four-set result. The contribution is a motivated exact single-graph benchmark, not a universal statement about cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
