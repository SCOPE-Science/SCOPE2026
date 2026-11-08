# Exact quadratic Walsh sampling spectra on arbitrary weighted pairs of Hamming layers

## Finding

Fix any integer \(n\ge5\), distinct Hamming weights \(2\le k<\ell\le n-2\), and any real sampling weight \(0<\vartheta<1\). Sample all degree-at-most-two Walsh characters on the two layers, with probability \(\vartheta\) on the first and \(1-\vartheta\) on the second. The restriction Gram matrix has **exactly one null direction**, the radial quadratic vanishing on both layers, and its entire nonzero spectrum is determined by **two explicit quadratic equations and one positive scalar**. All multiplicities and optimal nonzero squared singular-value bounds follow exactly. The formulas remain valid for every asymmetric pair of layers and unequal positive weights.

Put \(s=n-2k\), \(t=n-2\ell\), \(C=\binom n2\), and define
\[
Q(u)=\frac{u^2-n}{2},\qquad
 a(u)=1+\frac{u^2}{n}+\frac{Q(u)^2}{C},\qquad
 b(u,v)=1+\frac{uv}{n}+\frac{Q(u)Q(v)}{C},
\]
\[
c_1(u)=\frac{n^2-u^2}{n(n-1)},\qquad
c_2(u)=\frac{(n^2-u^2)((n-2)^2-u^2)}{n(n-1)(n-2)(n-3)}.
\]
Define five scalars
\[
T_0=\vartheta a(s)+(1-\vartheta)a(t),\quad
D_0=\vartheta(1-\vartheta)[a(s)a(t)-b(s,t)^2],
\]
\[
T_1=\vartheta c_1(s)\left(1+\frac{s^2}{n-2}\right)
 +(1-\vartheta)c_1(t)\left(1+\frac{t^2}{n-2}\right),
\]
\[
D_1=\frac{\vartheta(1-\vartheta)c_1(s)c_1(t)(s-t)^2}{n-2},
\qquad H_2=\vartheta c_2(s)+(1-\vartheta)c_2(t).
\]
The complete eigenvalue multiset of the coefficient Gram operator is:

* \(0\), multiplicity \(1\);
* \((T_0+\sqrt{T_0^2-4D_0})/2\) and \((T_0-\sqrt{T_0^2-4D_0})/2\), each multiplicity \(1\);
* \((T_1+\sqrt{T_1^2-4D_1})/2\) and \((T_1-\sqrt{T_1^2-4D_1})/2\), each multiplicity \(n-1\);
* \(H_2\), multiplicity \(n(n-3)/2\).

All five listed positive levels are strictly positive. Coincident values are to be combined. On the orthogonal complement of the kernel, the **optimal** lower and upper squared singular-value bounds are exactly the minimum and maximum of these five positive levels; no estimate is substituted for the exact roots. The rank is \(n+\binom n2\).

## Assumptions and scope

The source space is \(V_{\le2}=\operatorname{span}_{\mathbb C}\{\chi_I:|I|\le2\}\) inside the uniform Boolean cube \(\{-1,1\}^n\), where \(\chi_I(x)=\prod_{i\in I}x_i\). These basis vectors are orthonormal under **uniform cube probability**. The observation measure \(\mu\) is the convex combination of **uniform probability** on the weight-\(k\) and weight-\(\ell\) layers (weight is the number of negative coordinates), rather than unnormalized counting measure. The restriction operator is \(R:V_{\le2}\to L^2(\mu)\); \(G=R^*R\). Thus these are squared singular values for the stated probability normalization. Complex coefficient vectors are allowed, since all Gram matrices are real symmetric. Both layers are interior enough to support genuinely quadratic harmonic functions, and both mixture weights are strictly positive.

## Proof

**1. Orthogonal cube decomposition.** Let \(L=\sum_{i=1}^n x_i\) and \(Q=\sum_{i<j}x_ix_j=(L^2-n)/2\). Under uniform cube probability, \(1\), \(L/\sqrt n\), and \(Q/\sqrt C\) are an orthonormal radial triple. For \(c=(c_1,\ldots,c_n)\) with \(\sum_i c_i=0\), set \(f_c=\sum_i c_ix_i\). Then \(Lf_c=\sum_{i<j}(c_i+c_j)x_ix_j\), because the constant term vanishes. Their cube norms satisfy
\[
\|f_c\|_2^2=\sum_i|c_i|^2,\quad
\|Lf_c\|_2^2=(n-2)\sum_i|c_i|^2,\quad
\langle f_c,Lf_c\rangle=0.
\]
Consequently the standard sector consists of two orthogonal isometric copies of the \((n-1)\)-dimensional zero-sum coordinate space, represented by \(f_c\) and \(Lf_c/\sqrt{n-2}\). The remaining homogeneous quadratic sector has coefficients \(b_{ij}=b_{ji}\) with \(\sum_{j\ne i}b_{ij}=0\) for all \(i\); its dimension is \(C-n=n(n-3)/2\). These sectors span \(3+2(n-1)+n(n-3)/2=1+n+C\) orthogonal dimensions, so the decomposition is exhaustive. Orthogonality under \(\mu\) between the three sectors follows from permutation invariance; equivalently it follows from the shell moments in Step 4.

