# A complete Euclidean ridge-angle census and Gaussian concentration for the simplex-sum stellohedron

## Finding
Let \(m\ge2\) be an integer. Label the hub of \(K_{1,m}\) by \(0\), its leaves by \([m]\), and put
\[
K_m=\sum_{\varnothing\ne B\subseteq[m]}
  \operatorname{conv}\{e_0,e_i:i\in B\}\subset\mathbb R^{m+1}.
\]
The metric is the Euclidean metric inherited by the affine hull, parallel to the sum-zero hyperplane. The entire multiset of **interior dihedral angles at ridges** of this dimension-\(m\) polytope is the sum of the following three families. Repeated numerical angles in different rows or parameter choices have additive multiplicities:

1. **Two distinct leaf facets:** \(\arccos(1/m)\), with multiplicity \(\binom m2\).
2. **A leaf facet inside a hub tube:** for each \(1\le s\le m-1\),
   \[
   \pi-\arccos\sqrt{\frac{m-s}{m(s+1)}}
   \quad\text{with multiplicity}\quad s\binom ms.
   \]
3. **Two strictly nested hub tubes:** for every \(0\le s<t\le m-1\),
   \[
   \pi-\arccos\sqrt{\frac{(s+1)(m-t)}{(t+1)(m-s)}}
   \quad\text{with multiplicity}\quad\binom mt\binom ts.
   \]
Consequently, there are exactly \(\binom m2\) acute ridges, **no** right ridges, and
\[
R_m=3^m+(m-4)2^{m-1}+\binom{m-1}{2}
\]
total ridges. For a uniformly selected ridge angle \(\Theta_m\),
\[
\boxed{\quad \Theta_m\xrightarrow{\mathsf P}\frac{2\pi}{3},\qquad
\sqrt m\bigl(\Theta_m-2\pi/3\bigr)
\xrightarrow{\mathrm d}N(0,3/8).\quad}
\]
The fraction of acute ridges is \(\binom m2/R_m\sim m^2/(2\,3^m)\).

For \(m\ge4\), the **largest** angle is \(\pi-\arccos c_m\), where
\[
c_m=\begin{cases}
\frac{k}{k+1},&m=2k,\\
\sqrt{\frac{k}{k+2}},&m=2k+1.
\end{cases}
\]
It occurs at exactly \(k\binom{2k}{k}\) ridges when \(m=2k\), and at exactly \((2k+1)\binom{2k+1}{k}\) ridges when \(m=2k+1\). Its deficit from a flat angle obeys \(\pi-\max\Theta_m\sim2/\sqrt m\). Hence the nearly-flat extreme is exponentially rare while almost all ridge angles concentrate near \(2\pi/3\).

## Assumptions and scope
A *ridge* is a codimension-two face. Its interior dihedral angle is \(\pi\) minus the angle between its two outward unit facet normals. The stated sum includes every nonempty hub-plus-leaves simplex, including the full-vertex-set simplex. Singleton tube simplices would only translate \(K_m\), and are thus immaterial. This is the **specified intrinsic Euclidean realization** in \(\mathbb R^{m+1}\), not a claim about arbitrary combinatorially equivalent stellohedra or the ordinary Euclidean metric after nonorthogonally dropping the hub coordinate.

## Proof
**Facets and ridge incidences.** The standard connected-tube graph-associahedron construction identifies its facets with the proper nonempty tubes of \(K_{1,m}\), and its ridges with unordered compatible pairs of such tubes. A tube is either a leaf singleton \(\{i\}\) or \(\{0\}\cup S\) for \(S\subsetneq[m]\); two tubes are compatible if nested or disjoint and nonadjacent. Thus the only compatible pair types are (i) two different leaves, (ii) a leaf \(i\in S\) and hub tube \(\{0\}\cup S\), and (iii) hub tubes \(\{0\}\cup S\subsetneq\{0\}\cup T\) with \(S\subsetneq T\subsetneq[m]\). Each such pair extends to a maximal tubing and therefore defines one ridge; no other pair does. The unit-simplex sum is a simple realization with this tube fan, so each ridge has exactly those two incident facets.

