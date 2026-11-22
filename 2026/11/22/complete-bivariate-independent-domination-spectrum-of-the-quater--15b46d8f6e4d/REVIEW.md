# Scientific review of the bivariate independent-domination census

## Correctness — PASS

The complete finding is a finite exact identity for the point–line incidence graph of \(\operatorname{PG}(2,4)\). Every maximal independent set is determined uniquely by its selected point set \(S\): it contains exactly all lines disjoint from \(S\), and maximality is equivalent to coverage of every omitted point by those lines. A proof of both directions is included in RESULT.md. The C++17 checker constructs 21 homogeneous point representatives and 21 distinct line masks, checks their incidence axioms, and evaluates all \(2^{21}\) point masks. An independently encoded affine-coordinate model with a line at infinity reproduces every bidegree and multiplicity using NumPy. Both checkers pass. The finite enumeration is exhaustive; no unproved extrapolation is made beyond the order-four plane.

## Originality — PASS, with explicit uncertainty

Goldberg, Rajendraprasad and Mathew, arXiv:1405.3436v1, Theorem 5.2 and Section 6, establish the minimum size and discuss small examples, rather than the complete bivariate histogram. Héger and Nagy, arXiv:1603.02933, study small minimal dominating sets and explicitly pose a counting problem, without listing this order-four polynomial. Hauschild, Ortiz and Vega, arXiv:1408.2879, Lemma 1, give selected maximal-independent-set families sufficient for their well-covered-dimension theorem, not a full census. Searches of indexed mathematical results for this graph, polynomial, cardinalities, independent domination and point–line duality produced related but non-covering findings. The exact table could still have appeared in an unindexed historical computation; the indexed and accessible-literature check is not a proof of universal priority.

## Value — PASS

The projective plane of order four is a canonical 42-vertex finite-geometry incidence graph and the first square-order case after the Fano and ternary examples. The full bivariate polynomial distinguishes point-heavy from line-heavy independent dominating sets, exhibits unexpected missing cardinalities (notably 9), and provides an exact 25,237-set finite benchmark for the broader independent-domination counting question posed in the literature. Its complete and independently reproducible coverage is a mathematical fact beyond the previously known minimum cardinality. The result does not purport to settle asymptotic counting.

Self-review: passed. Independent audit: not yet performed.
