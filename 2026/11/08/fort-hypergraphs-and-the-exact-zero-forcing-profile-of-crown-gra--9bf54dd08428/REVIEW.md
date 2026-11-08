# Review of crown-graph fort and zero-forcing theorem

## Correctness — PASS

For every integer \(n\ge3\), the proof writes the exact number of fort-neighbors of an outside vertex as the number of opposite-part selected vertices minus an index-match indicator. All forts with at least three vertices in one part contain a pure triple. For forts with at most two selected vertices per part, the necessary and sufficient condition is two matching-aligned vertices on each side. The proof then uses the fort obstruction characterization to enumerate every zero-forcing set, establishes inclusion-minimality, constructs disjoint fort packings attaining the vertex-count upper bound, and exhibits matching upper and lower fractional-linear-program certificates. All quantifiers and exceptional small cases are explicit. The provided standalone graph-checking program exhaustively examines 87,360 subsets at orders three through eight and independently checks the fort-packing formula through order seven; no finite test is presented as an unrestricted proof.

## Originality — PASS (provisional priority)

The nearest relevant work is Cameron–Hogben–Kenter–Mojallal–Schuerger (arXiv:2310.17904), which defines the fractional fort problem and supplies general inequalities and complete-bipartite examples. Their inspected full-text family results and summary table do not determine the minimal forts or fractional value of the crown graph \(K_{n,n}\setminus M_n\). The older zero-forcing-polynomial paper (arXiv:1801.08910) treats other families; Pelayo–Abara (arXiv:2202.04997) studies four graph products other than the direct product giving this family; and Curtis et al. (arXiv:2208.12899) give general probabilistic bounds. The classifications were compared as mathematical implications, not merely by title. Public database and literature searches did not locate an equivalent family-specific theorem. This establishes only best-knowledge originality, not priority certification; unindexed literature remains a risk.

## Mathematical value — PASS

The crown graph is a standard connected regular bipartite family with the same two part sizes as \(K_{n,n}\) but with a perfect matching deleted. The complete minimal-fort list gives a uniform bounded-rank obstruction hypergraph, an exact cardinality polynomial for every zero-forcing set, a well-forced structural classification, and exact integer/fractional values. Deletion changes the fractional zero-forcing number from \(n\) to \(2n/3\) while ordinary zero forcing decreases only by two. The resulting ratio tends to three, a meaningful family-level integrality separation not supplied by the general parameter definitions. This goes beyond a routine substitution or known scalar table.

## Limitations and relevant literature

Publication priority is provisional; the only tested graph orders are \(3\le n\le8\) for subsets, and \(3\le n\le7\) for maximum disjoint fort packing. Infinite validity rests on the written proof. Primary sources inspected: arXiv:2310.17904, arXiv:1801.08910, arXiv:2202.04997, and arXiv:2208.12899; additional graph identification from MathWorld's Crown Graph entry. The mathematical status is a self-review, not independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