**Angles.** Set \(N=m+1\). For a proper tube \(A\) its outward normal is a positive multiple of \(-u_A\), where \(u_A=\mathbf1_A-(|A|/N)\mathbf1\) is the orthogonal projection of its incidence vector onto the intrinsic sum-zero hyperplane. Consequently,
\[
\langle u_A,u_B\rangle=|A\cap B|-\frac{|A||B|}{N},\qquad
\|u_A\|^2=\frac{|A|(N-|A|)}{N}.
\]
For two distinct leaf tubes the outward-normal cosine is \(-1/m\), hence the interior angle is \(\arccos(1/m)\). For nested proper tubes \(A\subsetneq B\), the outward-normal cosine is strictly positive and equals
\[
\sqrt{\frac{|A|(N-|B|)}{|B|(N-|A|)}}.
\]
Substituting the respective cardinalities \((1,s+1)\) and \((s+1,t+1)\) yields the two asserted obtuse families. No scalar product vanishes and every listed angle is strictly between \(0\) and \(\pi\).

**Exact multiplicities.** There are \(\binom m2\) distinct unordered leaf pairs. Choosing a hub tube with \(s\) leaves and a distinguished contained leaf gives \(s\binom ms\) pairs. Choosing \(T\) of size \(t\) and \(S\subsetneq T\) of size \(s\) gives \(\binom mt\binom ts\) nested hub pairs. Summation gives
\[
\sum_{s=1}^{m-1}s\binom ms=m2^{m-1}-m,
\qquad
\sum_{t=1}^{m-1}\binom mt(2^t-1)=3^m-2^{m+1}+1.
\]
Adding the leaf-leaf family simplifies to the displayed \(R_m\). The acute proportion follows since \(R_m\sim3^m\).

**Gaussian limit.** The nested-hub family accounts for \(1-O(m(2/3)^m)\) of all ridges. Choose a nested-hub ridge uniformly and classify each leaf independently into three bins \(S\), \(T\setminus S\), \([m]\setminus T\). Before conditioning, these are independent uniform three-color assignments; the only forbidden events are that the second or third bin is empty. Their total probability is at most \(2(2/3)^m\), so this conditioning does not affect the limit. Write \(X=|S|\), \(Y=|T\setminus S|\), and \(Z=m-X-Y\). The cosine of the *exterior* normal angle is exactly
\[
C_m=\sqrt{\frac{(X+1)Z}{(X+Y+1)(Y+Z)}}.
\]
The multinomial law of large numbers gives \(C_m\to1/2\) in probability and \(\Theta_m=\pi-\arccos C_m\to2\pi/3\). For \(p=X/m\), \(r=Z/m\), the limiting smooth function is
\[
f(p,r)=\sqrt{\frac{pr}{(1-p)(1-r)}},\qquad
f(1/3,1/3)=1/2,
\quad \nabla f(1/3,1/3)=(9/8,9/8).
\]
The \(1/m\) corrections in the exact expression are negligible at scale \(\sqrt m\). Since \(p+r=1-Y/m\), the multinomial central limit theorem and delta method give
\[
\sqrt m(C_m-1/2)\xrightarrow{\mathrm d}N(0,9/32),
\]
as \(\operatorname{Var}(Y)=2m/9\). The derivative of \(c\mapsto\pi-\arccos c\) at \(c=1/2\) equals \(2/\sqrt3\). A second delta method produces variance \((4/3)(9/32)=3/8\). The exponentially negligible other ridge classes do not change the weak limit.

**Sharp nearly-flat extreme.** The angle is increasing in the positive exterior-normal cosine. Within hub-hub pairs, at fixed \(s\) this cosine decreases as \(t\) increases; hence the maximum occurs for \(t=s+1\). Writing \(j=s+1\), its squared cosine is
\[
\frac{j(m-j)}{(j+1)(m-j+1)},\qquad1\le j\le m-1.
\]
The product is symmetric and strictly maximized at the integer(s) nearest \(m/2\), by strict concavity of \(x\mapsto\log(x/(x+1))\). In the leaf-hub family the squared cosine is largest at \(s=1\), equaling \((m-1)/(2m)\). For \(m\ge4\) even the hub-hub value at \(j=2\) is larger: their difference is \((m-3)(m+1)/(6m(m-1))>0\). Substitution gives the parity formulas for \(c_m\). The sole maximizing value of \(j\) is \(k\) for \(m=2k\); the two values \(k,k+1\) tie for \(m=2k+1\). The binomial multiplicities follow from the hub-hub formula. The Taylor expansion \(\arccos(1-u)\sim\sqrt{2u}\) gives \(\arccos(c_m)\sim2/\sqrt m\). (In the small cases \(m=2,3\), the maximum is also attained by leaf-hub ridges, and the stated exact extreme counts are not asserted.)

