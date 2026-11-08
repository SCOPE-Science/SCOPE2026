# The non-\(\mathbb Q\)-Gorenstein locus of the weight-\(13\) motivic toric fourfold

## Finding

Let \(\mathcal Z^{\mathfrak m}\) be the free graded algebra of motivic multiple zeta values in the Lyndon-generator presentation used in [1]. Let \(X=\mathcal R^{0}_{13}(\mathcal Z^{\mathfrak m})\) be its *base* toric variety at weight \(13\). The weights of the generators occurring in this base are \(2,3,5,7,8\). Accordingly, its projective monomial embedding in \(\mathbb P^8_{\mathbb C}\) is defined by the nine exponent vectors

\[
 A=\{(a,b,c,d,e)\in\mathbb Z_{\ge0}^{5}:2a+3b+5c+7d+8e=13\}.
\]

Write \(P=\operatorname{conv}(A)\) in its intrinsic affine difference lattice and let \(\Sigma_P\) be its normal fan. The projective toric variety \(X\) is normal by [1, Table 1], so it is the normal toric variety of \(\Sigma_P\).

**Theorem.** The non-\(\mathbb Q\)-Gorenstein locus of \(X\) is exactly the single torus-invariant curve

\[
 C=V(\sigma_E)\cong\mathbb P^1,\qquad
 E=[(0,2,0,1,0),(3,0,0,1,0)]\subset P.
\]

Precisely, the canonical Weil divisor \(K_X\) is Cartier at every point of \(X\setminus C\) and not even \(\mathbb Q\)-Cartier at any point of \(C\). The polytope has eight vertices; its six fixed-point charts away from the endpoints of \(E\) are Gorenstein, whereas the two charts at those endpoints are not \(\mathbb Q\)-Gorenstein.

## Assumptions and scope

All varieties and toric lattices are over \(\mathbb C\). The symbol \(X\) refers only to the four-dimensional base \(\mathcal R^{0}_{13}\), not to the eleven-dimensional projective cone \(\mathcal R_{13}\). Normality of the base, and the identification with the monomial polytope, are established in [1, Lemma 2.6, Proposition 3.9 and Table 1]. We use the usual toric convention \(K_X=-\sum_{\rho\in\Sigma_P(1)}D_\rho\). For a cone \(\sigma\) with primitive generators \(n_\rho\), this divisor is \(\mathbb Q\)-Cartier on \(U_\sigma\) exactly when there is \(m\in M_{\mathbb Q}\) such that \(\langle m,n_\rho\rangle=1\) for all its rays; it is Cartier when \(m\) can be chosen integral [2, Section 4.2].

## Proof

**1. Intrinsic lattice and all points.** In lexicographic order the nine elements of \(A\) are

\[
\begin{aligned}
p_0&=(0,0,1,0,1), & p_1&=(0,1,2,0,0), & p_2&=(0,2,0,1,0),\\
p_3&=(1,1,0,0,1), & p_4&=(1,2,1,0,0), & p_5&=(2,3,0,0,0),\\
p_6&=(3,0,0,1,0), & p_7&=(4,0,1,0,0), & p_8&=(5,1,0,0,0).
\end{aligned}
\]

Relative to \(p_0\), an integral basis of the rank-four affine difference lattice consists of columns of

\[
 B=\begin{pmatrix}-3&-4&-5&-4\\2&1&1&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
\]

In this basis the nine points have coordinates

\[
 z_0=(0,0,0,0),\ z_1=(0,1,0,-1),\ z_2=(1,-1,1,-1),\ z_3=(1,-1,0,0),
\]
\[
 z_4=(1,0,0,-1),\ z_5=(2,-1,0,-1),\ z_6=(0,-1,1,-1),\ z_7=(0,0,0,-1),\ z_8=(1,-1,0,-1).
\]

The equalities \(p_i-p_0=Bz_i\) are exact. Furthermore, the four row vectors \(z_1,z_2,z_3,z_6\) have determinant of absolute value one, so the displayed basis is precisely the difference lattice, not a larger ambient lattice.

**2. Complete facets.** The primitive outer facet inequalities \(n_i\cdot z\le c_i\), with facet label \(i\), are:

| \(i\) | \(n_i\) | \(c_i\) | Indices of points on facet |
|---|---|---:|---|
| 0 | \((1,1,1,1)\) | 0 | 0,1,2,3,4,5 |
| 1 | \((0,1,2,1)\) | 0 | 0,1,2,6 |
| 2 | \((0,0,-1,0)\) | 0 | 0,1,3,4,5,7,8 |
| 3 | \((-1,0,0,0)\) | 0 | 0,1,6,7 |
| 4 | \((0,0,1,1)\) | 0 | 0,2,3,6 |
| 5 | \((-1,-1,-1,0)\) | 0 | 0,3,6,7,8 |
| 6 | \((0,0,0,-1)\) | 1 | 1,2,4,5,6,7,8 |
| 7 | \((0,-1,0,0)\) | 1 | 2,3,5,6,8 |

