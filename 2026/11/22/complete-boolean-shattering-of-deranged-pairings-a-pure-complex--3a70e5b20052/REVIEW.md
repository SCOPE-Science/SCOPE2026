# Independent mathematical audit

## correctness

PASS

A positive matching T leaves 2k vertices. For |S|≤n−2 there are at most k−2 residual negative-query edges besides the fixed missing matching, giving minimum degree at least k and hence a perfect matching by alternating edges of a Dirac cycle. This proves the whole trace identity, including intersecting supports. On a matching support of size n−1, a proper positive subset leaves at least four vertices, and the residual forbidden graph is a union of two matchings; Dirac applies for k≥3, and at k=2 each forbidden matching can hit only one member of the three 1-factors of K4. The full positive trace is equivalent to the single remaining edge being allowed. At size n a perfect matching with exactly one queried edge set negative cannot be realized. Every smaller face extends to a perfect matching and hence to a face of size n−1; these top faces correspond bijectively to (perfect matching, removed edge). Inclusion–exclusion on the disjoint prescribed pairs gives both factorial sums, including n=2. An adaptive shattered tree's positive branch fixes two endpoints and restricts to a perfect-matching class on the remaining vertices, giving the inductive online upper bound n−1 from the two-vertex base; VC shattering gives the lower bound. An independent insertion enumeration in /workspace/reproduction/check_1.py (stdout check_1.out in the same directory) verifies all 104,500 supports for n=2–5, the face vectors, and adaptive depths 1,2,3 for n=2–4. The finite tests corroborate rather than establish the general proof.

## originality

PASS

Supported distinct claim: the trace and sharp shattering classification, pure complex and online dimension for the nonbipartite deranged-pairing class. The earlier bipartite local trace theorem is a substantial analogue, and the same-graph deranged-pairing count is prior. Neither implies this top-face or online statement. This is a best-of-knowledge assessment, not a priority certification.

## value

PASS

The cocktail-party graph is the standard nonbipartite model of pairings avoiding a fixed pairing. Its arbitrary-support trace law and exact near-perfect boundary determine the entire Boolean restriction structure at the critical sizes, information lost in the matching count and in VC dimension alone. Purity, the facet correction and the exact adaptive dimension are useful comparisons with the bipartite derangement-board result, whose top size is different.

The dated certificate retains the supplied scientific assessment, sources and limitations.
