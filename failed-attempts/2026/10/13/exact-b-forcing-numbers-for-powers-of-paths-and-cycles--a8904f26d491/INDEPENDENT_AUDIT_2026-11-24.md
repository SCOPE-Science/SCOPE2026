# Independent mathematical audit

## correctness

PASS

The first force needs its source and at least degree minus b already-black neighbors, giving max(1, minimum degree minus b plus 1); an initially all-black graph meets this bound as well. The endpoint of a nonsaturated path power fills its closed neighborhood from the stated initial segment, after which successive black vertices one at a time force the next vertex. On a nonsaturated cycle the chosen source's radius-k interval contains the entire seed, and its force fills a block of length 2k+1. A black vertex k-1 positions before the right endpoint sees only the next white vertex outside a block of that length or greater, so propagation reaches the entire cycle. Complete powers reduce to the white count at any black vertex. Independent exhaustive closure enumeration for paths of orders 2–9, cycles of orders 3–9, powers 1–7 and thresholds 1 through minimum degree plus 2 agreed in 589 profiles over 21493 candidate seeds. Replay: python3 /workspace/branches/3a953430-ceb1-40e5-9963-5c40a3df0143/independent_bforcing_check.py. This is bounded corroboration of the symbolic result.

## originality

FAIL

The all-threshold equality is a direct corollary of the prior ordinary zero-forcing equality with minimum degree, not just a coincidence at b=1. It follows on any nonempty graph satisfying that ordinary equality; no new path- or cycle-specific ingredient is needed. The saturated powers also follow from the earlier exact complete-graph result.

## value

FAIL

The higher-threshold exact values concern natural graph families, but are mechanically implied by the already established ordinary equalities and the known lower bound, with the saturated cases already explicit. The finding claims no additional extremal-seed classification or structural result beyond those values; replay does not create an independent useful unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
