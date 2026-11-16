# Simultaneous quadratic-harmonic spectra of all coordinate-rank observation masks

## Finding
Let \(d\ge4\), and let \(\mathcal H_2(S^{d-1})\) denote the complex vector space of restrictions of homogeneous harmonic quadratic polynomials on \(\mathbb R^d\). For \(1\le r\le d\), define \(C_{d,r}\) to be the spherical region where the first coordinate is positive and its absolute value has rank \(r\) in decreasing order among all \(d\) absolute coordinates. The cell boundaries, on which coordinates tie, have zero surface measure. For every subset \(J\subseteq\{1,\ldots,d\}\), put \(C_{d,J}=\bigcup_{r\in J}C_{d,r}\).

**Theorem.** All of the concentration operators \(T_{d,J}=P_{\mathcal H_2}\,\mathbf1_{C_{d,J}}\vert_{\mathcal H_2}\) commute, and their common orthogonal eigenspaces are the following four subspaces, independent of \(J\):

1. \(Z=\operatorname{span}_{\mathbb C}\{(d-1)x_1^2-\sum_{j=2}^d x_j^2\}\), dimension \(1\).
2. \(M=\operatorname{span}_{\mathbb C}\{x_1x_j:2\le j\le d\}\), dimension \(d-1\).
3. \(O=\operatorname{span}_{\mathbb C}\{x_ix_j:2\le i<j\le d\}\), dimension \(\binom{d-1}{2}\).
4. \(D=\{\sum_{j=2}^d a_jx_j^2:\sum_{j=2}^d a_j=0\}\), dimension \(d-2\).

Their eigenvalues are exact explicit one-dimensional integrals. Write \(n=d-1\), \(k=r-1\), \(\ell=d-r\). For \(t>0\), let \(f(t)=(2\pi t)^{-1/2}e^{-t/2}\) and \(F(t)=\operatorname{erf}(\sqrt{t/2})\), the density and distribution function of a \(\chi^2_1\) variable. Define the truncated conditional moments
\[
 a_j(t)=\frac{\int_t^\infty y^j f(y)\,dy}{1-F(t)},\qquad b_j(t)=\frac{\int_0^t y^j f(y)\,dy}{F(t)}\quad(j=1,2),
\]
\[
 m=ka_1+\ell b_1,\qquad v=k(a_2-a_1^2)+\ell(b_2-b_1^2),
\]
\[
 q=\frac{ka_2+\ell b_2}{n},\qquad p=\frac{k(k-1)a_1^2+2k\ell a_1b_1+\ell(\ell-1)b_1^2}{n(n-1)},
\]
\[
 \rho_{d,r}(t)=d\binom{d-1}{r-1}f(t)[1-F(t)]^{r-1}F(t)^{d-r}.
\]
Every expression above is evaluated at \(t\). The four exact eigenvalues for the rank-\(r\) cell are
\[
\begin{aligned}
 \lambda_{Z,r}&=\frac1{2d}\int_0^\infty\rho_{d,r}(t)\frac{[(d-1)t-m]^2+v}{2d(d-1)}\,dt,\\
 \lambda_{M,r}&=\frac1{2d}\int_0^\infty\rho_{d,r}(t)\frac{tm}{d-1}\,dt,\\
 \lambda_{O,r}&=\frac1{2d}\int_0^\infty\rho_{d,r}(t)p\,dt,\\
 \lambda_{D,r}&=\frac1{2d}\int_0^\infty\rho_{d,r}(t)\frac{q-p}{2}\,dt.
\end{aligned}
\]
For any \(J\), the eigenvalue on sector \(S\in\{Z,M,O,D\}\) is exactly \(\lambda_{S,J}=\sum_{r\in J}\lambda_{S,r}\), with the corresponding indicated multiplicity (combine any coinciding eigenvalues). Consequently the exact sharp concentration bounds for every nonzero \(h\in\mathcal H_2\) are
\[
 \min_S\lambda_{S,J}\le\frac{\int_{C_{d,J}}|h|^2\,d\sigma}{\int_{S^{d-1}}|h|^2\,d\sigma}\le\max_S\lambda_{S,J},
\]
and equality holds precisely in the direct sum of sectors attaining the applicable extreme.

Every \(C_{d,r}\) has normalized area \(1/(2d)\). With \(N=d(d+1)/2-1\), the exact trace and partition identities are
\[
\operatorname{tr}T_{d,J}=\frac{|J|N}{2d},\qquad \sum_{r=1}^{d}\lambda_{S,r}=\frac12\quad(S\in\{Z,M,O,D\}).
\]
For nonempty proper \(J\), all four eigenvalues lie strictly between \(0\) and \(1/2\); for \(J=\varnothing\) they vanish and for \(J=\{1,\ldots,d\}\) all equal \(1/2\).

## Assumptions and scope
All integrals use ordinary surface measure (the quotient cancels its normalization). Only homogeneous harmonic degree two is considered, not the entire degree-at-most-two band. The rank is among absolute coordinate values, not signed coordinate values. The result applies to complex coefficients because the concentration forms are Hermitian, and it includes possible accidental eigenvalue coincidences; it does not claim a universal ordering among the four sectors. No other mask geometry or harmonic degree is asserted.

