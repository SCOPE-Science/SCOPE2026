# The integral component group of the resolved quartic Ceva net

## Finding
Let \(A\subset\mathbb P^2_{\mathbb C}\) be the reduced twelve-line Ceva arrangement
\[
(x^4-y^4)(y^4-z^4)(z^4-x^4)=0.
\]
Blow up its sixteen ordinary triple points and three ordinary quadruple points. Let \(D\) be the **reduced** union of the twelve strict transforms of the lines with all nineteen exceptional curves. The resulting connected stable nodal curve has thirty-one rational components, sixty nodes, and arithmetic genus thirty. For its dual graph \(\Gamma\), the *full integral* critical group is
\[
K(\Gamma)\cong (\mathbb Z/11\mathbb Z)^3\oplus(\mathbb Z/33\mathbb Z)^4\oplus(\mathbb Z/528\mathbb Z)^2.
\]
Its order is \(2^8\cdot3^6\cdot11^9=440049629885184\) and its exponent is \(528\). In particular, the nine independent \(11\)-primary cyclic factors survive even though the only singular-point multiplicities of the original line arrangement are three and four.

## Assumptions and scope
The base field is \(\mathbb C\). The quartic Ceva net consists of the three classes of four lines cut out by \(x^4-y^4\), \(y^4-z^4\), and \(z^4-x^4\), respectively. Each class has a common concurrency point of multiplicity four. There are also sixteen ordinary triple points, one intersection of one line of each class per root-of-unity pair; no other singular points occur. The word *resolved boundary* denotes the reduced divisor on the blowup of all nineteen intersection points, including all exceptional components. The critical group is \(\operatorname{Div}^0(\Gamma)/\operatorname{im}(L)\), where \(L\) is the integer graph Laplacian, with one edge per distinct transverse node. It is not the critical group of the original twelve-line intersection graph or of a graph omitting the exceptional components.

## Proof
**1. Geometric incidence and stability.** Fix a primitive fourth root \(\zeta\) of unity. Label the three line families by \(\ell_{0,a}\), \(\ell_{1,b}\), and \(\ell_{2,c}\) for \(a,b,c\in\mathbb Z/4\mathbb Z\), choosing equations \(x=\zeta^a y\), \(y=\zeta^b z\), and \(z=\zeta^{c}x\). The three lines meet away from the coordinate vertices exactly when \(a+b+c=0\). Thus the sixteen triple points have labels \((a,b)\), with incident line labels \((0,a),(1,b),(2,-a-b)\). Lines within each of the three families meet only at that family's coordinate vertex, giving three quadruple points. Distinct points of the stated types exhaust all pairs of lines: \(3\binom42+16\binom32=18+48=66=\binom{12}{2}\). Every singularity is ordinary because the constituent line directions are distinct. Blowing up each singular point once separates its line branches; each strict transform meets the corresponding exceptional curve transversely once and no pair of strict transforms meets afterward. The dual graph has 12 line vertices of degree 5, 3 pencil vertices of degree 4, and 16 triple vertices of degree 3. Its sixty edges are precisely the 12 pencil incidences and 48 triple incidences. All components are rational, every vertex has degree at least three, and the graph is connected. Consequently \(D\) is stable and \(p_a(D)=60-31+1=30\).

**2. An integral Laplacian presentation.** Index the 31 vertices in this order: the lines \((j,a)\) for \(j=0,1,2\) and \(a=0,1,2,3\); the three pencil vertices \(P_j\); the sixteen triple vertices \(T_{a,b}\) in lexicographic order. Join \(P_j\) to \((j,a)\) for every \(a\), and join \(T_{a,b}\) to \((0,a)\), \((1,b)\), and \((2,-a-b\bmod4)\). Let \(L\) be the degree-minus-adjacency matrix. This graph is exactly the geometric dual graph by Step 1. Remove any one row and the corresponding column to form a 30-by-30 reduced Laplacian \(L_0\). Since \(\Gamma\) is connected, the finite abelian critical group is the cokernel of \(L_0\).

