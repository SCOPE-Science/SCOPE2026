# The seven-point loopless degree-two graph complex is a mixed-dimensional sphere wedge

## Finding
Let \(B=BD^{(2,2,2,2,2,2,2)}(K_7)\) be the simplicial complex whose vertices are the unordered pairs from \(\{1,\ldots,7\}\), and where a set of pairs is a face exactly when each label appears in at most two pairs. Its complete homotopy type is
\[
|B|\simeq S^4\vee\bigvee^{181} S^5.
\]
This is a homotopy refinement of *known* integral homology ranks, not a new homology computation: Jonsson's Table 12.2 already reports \(\widetilde H_4(B;\mathbb Z)=\mathbb Z\), \(\widetilde H_5(B;\mathbb Z)=\mathbb Z^{181}\), and all other reduced groups zero.

## Assumptions and scope
Only simple undirected loopless graphs on seven fixed labeled vertices are used; all \(21\) possible edges are allowed. This is the ordinary maximum-degree-two graph complex, also called the two-matching complex of the complete graph. It is **not** the degree-two complex permitting loops, and **not** the subcomplex forbidding triangles. All homotopy types are nonequivariant geometric realizations.

## Proof
Order the \(21\) edges lexicographically as the ordered pairs \((a,b)\) with \(0\le a<b<7\). Represent a graph by a \(21\)-bit mask. Enumerate precisely those masks in which each graph vertex has degree at most two. There are \(15,796\) masks including the empty mask; the numbers of nonempty faces in dimensions \(0\) through \(6\) are \((21,210,1190,3780,6132,3997,465)\).

Construct an explicit matching on the face poset: for each edge bit in ascending order, pair every *still available* lower mask not containing that bit with its upper mask obtained by inserting the bit whenever both masks are available. The full augmented matching has \(7,676\) pairs. Matchings in this procedure are acyclic: the included checker independently builds the directed Hasse graph, pointing matched incidences upward and unmatched incidences downward, and verifies that all \(15,796\) nodes are exhausted by a topological sort. Drop the unique empty-mask/vertex pair and retain that vertex as a critical zero-cell. The ordinary complex then has an acyclic Forman matching consisting of \(7,675\) pairs, with exactly \(132\) critical four-cells and \(312\) critical five-cells and no other positive-dimensional critical cells. Discrete Morse theory therefore supplies a CW model with those cells and no six-cells.

The checker constructs every original oriented simplicial boundary over \(\mathbb Z\) using the lexicographic vertex order. It algebraically cancels the \(7,675\) matched incident cell pairs by integer Schur-complement operations, verifying each signed pivot has absolute value one. The only remaining nonzero possible boundary is the \(132\)-by-\(312\) degree-five to degree-four map. A further \(131\) *actual integer unit pivots*, each checked by the code, reduce this attaching matrix to zero, leaving one four-cell and \(181\) five-cells besides the zero-cell. Crucially, because the Morse model has cells only in dimensions \(0,4,5\), its four-skeleton is \(\bigvee^{132}S^4\). The attaching maps of the five-cells are elements of \(\pi_4(\bigvee^{132}S^4)\cong\mathbb Z^{132}\); the integral attaching matrix therefore determines all of them (not just their homological shadows). Integer elementary row and column operations are realized by homotopy equivalences of the skeleton and cellular handle slides. Each unit entry can be canceled homotopically, leaving precisely the stated wedge.

## Verification
Run `python3 verify.py` and `python3 crosscheck.py` with the Python standard library. The primary verifier checks the entire degree-bounded face family, every directed Hasse incidence, all matched pivots, the critical-cell dimensions, and every final integer unit pivot. It prints `BOUNDED_DEGREE_LOOPLESS_7_OK` with counts \((1,132,312)\) in surviving dimensions \((0,4,5)\), then \((1,1,181)\) after cancellations. The independent Gray-code program inspects all \(2^{21}\) subsets without using recursive enumeration and reproduces the face vector and Euler characteristic \(-179\). Checks are exact and deterministic, not randomized or floating-point.

## Relationship to prior work
Jonsson's *Simplicial Complexes of Graphs*, Section 12.1.1, Theorem 12.2 and Table 12.2, supplies a general shifted-connectivity estimate and **the exact same integral homology groups**. We do not claim to rediscover those groups. Its presented results in that section do not give the CW attaching maps or the complete homotopy equivalence asserted here. The known homology alone is insufficient to determine the homotopy type of this six-dimensional complex. The work on degree-bounded complexes of forests by Singh and Matsushita concerns forest hosts or leaf-based decomposition; \(K_7\) is not a forest and has no leaves. A published triangle-free two-matching result for \(K_7\) excludes all triangular selected edge sets and therefore has a different domain; it does not imply this unrestricted conclusion.

## Limitations
This is a finite, non-equivariant classification at seven labels, not a classification for all \(n\), nor a proof of a general wedge property. The exact homology calculation was known in 2007; only the homotopy refinement is asserted here. Completeness of bibliographic coverage is not proved, and equivalent work could remain unindexed. No independent mathematical audit is claimed.

## References
- Jakob Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, first hardcover publication 15 November 2007, Section 12.1.1 and Table 12.2. https://doi.org/10.1007/978-3-540-75859-4
- Anurag Singh, *Bounded degree complexes of forests*, arXiv:1910.12793, first public 28 October 2019. https://arxiv.org/abs/1910.12793
- Takahiro Matsushita, *Independence complexes of hypergraphs and bounded degree complexes*, arXiv:2004.13281, first public 28 April 2020. https://arxiv.org/abs/2004.13281
