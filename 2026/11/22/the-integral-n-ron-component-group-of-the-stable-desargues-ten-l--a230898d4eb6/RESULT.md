# The integral Néron component group of the stable Desargues ten-line boundary

## Finding

Let \(\mathcal A\) be a complex projective realization of the classical Desargues \((10_3)\) configuration as ten distinct lines in \(\mathbb P^2\). The arrangement has ten ordinary triple points and fifteen ordinary double points. Blow up the ten triple points, and let \(B\) be the reduced divisor consisting of the ten strict-transform lines together with the ten exceptional curves. Then \(B\) is a connected stable nodal curve of arithmetic genus \(26\), and its dual graph \(\Gamma_B\) has integral critical group

\[
K(\Gamma_B)\cong (\mathbb Z/2\mathbb Z)^3\oplus\mathbb Z/14\mathbb Z\oplus\mathbb Z/28\mathbb Z\oplus(\mathbb Z/140\mathbb Z)^2\oplus\mathbb Z/420\mathbb Z.
\]

The reduced Laplacian has Smith diagonal \(1^{[11]},2^{[3]},14,28,140^{[2]},420\). The group has order \(25\,815\,552\,000=2^{12}\cdot3\cdot5^3\cdot7^5\) and exponent \(420\).

If \(B\) is the geometric special fiber of a regular semistable one-parameter smoothing whose nodes all have thickness one and whose residue field is algebraically closed, the component group of the Néron model of the smooth generic fiber's Jacobian is canonically described by \(K(\Gamma_B)\). In particular, these conditions can be realized by a suitable smoothing of this stable nodal curve.

## Assumptions and scope

The base field for the plane arrangement and special fiber is algebraically closed of characteristic zero. The ten triple points are ordinary with three distinct tangent directions. No fourfold or more singular points are present; the other fifteen pair intersections are ordinary nodes. The blow-up is of the ambient plane at exactly these ten triple points. The Néron interpretation refers to a **regular semistable smoothing with unit thicknesses**, not to every arbitrary degeneration of the original plane divisor. No claim concerns the Picard group of the blown-up surface or the original singular ten-line divisor.

Use the standard combinatorial labeling: the ten triple points are the two-element subsets \(P\subset\{1,2,3,4,5\}\), and the ten original lines are the three-element subsets \(T\subset\{1,2,3,4,5\}\). A point lies on a line precisely when \(P\subset T\). Of the \(\binom{10}{2}=45\) unordered pairs of original lines, thirty pairs meet at the ten triple points (three pairs per point). The other fifteen pairs meet at ordinary double points.

## Proof

**Step 1 (normal crossings and graph).** At each ordinary triple point, one blow-up replaces the three transverse branches by three distinct nodes on the exceptional curve. The other ordinary double intersections persist. Hence the reduced total transform has ten exceptional rational components, each of valence three, and ten strict-transform rational lines, each of valence six (three exceptional incidences and three surviving double intersections). It has \(20\) vertices and \(30+15=45\) edges. Every rational component has at least three special points; the curve is stable. Its connectedness follows from the point-line incidence structure. Thus \(p_a(B)=45-20+1=26\).

Two line vertices correspond to three-subsets \(T,U\). The incidence structure shows that their original lines meet at a triple point precisely when \(|T\cap U|=2\); their intersection persists as a direct edge of the blown-up dual graph precisely when \(|T\cap U|=1\). The direct line-to-line edges therefore form the Petersen graph on the ten three-subsets (isomorphic under complement to the Kneser graph on two-subsets).

**Step 2 (Laplacian and an independent determinant).** With exceptional vertices first and line vertices second, let \(C\) be the \(10\times10\) incidence matrix \(C_{P,T}=1\) if \(P\subset T\), and let \(A\) be Petersen adjacency on the three-subsets. The full integer Laplacian is

\[
L=\begin{pmatrix}3I_{10}&-C\\-C^{\mathsf T}&6I_{10}-A\end{pmatrix}.
\]

The identity \(C^{\mathsf T}C=2I_{10}+J_{10}-A\) is checked entrywise: its diagonal is three; different three-subsets have one common two-subset exactly when their intersection has size two. The Petersen adjacency spectrum is \(3^{[1]},1^{[5]},(-2)^{[4]}\), and the constant vector is the \(3\)-eigenvector. Consequently a Schur-complement calculation gives

\[
\det(xI_{20}-L)=x(x-6)(x^2-8x+14)^5(x^2-11x+20)^4.
\]

The zero eigenvalue is simple, so the graph is connected. The Matrix–Tree theorem yields

\[
\tau(\Gamma_B)=\frac{6\cdot14^5\cdot20^4}{20}=25\,815\,552\,000=2^{12}3\cdot5^3\cdot7^5.
\]

