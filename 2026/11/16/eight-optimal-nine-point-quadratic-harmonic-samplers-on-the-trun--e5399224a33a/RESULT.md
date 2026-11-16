# Eight optimal nine-point quadratic-harmonic samplers on the truncated tetrahedron

## Finding
Let \(v_0=(1,1,1)\), \(v_1=(1,-1,-1)\), \(v_2=(-1,1,-1)\), and \(v_3=(-1,-1,1)\). The twelve points
\[
 x_{ij}=\frac{2v_i+v_j}{\sqrt{11}},\qquad i,j\in\{0,1,2,3\},\quad i\ne j,
\]
are the vertices of a regular truncated tetrahedron on \(S^2\). Let \(\mathcal H_{\le2}\) be the nine-dimensional space of real spherical harmonics of degrees zero through two, with its \(L^2\) inner product for probability surface measure. For each nine-element sampling set \(S\) from these twelve vertices, define
\[
 \mathcal A_S f=\left(f(x)/\sqrt{12}\right)_{x\in S}.
\]
Among all \(\binom{12}{9}=220\) such sets, the sharp maximal lower squared sampling bound is
\[
 \boxed{\max_{|S|=9}\ \inf_{\|f\|_2=1}\|\mathcal A_Sf\|_2^2=\lambda_*},
\]
where \(\lambda_*=0.076064097377\ldots\) is the smallest root of
\[
161051z^3-356708z^2+194480z-12800=0.
\]
Exactly **eight** sampling sets attain this bound: their erased triples are the two directed triangles on each of the four unordered tetrahedral triples, i.e. \(\{x_{ij},x_{jk},x_{ki}\}\) for pairwise distinct \(i,j,k\). The remaining 212 sets have lower bound strictly less than \(7/100\), while \(\lambda_*>7/100\). Exactly 128 sets are invertible and 92 singular. Every invertible nine-set has the *same* squared sampling Gram determinant,
\[
\det(\mathcal A_S^*\mathcal A_S)=\frac{52428800000}{34522712143931}.
\]
Consequently all invertible samples are determinant-optimal among nine-sets, although only the eight indicated triples are maximally stable in the E-optimal sense.

## Assumptions and scope
A nine-point sampler is **E-optimal** if it maximizes the smallest eigenvalue of its squared sampling operator relative to the normalized surface-measure inner product on \(\mathcal H_{\le2}\). No rescaling is made after deleting three samples: each surviving datum has its original factor \(1/\sqrt{12}\). Points are labeled by the ordered pair \((i,j)\); relabeling all four tetrahedron indices by a permutation gives the full symmetry action used below. The theorem is restricted to this fixed regular truncated tetrahedron, to equal sample weights, and to harmonics of degree at most two.

For \(t\in[-1,1]\), the harmonic addition theorem gives the basis-independent twelve-point row Gram matrix
\[
K_{(ij),(kl)}=\frac{1+3t+5P_2(t)}{12},\qquad
 t=x_{ij}\cdot x_{kl},\quad P_2(t)=\frac{3t^2-1}{2}.
\]
For a nine-element set \(S\), the eigenvalues of \(K_{S,S}\) are precisely the eigenvalues of \(\mathcal A_S^*\mathcal A_S\). Every entry of \(K\) is rational.

## Proof
**Rank and determinant.** Set \(p_{ij}=\sqrt{11}x_{ij}=2v_i+v_j=(X,Y,Z)\). The twelve-by-nine integer matrix \(M\), with row
\[
(11,X,Y,Z,XY,YZ,ZX,X^2-Y^2,3Z^2-11),
\]
is an evaluation matrix for a basis of \(\mathcal H_{\le2}\), after invertible column scalings. It has rank nine, and its complete left kernel is represented by the following twelve-by-three integer matrix \(N\), whose rows are indexed in lexicographic ordered-pair order:
\[
N=\begin{pmatrix}
-1&-1&0\\ 1&0&-1\\0&1&1\\1&1&0\\-1&0&0\\0&-1&0\\-1&0&1\\1&0&0\\0&0&-1\\0&-1&-1\\0&1&0\\0&0&1
\end{pmatrix}.
\]
Direct substitution gives \(N^{\mathsf T}M=0\) and \(\operatorname{rank}N=3\). Therefore deleting a triple \(T\) leaves a nonsingular nine-by-nine evaluation matrix exactly when the three-by-three submatrix \(N_T\) is nonsingular. The exact minor evaluation yields 128 nonsingular and 92 singular choices; for every nonsingular choice \(|\det M_{T^c}|=276824064\). Changing from \(M\) to a normalized harmonic basis multiplies each determinant by the same fixed factor, so the squared sampling Gram determinants agree; direct evaluation of one case yields the stated rational value.