**2. Radial block.** On a layer with \(L=u\), the normalized radial functions have constant values forming the vector
\[
v_0(u)=\left(1,\frac{u}{\sqrt n},\frac{Q(u)}{\sqrt C}\right).
\]
Its radial Gram block is \(v_0(u)v_0(u)^*\). Hence the two-layer radial Gram block is \(\vartheta v_0(s)v_0(s)^*+(1-\vartheta)v_0(t)v_0(t)^*\). This is positive semidefinite of rank exactly two: \(s\ne t\) makes the first two coordinates of the vectors linearly independent. Its nonzero eigenvalues are the eigenvalues of the \(2\times2\) matrix obtained from the two weighted vectors. Their sum and product are exactly \(T_0,D_0\). The unique radial kernel function is a nonzero scalar multiple of \((L-s)(L-t)\).

**3. Standard block.** Let \(\rho_2(u)=(u^2-n)/(n(n-1))\). On the fixed-\(L\) layer, exchangeability and \(\sum c_i=0\) give
\[
\mathbb E_u|f_c|^2=(1-\rho_2(u))\sum_i|c_i|^2=c_1(u)\sum_i|c_i|^2.
\]
As \(Lf_c=uf_c\) on that layer, the restriction Gram matrix on each normalized two-copy standard sector is \(c_1(u)v_1(u)v_1(u)^*\), with
\[v_1(u)=\left(1,\frac{u}{\sqrt{n-2}}\right).\]
The mixture has trace \(T_1\) and determinant \(D_1\) in every one of the \(n-1\) standard copies. Its determinant is strictly positive because \(s\ne t\), \(0<\vartheta<1\), and \(c_1(s),c_1(t)>0\).

**4. Quadratic harmonic scalar.** A degree-two harmonic coefficient array has vanishing vertex sums. On a fixed layer the pair moments for distinct indices are \(\rho_2(u)\) and
\[
\rho_4(u)=\frac{u^4-(6n-8)u^2+3n(n-2)}{n(n-1)(n-2)(n-3)}.
\]
For pair variables the covariance operator depends only on whether two pairs coincide, share one vertex, or are disjoint. On the zero-incidence-sum subspace, the intersecting-pair adjacency operator acts as \(-2I\), while the disjoint-pair adjacency acts as \(+I\). Thus the quadratic sector scalar is
\[
1-2\rho_2(u)+\rho_4(u)=c_2(u).
\]
The mixture scalar is \(H_2\), of multiplicity \(n(n-3)/2\). Since \(2\le k,\ell\le n-2\), both \(|s|\) and \(|t|\) are at most \(n-4\), so all factors defining \(c_2\) are strictly positive.

**5. Positivity, multiplicities, and sharpness.** The radial rank is two, the two standard roots are positive, and the quadratic harmonic scalar is positive. The **only** kernel is radial and one-dimensional. The positive eigenvalues listed in the theorem exhaust all orthogonal sectors and count \(2+2(n-1)+n(n-3)/2=n+C\) dimensions. Standard finite-dimensional spectral theory gives the exact optimal restriction bounds from their min/max. This proves the assertion for every integer and weight in the stated ranges, without extrapolation from finite computation.

## Verification

Run `python checker.py` with Python 3 and SymPy installed. The self-contained checker builds exact rational Gram matrices from hypergeometric shell moments, verifies the radial and standard actions on explicit bases and the harmonic quadratic sector, and tests mixed weights for multiple asymmetric and symmetric layer pairs. It also performs independent simplification checks on seven odd-dimensional central pairs. Its success message is `TWO_HAMMING_LAYERS_EXACT_CHECKS_PASS 201 matrix directions and seven central families`. The finite tests are corroboration; the preceding invariant-sector argument proves the infinite family.

## Relationship to prior work

Classical harmonic analysis on Boolean slices supplies the representation-theoretic setting; in particular, Filmus and Mossel describe harmonic multilinear decompositions on slices, and Rao studies Fourier coefficients of restrictions **within a single slice**. Marceca, Romero, and Speckbacher study spectral concentration for Euclidean and lattice Fourier cutoffs with geometric domain assumptions and effective bounds, not this exact Boolean two-layer Gram spectrum. A prior exact result for **equally weighted antipodal two-layer sampling** is a special case when \(t=-s\) and \(\vartheta=1/2\); that specialization is not claimed as a new contribution. The present result is the **entire asymmetric and unequally weighted two-layer class**: its noncommuting rank-one radial and standard contributions generally have different eigenvectors, so the arbitrary-layer spectrum cannot be obtained merely by adding the known antipodal eigenvalue lists. An exhaustive literature uniqueness claim is not made.

## Limitations

The theorem addresses the complete Walsh band of degree at most two, precisely two distinct interior layers, and strictly positive mixture weights. It gives the exact identifiable-quotient bounds but does not optimize the layer indices or weights, provide higher-degree formulas, or assert uniqueness among all possible observation sets. At boundary layers some harmonic positive factors can vanish, and they are deliberately excluded. A general harmonic-decomposition treatment under other terminology might cover these formulas; independent priority review remains appropriate. The checker is finite and does not constitute a computer-assisted infinite proof.

## References

1. F. Marceca, J. L. Romero and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, first publicly available 2023-01-27, arXiv:2301.11685; open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11014824/ .
2. Y. Filmus and E. Mossel, *Harmonicity and invariance on slices of the Boolean cube*, first publicly available 2015-07-09, arXiv:1507.02713.
3. S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, first publicly available 2021-11-05, arXiv:2111.03213.
4. Y. Filmus and F. Ihringer, *Boolean constant degree functions on the slice are juntas*, arXiv:1801.06338.
