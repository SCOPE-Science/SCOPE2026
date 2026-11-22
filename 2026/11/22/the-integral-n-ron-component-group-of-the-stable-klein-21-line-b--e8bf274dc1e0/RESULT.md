# The integral Néron component group of the stable Klein 21-line boundary

## Finding

Let \(\mathcal K\subset\mathbb P^2_{\mathbb C}\) be the classical 21-line Klein reflection arrangement. Let \(X\) be the blowup of the 49 distinct singular points of \(\mathcal K\), and let \(B\subset X\) be the reduced union of the 21 strict transforms of its lines and the 49 exceptional divisors. Its dual graph \(\Gamma\) has one vertex per component and one edge per ordinary node.

**Theorem.** The curve \(B\) is a connected stable nodal curve with 70 rational components, 168 nodes, and arithmetic genus 99. Its complete integral graph critical group (the degree-zero divisor class group of \(\Gamma\)) is

\[
K(\Gamma)\cong \mathbb Z/4\mathbb Z\oplus\mathbb Z/72\mathbb Z\oplus\mathbb Z/216\mathbb Z\oplus\mathbb Z/155304\mathbb Z\oplus(\mathbb Z/1087128\mathbb Z)^5.
\]

The order is \(2^{26}3^{23}7^5 719^6\), and the exponent is \(1087128\). For every proper, regular, one-parameter semistable smoothing over \(\mathbb C[[t]]\) whose special fiber is \(B\), with all local node thicknesses one, the geometric component group of the Néron model of the smooth generic Jacobian is isomorphic to \(K(\Gamma)\).

## Assumptions and scope

All geometry of the arrangement and the boundary is over \(\mathbb C\); the calculation is integral over \(\mathbb Z\). Write \(a\in\mathbb C\) for either root of \(a^2+a+2=0\). The 21 projective lines are the vanishing loci of coefficient triples \((u,v,w)\) in the following order:

\[
\begin{array}{lll}
(1,0,0)&(0,1,1)&(a,1,-1)\\
(a,-1,1)&(0,-1,1)&(1,a,-1)\\
(a,-1,-1)&(-1,1,a)&(a,1,1)\\
(-1,a,1)&(-1,-1,a)&(1,0,1)\\
(-1,a,-1)&(1,a,1)&(-1,0,1)\\
(1,-1,a)&(1,1,a)&(0,0,1)\\
(-1,1,0)&(1,1,0)&(0,1,0).
\end{array}
\]

For a connected graph \(G\), its critical group is the cokernel of any reduced integer graph Laplacian, including only the finite torsion (all reduced Laplacians are nonsingular). The model over a discrete valuation ring in the theorem is required to be regular; no claim is made for nonunit thicknesses, other special fibers, or any Picard group of the blown-up surface itself.

## Proof

**1. Exact incidence and stability.** Work in the quadratic order \(\mathbb Z[a]/(a^2+a+2)\), which embeds in \(\mathbb C\). Cross products of the 21 coefficient triples give the 210 pairwise line intersections. Two resulting projective points coincide precisely when their cross product vanishes. Exact ring arithmetic yields 49 points: 21 have multiplicity four and 28 have multiplicity three. Every line contains four points of each kind, and every line pair meets at exactly one of these 49 points. These facts are also directly checked in the standalone verifier. A single blowup at each point separates the strict line transforms; an exceptional divisor meets its three or four branches transversely at distinct points. Therefore the reduced divisor \(B\) is nodal with exactly

\[
21+49=70\quad\text{components},\qquad 21\cdot4+28\cdot3=168\quad\text{nodes}.
\]

Every rational component has at least three special points (line components have eight and exceptional components have three or four), so \(B\) is stable. The dual graph is connected, since any two original lines intersect. The normalization components all have genus zero, hence \(p_a(B)=168-70+1=99\).

**2. Graph Laplacian and an independent tree-count calculation.** Let \(H\) be the \(21\times49\) zero-one incidence matrix and let \(D\) be the diagonal matrix with a \(3\) for each triple point and a \(4\) for each quadruple point. The graph Laplacian is

\[
L=\begin{pmatrix}8I_{21}&-H\\-H^{\mathsf T}&D\end{pmatrix}.
\]

Deleting a line vertex and taking the Schur complement of \(D\) gives

\[
\det L_{\mathrm{red}}=\frac{3^{28}4^{21}}{12^{20}}\det W_{\mathrm{red}}=4\cdot3^8\det W_{\mathrm{red}},
\]

where \(W\) is the weighted \(21\)-vertex Laplacian with edge weight \(3\) when two lines meet at a quadruple point and weight \(4\) when they meet at a triple point. Its diagonal is \(68\). If \(Q\) is the zero-one adjacency matrix joining two distinct lines exactly when they share a quadruple point and \(J\) is the all-ones matrix, then

\[
W=72I_{21}-4J+Q.
\]

Exact integer multiplication gives \(Q(Q-12I)(Q^2+2Q-7I)=0\), and exact row reduction gives \(\operatorname{rank}Q=13\), \(\operatorname{rank}(Q-12I)=20\). Since \(Q\) is real symmetric and the quadruple-adjacency graph is connected and 12-regular, its characteristic polynomial is

\[
\lambda^8(\lambda-12)(\lambda^2+2\lambda-7)^6.
\]

Thus the nonzero eigenvalues of \(W\) are eight copies of \(72\) and six conjugate pairs \(71\pm\sqrt8\). Kirchhoff's matrix-tree theorem gives

