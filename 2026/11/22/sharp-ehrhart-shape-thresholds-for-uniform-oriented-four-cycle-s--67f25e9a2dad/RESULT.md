# Sharp Ehrhart-shape thresholds for uniform oriented four-cycle simplices

## Finding
For each integer \(w\ge 2\), let \(e_1,\ldots,e_4\) be the standard basis of \(\mathbb R^4\), with indices modulo four, and set
\[
 P_w=\operatorname{conv}\{e_j+w e_{j-1}:1\le j\le4\}.
\]
This is a three-dimensional lattice simplex in the affine lattice \(\{x\in\mathbb Z^4:\sum_i x_i=w+1\}\), whose normalized volume is \(w^3-w^2+w-1\). Its Ehrhart numerator is exactly
\[
 h^*_{P_w}(t)=1+\binom{w}{3}t+\frac{2w^3+w-6}{3}t^2+\binom{w}{3}t^3.
\]
(The binomial coefficient is zero when \(w=2\).) Three distinct sharp transitions occur:
\[
 \begin{array}{c|c}
 \text{property of the coefficient sequence or polynomial}&\text{exact parameter range}\\ \hline
 \text{unimodal coefficient sequence}&w\ge3\\
 \text{log-concave coefficient sequence}&w\ge5\\
 \text{all zeros simple, real and strictly negative}&w\ge7.
 \end{array}
\]
In particular, at all integer weights \(w\ge7\), the Ehrhart numerator has three simple negative real zeros even though the weighted-oriented edge simplex does not have the integer decomposition property for any \(w\ge2\), by the published non-IDP theorem for oriented cycles.

## Assumptions and scope
The coefficient sequence is \((h_0^*,h_1^*,h_2^*,h_3^*)\), including its trailing zero at \(w=2\). Unimodality means it weakly increases and then weakly decreases, and log-concavity means \((h_i^*)^2\ge h_{i-1}^*h_{i+1}^*\) for both interior indices. The Ehrhart generating function is \(\sum_{m\ge0}|mP_w\cap\mathbb Z^4|t^m=h^*_{P_w}(t)/(1-t)^4\). All counts and volume are taken in the affine difference lattice induced from \(\mathbb Z^4\). No assertion is made for nonintegral, nonuniform or differently oriented weights.

## Proof
**1. The lattice simplex and its volume.** Let \(M_w\) be the matrix with \((M_w)_{ij}=\delta_{ij}+w\delta_{j,i+1\pmod4}\). Its columns are the four specified vertices and
\[
 \det M_w=1-w^4\neq0,\qquad\mathbf1^{\mathsf T}M_w=(w+1)\mathbf1^{\mathsf T}.
\]
They are affinely independent and lie on the primitive affine hyperplane \(\sum x_i=w+1\). A lattice basis of the difference hyperplane together with a primitive normal-direction basis shows that the normalized simplex volume is
\[
 N_w=\frac{\lvert\det M_w\rvert}{w+1}=w^3-w^2+w-1.
\]

**2. Exact interior lattice points.** Write any \(x\in P_w\) uniquely as \(x=M_wc\), where \(c_i\ge0\) and \(\sum c_i=1\). Thus \(x_i=c_i+w c_{i+1}\), cyclically. Suppose \(x_j=0\) for some \(j\). Nonnegativity gives \(c_j=c_{j+1}=0\), so \(x_{j-1}=c_{j-1}\) is an integer between zero and one. Consequently \(c_{j-1}\in\{0,1\}\); because the other nonzero coefficient can only be \(c_{j+2}\), the point is a vertex. Therefore every other lattice point of \(P_w\) has four strictly positive coordinates.

When \(w\ge3\), the positive integer vectors summing to \(w+1\) form the lattice points of the smaller simplex whose vertices are the four cyclic permutations of \((w-2,1,1,1)\). One such extreme vector has unique barycentric coordinates
\[
 c=\frac{1}{N_w}\left(w^2-2w+2,\;w^3-3w^2+2w-1,\;2w-1,\;w^2-w-1\right).
\]
All components are strictly positive for \(w\ge3\); they sum to one. Cyclic invariance places all four extremes in the strict interior of \(P_w\), hence all positive integer compositions in its interior. There are exactly \(\binom w3\) such compositions. If \(w=2\), no strictly positive integer quadruple has sum three, so there are no nonvertex lattice points.

Consequently, in every case
\[
 |P_w\cap\mathbb Z^4|=4+a_w,\quad |\operatorname{int}(P_w)\cap\mathbb Z^4|=a_w,
 \quad a_w=\binom w3.
\]
For a three-dimensional lattice polytope, the Ehrhart numerator has \(h_0^*=1\), \(h_1^*=|P_w\cap\mathbb Z^4|-4\), \(h_3^*=|\operatorname{int}P_w\cap\mathbb Z^4|\), and \(\sum_i h_i^*=N_w\). Thus \(h_2^*=N_w-1-2a_w=(2w^3+w-6)/3\), proving the displayed exact numerator formula.

