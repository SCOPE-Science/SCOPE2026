# Icosahedral facet Walsh zero locus and sharp range-projection constant

## Finding

Let \(I\) be the graph of the regular icosahedron, with vertex set \(V\) of size \(12\) and its \(20\) triangular facets \(\mathcal F\). Identify subsets of \(V\) with \(G=\mathbb F_2^{V}\). Let \(\mu:G\to\mathbb Z\) be the indicator of the set of facet-incidence vectors and define the unnormalized XOR-convolution operator
\[
(Tf)(x)=\sum_{y\in G}\mu(y)f(x+y).
\]
For a character indexed by \(S\subseteq V\), put \(\chi_S(x)=(-1)^{|S\cap\operatorname{supp}(x)|}\). Write \(e(S)\) for the number of graph edges with both ends in \(S\), and \(t(S)\) for the number of triangular facets wholly inside \(S\). Then the exact eigenvalue formula is
\[
\boxed{\lambda(S)=20-10|S|+8\bigl(e(S)-t(S)\bigr).}
\]
Its zero locus is precisely the following set of \(796\) characters: the \(36\) nonedge pairs, their \(36\) ten-vertex complements, and the \(724\) six-vertex subsets satisfying \(e(S)-t(S)=5\). There are no other zeros. Thus
\[
\operatorname{rank}(T)=3300,\qquad\operatorname{nullity}(T)=796,
\qquad\min_{\lambda(S)\ne0}|\lambda(S)|=2,\quad\max_S|\lambda(S)|=20.
\]
The sharp Hilbert-space condition number on the image is \(10\), and the Hilbert-space pseudoinverse norm is \(1/2\).

Let \(W=\operatorname{im}T\), a translation-invariant subspace of real or complex functions on \(G\). Among **all** linear projections \(R\) onto \(W\), not merely translation-invariant projections, the exact minimum endpoint norms are
\[
\boxed{\min_{R^2=R,\ \operatorname{im}R=W}\|R\|_{\ell^1\to\ell^1}
=\min_{R^2=R,\ \operatorname{im}R=W}\|R\|_{\ell^\infty\to\ell^\infty}
=\frac{7029}{512}.}
\]

The full **signed** Walsh eigenvalue histogram (value : multiplicity) is

| Value | Multiplicity | Value | Multiplicity |
|---:|---:|---:|---:|
| \(-20\) | 1 | \(20\) | 1 |
| \(-12\) | 30 | \(12\) | 30 |
| \(-10\) | 44 | \(10\) | 44 |
| \(-8\) | 130 | \(8\) | 130 |
| \(-6\) | 380 | \(6\) | 380 |
| \(-4\) | 465 | \(4\) | 465 |
| \(-2\) | 600 | \(2\) | 600 |
| \(0\) | 796 | | |

## Assumptions and scope

Only the ordinary twelve-vertex regular icosahedral graph is meant; its twenty facets are distinct binary incidence vectors, each counted once. A completely combinatorial realization uses vertices
\[
V=\{p,q\}\cup\{u_i:i\in\mathbb Z/5\mathbb Z\}
\cup\{v_i:i\in\mathbb Z/5\mathbb Z\}.
\]
The twenty facets are, for each \(i\in\mathbb Z/5\mathbb Z\),
\[
\{p,u_i,u_{i+1}\},\quad
\{q,v_i,v_{i+1}\},\quad
\{u_i,u_{i+1},v_i\},\quad
\{u_i,v_i,v_{i-1}\}.
\]
Consequently the graph has thirty edges, each vertex belongs to five facets, and each edge to two facets. Arithmetic and Fourier transforms are over the real or complex numbers; binary vectors supply the additive group, not the scalar field. The finite dimension is exactly \(2^{12}=4096\).

## Proof

**Structural Fourier formula.** For each facet \(F=\{a,b,c\}\), write \(s_w=1_{\{w\in S\}}\). The identity
\[
(-1)^{|F\cap S|}=(1-2s_a)(1-2s_b)(1-2s_c)
=1-2(s_a+s_b+s_c)+4(s_as_b+s_as_c+s_bs_c)-8s_as_bs_c
\]
holds termwise. Summing over the twenty facets and using the five-facets-per-vertex and two-facets-per-edge incidences yields \(\lambda(S)=20-10|S|+8(e(S)-t(S))\). Every face has odd size, hence \(\lambda(V\setminus S)=-\lambda(S)\). Reducing the structural formula modulo eight gives \(\lambda(S)\equiv4-2|S|\pmod8\). Thus a zero can occur only when \(|S|\equiv2\pmod4\), namely at sizes \(2,6,10\). At size two the formula reduces to \(\lambda(S)=8e(S)\), so exactly the \(\binom{12}{2}-30=36\) nonedges vanish. Complementarity gives the ten-subset zeros. At size six the formula is \(8(e(S)-t(S)-5)\), proving the exact criterion without approximation.

**Finite six-subset census.** Among the \(\binom{12}{6}=924\) six-subsets, exactly \(724\) satisfy \(e(S)-t(S)=5\); the table classifies all \(724\) by \((e(S),t(S))\). This is an exhaustive finite count using the explicit five-cyclic facet construction above, not an asymptotic inference.

| \(e(S)\) | \(t(S)\) | Number of six-subsets |
|---:|---:|---:|
| 5 | 0 | 72 |
| 6 | 1 | 260 |
| 7 | 2 | 180 |
| 8 | 3 | 120 |
| 9 | 4 | 80 |
| 10 | 5 | 12 |
| **Total** | | **724** |

