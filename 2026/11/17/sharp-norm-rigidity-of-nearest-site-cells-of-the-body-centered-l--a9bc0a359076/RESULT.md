# Sharp norm rigidity of nearest-site cells of the body-centered lattice

## Finding
For every integer \(d\ge 1\), let
\[
\Lambda_d=\mathbb Z^d\cup\bigl(\mathbb Z^d+\tfrac12\mathbf1\bigr).
\]
This is a lattice of covolume \(1/2\). Write \(V_p(\lambda)\) for the closed nearest-site cell of \(\lambda\in\Lambda_d\) in the coordinate \(\ell_p\) norm, \(1\le p\le\infty\). The following is an exact classification, not merely a combinatorial equivalence.

**Theorem (sharp exponent and dimension classification).** The complete family of nearest-site cells \(\{V_p(\lambda):\lambda\in\Lambda_d\}\) agrees with the Euclidean family \(\{V_2(\lambda):\lambda\in\Lambda_d\}\), with corresponding sites fixed, precisely in these cases:

* \(d=1\) or \(d=2\), for every \(1\le p\le\infty\);
* \(d\ge3\), exactly for \(p=1\) and \(p=2\).

Outside these cases the nearest-site maps differ on a **nonempty open set**, not just on their tie boundaries. In all dimensions,
\[
V_1(0)=V_2(0)=\Bigl\{x\in[-\tfrac12,\tfrac12]^d:\sum_{i=1}^d|x_i|\le\tfrac d4\Bigr\}.
\]
Thus the usual body-centered cubic lattice in dimension three has exactly the same labeled truncated-octahedral Voronoi tiling under Manhattan and Euclidean distance. The coincidence persists under arbitrary common positive coordinate weights: for \(w_i>0\), the nearest-site cells for the costs \(\sum_iw_i|x_i-\lambda_i|\) and \(\sum_iw_i(x_i-\lambda_i)^2\) coincide, and the origin cell is
\[
\Bigl\{x\in[-\tfrac12,\tfrac12]^d:\sum_iw_i|x_i|\le\tfrac14\sum_iw_i\Bigr\}.
\]
The weights in the two costs are the same; this assertion does not compare arbitrary independently weighted metrics.

## Assumptions and scope
All dimensions are positive integers. Distances are measured in the fixed coordinate system of \(\Lambda_d\), not after arbitrary rotations. The convention for nearest-site cells includes all sites tied for the minimum; the strict disagreement for excluded exponents is independent of tie conventions. For \(p=\infty\), \(\ell_\infty\) denotes the maximum-coordinate norm. Positive weights are finite and fixed. No general equality of \(\ell_1\)- and \(\ell_2\)-Voronoi diagrams for arbitrary lattices is asserted.

## Proof
**1. Reduction to two coset representatives.** The lattice is closed under addition because twice \(\tfrac12\mathbf1\) is integral. Translate by an integer vector and reflect individual coordinates to reduce to \(x=(x_1,\dots,x_d)\) with \(0\le x_i\le\tfrac12\). Reflections preserve each coset because \(-\tfrac12\equiv\tfrac12\pmod{\mathbb Z}\). In this cube a nearest integer-lattice point is \(0\), and a nearest half-integer-lattice point is \(h=\tfrac12\mathbf1\), for every coordinatewise monotone \(\ell_p\) cost. For interior cube points both representatives are the unique minimizers within their own cosets; boundary cases follow by closure. For finite \(p\), comparing the two selected representatives is equivalent to comparing
\[
A_p(x)=\sum_i x_i^p,\qquad B_p(x)=\sum_i(\tfrac12-x_i)^p.
\]
For \(p=\infty\), compare \(\max_i x_i\) and \(\tfrac12-\min_i x_i\).

**2. Exact weighted coincidence.** For positive \(w_i\), the weighted Manhattan difference and the weighted squared-Euclidean difference are respectively
\[
\sum_iw_i\bigl(x_i-(\tfrac12-x_i)\bigr)=2\sum_iw_ix_i-\tfrac12\sum_iw_i,
\]
\[
\sum_iw_i\bigl(x_i^2-(\tfrac12-x_i)^2\bigr)=\tfrac12\sum_iw_ix_i-\tfrac18\sum_iw_i.
\]
The first is exactly four times the second, hence both select the same nearest coset and have identical ties. Within each coset, coordinatewise rounding is optimal for both costs. Undoing the reflections yields the weighted origin cell above. Setting \(w_i=1\) proves coincidence for \(p=1,2\) in every dimension.

**3. The two-coordinate exception.** For finite \(p\ge1\), put \(a=\tfrac14\), \(u_i=x_i-a\), and define the odd, strictly increasing function
\[
g_p(u)=(a+u)^p-(a-u)^p\qquad(-a\le u\le a).
\]
With two coordinates, \(A_p-B_p=g_p(u_1)+g_p(u_2)\). Since \(g_p\) is odd and strictly increasing, this expression has the sign of \(u_1+u_2\). With one coordinate the same conclusion is immediate. For \(p=\infty\), in two coordinates
\[
\max\{x_1,x_2\}-(\tfrac12-\min\{x_1,x_2\})=x_1+x_2-\tfrac12,
\]
and in one coordinate it is \(2x_1-\tfrac12\). Thus every \(\ell_p\) selects the same two coset representatives in dimensions one and two. Applying lattice translations and coordinate reflections gives equality of their entire closed cell families, including ties.

