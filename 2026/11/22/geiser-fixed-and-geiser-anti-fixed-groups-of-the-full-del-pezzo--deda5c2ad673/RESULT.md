# Geiser-fixed and Geiser-anti-fixed groups of the full del Pezzo exceptional boundary

## Finding
For every smooth degree-two del Pezzo surface \(S\) over \(\mathbb C\), let \(\Gamma\) be the canonical multigraph whose vertices are all 56 exceptional curves and which has \(E\cdot F\) parallel edges for any two distinct exceptional curves \(E,F\). The anticanonical double-cover involution \(\iota\) (the Geiser involution) exchanges the 28 paired exceptional curves and acts on the integral critical group \(K=K(\Gamma)\).

Define the fixed and anti-fixed subgroups, respectively, by
\[
K^+=\ker(\iota_*-1:K\to K),\qquad K^-=\ker(\iota_*+1:K\to K).
\]
The **complete integral decompositions** are
\[
\boxed{K^+\cong \mathbb Z/2\mathbb Z\oplus(\mathbb Z/28\mathbb Z)^{26}},
\]
\[
\boxed{K^-\cong(\mathbb Z/2\mathbb Z)^6\oplus(\mathbb Z/28\mathbb Z)^{14}\oplus(\mathbb Z/560\mathbb Z)^7}.
\]
In particular the Geiser involution acts by negation on the entire 5-primary subgroup of \(K\), whereas its fixed subgroup has **no 5-primary torsion**. Also,
\[
|K^+|\,|K^-|=2|K|,
\]
so the two canonical subgroups are **not** an integral direct-sum decomposition of \(K\). The one-factor-of-two discrepancy detects an integral gluing phenomenon invisible in rational eigenspaces.

This is an equivariant refinement of the known nonequivariant group
\[
K\cong (\mathbb Z/28\mathbb Z)^{40}\oplus \mathbb Z/560\mathbb Z\oplus(\mathbb Z/1120\mathbb Z)^6;
\]
that nonequivariant decomposition is treated as prior information, **not** as the new claim. If the full exceptional divisor is nodal and occurs as the special fiber of a proper regular split semistable smoothing with unit node thicknesses on which \(\iota\) extends, the same formulas describe the fixed and anti-fixed subgroups of the geometric Néron component group, including its induced Geiser action.

## Assumptions and scope
Let \(S=\operatorname{Bl}_{p_1,\ldots,p_7}\mathbb P^2\) for seven complex points in del Pezzo general position, with plane hyperplane class \(H\), exceptional classes \(F_1,\ldots,F_7\), and \(K_S=-3H+\sum_iF_i\). The intersection form is \(H^2=1\), \(F_i^2=-1\), all other basis pairings zero. The 56 exceptional curves are seven \(F_i\), 21 curves \(H-F_i-F_j\), 21 curves \(2H-\sum_{i\in I}F_i\) over five-element sets \(I\), and seven cubics \(3H-2F_i-\sum_{j\ne i}F_j\). The Geiser action sends every exceptional class \(E\) to \(-K_S-E\). It pairs the seven exceptional divisors with the seven cubics and the 21 lines with the complementary 21 conics.

All claims about \(K\), \(K^+\) and \(K^-\) concern the intersection-multiplicity multigraph; they are valid on **every** smooth complex degree-two del Pezzo surface and do not assume nodality of the reduced full exceptional divisor. The final Néron interpretation is conditional on nodality, the actual existence of the stated equivariant regular semistable smoothing, and unit thicknesses. No assertion is made for all special surfaces or arithmetic twists.

