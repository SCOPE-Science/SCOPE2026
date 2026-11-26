# Independent mathematical audit

## correctness

PASS

The graphical-group alternating form for an edge weighting has rank twice the matching number of its forest support: a maximum matching gives a nonzero principal Pfaffian on its endpoints, with no cancellation because two different perfect matchings would give a cycle. Conversely the rank of an alternating matrix is attained on a nonsingular principal submatrix (successive coordinate-pair pivots suffice), whose Pfaffian requires a matching of half that size. There are (q-1)^k weightings of a fixed k-edge support, yielding the stated q^(n-2r) character multiplier per rank-2r weighting in odd characteristic. Equality of profiles forces the same n since the number of linear characters is q^n; at fixed n, equality at all odd prime powers is equivalent to polynomial equality by the infinite-root test. The independent replay `python3 -B /workspace/reproduce_frozen.py 2` generates rooted trees as multisets of smaller rooted trees, identifies unrooted trees by the minimum rooted code over all roots, and derives each support matching number from the largest matching submask. It reproduced orders 1–10, 106 trees and 105 profiles at ten and no collision below, the exact two witnesses and all 19 coefficients. The diameters are six and seven. The frozen checker was inspected, not executed.

## originality

FAIL

A distinct earlier catalogued result gives the same minimal order, unique unordered isomorphism pair and complete character-degree distribution. The relabellings and coefficient comparison establish actual equivalence, not just a similar invariant or a matching title.

## value

FAIL

The sharp reconstruction cutoff of a representation-theoretic invariant is a meaningful question, but this frozen finding gives the same answer, witnesses and exact distribution as the earlier record. Its recomputation is useful corroboration, not a distinct mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