**4. Exhaustion in dimensions at least three.** Fix \(1<p<\infty\), \(p\ne2\). In the cube, for small \(t>0\), consider the first three displaced coordinates \((u_1,u_2,u_3)=(t,t,-2t)\), with all additional \(u_i=0\). The Euclidean and Manhattan two-coset differences vanish. For the \(p\)-cost, Taylor expansion at the strictly positive point \(a=1/4\) gives
\[
g_p(u)=2p a^{p-1}u+\frac{p(p-1)(p-2)}{3}a^{p-3}u^3+O_p(u^5),
\]
so
\[
2g_p(t)-g_p(2t)=-2p(p-1)(p-2)a^{p-3}t^3+O_p(t^5),
\]
which is nonzero for all sufficiently small \(t\). Perturb the third coordinate by a still smaller number of the opposite sign to this difference. The Manhattan difference now has the sign of the perturbation, while the \(p\)-difference retains its previous sign. Hence the two nearest cosets disagree strictly. Continuity gives an open disagreement region. For \(p=\infty\), take the same three coordinates and perturb the third displacement upward by \(0<\delta<t\). Their sum is positive, so \(\ell_1\) selects the half-integer coset, but \(\max_i x_i=a+t<a+2t-\delta=\tfrac12-\min_i x_i\), so \(\ell_\infty\) selects the integer coset. The same positive-volume conclusion follows. This proves necessity and finishes the classification.

## Verification
`verify_norm_rigidity.py` is a standalone Python-standard-library check. It compares direct enumerated lattice-site minima against the two-coset formula for dimensions one through four and all sampled exponents, checks exponent coincidence in dimensions one and two and at \(p=1,2\), exhibits strict disagreement witnesses for exponents on both sides of two and at infinity, and independently tests positive weighted cost differences. The deterministic seeded run reports `PASS 9011 deterministic seeded geometric checks`. These numerical and finite checks supplement the exact argument; the Taylor step and the universal quantifiers are proved above rather than inferred from testing. To reproduce, run `python3 verify_norm_rigidity.py` from the directory holding the two files.

## Relationship to prior work
Lian and Xue (2026) proved the sharp \(9/8\) lattice covering density of the regular octahedron using the body-centered cubic lattice. This motivates comparing the octahedral \(\ell_1\) geometry with the classical Euclidean body-centered cubic Voronoi tiling. The ordinary Euclidean truncated-octahedral cell and the optimal covering are preexisting facts, not claimed as new. Deza and Dutour Sikirić (2015) developed general algorithms for polyhedral-norm lattice Voronoi cells; Blömer and Kohn (2018) developed general theory for arbitrary norms. Neither general description logically forces the sharp all-exponent classification for this specific two-coset lattice; the precise novelty claim is the labeled-cell identity with arbitrary common diagonal weights and the if-and-only-if exponent/dimension breakdown, including open counterexample regions. A separate published record on exact subcritical octahedral-lattice covering profiles determines the distribution of **minimum \(\ell_1\) distance**, but a one-metric distribution does not determine the cross-norm equality of nearest-site maps. An inaccessible full text could contain an earlier equivalent statement, as acknowledged below.

## Limitations
The theorem is tied to coordinate \(\ell_p\) geometry and to the half-diagonal two-coset lattice. It does not characterize all lattices whose Voronoi diagrams remain fixed under different norms. Finite checks do not independently certify the infinite-dimensional or continuum-parameter claims. Full text of the recent covering paper and of two older broad norm-Voronoi papers could not be retrieved in this inspection; any precise overlap hidden there remains a historical-priority risk. None of the covering-optimality claims of earlier authors are reproved or extended here.

## References
1. Yanlu Lian and Fei Xue, *The lattice covering density of the regular octahedron*, arXiv:2609.23210, first public version 2026-09-19, https://arxiv.org/abs/2609.23210.
2. Michel Deza and Mathieu Dutour Sikirić, *Voronoi polytopes for polyhedral norms on lattices*, Discrete Applied Mathematics **197** (2015), 42–52; arXiv:1401.0040, https://arxiv.org/abs/1401.0040.
3. Johannes Blömer and Kathlén Kohn, *Voronoi Cells of Lattices with Respect to Arbitrary Norms*, SIAM Journal on Applied Algebra and Geometry **2** (2018), 314–338; arXiv:1512.00720, https://arxiv.org/abs/1512.00720.
4. J. H. Conway and N. J. A. Sloane, *Voronoi regions of lattices, second moments of polytopes, and quantization*, IEEE Transactions on Information Theory **28** (1982), 211–226, https://doi.org/10.1109/TIT.1982.1056483.