**Exhaustive symmetry reduction.** The group \(S_4\) permutes all labels by \((i,j)\mapsto(\pi(i),\pi(j))\); its action is orthogonal on the sphere, hence preserves \(K\), spectra, and determinants. The 220 deleted triples split into thirteen orbits. The following exact table lists all representatives, their orbit sizes, ranks after deletion, and a certificate relative to \(r=7/100\). A word such as `01` denotes the label \((0,1)\).

| Deleted triple | Orbit size | Rank | Exact certificate |
|:--|--:|--:|:--|
| 01,02,03 | 4 | 8 | singular |
| 01,02,10 | 24 | 8 | singular |
| 01,02,12 | 24 | 9 | negative determinant at \(r\) |
| 01,02,13 | 24 | 9 | negative determinant at \(r\) |
| 01,02,30 | 12 | 8 | singular |
| 01,02,31 | 24 | 9 | negative determinant at \(r\) |
| 01,10,20 | 24 | 8 | singular |
| 01,10,23 | 12 | 8 | singular |
| 01,12,20 | 8 | 9 | positive definite at \(r\) |
| 01,12,23 | 24 | 9 | negative determinant at \(r\) |
| 01,12,31 | 12 | 8 | singular |
| 01,12,32 | 24 | 9 | negative determinant at \(r\) |
| 01,21,31 | 4 | 8 | singular |

Here “negative determinant at \(r\)” means \(\det(K_{T^c,T^c}-rI_9)<0\), which forces some eigenvalue below \(r\). For the single eight-element orbit, all nine leading principal minors of \(K_{T^c,T^c}-rI_9\) are strictly positive; Sylvester's criterion therefore gives every eigenvalue greater than \(r\). All thirteen assertions are exact rational calculations (not numerical eigenvalue comparisons), and the table sums to 220. This separates the eight optima strictly from all others.

**Sharp value.** For the representative deleted triple \(T=\{(0,1),(1,2),(2,0)\}\), the characteristic polynomial of the nine-by-nine retained row Gram matrix is
\[
\frac{(5324z^3-12353z^2+7904z-1280)(161051z^3-356708z^2+194480z-12800)^2}{138090848575724}.
\]
Exact rational root isolation places the smallest root of the second cubic in \((0.076,0.077)\), below every root of the first cubic and every other root of the second. Hence the least eigenvalue is the asserted \(\lambda_*\), of multiplicity two. The eight orbit members are exactly the directed triangles, as each choice of three tetrahedral vertices has two cyclic orientations.

## Verification
Run `python3 verify_truncated_tetrahedron.py` in the directory containing the embedded standalone checker. The checker constructs the exact twelve-by-twelve rational harmonic kernel, the integer evaluation and Gale-dual matrices, all thirteen \(S_4\) orbits, and exact determinant and inertia-separation certificates. It checks the complete 220-case partition, the 128/92 rank split, uniform nonzero integer minors and sampling Gram determinants, positive leading principal minors for the eight optima, negative shifted determinants for all other nonsingular orbit representatives, the characteristic polynomial factorization, and exact rational isolation of the smallest root. Its calculations are finite and exhaustive because the symmetry group preserves the kernel. The algebraic orbit reduction, Sylvester criterion, determinant-sign argument, and harmonic addition theorem explain why those computations certify the claim.

## Relationship to prior work
Xiao and Zhuang (first public March 9, 2023) develop spherical-design sampling and spherical framelet operators, including degree-bounded harmonic transforms, but do not classify optimal three-erasure masks on the truncated tetrahedron. The published cuboctahedral quadratic-harmonic erasure-rank theorem gives a graphic-matroid rule and the same numerical 128/92 rank split on a **different** twelve-point geometry; it does not determine these truncated-tetrahedron singular values or their eight maximizers. General well-conditioned spherical-design and interpolation results supply sampling motivation but do not imply an exact fixed-grid E-optimal selection. The rank census and equality of all nonzero determinants are included as context, not used on their own as the novelty claim. The proposed novelty is the strict E-optimal separation and complete eight-set characterization.

## Limitations
The result is for equal-weight samples from this fixed twelve-vertex geometry and the degree-zero-through-two harmonic band. It provides a sharp deterministic lower norm bound, not noisy-data minimax optimality, optimality among arbitrary spherical nodes or weights, or higher-degree statements. Historical priority is subject to independent scholarly comparison, including unindexed exact sampling tables. No independent audit has been performed.

## References
1. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, first public March 9, 2023, arXiv:2303.05365v1, https://arxiv.org/html/2303.05365v1 (primary MSC2020 42C15).
2. C. An et al., *Well-conditioned spherical designs for integration and interpolation on the two-sphere*, https://ira.lib.polyu.edu.hk/bitstream/10397/6097/1/An_Spherical_Designs_Two-Sphere.pdf .
3. *The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron*, complete public mathematical account, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-the-tetrahedral-graphic-matroid-controls-quadratic-harmonic-samp--22932f55648e/RESULT.md .
