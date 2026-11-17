# Integral homology and trivial mod-two products at the critical fourth-power cycle

## Finding
Let \(G=C_{16}^{(4)}\) be the simple graph on \(\mathbb Z/16\mathbb Z\) with an edge between distinct vertices precisely when their cyclic distance is at most four. Let \(X=\mathcal N(G)\) be the **open** Lovász neighborhood complex: a nonempty vertex set is a simplex when all its vertices have a common graph neighbor, distinct from every vertex in that set.

**Theorem.** All integral homology of \(X\) is torsion-free, and
\[
H_i(X;\mathbb Z)=
\begin{cases}
\mathbb Z,&i=0,3,4,\\
\mathbb Z^{7},&i=2,\\
0,&\text{otherwise}.
\end{cases}
\]
Furthermore, the product of any two positive-degree elements of \(H^*(X;\mathbb F_2)\) is zero. In particular the complete degree-two cup pairing
\[
H^2(X;\mathbb F_2)\otimes H^2(X;\mathbb F_2)\longrightarrow H^4(X;\mathbb F_2)
\]
vanishes identically.

The order sixteen is the first length immediately below the established stable regime \(n\ge17\) for neighborhood complexes of fourth-power cycles. In contrast to the stable, even-length mapping-torus model, this critical complex has no first homology but has seven independent second-homology classes. No assertion of a wedge-of-spheres homotopy equivalence is made.

## Assumptions and scope
The graph is simple, undirected and loopless; the neighborhood is **open**, not closed. Vertices are ordered \(0,1,\ldots,15\), and all simplicial chains use increasing vertex order to orient each simplex. The theorem concerns this one canonical critical graph; it is not an unbounded-parameter assertion. The integral groups use ordinary unreduced homology, and the cup product uses the standard simplicial Alexander–Whitney diagonal over \(\mathbb F_2\).

## Proof
**1. Complete complex and a genuine simplicial collapse.** For each \(a\in\mathbb Z/16\mathbb Z\), the open neighborhood
\[
N_a=\{a-4,a-3,a-2,a-1,a+1,a+2,a+3,a+4\}
\]
(with indices modulo sixteen) is an eight-vertex facet. The sixteen facets are distinct and every simplex is contained in one of them. Enumerating their nonempty subsets and removing repetitions gives the number of \(i\)-simplices, for \(0\le i\le7\), as
\[
(16,120,432,784,784,432,128,16).
\]
The same count follows from testing all \(2^{16}\) possible vertex subsets against the sixteen neighborhoods.

There is a deterministic elementary simplicial-collapse certificate. Represent each simplex by its sixteen-bit vertex mask and count its immediate surviving cofaces. Start with the ascending queue of nonempty masks having exactly one immediate coface. At each step, remove the queued mask and that unique coface if the mask is still present and still has exactly one coface; update all codimension-one subface counts and append any newly free nonempty masks. The unique coface is maximal, because any larger containing simplex would create at least two immediate cofaces of the free face. The included verifier checks every such condition and all remaining downward-closure conditions. Exactly **999** free-face/coface pairs are removed; the resulting simplicial subcomplex \(Y\) has \(i\)-face counts
\[
(f_0,f_1,f_2,f_3,f_4)(Y)=(16,98,243,255,102)
\]
and no higher-dimensional faces. Thus \(X\) simplicially collapses onto \(Y\), preserving integral homology and cup products.

**2. Exact integer chain computation.** Form each signed simplicial boundary matrix of \(Y\), with row and column basis masks in ascending order. In each matrix, choose a coefficient \(+1\) or \(-1\) minimizing the product of the counts of nonzero entries in its row and column, then their sum, then row and column indices. Clear that pivot row by integer column operations and remove its pivot row and column. These operations are unimodular. Repeat until no unit remains. The attached verifier recomputes all entries, checks all row operations exactly, and establishes that *no nonzero entries remain* after respectively
\[
(15,83,153,101)
\]
unit pivots in degrees \(1,2,3,4\). Every nonzero Smith invariant factor is consequently one; in particular the integral homology has no torsion. Chain-group ranks and boundary ranks give
\[
\begin{aligned}
\beta_0&=16-15=1,\\
\beta_1&=98-15-83=0,\\
\beta_2&=243-83-153=7,\\
\beta_3&=255-153-101=1,\\
\beta_4&=102-101=1.
\end{aligned}
\]
All higher groups vanish because \(Y\) has dimension four. This proves the integral homology assertion. The calculation does **not** treat algebraic cancellations as simplicial collapses; they are used only for integer homology.

