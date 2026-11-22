# Sharp cubic spherical-gradient sampling spectra at hypercube vertices

## Finding

For every integer \(d\ge3\), let \(X_d=\{d^{-1/2}\varepsilon:\varepsilon\in\{-1,1\}^d\}\subset S^{d-1}\). Let \(\mathcal H_3(\mathbb R^d)\) be the complex space of homogeneous harmonic cubics, viewed as scalar functions on the sphere. Define the **gradient-only** observation map
\[
E_d:\mathcal H_3\longrightarrow\bigoplus_{x\in X_d}T_xS^{d-1}\otimes\mathbb C,
\qquad E_df=(\nabla_S f(x))_{x\in X_d}.
\]
Use normalized sphere measure \(d\sigma\) and the source Dirichlet norm \(\|f\|_D^2=\int_{S^{d-1}}|\nabla_Sf|^2\,d\sigma=3(d+1)\int_{S^{d-1}}|f|^2\,d\sigma\); equip the target with the equally weighted norm \(\|u\|_X^2=2^{-d}\sum_{x\in X_d}|u_x|^2\). Then \(T_d=E_d^*E_d\), on the source Dirichlet space, has the **complete spectrum**
\[
\begin{array}{c|c|c}
\text{sector}&\text{squared singular value}&\text{multiplicity}\\\hline
Z&\displaystyle\lambda_Z=\frac{2(d+4)}{d^2(d+1)}&d\\[3pt]
T&\displaystyle\lambda_T=\frac{2(d+2)(d+4)}{3d(d+1)}&d(d-2)\\[3pt]
S&\displaystyle\lambda_S=\frac{(d-3)(d+2)(d+4)}{d^2(d+1)}&\displaystyle\binom d3.
\end{array}
\]
Coincident eigenvalues are combined. Consequently \(\operatorname{rank}E_3=6\), with one-dimensional kernel \(\operatorname{span}\{x_1x_2x_3\}\); for **every \(d\ge4\)** the gradient data determine every harmonic cubic uniquely. For \(d\ge4\), \(\lambda_Z\) is the smallest eigenvalue; the largest is \(\lambda_T\) at \(4\le d<9\), both \(\lambda_T=\lambda_S\) at \(d=9\), and \(\lambda_S\) at \(d>9\). Thus the **sharp squared-singular-value condition number** is
\[
\kappa_d=\frac{\lambda_{\max}}{\lambda_{\min}}=
\begin{cases}
\displaystyle\frac{d(d+2)}3,&4\le d\le9,\\[3pt]
\displaystyle\frac{(d-3)(d+2)}2,&d\ge9,
\end{cases}
\qquad\kappa_d\sim\frac{d^2}2.
\]
At \(d=9\) the two expressions agree. Equivalently the sharp frame inequalities for all \(d\ge4\) are \(\lambda_Z\|f\|_D^2\le\|E_df\|_X^2\le\lambda_{\max}\|f\|_D^2\). The ordinary singular-value condition number is \(\sqrt{\kappa_d}\).

## Assumptions and scope

The dimension is an integer \(d\ge3\); the harmonic degree is **exactly three**, not a cumulative band. Every one of the \(2^d\) signed-cube corners is observed, with all \(d-1\) tangent-vector components measured and equal probability weighting. Complex-valued harmonics are allowed, with real harmonics as the real subspace. There is no scalar-value observation mixed into the map. The dimension is \(\dim\mathcal H_3=d(d-1)(d+4)/6\). No claims of uniform stability under perturbations of the sample nodes or of a high-degree theorem are made.

## Proof