Each displayed inequality holds at all nine lattice points and is tight on a rank-three affine configuration. To certify completeness, enumerate all four-element subsets of the nine points, retain those affinely independent on a supporting hyperplane, primitive-normalize the corresponding integral normal, and deduplicate. Every facet of a four-dimensional polytope contains four affinely independent vertices; thus this finite enumeration is exhaustive. It returns exactly the eight table entries. The only nonvertex among the nine points is \(p_4\); hence there are eight torus-fixed points.

**3. The obstruction on a distinguished edge.** The four facets with labels \(1,4,6,7\) meet precisely in the edge \(E=[p_2,p_6]\). Their primitive normals satisfy the exact relation

\[
 n_1-2n_4-n_6+n_7=0,
 \qquad 1-2-1+1=-1\ne0.
\]

If \(K_X\) were \(\mathbb Q\)-Cartier on the affine toric chart corresponding to this edge, a rational \(m\) would pair to \(1\) with all four rays. Pairing the displayed relation with \(m\) would give \(0=-1\), impossible. Therefore \(K_X\) is not \(\mathbb Q\)-Cartier at the dense orbit of \(V(\sigma_E)\), nor at any point in its closure, including the two endpoint fixed points.

**4. No further obstruction.** For the other six vertices, the vectors solving \(\langle m,n_i\rangle=1\) on every facet active at that vertex are all integral. In the lattice dual to \(B\), they are

\[
\begin{array}{c|c}
\text{vertex}&m\\\hline
p_0&(-1,1,-1,2)\\
p_1&(-1,4,-1,-1)\\
p_3&(1,-1,-1,2)\\
p_5&(4,-1,-1,-1)\\
p_7&(-1,1,-1,-1)\\
p_8&(1,-1,-1,-1)
\end{array}
\]

The facet table gives the entire proper-face lattice: \(8\) vertices, \(19\) edges, \(19\) two-faces, and \(8\) facets. Checking intersections of subsets of the eight facets shows that every proper face except \(E\), \(p_2\), and \(p_6\) contains at least one of the six vertices in the preceding table. Its dual cone is a face of one of the six Gorenstein maximal cones. Thus \(K_X\) is Cartier at every torus orbit not associated with those three faces. By the orbit-cone correspondence, the remaining orbits form precisely \(V(\sigma_E)\). This proves the asserted equality of loci.

Finally, the orbit closure of a one-dimensional polytope edge in the complete normal-fan fourfold is a complete normal toric curve; hence \(C\cong\mathbb P^1\).

## Verification

The companion `verify.py` uses only the Python 3 standard library. It generates the nine exponent vectors from the weight equation, checks the displayed intrinsic lattice basis and a unimodular minor, reconstructs all primitive supporting hyperplanes by testing every four-point subset, and enumerates every proper face from all subsets of the eight facets. Rational row reduction independently tests local canonical Cartier equations on every cone. The output verifies the face vector \((8,19,19,8)\), the six integral support vectors, and the exact three non-\(\mathbb Q\)-Gorenstein faces \(\{p_2\},\{p_6\},E\). These finite checks cover every face of this fixed polytope; no extrapolation to other weights is made.

Run `python3 verify.py` from the extracted bundle.

## Relationship to prior work

Reference [1] constructs these motivic toric varieties, identifies the monomial polytope by general toric theory, and reports that the weight-\(13\) base is a normal, projectively normal, singular fourfold in \(\mathbb P^8\) of degree \(7\) (Table 1). It also illustrates the associated four-dimensional polytope (Figure 1(b)). Those are prior facts, not new claims. The present result adds the precise canonical Cartier/non-\(\mathbb Q\)-Cartier stratification; neither a ``singular'' label nor the general normality statements imply it. The standard local toric Cartier test in [2] is used, not claimed as new. A related general analysis of quotients of \(\mathbb Q\)-factorial toric varieties [3] does not classify this non-\(\mathbb Q\)-Gorenstein example.

## Limitations

The theorem is restricted to the complex weight-\(13\) base toric fourfold, not the projective cone and not general motivic or numerical multiple-zeta relation varieties. It classifies the canonical-divisor Cartier locus, not the full singular locus, local analytic singularity types, divisor class groups, or resolutions. It makes no claim about transcendence or linear independence of numerical multiple zeta values. Historical priority beyond the inspected sources is not independently certified.

## References

[1] A. Burmester, S. Charlton, A. Kidambi, F. Lotter, R. Preiß, *Toric Varieties from Multiple Zeta Values*, arXiv:2610.37351v1, 27 October 2026, especially Lemma 2.6, Theorem 3.7, Proposition 3.9, Figure 1(b), and Table 1. https://arxiv.org/abs/2610.37351

[2] D. Cox, J. Little, H. Schenck, *Toric Varieties*, American Mathematical Society, 2011, Sections 3.2 and 4.2 (orbit-cone correspondence and Cartier divisor criterion).

[3] M. Rossi, L. Terracini, *A Q-factorial complete toric variety is a quotient of a poly weighted space*, arXiv:1502.00879, 2015 (background comparison; no specific computation for the present example).
