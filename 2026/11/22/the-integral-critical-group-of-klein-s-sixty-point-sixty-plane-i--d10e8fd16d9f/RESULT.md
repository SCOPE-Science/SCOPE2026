# The integral critical group of Klein's sixty-point/sixty-plane incidence graph

## Finding

For Klein's classical \(60_{15}\) point–plane configuration over \(\mathbb C\), the incidence graph \(\Gamma\) has 120 vertices, 900 edges, and the following *complete integral* critical group:

\[
\begin{aligned}
K(\Gamma)\cong{}&
(\mathbb Z/2)^7\oplus\mathbb Z/4\oplus(\mathbb Z/20)^3
\oplus(\mathbb Z/40)^{14}\
&\oplus(\mathbb Z/1120)^{16}\oplus(\mathbb Z/4480)^3\
&\oplus(\mathbb Z/13440)^7\oplus(\mathbb Z/40320)^3
\oplus\mathbb Z/201600.
\end{aligned}
\]

There are 55 nontrivial invariant factors (and 64 unit factors in the reduced Laplacian). In particular the exponent is \(201600\) and the number of spanning trees is

\[
\tau(\Gamma)=|K(\Gamma)|=2^{235}3^{15}5^{48}7^{30}.
\]

## Assumptions and scope

All projective geometry is in characteristic zero. Let \(e_0,e_1,e_2,e_3\) be the standard basis of \(\mathbb C^4\), and set \(\mu_4=\{1,-1,i,-i\}\). Use the following projective representatives for a set \(P\) of sixty points:

* Four coordinate points \([e_j]\), \(0\le j\le3\).
* Twenty-four two-coordinate points \([e_j+\zeta e_k]\), \(0\le j<k\le3\) and \(\zeta\in\mu_4\).
* Eight four-coordinate points \([1:\epsilon_1:\epsilon_2:\epsilon_3]\) with each \(\epsilon_j\in\{\pm1\}\).
* Twenty-four four-coordinate points \([x_0:x_1:x_2:x_3]\), where \(x_0=1\), one of \(x_1,x_2,x_3\) equals \(\pm1\), and each of the other two equals \(\pm i\).

These are the projective coordinates of the classical sixty-point Klein configuration (also the dual normals to the sixty reflection planes). Define the plane \(H_q\) by \(\sum_{j=0}^3 q_jX_j=0\) for each \(q\in P\); the pairing is algebraic bilinear, **not Hermitian**. The distinct point and plane vertex labels are kept separate even when they use the same coordinate vector. The incidence matrix is \(B_{p,q}=1\) when \(\sum p_jq_j=0\), and \(0\) otherwise. This gives the historical \(60_{15}\) incidence graph, also known as the 120-Klein Levi graph.

For a finite connected graph \(G\), its critical group means the torsion subgroup of \(\operatorname{coker}(L_G:\mathbb Z^{V(G)}\to\mathbb Z^{V(G)})\); equivalently it is the cokernel of a reduced integer Laplacian. No identification with a Picard lattice of a threefold or a Kummer surface is asserted.

## Proof

**Exact incidence.** Direct Gaussian-integer multiplication with the displayed coordinate classes gives 60 distinct point vectors, 60 distinct plane normals, 15 zeros in each row and column of \(B\), and hence 900 incidences. The matrix is symmetric. This identifies a canonical concrete integer presentation of the classical point–plane incidence, independent of the ordering of its points and planes. Its bipartite graph Laplacian is

\[
L_\Gamma=\begin{pmatrix}15I_{60}&-B\-B^\mathsf T&15I_{60}\end{pmatrix}.
\]

**Spectrum and determinant.** Exact matrix polynomial multiplication verifies

\[
\prod_{\lambda\in\{15,-3,-5,-1,5,1\}}(B-\lambda I)=0.
\]

The traces of powers \(B^r\), \(0\le r\le5\), agree with the multiplicity vector \((1,5,9,12,15,18)\) in that eigenvalue order. Since the distinct-root polynomial annihilates the real symmetric integer matrix, this determines the entire spectrum, rather than only numerical approximations. Consequently the Laplacian eigenvalues, with multiplicities, are

\[
0^{[1]},\ 30^{[1]},\ 12^{[5]},\ 18^{[5]},\ 10^{[24]},\ 20^{[24]},\ 14^{[30]},\ 16^{[30]}.
\]

In particular the zero eigenvalue is simple, so \(\Gamma\) is connected. The matrix–tree theorem yields the stated exact determinant of each reduced Laplacian.