## Proof
**1. The canonical graph and involution.** Represent an exceptional curve class \(dH-\sum m_iF_i\) by \((d,m_1,\ldots,m_7)\); its pairing with a class \((d',m'_1,\ldots,m'_7)\) is \(dd'-\sum m_i m'_i\). The four class families above enumerate all 56 curves. Among the 1540 unordered pairs, exactly 756 have intersection zero, 756 have intersection one, and 28 Geiser pairs have intersection two. Hence \(\Gamma\) is a connected 29-regular multigraph with 812 edges. Let \(B\) be the integer \(8\times56\) matrix of class columns, \(J=\operatorname{diag}(1,-1,\ldots,-1)\), and \(L\) the graph Laplacian. Then \(L=28I-B^TJB\). An exact eight-dimensional Gram calculation yields the Laplacian eigenvalue multiset \(0^1,28^{48},40^7\) and \(|K|=\tau(\Gamma)=2^{114}5^7 7^{47}\). Direct Smith reduction gives the nonequivariant invariant factors \(1^8,28^{40},560,1120^6\); these baseline facts are also independently replayed by `verify.py`.

The unique nontrivial deck transformation \(\iota\) sends \(E\mapsto -K_S-E\). Since \((-K_S)^2=2\) and \((-K_S)\cdot E=1\) for all exceptional \(E\),
\[
(-K_S-E)\cdot(-K_S-F)=2-1-1+E\cdot F=E\cdot F.
\]
Thus \(\iota\) is an automorphism of the weighted graph, interchanging all 28 vertex pairs and preserving its Laplacian.

**2. Integral action on the degree-zero divisor presentation.** Choose a root vertex \(r\) and let \(I\) be the remaining 55 vertices. Write \(M=L_{I,I}\) for the reduced Laplacian. The degree-zero divisor lattice has basis \(b_i=[i]-[r]\), \(i\in I\), and
\[
K=\mathbb Z^{55}/M\mathbb Z^{55}.
\]
The involution acts in this basis by the exact integer matrix
\[
T_{j i}=\mathbf1_{j=\iota(i)}-\mathbf1_{j=\iota(r)},\qquad i,j\in I.
\]
For \(\epsilon\in\{1,-1\}\), define the integral rectangular presentation
\[
P_\epsilon=[\,M\mid T-\epsilon I_{55}\,].
\]
Its cokernel is \(K/(\iota_* -\epsilon)K\). The graph critical group has its canonical perfect monodromy pairing with values in \(\mathbb Q/\mathbb Z\), invariant under graph automorphisms. Since \(\iota_*^2=1\), the endomorphism \(\iota_* -\epsilon\) is self-adjoint. Therefore Pontryagin duality identifies the dual of \(\operatorname{coker}(\iota_* -\epsilon)\) with \(\ker(\iota_* -\epsilon)\); a finite abelian group is abstractly isomorphic to its Pontryagin dual. It is consequently enough to compute the integral Smith invariants of \(P_\epsilon\), not merely their orders.

**3. Exact local Smith calculations.** The accompanying `verify.py` constructs both \(55\times110\) matrices explicitly for four different root choices, and performs unimodular row and column operations modulo \(2^{115}\), \(5^8\), and \(7^{48}\). These precisions strictly exceed the corresponding valuations \(114,7,47\) of the independently verified determinant \(\det(M)\). Adding columns to \(M\) can only reduce its cokernel; therefore its prime-primary orders divide \(|K|\), so the modular Smith valuations are exact rather than truncated. For **each** root the valuation multiplicities among the 55 Smith factors are:

\[
\begin{array}{c|c|c|c}
 &p=2&p=5&p=7\\\hline
\epsilon=+1 &0^{[28]},1^{[1]},2^{[26]}&0^{[55]}&0^{[29]},1^{[26]}\\
\epsilon=-1 &0^{[28]},1^{[6]},2^{[14]},4^{[7]}&0^{[48]},1^{[7]}&0^{[34]},1^{[21]}
\end{array}
\]

Here \(v^{[m]}\) denotes \(m\) occurrences of the integer valuation \(v\), rather than exponentiation. The smith factors for \(P_{+1}\), in order, are \(1^{[28]},2,28^{[26]}\); those for \(P_{-1}\) are \(1^{[28]},2^{[6]},28^{[14]},560^{[7]}\). Their cokernel structures are exactly the two claimed fixed and anti-fixed structures by the pairing argument. No other primes occur because the augmented cokernels are quotients of \(K\).

**4. Structural consequences.** The plus group has order \(2^{53}7^{26}\), and the minus group has order \(2^{62}5^7 7^{21}\). Their product is \(2^{115}5^7 7^{47}=2|K|\), ruling out a direct-sum splitting via the two subgroups. Since the whole 5-primary part of \(K\) is \((\mathbb Z/5)^7\), and the minus subgroup contains exactly that entire 5-primary order while the plus subgroup contains none, \(\iota_*\) acts by \(-1\) on all 5-primary torsion. This concludes the theorem.

## Verification
Run `python3 verify.py` with standard Python 3 and no external libraries. It prints `GEISER_FIXED_ANTIFIXED_COMPONENT_GROUPS_OK` only after rebuilding all exceptional classes, reconstructing 812 edge multiplicities, verifying the 28 Geiser vertex swaps and Laplacian equivariance, and replaying twelve separate rectangular Smith calculations for each sign (three primes and four roots), as well as the nonequivariant controls and four exact Bareiss reduced determinants. Each local pivot is a unit-times-prime-power and all operations are invertible over the indicated finite rings. The computed factor lists agree in all root choices. No floating-point experiments or external certificates are used.

## Relationship to prior work
The degree-two del Pezzo exceptional-curve classes and the bitangent/Geiser pairing are classical (Knecht–Reyes; Rieken). The ordinary integral critical group of this same 56-vertex, 812-edge weighted intersection graph is treated here as a known baseline, not as a novel assertion. Its invariant factors alone do **not** determine the integral automorphism action: a finite abelian group can carry inequivalent involutions with different fixed subgroups. Reiner–Tseng's graph-covering theory and Glass's dihedral-action results explain the importance of equivariant graph Jacobians, but their general statements and examples do not identify the specific Geiser fixed and anti-fixed integral groups of this 56-curve boundary. The current computation additionally resolves the two-primary interaction which cannot be inferred from rational \(\pm1\)-eigenspaces. A search for equivalent formulations under antipodal, signed-graph and geometric-component terminology found no statement giving these exact two groups; historical priority remains provisional, not certified by search failure.

## Limitations
These are abstract isomorphism types of two subgroups of the finite graph Jacobian, **not** a claim of a canonical direct-sum decomposition. The nodal geometric and Néron interpretations require their separately specified geometric and equivariance hypotheses. The graph involution has edge behavior near Geiser pairs that prevents treating it indiscriminately as a free unramified graph double cover; the proof uses the direct integral presentation instead. The calculations do not classify other Weyl-group involutions, Frobenius types, nonregular models, or nonunit node thickness. An unindexed historical treatment of this involution could affect priority.

## References
1. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields* (2015-10-15), https://arxiv.org/abs/1510.04621. Sections 1–2 classify the 56 exceptional curves and describe their Geiser-paired intersections.
2. S. Rieken, *Moduli of real pointed quartic curves*, Geometriae Dedicata 185 (2016), 171–203, https://doi.org/10.1007/s10711-016-0174-0. Section 3.3 describes the geometric marking and all 28 pairs under the Geiser involution.
3. V. Reiner and D. Tseng, *Critical groups of covering, voltage, and signed graphs* (first public 2013-01-14), https://arxiv.org/abs/1301.2977. Sections 1–2 and 7–10 give general graph critical-group presentations and double-cover methods; they do not compute the two Geiser groups in this theorem.
4. D. Glass, *Critical Groups of Graphs with Dihedral Actions II* (first public 2015-08-21), https://arxiv.org/abs/1508.05401. General results about Jacobians of graphs with group actions.
5. A. E. Brouwer and R. J. Riebeek, *The spectra of Coxeter graphs*, Journal of Algebraic Combinatorics 8 (1998), 15–28, https://doi.org/10.1023/A:1008670825910. Classical non-equivariant Coxeter-graph spectra, not the present integral action.
