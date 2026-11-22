# Review of the extremal permutation-diagram equality criterion

## Correctness — PASS

The invariant is an external open-neighbourhood trace count over all finite diagram extensions, not a vertex-count invariant of a fixed graph. For a two-line diagram, the cut pair \((i,j)\) gives \(P_i\triangle Q_j\), and every cut pair is realizable. Equalities correspond to common intervals. The baseline singleton/full common-interval edges are a forest for nonmonotone marked permutations and account for \(2m+2\) necessary cell identifications. Simple permutations have no other equalities. For a non-simple marked permutation, a proper nonmonotone interval supplies another independent identification. For a monotone interval, adjacent bonds or the extreme-bond argument supply one; monotone full permutations are counted separately. The explicit prepend-minimum construction gives the exact next value \(m^2-2\). The associated checker exhausts all marked permutations through eight elements and tests the constructive series through thirty; finite computation is auxiliary to the proof.

## Originality — PASS within checked evidence

The sharp numeric bound is **not new**. Foucaud et al., Theorem 13 and Proposition 14, give a sharp locating-domination bound which implies the external profile capacity after including the empty trace. Prior mathematical work had also shown that simple marked permutations are sufficient for the upper capacity. The proved new implication is the converse: maximum capacity forces no proper common interval, along with the exact sharp non-simple boundary. The 2017 article's permutation-graph section and construction provide no all-equality classification; the 2026 neighbourhood-complexity paper treats bounded treewidth and pathwidth instead. Common-interval theory is classical and is not re-claimed. Relevant published mathematical records were queried for stronger statements, equality classifications and aliases; no covering result was identified, but this is not proof of uniqueness. Risk: earlier specialist studies of all equality cases or permutation-pattern trace ranks might already imply the converse.

## Value — PASS

An inequality and a family of witnesses do not determine whether other parameter representations attain equality. The converse solves the natural equality-case question for an entire graph class at all parameter sizes, giving a representation-level rigidity characterization, a simple certificate for extremality (test common intervals), and a sharp second stratum when that certificate fails. This is a structurally motivated classification, rather than a numerical recomputation.

## Limits

No claim is made about graph-isomorphism classes, distinct minimal ambient orders, closed neighbourhoods, or independent external validation. Historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