**1. Three harmonic sectors.** For a homogeneous polynomial \(p\) let \(r^2=\sum_{j=1}^d x_j^2\). Define
\[
Z_i=x_i^3-\frac3{d+2}x_ir^2,\qquad
Q_{i;jk}=x_i(x_j^2-x_k^2)\quad(i,j,k\text{ distinct}),\qquad
R_{ijk}=x_ix_jx_k\quad(i<j<k).
\]
Their Euclidean Laplacians vanish: \(\Delta(x_i^3)=6x_i\), \(\Delta(x_ir^2)=2(d+2)x_i\), \(\Delta[x_i(x_j^2-x_k^2)]=0\), and \(\Delta(x_ix_jx_k)=0\). For each fixed \(i\), the \(Q_{i;jk}\) span a space of dimension \(d-2\) (differences of the \(d-1\) off-axis squared variables). Together they give \(d\), \(d(d-2)\), and \(\binom d3\) linearly independent vectors, respectively, summing to \(\dim\mathcal H_3\). The decomposition is therefore exhaustive.

Under coordinate sign flips, \(Z_i\) and each \(Q_{i;jk}\) have the singleton sign character \(\varepsilon_i\), whereas \(R_{ijk}\) has the triple sign character \(\varepsilon_i\varepsilon_j\varepsilon_k\). Under permutations of the other coordinates, the singleton-character sector splits into a one-dimensional invariant line \(\mathbb CZ_i\) and the \((d-2)\)-dimensional standard representation spanned by the \(Q_{i;jk}\). Thus these three summands are pairwise orthogonal irreducible subrepresentations of the signed-permutation group. Both the sphere and the cube norms of sampled tangent gradients are invariant under this group, so their ratio is constant on each summand and their cross terms vanish. This also follows directly from sign parity and permutation invariance, without requiring representation theory.

**2. Exact scalar ratios.** For a homogeneous harmonic cubic \(p\) and \(x\in S^{d-1}\), the tangential gradient is \(\nabla_Sp=\nabla p-3px\), hence \(|\nabla_Sp|^2=|\nabla p|^2-9|p|^2\). The normalized spherical moment formula is
\[
\int_{S^{d-1}}x_1^{2a_1}\cdots x_d^{2a_d}\,d\sigma
=\frac{\prod_j(2a_j-1)!!}{d(d+2)\cdots(d+2m-2)},\qquad m=\sum_ja_j,
\]
with odd-exponent moments zero and \((-1)!!=1\). At a cube vertex, substitute \(x_j=\varepsilon_j/\sqrt d\) and average over all signs. These rules give the following quantities for the three representative harmonics \(Z_1\), \(Q_{1;23}\), and \(R_{123}\):
\[
\begin{array}{c|c|c}
&\displaystyle\int_{S^{d-1}}|p|^2\,d\sigma&\displaystyle 2^{-d}\sum_{x\in X_d}|\nabla_Sp(x)|^2\\\hline
Z_1&\displaystyle\frac{6(d-1)}{d(d+2)^2(d+4)}&\displaystyle\frac{36(d-1)}{d^3(d+2)^2}\\[3pt]
Q_{1;23}&\displaystyle\frac4{d(d+2)(d+4)}&\displaystyle\frac8{d^2}\\[3pt]
R_{123}&\displaystyle\frac1{d(d+2)(d+4)}&\displaystyle\frac{3(d-3)}{d^3}.
\end{array}
\]
Dividing each third-column entry by \(3(d+1)\) times the corresponding second-column entry gives exactly \(\lambda_Z,\lambda_T,\lambda_S\) above. Since the decomposition is exhaustive, these are **all** eigenvalues with their stated multiplicities. In particular, this is an all-dimensional identity, not an inference from tested dimensions.

**3. Sharp rank and ordering.** The first two eigenvalues are strictly positive for \(d\ge3\), while \(\lambda_S=0\) exactly for \(d=3\). Its one-dimensional sector is \(\mathbb C R_{123}\), so this is the entire kernel in that dimension. For \(d\ge4\), the ratios are
\[
\frac{\lambda_T}{\lambda_Z}=\frac{d(d+2)}3,
\qquad
\frac{\lambda_S}{\lambda_Z}=\frac{(d-3)(d+2)}2,
\qquad
\frac{\lambda_T}{\lambda_S}=\frac{2d}{3(d-3)}.
\]
The first two exceed one. The third is greater than, equal to, or less than one according as \(d<9\), \(d=9\), or \(d>9\). This yields the unique least sector, the maximizing-sector crossover, and the sharp frame and condition-number formulas.