**3. Complete integer invariant factors.** The accompanying standard-library-only program `verify_ceva4.py` builds \(L\) from those explicit incidence rules. It performs a deterministic exact Smith reduction of \(L_0\), using only elementary unimodular integer row and column operations. At each pivot, Euclidean reduction clears its row and column, and if a later entry is not divisible by the pivot, a unimodular row addition restarts the Euclidean step. Hence when it terminates, its nonzero diagonal entries divide the next entry. On each of four independent choices of deleted vertex the resulting 30 invariant factors are exactly twenty-one units, three copies of \(11\), four copies of \(33\), and two copies of \(528\). These entries prove the displayed group decomposition, including every prime-primary exponent, without relying on graph eigenvalues alone. A separate fraction-free Bareiss determinant evaluation of each independently rooted matrix gives \(440049629885184\), in agreement with the product of Smith factors.

**4. Independent rational spectral check.** The same program computes the entire characteristic polynomial by exact Faddeev–LeVerrier trace identities and checks
\[
\det(\lambda I-L)=\lambda(\lambda-3)^6(\lambda^2-12\lambda+31)(\lambda^2-9\lambda+16)^2(\lambda^2-8\lambda+11)^9.
\]
Thus Kirchhoff's theorem also predicts the spanning-tree count
\[
\frac{3^6\cdot31\cdot16^2\cdot11^9}{31}=2^8\cdot3^6\cdot11^9,
\]
independent of the integral diagonalization. The factor \(\lambda\) occurs once, confirming connectedness.

**5. Conditional Néron interpretation.** For any proper regular split semistable smoothing of the specified nodal curve in which every node has thickness one, the standard dual-graph component-group identification gives the same geometric Néron component group of its generic Jacobian. No claim is made about a specific arithmetic smoothing or about non-unit node thicknesses.

## Verification
Run `python3 verify_ceva4.py` using only the Python standard library. It constructs the graph from the 4-by-4 net incidence, checks all degree counts and zero row sums, evaluates the complete Smith forms for four distinct deleted vertices, confirms four determinants by a separate exact Bareiss routine, and reproduces the rational characteristic polynomial from trace recurrences. Expected success output: `CEVA4_RESOLVED_INTEGRAL_CRITICAL_GROUP_OK`. This is a finite exact certificate for the explicitly defined 31-vertex graph, not a claim about all Ceva nets or all semistable models.

## Relationship to prior work
Falk and Yuzvinsky's 2006 paper (Example 3.4 and Section 4) identifies the Fermat/Ceva pencil, its three split fibers, its three line classes, and its multinet geometry. These are inputs, not discoveries here. Lorenzini's work explains how a regular semistable model's dual graph yields the Jacobian component group, but does not tabulate this quartic Ceva graph. Published calculations of Hesse, Fermat-surface-line and other classical arrangement graph Jacobians concern distinct graphs. The new assertion is specifically the **integral Smith decomposition of the resolved quartic-Ceva boundary**, not its already known incidence, the degree-four pencil, or an automatic application of a general component-group theorem. The three primary searches for Ceva-four Smith forms, its graph critical group and its numerical invariant factors found no exact prior calculation; failure to find a source is not proof of historical priority.

## Limitations
This is a precise finite classification for the quartic member of the Ceva arrangement family, not a formula for arbitrary degree. The result is a graph-Jacobian invariant of the resolved boundary, not the Picard group of the ambient blowup surface. The arithmetic Néron identification requires a regular split semistable thickness-one model. Exact code and two independent determinant/spectral checks validate the stated finite computation but do not establish historical uniqueness; an unindexed result for the same Levi incidence graph could supersede novelty. No independent mathematical audit has been performed.

## References
1. M. Falk and S. Yuzvinsky, *Multinets, resonance varieties, and pencils of plane curves*, arXiv:math/0603166v1, first publicly submitted 2006-03-07; particularly Example 3.4 and Section 4. https://arxiv.org/abs/math/0603166 .
2. D. J. Lorenzini, *Groups of components of Néron models of Jacobians*, Compositio Math. 73 (1990), 145–160. https://archive.numdam.org/item/CM_1990__73_2_145_0/ .
3. Standard integer Smith normal form and Kirchhoff matrix-tree theorem; explicit calculations reproduced in `verify_ceva4.py`.