**3. Complete mod-two cup pairing.** Independently of the collapse and integer reductions, construct every oriented simplicial boundary matrix of \(X\) itself, reduce it modulo two, and verify \(\partial^2=0\). The resulting Betti ranks in degrees zero through seven are \((1,0,7,1,1,0,0,0)\). In the 432-dimensional space of triangle cochains, \(\ker\delta_2\) has dimension \(112\) and \(\operatorname{im}\delta_1\) has dimension \(105\). Exact binary elimination selects seven cocycles forming a basis of \(H^2(X;\mathbb F_2)\). A separate binary reduction of \(\partial_4\) and \(\partial_5\) selects a nonbounding four-cycle supported on 102 four-simplices, representing the generator of one-dimensional \(H_4(X;\mathbb F_2)\).

For two selected triangle cocycles \(u,v\), evaluate their Alexander–Whitney product on each increasing four-simplex \([a_0,a_1,a_2,a_3,a_4]\) as
\[
(u\smile v)([a_0,a_1,a_2,a_3,a_4])
=u([a_0,a_1,a_2])v([a_2,a_3,a_4]).
\]
The exact seven-by-seven matrix of product evaluations on the nonbounding four-cycle has **all 49 entries zero**. The included `cycle_certificate.json` contains the seven cocycle vectors and the four-cycle as hex-encoded binary incidence vectors, in documented ascending mask bases. The verifier reconstructs and checks the cocycle conditions, nonbounding cycle, basis independence and all product evaluations. Since \(H^4(X;\mathbb F_2)\) is one-dimensional, the pairing is identically zero. There are no other possible nonzero positive-degree products: \(H^1=0\), and degrees above four have zero cohomology. The theorem follows.

## Verification
Run `python3 verify.py cycle_certificate.json` from the directory containing `verify.py`; the script uses only the Python standard library. It independently cross-checks face enumeration using all 65,536 vertex masks, executes and validates all 999 elementary collapses, reduces all four exact integer boundary matrices using unit pivots, verifies the entire original mod-two chain complex, and computes the degree-two cup product from the original simplices. Its exact expected output is provided as `verification_output.txt` and ends in `VERIFY_OK`. The binary chain and cocycle bases use ascending integer masks, with bit \(j\) indicating inclusion of the basis simplex in position \(j\). The `cycle_certificate.json` vectors are explicit finite witnesses; the script regenerates them and checks the claimed pairing. These are exhaustive finite checks on one specified simplicial complex, not extrapolations to infinitely many cycles.

## Relationship to prior work
Namiq, *A Complete Classification of 2-Linear Neighborhood Complexes* (first posted June 2, 2026), develops a structural algebraic classification for neighborhood complexes of certain bipartite graphs. The present 8-regular cycle-power graph contains triangles, so its exact integral homology and cup ring are not instances of that classification. Shukla's earlier theorem concerns graphs of maximum degree three and 4-regular circulants, not this degree-eight circulant.

A related publicly available result, *Sphere mapping-tori in neighborhood complexes of every stable cycle power* (October 25, 2026), establishes the homotopy type of \(\mathcal N(C_n^{(k)})\) for \(n\ge4k+1\). Another, *A cyclic four-dimensional collapse and a nonzero cup product for fourth-power cycle neighborhood complexes* (November 1, 2026), establishes a uniform collapse and a nonzero degree-one/degree-three product for \(k=4,n\ge17\). Their hypotheses strictly exclude \(n=16\); neither result asserts the critical homology or mod-two product computed here. At \(n=16\), the two-step lifting condition underlying the stable proof no longer holds because the circumference equals four times the graph-power radius. The added seven second-homology classes and vanished first homology show that the stable conclusion cannot simply be extended down one length. Equivalent unindexed calculations remain a residual priority risk.

## Limitations
This calculation proves homology and the mod-two cohomology-ring product assertion for precisely \(C_{16}^{(4)}\). It does **not** determine the fundamental group, all homotopy attaching maps, the integral cup-product coefficients, higher cohomology operations, or the corresponding critical complexes for other graph powers. Although integer Smith reductions and the mod-two cup product are exhaustive and reproducible, an independent mathematical audit has not been performed.

## References
1. M. R. Namiq, *A Complete Classification of 2-Linear Neighborhood Complexes*, arXiv:2606.03573v1, first publicly posted June 2, 2026, https://arxiv.org/abs/2606.03573.
2. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1, first publicly posted February 13, 2018, https://arxiv.org/abs/1802.04526.
3. *Sphere mapping-tori in neighborhood complexes of every stable cycle power*, mathematical research record, published October 25, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sphere-mapping-tori-in-neighborhood-complexes-of-every-stable-cy--a2339801b688.
4. *A cyclic four-dimensional collapse and a nonzero cup product for fourth-power cycle neighborhood complexes*, mathematical research record, published November 1, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-cyclic-four-dimensional-collapse-and-a-nonzero-cup-product-for--d6abfd03a954.
