# Determinantal transverse cones on every rank-two quasisymmetric Grassmannian component

## Finding

For every integer \(n\ge3\), the rank-two quasisymmetric Grassmannian \(\operatorname{QGr}(2,n)\) has \(n-2\) maximal irreducible components, indexed by two-part compositions \((b,a)\) of \(n-1\) [1]. The following is an explicit classification of the reduced singular locus and transverse analytic type of **each component**, not of the singular locus of their union.

Fix \(a,b\ge1\), \(a+b=n-1\), and choose the component \(X_{a,b}\) after its coordinate permutation so that its nonzero Plücker positions are the pairs joining different classes in
\[
L=\{1,\ldots,b\},\qquad \{c\}=\{b+1\},\qquad R=\{b+2,\ldots,n\}.
\]
Write \(U_i=p_{i,c}\), \(V_j=p_{c,j}\), \(W_{ij}=p_{i,j}\) for \(i\in L\), \(j\in R\). All Plücker coordinates within \(L\) or within \(R\) vanish. Define \(P_U\cong\mathbb P^{b-1}\) by \(V=W=0\) and \(P_V\cong\mathbb P^{a-1}\) by \(U=W=0\); these are disjoint closed subvarieties of \(X_{a,b}\).

Let \(D_s\) denote the affine determinantal variety of \(2\times s\) complex matrices of rank at most one, defined by all their \(2\times2\) minors. Then
\[
\operatorname{Sing}(X_{a,b})_{\mathrm{red}}=\bigl(P_U\text{ if }a\ge2\bigr)\ \sqcup\ \bigl(P_V\text{ if }b\ge2\bigr).
\]
The analytic transverse germ is \(D_a\) along every point of \(P_U\), and \(D_b\) along every point of \(P_V\). More precisely, the germ along \(P_U\) is a product of a smooth \((b-1)\)-dimensional germ and \((D_a,0)\), and the counterpart along \(P_V\) has smooth dimension \(a-1\) and transverse germ \((D_b,0)\).

At these points the Hilbert–Samuel multiplicities are respectively \(a\) and \(b\), and the local divisor class group is \(\mathbb Z\). A transverse cone \(D_s\) is Gorenstein (indeed an ordinary threefold double point) if \(s=2\), and is not \(\mathbb Q\)-Gorenstein if \(s\ge3\). Thus the non-\(\mathbb Q\)-Gorenstein locus is exactly \(P_U\) when \(a\ge3\) together with \(P_V\) when \(b\ge3\); there are no additional non-\(\mathbb Q\)-Gorenstein points.

## Assumptions and scope

All schemes and analytic germs are over \(\mathbb C\). Here \(n\ge3\), \(a,b\ge1\), \(a+b=n-1\). A missing projective stratum is omitted rather than interpreted as an empty negative-dimensional projective space. The claim concerns maximal irreducible components individually, with their reduced singular supports. No assertion is made about the nonreduced singular scheme of the entire reducible union \(\operatorname{QGr}(2,n)\).

For \(n=3\), \(a=b=1\), the component is \(\mathbb P^2\) and is smooth. For \(n=4\), the two components each have one isolated ordinary threefold double point, consistent with the square-pyramid moment-polytope example in [1]. For \(n=5\), the balanced component \((a,b)=(2,2)\) has two disjoint singular projective lines, transversely ordinary threefold nodes; the unbalanced components have one isolated transverse \(D_3\) singularity.

## Proof

**1. The component and its Plücker support.** The source construction identifies all maximal components with coordinate permutations of rank-two ribbon Richardson varieties [1, Theorem 6.7]. For composition \((b,a)\), a ribbon diagram is the skew shape \(\eta/\nu\) with \(\eta=(n-2,a)\) and \(\nu=(a-1,0)\). The two Grassmannian pivot pairs are \(\{1,b+1\}\) and \(\{b+1,n\}\). Thus the permitted Richardson coordinates are exactly \(p_{i,j}\) for \(1\le i\le b+1\le j\le n\), \(i<j\). Equivalently, the Plücker coordinates joining two elements of \(L\), or two elements of \(R\), vanish, and no other coordinate is required to vanish. Grassmannian Schubert/Richardson subvarieties are scheme-theoretically cut out by these coordinate vanishings inside the Grassmannian, and the local charts below independently exhibit the resulting reduced, irreducible variety.