## Proof
1. Every quadratic harmonic is \(h_A(x)=x^\mathsf{T}Ax\) for a symmetric complex trace-zero matrix \(A\). The four displayed subspaces are mutually orthogonal for full-sphere \(L^2\), span all \(N\) dimensions, and are invariant under permutations and sign changes of coordinates \(2,\ldots,d\). Because rank cells without the positive sign condition are also invariant under flipping coordinate one, every cross term between different displayed sectors has zero integral; within each sector sign symmetry and permutation symmetry give a scalar Hermitian quadratic form. This proves common diagonalization directly, including the two transverse types.
2. Let \(G\) be a standard real Gaussian in \(\mathbb R^d\) and \(Y_j=G_j^2\). The direction \(G/\lVert G\rVert\) is uniform on the sphere and independent of the Gaussian radius. Homogeneity cancels the fourth radial moment in the concentration quotient. Every degree-two harmonic is even under \(G\mapsto-G\), so requiring \(G_1>0\) halves the numerator on the rank event; it does **not** halve the denominator. The exact Gaussian identities \(\mathbb E[G_i^2G_j^2]=1\) for \(i\ne j\) and \(\mathbb E[((d-1)Y_1-\sum_{j>1}Y_j)^2]=2d(d-1)\) give the denominator normalizations in the four formulas.
3. Conditional on \(Y_1=t\) having decreasing rank \(r\), exactly \(k=r-1\) of the other squares independently exceed \(t\), exactly \(\ell=d-r\) fall below \(t\), and their assignments to labels are uniformly distributed. The conditional density of \(Y_1\) is \(\rho_{d,r}\), which integrates to one. The sum of the other squares has conditional mean \(m\) and variance \(v\); one other square has mean \(m/n\) and second moment \(q\); two distinct other squares have product mean \(p\). Substituting the four representative harmonics \((d-1)x_1^2-\sum_{j>1}x_j^2\), \(x_1x_2\), \(x_2x_3\), and \(x_2^2-x_3^2\) gives the formulas. In the last sector, \(\mathbb E[(Y_2-Y_3)^2\mid t]=2(q-p)\) and its unconditional value is four.
4. Rank cells partition the open hemisphere \(x_1>0\), so their indicators add. Since every quadratic harmonic's squared absolute value is antipodally even, concentration on that hemisphere is exactly half its global energy, proving \(\sum_rT_{d,r}=I/2\). Rotation invariance gives a constant full-sphere reproducing-kernel diagonal, hence trace equals area fraction times \(N\). Every nonempty rank cell contains an open subset of the sphere, as does the complement of any nonempty proper union within the hemisphere. A nonzero harmonic polynomial cannot vanish on an open spherical patch; this proves strict positivity and strict upper bound \(1/2\).

## Verification
`CHECK.py` requires only Python's standard library. Run `python CHECK.py` to evaluate the chi-square integrals using midpoint quadrature in the variable \(u=\sqrt t\); test the partition and trace identities for dimensions \(4,5,6,8,12\); and compare the four rank-two spectral levels in dimension four against independent direct Gaussian fourth-moment sampling. The checker does not replace the proof. For \(d=4,r=2\), its numerical values in sector order \(Z,M,O,D\) are about \((0.02367881636,0.17566059182,0.07433940818,0.17566059182)\); an exact coincidence of the numerically equal \(M\) and \(D\) levels is **not separately claimed or required**.

## Relationship to prior work
Classical spherical spatiospectral concentration theory defines the restriction eigenvalue problem for arbitrary regions but does not evaluate these coordinate-order masks. Roddy and McEwen's 2023 manifold Slepian-wavelet framework motivates region-adapted observation but works with different spectral objects. Gerhards and Huang's 2023 ball study analyzes asymptotic spectra for polynomial and radial-angular bandwidths, not the present pure degree-two spherical rank cells. Related pre-existing positive-orthant, quarter-wedge, and coordinate-dominant rank-one calculations concern different or special masks; in particular, the known rank-one calculation is only the \(r=1\) member here and is not independently claimed as new. The additional content is the simultaneous exact spectral resolution of **every** rank and of **every** union of ranks, including sharp reconstruction bounds from a single set of common harmonic eigenspaces.

## Limitations
The one-dimensional formulas are exact integrals, not generally elementary closed forms. They identify sharp extrema but do not order the four levels universally for every dimension and rank, nor classify all possible degeneracies. No higher harmonic degrees, nonsymmetric label-dependent masks, or optimal selection of \(J\) under a size budget is asserted. An unindexed earlier equivalent order-statistic mask computation remains a historical-priority risk. Numerical experiments validate representative cases but do not certify the infinite-parameter theorem.

## References
- P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on Manifolds*, arXiv:2302.06006, initially posted 2023-02-12, https://arxiv.org/abs/2302.06006.
- F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review 48 (2006), preprint arXiv:math/0408424, https://arxiv.org/abs/math/0408424.
- C. Gerhards and X. Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543, initially posted 2023-08-07, https://arxiv.org/abs/2308.03543.