## Verification

Run `python3 check_cubic_gradient.py` from the extracted package with Python 3 standard library. The checker constructs an exhaustive harmonic-cubic basis, computes **every** pair of sphere-inner-product and sampled-tangent-gradient Gram entries in rational arithmetic, checks cross-sector vanishing and exact sector eigenvalue identities, and verifies dimensions, trace and the sharp condition-number formulas for dimensions \(3,4,5,6,7\). All tests passed. The proof above supplies the quantifiers for arbitrary \(d\); finite checks corroborate the algebra only.

## Relationship to prior work

Allasia, Cavoretto and De Rossi (first posted 2 May 2017) study general Hermite–Birkhoff interpolation of scattered function/derivative data on the sphere using geodesic radial bases. Their interpolant is not the restricted pure cubic-harmonic gradient map, and no all-dimensional signed-cube spectrum is reported. Bigi, Fraux, Browning and Ceriotti (first posted 16 February 2023) supply efficient spherical-harmonic Cartesian derivative evaluation, rather than exact conditioning of fixed sampling nodes. Xiao and Zhuang (first posted 9 March 2023) construct framelets from spherical designs and evaluate gradients of a design *optimization objective*; these are not tangential gradient samples of each harmonic cubic at cube vertices.

Moore and Russell (2014) give a Gegenbauer–Krawtchouk identity for **point-value** sampling energy of rotated spherical harmonics on Boolean cubes, while the earlier all-degree hypercube point-value rank classification listed in References also concerns only \(f(x)\). Neither yields the present gradient-only three-branch singular spectrum, its isolated three-dimensional gradient kernel, or the crossover at dimension nine as a stated consequence. General representation and moment methods are classical, and an equivalent unpublished or unindexed specialization cannot be excluded.

## Limitations

The claim covers degree-three tangent-gradient observations at the exact unperturbed Boolean cube nodes only. The one-dimensional \(d=3\) failure prevents uniform recovery in that dimension; for \(d\ge4\), the squared condition number grows quadratically. No all-degree extension, approximate noisy sampling error theorem, or independent mathematical audit is asserted. The scientific-priority assessment is based on specific literature and searchable records rather than an exhaustive proof of novelty. One related general cubed-sphere interpolation article was accessible only in summary form; its full-text comparison remains a residual priority risk, although its node geometry and point-value data differ materially.

## References

1. G. Allasia, R. Cavoretto and A. De Rossi, *Hermite–Birkhoff interpolation on scattered data on the sphere and other manifolds*, arXiv:1705.01032v1 (2 May 2017), https://arxiv.org/abs/1705.01032.
2. F. Bigi, G. Fraux, N. J. Browning and M. Ceriotti, *Fast evaluation of spherical harmonics with sphericart*, arXiv:2302.08381v1 (16 February 2023), https://arxiv.org/abs/2302.08381.
3. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1 (9 March 2023), https://arxiv.org/abs/2303.05365.
4. C. Moore and A. Russell, *Heat and Noise on Cubes and Spheres: The Sensitivity of Randomly Rotated Polynomial Threshold Functions*, arXiv:1408.5425v1 (2014), https://arxiv.org/html/1408.5425v1 (especially Section 5 and Appendix A).
5. *Two exceptional Walsh obstructions in exact-degree harmonic interpolation on the hypercube*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-exceptional-walsh-obstructions-in-exact-degree-harmonic-inte--6c86ac9d380a (scalar values, not gradients).
6. A. Bellet, M.-É. Brachet and J.-P. Croisille, *Interpolation on the Cubed Sphere with Spherical Harmonics*, published 2022, DOI:10.1007/s00211-022-01340-w (full text not inspected).