**2. The \(U\)-charts.** Suppose \(U_1=p_{1,c}\ne0\). Choose the unique Grassmannian matrix representative with columns \(1\) and \(c\) equal to \((1,0)^\mathsf T\) and \((0,1)^\mathsf T\), respectively. Vanishing of the minors between any two columns of \(L\) forces column \(i\in L\) to be \((u_i,0)^\mathsf T\), with \(u_1=1\). Write the columns of \(R\) as \((v_j,w_j)^\mathsf T\). The only remaining equations are
\[
 v_jw_k-v_kw_j=0\quad(j,k\in R),
\]
which are exactly the defining minors of \(D_a\). Consequently there is an *algebraic isomorphism of entire principal affine charts*
\[
X_{a,b}\cap\{U_1\ne0\}\ \cong\ \mathbb A^{b-1}\times D_a.
\]
The same is true on every chart \(U_i\ne0\). In these charts \(P_U\) is precisely the locus \(v_j=w_j=0\) for all \(j\in R\).

**3. The \(V\)-charts.** Interchanging the roles of \(L\) and \(R\) gives, on every \(V_j\ne0\), the algebraic chart \(\mathbb A^{a-1}\times D_b\). The rank-zero locus of its \(2\times b\) matrix is \(P_V\) in that chart.

**4. The \(W\)-charts.** If \(W_{ij}=p_{i,j}\ne0\), fix columns \(i\in L\), \(j\in R\) as the standard basis vectors of \(\mathbb C^2\). The remaining \(b-1\) columns of \(L\) are independent multiples of the first, the remaining \(a-1\) columns of \(R\) independent multiples of the second, and the central column is arbitrary with two coordinates. Therefore
\[
X_{a,b}\cap\{W_{ij}\ne0\}\ \cong\ \mathbb A^{(b-1)+(a-1)+2}=\mathbb A^{a+b}.
\]
Every nonzero Plücker coordinate of a point in \(X_{a,b}\) is of type \(U,V\), or \(W\), so these charts cover the whole component. This excludes all other singular strata.

**5. Singular support and multiplicity.** For \(s=1\), \(D_1=\mathbb A^2\) is smooth. For \(s\ge2\), the nonzero matrices in \(D_s\) have rank exactly one and form a smooth \((s+1)\)-dimensional variety, while the origin has Zariski tangent dimension \(2s>s+1\). Hence its singular locus is exactly its origin. This proves the displayed reduced singular locus. For \(s\ge2\), \(D_s\) is the affine cone over the Segre embedding \(\mathbb P^1\times\mathbb P^{s-1}\) by \(\mathcal O(1,1)\). Its multiplicity at the vertex equals the degree of this Segre variety:
\[
\operatorname{mult}_0(D_s)=\int_{\mathbb P^1\times\mathbb P^{s-1}}(H_1+H_2)^s=s.
\]
A smooth product factor does not change multiplicity, yielding \(a\) on \(P_U\) and \(b\) on \(P_V\).