**Step 3 (integral elementary divisors, not just spectrum).** Delete the exceptional-vertex row and column from \(L\), obtaining an integer \(19\times19\) reduced Laplacian \(R\). Over each of the prime-local rings \(\mathbb Z/p^N\mathbb Z\), for \(p\in\{2,3,5,7\}\) and \(N=v_p(\tau)+2\), pivot on unit entries and clear their row/column by invertible elementary operations. Once every remaining entry is divisible by \(p\), divide the remaining block by \(p\) and increase the valuation level. The resulting complete valuation multiplicities are

| Prime | Valuation multiplicities for the 19 diagonal entries |
|---|---|
| \(2\) | \(0:11,\;1:4,\;2:4\) |
| \(3\) | \(0:18,\;1:1\) |
| \(5\) | \(0:16,\;1:3\) |
| \(7\) | \(0:14,\;1:5\) |

The embedded exact checker performs these steps with two different deleted vertices, one exceptional and one line component. Because the determinant in Step 2 has no other prime divisor, the four local Smith lists uniquely determine the global invariant factors. Sorting the valuations in each prime and multiplying positionwise gives precisely

\[
\operatorname{SNF}(R)=\operatorname{diag}\left(1^{[11]},2^{[3]},14,28,140^{[2]},420\right).
\]

The product of these entries equals the independently obtained spanning-tree number. Therefore the stated critical group follows from the graph-divisor exact sequence.

**Step 4 (Néron interpretation).** For a regular semistable model with reduced nodal special fiber and node thickness one, Raynaud's identification describes the geometric Néron component group of the generic Jacobian by the graph's degree-zero divisors modulo chip firing. This group is the critical group just computed. Standard deformation theory permits a regular semistable smoothing of the present connected stable nodal curve over a complete characteristic-zero discrete valuation ring. The theorem requires this particular smoothing condition and does not assert that a predetermined pencil of plane curves already provides it.

## Verification

Run `python3 verify_desargues_boundary.py`. It uses only the Python standard library; no floating-point computation or external tables. It reconstructs the twenty vertices, checks the fifteen Petersen edges and thirty point-line edges, the two degree classes and genus, then computes prime-local Smith exponents from the actual two reduced Laplacians. The matrices are constructed internally; the required result is `DESARGUES_STABLE_BOUNDARY_CRITICAL_GROUP_OK`. The accompanying `verification_output.txt` records the output obtained from this embedded script. The displayed spectral determinant is also independently obtained from the rank-ten Petersen adjacency identity in the proof.

## Relationship to prior work

The realizability and combinatorial classification of ten-line arrangements with ordinary double and triple points, including the Desargues type, are classical and treated explicitly in Amram–Cohen–Teicher–Ye [1], especially their ten-triple-point classification. The abstract Desargues Levi graph is the 3-regular, thirty-edge generalized Petersen graph; it is **not** the twenty-vertex, forty-five-edge, biregular stable-boundary graph computed here. Kwon–Mednykh–Mednykh [3] analyze generalized Petersen graph Jacobians, hence their graph is missing the fifteen additional ordinary-double-point edges. Baker [2] describes the graph-theoretic Raynaud correspondence and a smoothing construction. The exact integral Smith factors of this *augmented stable boundary* do not follow from the incidence counts, the graph spectrum, or the general component-group correspondence without an additional integral calculation.

## Limitations

The result is a self-review mathematical calculation, not an independently audited priority claim. A published or otherwise indexed exact Smith computation of this augmented graph could pre-empt originality; no such matching computation was identified among the inspected sources. The result holds for the specified Desargues incidence type and a unit-thickness regular smoothing; different ten-line incidence types, nonunit thicknesses, or arithmetic Galois descents can have different component groups. The genus and determinant alone do not determine the integral group. The computation does not describe the ambient rational surface's Néron–Severi lattice.

## References

1. M. Amram, M. Cohen, M. Teicher, F. Ye, *Moduli spaces of ten-line arrangements with double and triple points*, arXiv:1306.6105 (first public version June 25, 2013), https://arxiv.org/abs/1306.6105.
2. M. Baker, *Specialization of linear systems from curves to graphs*, with appendix by B. Conrad, arXiv:math/0701075 (first public version January 2, 2007), https://arxiv.org/abs/math/0701075.
3. Y. S. Kwon, A. D. Mednykh, I. A. Mednykh, *On Jacobian group and complexity of the generalized Petersen graph GP(n,k) through Chebyshev polynomials*, arXiv:1612.03372 (December 11, 2016), https://arxiv.org/abs/1612.03372.