**3. Sharp unimodality and log-concavity.** Write \(a=a_w\) and \(b=(2w^3+w-6)/3\). Direct calculation gives
\[
 b-a=\frac{w^3+w^2-4}{2}>0\quad(w\ge2).
\]
The sequence \((1,a,b,a)\) is unimodal exactly when \(a\ge1\), i.e. \(w\ge3\). Since \(b\ge a\), its only potentially failing log-concavity inequality is \(a^2\ge b\). It fails for \(w=2,3,4\), where \(a^2-b=-4,-16,-26\). For \(w=5+u\), \(u\ge0\), its positive certificate is
\[
 36(a^2-b)=u^6+24u^5+238u^4+1224u^3+3289u^2+3828u+612>0.
\]
Hence the log-concavity threshold is exactly five.

**4. Sharp real-rootedness.** When \(w=2\), the numerator is \(1+4t^2\), with nonreal roots. For \(w=3,4,5,6\), the discriminants of the cubic \(at^3+bt^2+at+1\) are respectively
\[
 -19088,\quad-257488,\quad-1491548,\quad-3263536,
\]
all strictly negative. Thus none has three real roots. For \(w\ge7\), put \(g(x)=h^*_{P_w}(-x)=1-ax+bx^2-ax^3\). Then \(g(0)=1>0\), \(g(1)=b-2a+1=(w-1)(w+1)(w+3)/3>0\), and \(\lim_{x\to\infty}g(x)=-\infty\). Moreover \(a>2\), so \(0<2/a<1\), and
\[
 g(2/a)=-1+\frac{4b-8}{a^2}<0.
\]
For the last inequality, write \(w=7+u\) with \(u\ge0\), and note
\[
 36(a^2-4b+8)=u^6+36u^5+538u^4+4176u^3+16993u^2+30780u+11412>0.
\]
The intermediate-value theorem gives a root in each of the disjoint intervals \((0,2/a)\), \((2/a,1)\), \((1,\infty)\). Degree three makes them the three distinct positive zeros of \(g\), so all zeros of \(h^*_{P_w}\) are distinct and negative. This establishes the exact threshold seven.

## Verification
The accompanying `checker.py` uses only Python standard-library exact integers and fractions. It independently constructs \(M_w^{-1}\), checks all eight determinant identities for \(2\le w\le9\), exhaustively counts the lattice points in dilations \(m=1,2,3\) for each of those eight weights (24 complete finite enumerations), compares every count against the stated Ehrhart numerator, checks the interior count, and tests the coefficient/root threshold data. Run `python3 checker.py`. The infinite-parameter conclusions are proved above analytically and do not rest on finite enumeration.

## Relationship to prior work
Biermann, Lin and O'Keefe (arXiv:2611.17047, November 12, 2026) define this weighted oriented edge-polytope model and prove that naturally oriented uniformly weighted cycles with \(w>1\) lack the integer decomposition property. Their Proposition 3.10 identifies the nonvertex lattice points of such cycles and implies the lattice-point-count step above, but their stated results do not give the exact Ehrhart numerator or sharp unimodality, log-concavity and real-rootedness regimes. Those coefficient/root transitions are the contribution here.

The oriented-cycle root-polytope formula of Kálmán and Tóthmérész, as subsequently refined in *Exact Ehrhart polynomials of oriented cycle root polytopes* (2026), concerns the difference vectors \(e_{\mathrm{head}}-e_{\mathrm{tail}}\) in the sum-zero lattice, rather than the positive weighted exponent vectors of the present simplex. *Weighted four-cycle symmetric edge polytopes: exact Minkowski-decomposition strata* (2026) instead treats the centrally symmetric convex hull of signed weighted edge differences and its Minkowski summands. Neither covers the stated threshold classification. General cubic polynomial root criteria alone do not provide the parameter-dependent Ehrhart numerator needed here.

## Limitations
The result is specific to an all-forward four-cycle with uniform integer vertex weight \(w\ge2\). A three-dimensional Ehrhart numerator may be real-rooted despite the polytope failing IDP; no implication for arbitrary non-IDP polytopes, all four-cycle weightings, other cycle lengths, or Hilbert-basis normality is asserted. The literature comparison is targeted rather than exhaustive, and independent mathematical validation has not been performed.

## References
1. Jennifer Biermann, Kuei-Nuan Lin and Augustine O'Keefe, *Integer Decomposition Property of Edge Polytopes of Weighted Oriented Graphs*, arXiv:2611.17047v1, first posted 2026-11-12, especially Definition 2.8, Proposition 3.10, and Theorem 4.5.
2. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960, first posted 2021-05-03.
3. *Exact Ehrhart polynomials of oriented cycle root polytopes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ehrhart-polynomials-of-oriented-cycle-root-polytopes--e32575b66377 .
4. *Weighted four-cycle symmetric edge polytopes: exact Minkowski-decomposition strata* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-weighted-four-cycle-symmetric-edge-polytopes-exact-minkowski-dec--defbb48b70e7 .
