# Independent mathematical audit

## correctness

PASS

An independent exhaustive census built the graph from the 15 duads and 15 synthemes of six symbols. This agrees with the symplectic model: represent a duad by its binary characteristic vector in the even-weight subspace of F₂⁶ modulo the all-ones vector. This quotient is symplectic of dimension four for the induced dot product; distinct disjoint duads are orthogonal and each perfect matching's three duads sum to zero there. The 15 distinct duads and matchings give the points and lines. Cubic degree makes each closed neighborhood size four; at most seven vertices cannot dominate. Direct closed-neighborhood bitwise unions ruled out all 5,852,925 eight-sets and found exactly 90 dominating sets among all 14,307,150 nine-sets, without assuming the cited templates are complete. For each of the 174,437 supports of size at most five, the census compared the exact mask of realized traces from the complete family with the proposed incidence rule. Agreement was pointwise, including the (2,2) test with the third point R distinct from the concurrency point Q. Counts were (1,30,390,2730,420,0), with 120/180/120 four-supports by point count 1/2/3. Checking one-element extensions yields 1,980 maximal triples and 420 maximal four-sets and no smaller facets; shattering is hereditary so no larger support can be shattered. An independently generated depth-five query tree was checked at all 32 leaves, with 32 distinct consistent concepts. Each vertex lies in 27 minimum sets, so at any root the positive subtree has fewer than the 32 witnesses necessary for depth six. Replay in /workspace/branches/526c3a33-cf75-4a09-bf94-c87ba0ffa8ec via python3 duad_gq2_audit.py --full (audit_output.txt and adaptive_tree_duad.json). The supplied Python/C++ implementations and output were inspected, not executed. The frozen TREE_DEPTH5.json is present; the check for the adaptive lower bound used the independent witness. This finite census does not extrapolate to other generalized quadrangles.

## originality

PASS

The underlying minimum-domination problem and classification are prior, as are other VC–Littlestone separations. The checked exact results for this query class, notably the incidence criterion and its shattering complex, are not matched by those prior statements. The strongest same-day overlap has the same graph and two dimensions but different hypotheses and domain.

## value

PASS

Optimal ordinary domination on the canonical doily gives a natural finite concept class. The full shattering complex, including its geometric exclusions and nonpure facets, says more than either dimension alone. The adaptive depth certificate gives a concrete strict improvement of online querying over fixed supports of the same depth, verified for the complete exact class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