## Verification
The accompanying standalone `verify.py`, requiring only Python 3's standard library, constructs all tube pairs and checks their normal-cosine identities and multiplicities for \(2\le m\le6\). It separately constructs the actual Minkowski-sum vertices by optimizing in every strict coordinate order and checks the exact rational affine ranks of the common active faces of every facet pair for \(2\le m\le5\). It also checks the sharp maximum-cosine formula for \(4\le m\le100\). Running `python3 verify.py` finishes with `STELLOHEDRON_RIDGE_SPECTRUM_PASS`. These are finite independent consistency checks; they do not replace the infinite tube-incidence proof and multinomial limit argument.

## Relationship to prior work
Pilaud, Santos and Ziegler (2023), Section 4.1, give the graph-associahedron tube compatibility, projected normal rays and Minkowski-sum realization used here. Behrend (2024), Section 3(v), writes the **exact same star unit-simplex sum** and records its combinatorial equivalence to partial permutohedra; this is not a Euclidean identification in their standard coordinates. In particular, dropping the hub coordinate is not an isometry: the squared intrinsic length corresponding to a leaf displacement \(d\in\mathbb R^m\) is \(\sum_i d_i^2+(\sum_i d_i)^2\). The total ridge count is already determined by the known face enumeration: it is \([t^{m-2}]h(t+1)\) for the stellohedron \(h\)-polynomial of Postnikov, Reiner and Williams, Section 10.4, equation (10.2). That polynomial does not keep track of angles.

The same-date type-A permutohedral ridge-angle result has substantial overlap with the nested-tube part. A nested pair \(A\subsetneq B\) gives the same two normal rays as the corresponding braid fan flag with ordered blocks \((A,B\setminus A,\{0,1,\ldots,m\}\setminus B)\). The hub-hub law is precisely the uniform braid-flag law conditioned on the hub in the first block. The leaf-hub family restricts instead to a singleton first block and the hub in the second block. Forcing the hub into the first block changes the normalized block sizes by \(O(1/m)\) relative to independent coloring with the hub free; excluding empty blocks has exponentially small cost. Thus the bulk Gaussian constants are shared. The maximal angle value also agrees with the maximum of the braid angle formula, since a balanced flag with singleton middle block can have its hub in the first block. The contribution here is the **full star-specific spectrum**: the disjoint leaf-pair ridges have no counterpart among nested braid flags, and the star restrictions give different weights and maximizing multiplicities.

The older standard-coordinate generalized parking-function angle law has right ridges, no acute ridges in its stellohedral regime, and bulk center \(3\pi/4\). Its formulas use a different metric and do not transfer by combinatorial equivalence. The contrast shows that changing the realization can change both the angle near which most ridges concentrate and whether acute or right ridges occur at all.

## Limitations
This is a metric statement for the displayed unit-weight realization, not for all affine deformations of the star graph associahedron. The central limit theorem describes uniformly sampled ridges (not ridge-area weighting or random supporting directions). The exact finite enumerations do not certify the all-dimensional statement. The literature comparison is not an exhaustive historical-priority proof; an unindexed equivalent tube-angle calculation remains possible.

## References
- V. Pilaud, F. Santos and G. M. Ziegler, *Celebrating Loday's Associahedron*, arXiv:2305.08471, first public 2023-05-15, especially Section 4.1. https://arxiv.org/html/2305.08471v1#S4.SS1
- R. E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975, first public 2024-03-11, especially Section 3(v), equation (11). https://arxiv.org/html/2403.06975v1
- C. Eur, J. Huh and M. Larson, *Stellahedral geometry of matroids*, arXiv:2207.10605, first public 2022-07-21, Sections 1 and 3. https://arxiv.org/abs/2207.10605
- A. Postnikov, *Permutohedra, associahedra, and beyond*, International Mathematics Research Notices (2009), foundational nested-set/generalized-permutohedral construction. https://arxiv.org/abs/math/0507163
- A. Postnikov, V. Reiner and L. Williams, *Faces of generalized permutohedra*, Sections 2.2 and 10.4. https://arxiv.org/html/math/0609184v2#S10.SS4
- *An exact type-A permutohedral ridge-angle law and its second-order Gaussian variance*, public result (22 November 2026). https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-an-exact-type-a-permutohedral-ridge-angle-law-and-its-second-ord--7a4bdf8175dd/RESULT.md
- *Universal dihedral-angle spectra and Gaussian ridge law for generalized parking-function polytopes*, public result (17 November 2026). https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-universal-dihedral-angle-spectra-and-gaussian-ridge-law-for-gene--676f0e5f85c3/RESULT.md
