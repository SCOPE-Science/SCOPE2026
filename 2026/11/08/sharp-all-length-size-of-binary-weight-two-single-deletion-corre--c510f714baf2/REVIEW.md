# Scientific review

## Correctness — PASS

The theorem fixes the alphabet, length, exact Hamming weight, and deletion-shadow convention. Adjacent one-pairs produce exactly one weight-one descendant and separated one-pairs exactly two, yielding \(a+2b\le n-1\). Consecutive adjacent pairs share a weight-two descendant, so \(a\le\lceil(n-1)/2\rceil\). The resulting integer upper bound is attained by two explicit noncolliding pair families; all possible weight-one and weight-two descendants are handled in the proof, including endpoint cases where a zero-deletion category is absent. The accompanying checker directly reconstructs deletion shadows through length \(120\) and exact optimum graph searches through length \(12\). The proof, not finite enumeration, covers all lengths.

## Originality — PASS (qualified)

The strongest pertinent primary comparison is Cullina–Kulkarni–Kiyavash, arXiv:1211.4056, which calculates the **chromatic number** of constant-weight deletion graphs. The chromatic number is not the present maximum independent-set cardinality; an optimal coloring cannot alone imply the asserted exact maximum. Sloane, arXiv:math/0207197, gives the general single-deletion framework; Kulkarni–Kiyavash, arXiv:1211.3128, treats general upper bounds, not the sharp weight-two result. Public research-record searches under constant-weight, deletion shadow, maximum independent set, and matching formulas did not identify the claimed all-length equality. An unindexed or differently expressed combinatorial equivalent remains a genuine historical-priority risk.

## Value — PASS

Constant-Hamming-weight deletion codes are a natural restricted-input channel problem explicitly highlighted by weight-partitioning code design. The weight-two layer is the first nontrivial low-weight family; an exact maximum independent-set size (rather than a coloring, bound, or isolated small table) determines its full-length storage capacity. The matching constructive design is particularly simple, using a periodic sparse support pattern. No generalization to other weights is claimed.

## Limits

All-length theorem is proved under binary alphabet, exact weight two and a single deletion. Reproducibility tests do not certify the infinite theorem independently. No independent mathematical audit has occurred. Unindexed priority equivalents cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