**Prime-local integral Smith calculation.** Delete one point vertex, forming an integer matrix \(M\) of size 119. Since its determinant has only the prime factors \(2,3,5,7\), no other prime can occur in its nonunit Smith factors. Over \(\mathbb Z/p^K\mathbb Z\), a unit pivot can be split off by row/column equivalences; after all unit pivots are exhausted, division of the remaining block by \(p\) increases every remaining valuation by one. The accompanying independent program uses sufficiently high moduli \(2^{12},3^8,5^6,7^5\), finds the complete valuation multisets, and confirms the same result after instead deleting a plane vertex:

| Prime | Smith valuations, with multiplicities |
|---|---|
| \(2\) | \(0^{[64]},1^{[7]},2^{[4]},3^{[14]},5^{[16]},7^{[14]}\) |
| \(3\) | \(0^{[108]},1^{[7]},2^{[4]}\) |
| \(5\) | \(0^{[72]},1^{[46]},2^{[1]}\) |
| \(7\) | \(0^{[89]},1^{[30]}\) |

Every listed multiset has 119 entries, and their weighted valuation totals are respectively 235, 15, 48, 30, precisely the independent tree-determinant exponents. Sorting valuations and multiplying the prime powers position by position yields the invariant factors in the Finding. All subsequent factors are divisible by their predecessors, proving the displayed isomorphism type. Because the moduli exceed all observed valuations and the full determinant is known, the finite modular reductions recover the integral Smith invariants, not merely ranks modulo the primes.

## Verification

Execute `python3 verify_klein120.py` using a Python 3.9+ standard-library interpreter. The program reconstructs the sixty Gaussian-integer coordinates and all 3,600 point–plane pairs, checks row/column degrees, proves the characteristic-polynomial factorization through exact matrix polynomial and power-trace identities, computes the Kirchhoff determinant, and repeats the prime-local Smith computation with two separately deleted vertices. `verify_output.txt` records the actual output. The expected completion marker is `KLEIN_60_15_INTEGRAL_CRITICAL_GROUP_OK`. No numerical eigenvalue approximation or finite-field inference replaces an infinite statement; this theorem itself concerns one specified finite integer matrix.

## Relationship to prior work

The configuration and its 15-to-15 incidence are classical; Dolgachev's *Abstract Configurations in Algebraic Geometry* (arXiv:math/0304258, §10.9, first posted April 18, 2003) constructs it from the fifteen invariant tetrahedra. Pokora, Szemberg, and Szpond (arXiv:2010.08863, §2–3, first posted 2020) supply detailed projective coordinates and study unexpected surfaces and projection complete intersections. MathWorld identifies the Levi graph as the 120-Klein graph. These known results are not claimed as new. The contribution is its *complete integer Laplacian Smith form*. The inspected sources supply the geometry, not an integral critical-group decomposition; searches for its alternative names, tabulations, and stronger graph-group formulas did not identify a covering result. This negative evidence is not a proof of historical novelty.

## Limitations

The result is specific to the graph of incidences between sixty points and sixty planes, not to the 30-line incidence graph, the 24-vertex Klein graph, or the Picard group of any Kummer surface. It says nothing about specialization in positive characteristic or the arithmetic Galois representation on a geometric configuration. The graph can be realized as the dual graph of a stable nodal genus-781 curve made from 120 rational components with 900 nodes; under a regular semistable smoothing with unit edge thicknesses, the usual graph–component-group theorem identifies this critical group with the Néron component group. That interpretation concerns an abstract glued curve, not an asserted canonical geometric degeneration of the arrangement. A separately published computation hidden under other terminology or in an unindexed table remains a priority risk; no independent audit has occurred.

## References

1. I. Dolgachev, *Abstract Configurations in Algebraic Geometry*, arXiv:math/0304258, §10.9 (first public posting 2003-04-18), https://arxiv.org/abs/math/0304258 .
2. P. Pokora, T. Szemberg and J. Szpond, *Unexpected properties of the Klein configuration of 60 points in \(\mathbb P^3\)*, arXiv:2010.08863, §§2–3, https://arxiv.org/abs/2010.08863 .
3. E. W. Weisstein, *Klein Configuration* and *Klein Graphs*, MathWorld, https://mathworld.wolfram.com/KleinConfiguration.html and https://mathworld.wolfram.com/KleinGraphs.html .
4. F. Klein, *Zur Theorie der Liniencomplexe des ersten und zweiten Grades*, Math. Ann. 2 (1870), 198–226; R. W. H. T. Hudson, *Kummer's Quartic Surface* (1905), §25. Exact original day of publication for these historic sources was not verified, so the dated 2003 open posting is used for the required day-resolution source field.
