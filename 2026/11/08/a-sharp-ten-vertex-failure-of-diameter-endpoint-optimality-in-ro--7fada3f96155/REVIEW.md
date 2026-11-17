# Independent mathematical audit

## correctness

PASS

Reconstructed the root-directed overflow q_v=max(0,c_v+sum_child q-1) and labelled-car binomial-interleaving recurrence. Checked the finite n<=10 classification with an independent exact-rational root-by-root recurrence and nonisomorphic free-tree generator: only B(3,3) at m=4,5 defeats diameter endpoints, across all tree types and loads. Verified sample B(a,b) families directly against the five four-car orbit polynomial differences; the falling factorial orbit construction uses at most four distinct outer leaves and proves all positive integer a,b, not an interpolation. For m=4 n=10 direct counts are N_c=9290,N_diameter=9263. The proof sharply separates exhaustive n<=10 census from its all-(a,b) exact identity. Original pinned checker.py and RESULT.md reviewed; no opaque code run.

## originality

PASS

No identified earlier result computes the first fixed-tree nonperipheral root optimum at n=10 with load sensitivity, nor the all-(a,b) orbit count differences. General rooted parking criteria explain computations but do not identify the optimum.

## value

PASS

The natural heuristic that a diameter endpoint maximizes directed-tree parking success fails at a provably minimal order. The explicit 27/10^4 edge-of-failure and infinite B(a,b) family reveal nontrivial root and load sensitivity, a motivated combinatorial counterexample rather than arbitrary table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
