# The lower mutual-visibility number of every triangular Cartesian cylinder

## Finding

For each integer \(n\ge2\), write \(G_n=C_3\square P_n\), with vertex set \(\{(i,r):0\le i<n,\ r\in\{0,1,2\}\}\). The graph has clique edges between distinct rows of each fixed column, and horizontal edges between equal rows in consecutive columns. Then
\[
\boxed{\mu^-(G_n)=4\qquad(n\ge2).}
\]
Here \(\mu^-(G)\) is the minimum cardinality of an *inclusion-maximal ordinary mutual-visibility set*: for each selected pair \(a,b\), some shortest \(a,b\)-path has no other selected vertex internally.

A useful strengthened assertion is: every mutual-visibility three-set which is not an entire three-vertex column extends to a mutually visible four-set using a vertex in a column already occupied by the three-set. An entire column extends by any vertex in a neighboring column.

## Assumptions and scope

All graphs are finite, simple, and undirected, with \(n\ge2\). The path has consecutively numbered vertices \(0,\ldots,n-1\), while \(C_3=K_3\). The term *maximal* refers to inclusion, not maximum cardinality. This concerns ordinary mutual visibility of pairs *inside* the selected set, not total mutual visibility of all graph vertices.

## Proof

**Upper bound.** Take \(v=(0,0)\) in the endpoint column and its closed neighborhood
\[
S=N[v]=\{(0,0),(0,1),(0,2),(1,0)\}.
\]
The three vertices in column zero are mutually adjacent. From \((1,0)\) to either \((0,1)\) or \((0,2)\), move through \((1,1)\) or \((1,2)\), respectively; those internal vertices are not in \(S\). Thus \(S\) is mutually visible. Every remaining vertex \(z\notin S\) has distance at least two from \(v\), and each shortest \(v,z\)-path starts at a vertex of \(N(v)\subset S\). Hence \(S\cup\{z\}\) cannot be mutually visible, proving that \(S\) is inclusion-maximal and \(\mu^-(G_n)\le4\).

**Every set of at most two vertices extends.** Any pair \(a=(i,r)\), \(b=(j,s)\) extends to a mutually visible triple. If \(i=j\), choose the third row in column \(i\). Otherwise choose any row \(t\ne r,s\) when \(r\ne s\), or a row \(t\ne r\) when \(r=s\), and put \(c=(i,t)\). The paths from \(a\) and \(c\) to \(b\) can move horizontally to column \(j\) in their respective rows and then, where needed, switch rows in column \(j\), avoiding the other selected vertex. Thus no pair is maximal, and singletons and the empty set are not maximal either.

**Column-gap normalization.** For any pair \(a=(i,r),b=(j,s)\),
\[
d(a,b)=|i-j|+\mathbf{1}_{r\ne s}.
\]
If their rows agree, the geodesic is the unique horizontal segment. Otherwise a geodesic makes exactly one vertical row switch, at any integer column between \(i\) and \(j\), inclusive. Suppose the selected set is entirely in a fixed list of occupied columns. Replacing any gap between consecutive occupied columns of length at least two by a gap of length exactly two does not change mutual visibility of any subset of vertices in those occupied columns. To verify this, look at each geodesic between selected endpoints: the only possible selected internal vertices lie at occupied columns; switching at an occupied column gives a separate possibility at each endpoint of a gap, while switching in an unoccupied gap has the same selected-vertex avoidance behavior regardless of which of its unoccupied columns is chosen. Thus precisely the three possibilities (left boundary, some empty interior, right boundary) matter, so replacing a gap by its capped length \(\min(g,2)\) preserves feasibility for every subset of those vertices.

A triple has one, two, or three occupied columns. After translation, the normalized column lists are exactly
\[
(0),\ (0,1),\ (0,2),\ (0,1,2),\ (0,1,3),\ (0,2,3),\ (0,2,4).
\]
For each normalized type enumerate all three-subsets using exactly those occupied columns; retain only mutually visible triples. Check whether each admits a fourth vertex within the same occupied columns. The following *complete* finite census is produced by the independent shortest-path breadth-first search in `canonical_check.py`:

| Occupied columns | Mutually visible triples | Extend within occupied columns | Exceptions |
|---|---:|---:|---:|
| (0) | 1 | 0 | 1 |
| (0,1) | 18 | 18 | 0 |
| (0,2) | 18 | 18 | 0 |
| (0,1,2) | 24 | 24 | 0 |
| (0,1,3) | 24 | 24 | 0 |
| (0,2,3) | 24 | 24 | 0 |
| (0,2,4) | 24 | 24 | 0 |
| **Total** | **133** | **132** | **1** |

The only exception is a complete vertical triangle. Since \(n\ge2\), at least one neighboring column exists. Adding any vertex in such a neighboring column gives a mutually visible four-set: it is adjacent to the vertex of its own row in the original triangle, and has two-step geodesics to the other two original vertices through unselected vertices in the new column. Consequently every mutually visible triple extends. Combined with the pair-extension argument, every inclusion-maximal mutually visible set has at least four vertices. The exhibited four-set attains this bound. \(\square\)

## Verification

Run `python3 canonical_check.py`, with standard Python 3 only. It examines all seven normalized column types and verifies the exact counts 133, 132, and one; every pair check uses graph shortest-path BFS with selected internal vertices forbidden. The reduction lemma makes this *finite complete case analysis* an all-order argument; no extrapolation from experiments is required. Independently run `python3 verify_strip.py`, which explicitly lists all geodesics rather than using BFS, and checks every mutual-visibility triple on \(G_n\) for \(2\le n\le12\). It also validates a maximal four-set at each order. Recorded outputs appear in `CHECKS.txt`. The infinite proof additionally requires the written column-gap lemma, pair-extension argument, and endpoint construction; the finite cylinder tests alone do not prove the theorem.

## Relationship to prior work

Brešar and Yero introduced the lower mutual-visibility invariant and the Neighborhood Lemma, and explicitly posed the determination of lower (total) mutual-visibility numbers on Cartesian cylinders as an open direction [1]. Their general neighborhood argument provides the upper bound here, not the all-order lower bound. Previously recorded lower mutual-visibility results for \(C_4\square P_n\) use four-cycle fibers, not triangular fibers; a result for \(C_3\square C_n\) with odd circumference obtains five rather than four, and does not transfer through deletion of wraparound edges. The independent mutual-visibility parameter for \(P_n\square K_m\) concerns maximum independent feasible sets, not minimum inclusion-maximal ordinary sets. Our contribution is the sharp all-order lower bound and the finite-gap local extension mechanism.

## Limitations

The claim is restricted to triangular cylinders with \(n\ge2\). The proof does not count all maximal configurations, does not classify larger widths, and does not address total mutual visibility. The finite census is an explicit certificate whose correctness is supported by two different implementations but has not received independent mathematical review. Historical publication priority cannot be guaranteed beyond the identified and inspected literature.

## References

[1] B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, first posted 2023-07-06; subsequently Applied Mathematics and Computation 465 (2024), 128411. https://arxiv.org/abs/2307.02951

[2] D. Kuziak and J. A. Rodríguez-Velázquez, *Total Mutual-Visibility in Graphs with Emphasis on Lexicographic and Cartesian Products*, arXiv:2306.15818 (2023), https://arxiv.org/abs/2306.15818 — distinct total, maximum-cardinality invariant.