**6. Divisor classes and the canonical obstruction.** The punctured cone \(D_s\setminus\{0\}\) is the complement of the zero section in the line bundle \(\mathcal O(-1,-1)\) over \(\mathbb P^1\times\mathbb P^{s-1}\). Since the vertex has codimension at least two for \(s\ge2\), its local class group is
\[
\operatorname{Cl}(\mathcal O_{D_s,0})\cong\operatorname{Pic}(\mathbb P^1\times\mathbb P^{s-1})/\mathbb Z[\mathcal O(1,1)]\cong\mathbb Z.
\]
The canonical class corresponds to \(\mathcal O(-2,-s)\) modulo \(\mathcal O(1,1)\); its class is \(s-2\) times a primitive generator. Thus it is torsion precisely for \(s=2\), when it is Cartier. For \(s=2\), the sole determinantal equation is a nondegenerate quadratic form in four variables, giving an ordinary threefold double point. For \(s\ge3\), the canonical class has infinite order, so the vertex is not \(\mathbb Q\)-Gorenstein. Adding a smooth factor preserves all these local conclusions.

## Verification

The standalone script `verify_ribbon_singularities.py` checks the affine chart exponent lattices for all \(64\) pairs \(1\le a,b\le8\), including the dimensions of the rank-one matrix relations and smooth mixed-pair charts. It also exhaustively enumerates the \(2\times s\) matrices over \(\mathbb F_2\), for \(1\le s\le7\), and verifies their rank-one counts. Finally it checks the leading differences of the Segre Hilbert function \((d+1)\binom{d+s-1}{s-1}\), which give multiplicity \(s\). These are independent finite corroborations; the proof above, not enumeration, establishes the result for all \(a,b\).

## Relationship to prior work

Bergeron, Gagnon, Spink, and Tewari [1] introduced the varieties, proved the correspondence with translated ribbon Richardson varieties, and explicitly described the singular square-pyramid components for \(n=4\). The present result starts from their component identification; it does **not** claim that construction, toricity, or the component count as new. Its contribution is the complete, uniform determination of every reduced singular stratum, the entire local product charts, their transverse analytic determinantal types and multiplicities, and their local canonical-class obstruction.

Billey–Weaver [2] and Fluegemann [3] provide general smoothness tests for positroid varieties, and Fluegemann also has general fixed-point multiplicity methods [4]. Those methods can be applied to individual cases, but the inspected material does not state the all-parameter transverse local-isomorphism theorem above. Lasoń–Michałek [5] classified Gorenstein matroid polytopes; no global Gorenstein criterion is presented here as an independent new theorem. Gonzales–Le–Lowen [6] study toric Richardson varieties and their cohomology; a full-text comparison of this source was not possible, so it is an explicit historical-priority risk.

## Limitations

Only the stated maximal rank-two components are classified, individually over \(\mathbb C\). The result does not describe scheme-theoretic intersections of distinct components, the reduced or nonreduced singular locus of their full union, or higher-rank quasisymmetric Grassmannians. It also does not claim that general determinantal-cone theory, general smoothness criteria, or previously known Gorenstein classifications are new. The classification's historical priority requires independent literature review.

## References

[1] N. Bergeron, L. Gagnon, H. Spink, V. Tewari, *The Quasisymmetric Grassmannian*, arXiv:2604.24903, first submitted 2026-04-27, revised 2026-11-04, especially Theorem 6.7, Figure 1, Section 9.

[2] S. C. Billey, J. E. Weaver, *A Pattern Avoidance Characterization for Smoothness of Positroid Varieties*, arXiv:2204.09013 (2022), especially Theorems 1.3–1.5.

[3] J. Fluegemann, *Smooth Points on Positroid Varieties*, arXiv:2407.21116 (2024), especially the smoothness test by affine pipe dreams.

[4] J. Fluegemann, *Singular Points on Positroid Varieties and Planar N=4 Supersymmetric Yang-Mills Theory*, arXiv:2608.28735 (2026), abstract; full text not accessible during comparison.

[5] M. Lasoń, M. Michałek, *Gorenstein matroids*, arXiv:2005.08359, especially Theorem 7.1; the studied arithmetic Gorenstein property of base polytopes must be distinguished from the local projective \(\mathbb Q\)-Gorenstein condition.

[6] T. Gonzales, T. Le, C. Lowen, *A quasisymmetric analog of Grassmannian Schubert varieties*, arXiv:2609.30257 (2026); only the abstract was accessible during comparison.