\[
\det W_{\mathrm{red}}=\frac{72^8(71^2-8)^6}{21}
=2^{24}3^{15}7^5 719^6.
\]

Consequently, \(|K(\Gamma)|=\det L_{\mathrm{red}}=2^{26}3^{23}7^5 719^6\). As an independent exact-arithmetic check, the verifier also computes \(\det W_{\mathrm{red}}\) by fraction-free Bareiss elimination on a \(20\times20\) matrix.

**3. Full integral Smith factors.** The actual critical group requires integral elementary divisors, not only the determinant. The verifier constructs the complete \(70\times70\) integer Laplacian from the exact equations above and deletes either of two different vertices, separately. For every prime divisor of the verified determinant, it performs Gaussian elimination over \(\mathbb Z/p^{e+1}\mathbb Z\), choosing at each stage a pivot of minimum \(p\)-adic valuation in the remaining submatrix. Such a pivot divides all entries in that submatrix in the discrete valuation ring; after integral row and column elimination it yields the next local Smith valuation. The code uses row elimination, which leaves an upper triangular matrix with the same valuations. The exponent bound \(e+1\), where \(e=v_p(\det L_{\mathrm{red}})\), is sufficient to distinguish all finite valuations. In increasing order, the resulting valuation multiplicities are

\[
\begin{array}{c|l}
p & \text{valuations and multiplicities (69 factors total)}\\\hline
2 & 0^{[60]},2^{[1]},3^{[8]}\\
3 & 0^{[61]},2^{[1]},3^{[7]}\\
7 & 0^{[64]},1^{[5]}\\
719 & 0^{[63]},1^{[6]}.
\end{array}
\]

Combining the four sorted prime-local lists gives 60 unit factors, then \(4,72,216,155304\), then five copies of \(1087128\). Both independently rooted Laplacians give the identical list. Because the product equals the independently determined determinant, this is the complete Smith form.

**4. Arithmetic interpretation.** By Raynaud's component-group theorem for regular semistable curves, the component group of the Néron model of the Jacobian of a smooth generic fiber is the Jacobian (critical group) of its dual graph when every node has thickness one. Applying it to \(B\) proves the final assertion. Existence of suitable formal smoothings follows from standard unobstructedness of nodal stable curves, although the theorem is stated for any such smoothing rather than asserting a canonical one.

## Verification

The included file `verify_klein_boundary.py` is a complete standalone standard-library checker and needs only `python3 verify_klein_boundary.py`. It computes incidence directly from the 21 coefficient rows; checks all 210 pairs; reconstructs the 70-vertex graph; verifies the 21-vertex spectral polynomial identity and ranks; computes the independent weighted determinant; and computes the four local Smith valuation lists for two distinct roots. The included `CHECKS.txt` contains the actual successful execution output. No floating-point geometry or incomplete finite enumeration is used in the proof or checker.

## Relationship to prior work

Klein's configuration and its 49 singular points are classical. Seceleanu's 2014 preprint identifies the 21-line/49-point incidence and studies its symbolic-power ideal, not this stable boundary's integral critical group. Gévay–Pokora construct and compare Klein configurations and supply equations; their geometric configuration and rigidity results do not compute the present Néron group. Innamorati studies derived finite-field quasi-configurations, not integer Laplacian invariant factors. Bauer–Di Rocco–Harbourne–Huizenga–Seceleanu–Szemberg (arXiv:1609.08648) study this exact blowup surface and its invariant negative curves and point ideals, but do not compute the integral critical group of the nodal boundary. The classical Raynaud theorem supplies the component-group interpretation, but it does not compute this graph's group.

Related exact calculations for the *quadruple-only* \(42\)-vertex Klein Levi graph and the *triple-only* \(49\)-vertex dual-bitangent Levi graph concern different reduced incidence graphs; neither integral Smith group determines the result for the complete \(70\)-vertex graph. In particular the present prime \(719\) is not obtained simply from either group's order. This statement is about the simultaneous inclusion of all 49 singular points, not one of those two subconfigurations.

## Limitations

The numerical group is an exact algebraic consequence of the explicitly stated classical line equations and the standard graph/Laplacian construction. Historical priority is not independently established: an older unindexed graph-invariant table or an alternative presentation of the full \(70\)-vertex incidence graph could already contain its Smith form. The result does not identify the Néron component group for a nonregular smoothing, for arbitrary edge thicknesses, or for the singular original union before blowing up its multiple intersections. The calculation does not assert anything about the divisor-class group of the ambient surface. Independent mathematical validation remains unperformed.

## References

1. A. Seceleanu, *A homological criterion for the containment between symbolic and ordinary powers of some ideals of points in \(\mathbb P^2\)*, first submitted October 2, 2014, arXiv:1410.0312, especially Section 4.2. https://arxiv.org/pdf/1410.0312
2. G. Gévay and P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309, Section 2 (2022/2023). https://arxiv.org/abs/2211.15309
3. S. Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, Axioms 13 (2024), 321, Section 4. https://doi.org/10.3390/axioms13050321
4. O. Amini, M. Baker, E. Brugallé and J. Rabinoff, *Lifting harmonic morphisms I* (for the cited formulation of Raynaud's component-group theorem), Section 8; https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf
5. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu and T. Szemberg, *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, first public September 27, 2016, arXiv:1609.08648, Sections 1–2 and Appendix. https://arxiv.org/pdf/1609.08648