For reproducibility, the included `verify.py` enumerates the \(924\) six-subsets and all \(4096\) subsets with exact integers, checking the displayed table, the per-weight signed histogram, and the signed face sums. A second construction finds graph triangles from its edge set rather than from the explicit face list. These independent constructions agree, and the direct face sums agree with the structural formula and with a complete Walsh–Hadamard transform.

**Full spectrum and Hilbert estimates.** The same exhaustive finite census gives the stated fifteen signed multiplier levels. Since Walsh characters form an orthogonal basis, rank counts nonzero multipliers. The smallest surviving multiplier modulus is exactly two, attained at multiplicities \(600\) for each sign, and the maximum is twenty, attained by the trivial and the parity characters. This proves the Hilbert estimates.

**Sharp endpoint projection.** Let \(Q\) be the orthogonal Walsh projection onto \(W\): its character multiplier is \(1_{\{\lambda(S)\ne0\}}\). Write \(Qf=p*f\); then
\[
4096p(x)=\sum_{S:\lambda(S)\ne0}\chi_S(x).
\]
The exact integer histogram of \(4096p(x)\), computed from the finite formula and independently checked by two Walsh transforms, is

| Integer value | Number of \(x\) | Integer value | Number of \(x\) |
|---:|---:|---:|---:|
| \(-796\) | 1 | \(3300\) | 1 |
| \(-60\) | 60 | \(84\) | 60 |
| \(-44\) | 240 | \(52\) | 32 |
| \(-28\) | 294 | \(36\) | 280 |
| \(-12\) | 240 | \(20\) | 420 |
| \(0\) | 2048 | \(4\) | 420 |

It follows directly that
\[
\|Q\|_{\ell^1\to\ell^1}=\|Q\|_{\ell^\infty\to\ell^\infty}
=\sum_{x\in G}|p(x)|=\frac{56232}{4096}=\frac{7029}{512}.
\]
For any other projection \(R\) onto \(W\), average its conjugates under all translations of \(G\). The average is a translation-invariant projection onto \(W\), and the endpoint operator norms cannot increase because translations are isometries. A translation-invariant projection must act by scalar multipliers on each character; the projection/range condition forces multiplier one on the characters in \(W\) and zero on the others. Hence the average equals \(Q\), and \(\|Q\|\le\|R\|\) in both endpoint norms. The above value is therefore minimal over arbitrary real or complex projections.

## Verification

Run `python3 verify.py` with Python 3.8 or later, in the directory containing the script. It uses only the standard library. It independently constructs the triangular facets in two ways, verifies the thirty-edge/five-at-each-vertex/two-at-each-edge incidences, reconstructs all \(4096\) signed coefficients by three exact methods, checks the \(724\)-subset six-vertex criterion, verifies the entire signed spectrum, reconstructs the projection multiplier from its inverse Walsh kernel, and checks the numerator \(56232\) without floating-point arithmetic. A finite enumeration is a valid proof of these fixed twelve-vertex statements; it is not claimed to establish any all-order extension.

## Relationship to prior work

The twenty-face geometry, the twelve vertices, and the fivefold symmetry of the regular icosahedron are classical. Nash's 2013 exposition, especially its complete section on the icosahedron, supplies a precise fivefold geometric model but does not study binary-incidence Walsh convolution, the stated zero locus, or the endpoint projection constant. Aksoy and Lewicki (2010, Theorem 2.1 and Corollary 2.2) explain the classical Rudin averaging method for minimal projections; the optimality principle is credited, not claimed new. Zippin's 2004 finite-abelian-group projection paper discusses the related general principle in its accessible abstract; its full text was not inspected.

The published *Icosahedral six-set edge criterion and zero-forcing exchange geometry* identifies \(200\) minimum zero-forcing six-subsets of the same graph by an induced-edge condition, but has a different graph-propagation question and does not calculate the face-incidence Walsh eigenvalues, the \(724\) six-set zeros, or the endpoint projection kernel. Earlier exact tables of the same incidence Fourier transform, if unindexed, would limit historical originality; none was located in the checked sources. The new content assessed here is the exact signed spectral classification, geometric zero criterion, and sharp numerical endpoint constant—not the classical incidence geometry or averaging theorem.

## Limitations

This theorem is only for the ordinary fixed icosahedron with twenty triangular facets; no analogous assertion is proved for arbitrary triangulated spheres, other Platonic solids or higher-dimensional polytopes. The finite integer calculations are fully reproducible but do not replace an independent mathematical audit. Web and mathematical-index searches cannot establish absolute historical priority, and the full text of Zippin (2004) was not accessible for comparison.

## References

1. O. Nash, *On Klein's Icosahedral Solution of the Quintic*, arXiv:1308.0955, first posted 2013-08-05. https://arxiv.org/abs/1308.0955 (especially section 2).
2. A. G. Aksoy and G. Lewicki, *Minimal projections with respect to various norms*, arXiv:1007.2214, first posted 2010-07-13. https://arxiv.org/abs/1007.2214 (especially Theorem 2.1 and Corollary 2.2).
3. M. Zippin, *A variant of Rudin's inequality for translation invariant projections on group algebras and its generalization to finite dimensional Banach spaces*, Archiv der Mathematik 82 (2004), 61–67, DOI:10.1007/s00013-003-0582-x. https://doi.org/10.1007/s00013-003-0582-x (abstract inspected).
4. *Icosahedral six-set edge criterion and zero-forcing exchange geometry*, published mathematical record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-icosahedral-six-set-edge-criterion-and-zero-forcing-exchange-geo--3e6559fd96e0 (RESULT.md inspected).
