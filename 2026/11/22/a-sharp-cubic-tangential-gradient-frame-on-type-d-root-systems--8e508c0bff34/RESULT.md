# A sharp cubic tangential-gradient frame on type-\(D\) root systems

## Finding
For every integer \(d\ge3\), put
\[
R_d=\{(\varepsilon e_i+\eta e_j)/\sqrt2:1\le i<j\le d,\ \varepsilon,\eta\in\{-1,1\}\}\subset S^{d-1}.
\]
Let \(\mathcal H_3(d)\) be the complex Hilbert space of restrictions of homogeneous harmonic cubics in \(d\) real variables, with Dirichlet inner product
\[
\langle f,g\rangle_D=3(d+1)\int_{S^{d-1}}f\overline g\,d\sigma,
\]
where \(\sigma\) is probability surface measure. Define the tangent-gradient observation map \(G_d f=(\nabla_S f(x))_{x\in R_d}\), with squared output norm \(|R_d|^{-1}\sum_{x\in R_d}\|\nabla_S f(x)\|^2\). Its squared singular values (the eigenvalues of \(G_d^*G_d\)) are **exactly**

| Sector | Squared singular value | Multiplicity |
|---|---|---|
| Zonal \(Z\) | \(\displaystyle \lambda_Z=\frac{(d+4)(d^2+4d-8)}{8(d-1)(d+1)}\) | \(d\) |
| Transverse \(T\) | \(\displaystyle \lambda_T=\frac{(d+2)(d+4)(2d-5)}{24(d-1)(d+1)}\) | \(d(d-2)\) |
| Squarefree \(Q\) | \(\displaystyle \lambda_Q=\frac{(d+2)(d+4)}{2(d-1)(d+1)}\) | \(\binom d3\) |

All values are strictly positive. The map \(G_d\) is therefore injective for every \(d\ge3\), including the regular 24-cell (\(d=4\)) where the **point-value** sampling map annihilates the \(d\)-dimensional zonal cubic sector.

The sharp squared condition number is
\[
\kappa_d=\begin{cases}
12,&d=3,\\
\displaystyle\frac{3(d^2+4d-8)}{(d+2)(2d-5)},&4\le d\le8,\\
\displaystyle\frac{d^2+4d-8}{4(d+2)},&d\ge9.
\end{cases}
\]
Among all integer dimensions \(d\ge3\), the **unique best-conditioned dimension** is \(d=8\), with \(\kappa_8=12/5\). The sharp all-dimension lower frame bound is \(35/192\), attained only at \(d=3\) in the transverse sector.

## Assumptions and scope
The root orbit consists of all \(2d(d-1)\) listed points; equal weights and the full tangent vector at each root are essential. The Dirichlet norm is the intrinsic \(\dot H^1\) norm, since the degree-three Laplace–Beltrami eigenvalue on \(S^{d-1}\) is \(3(d+1)\). Squared singular values and condition numbers are for these stated Hilbert-space normalizations. No claim is made for noisy derivative measurements outside this model, for higher harmonic degrees, or for arbitrary subsets of roots.

## Proof
Write \(r^2=\sum_{i=1}^d x_i^2\). The full harmonic cubic space has dimension \(d(d-1)(d+4)/6\). Under independent coordinate sign changes, every cubic has odd-coordinate support of cardinality one or three. For every \(i\), the support-one harmonics split orthogonally into a one-dimensional permutation-invariant line and a \((d-2)\)-dimensional standard representation of the permutations fixing \(i\). Representatives are
\[
Z_i=x_i^3-\frac3{d+2}x_ir^2,\qquad T_i=x_i(x_j^2-x_k^2)\quad(i,j,k\ \text{distinct}).
\]
The sign-support-three representative is \(Q=x_ix_jx_k\). The hyperoctahedral symmetry of \(R_d\), together with these irreducible and inequivalent sign/permutation sectors, makes both the spherical Dirichlet form and the discrete gradient form scalar on each sector, with no cross-terms. Their dimensions sum to
\(d+d(d-2)+\binom d3=d(d-1)(d+4)/6\); thus no harmonic modes are omitted. The assertions can equivalently be checked by direct sign averaging and zero-sum coefficient constraints, without representation-theoretic assumptions.

For any homogeneous harmonic cubic \(F\), Euler's identity gives
\[
\|\nabla_SF(x)\|^2=\|\nabla F(x)\|^2-9|F(x)|^2,\quad\|x\|=1.
\]
Put \(D=d(d+2)(d+4)\). The standard spherical sixth-order moment formula yields
\[
\int|Z_i|^2d\sigma=\frac{6(d-1)}{d(d+2)^2(d+4)},\quad
\int|T_i|^2d\sigma=\frac4D,\quad
\int|Q|^2d\sigma=\frac1D.
\]
For the first representative, \(Z_i|_{S^{d-1}}=x_i^3-cx_i\) with \(c=3/(d+2)\), so
\(\|\nabla_SZ_i\|^2=(3x_i^2-c)^2(1-x_i^2)\). In the root set \(x_i^2=1/2\) at fraction \(2/d\) of nodes and is zero at fraction \((d-2)/d\). Hence
\[
\frac1{|R_d|}\sum_{R_d}\|\nabla_SZ_i\|^2=\frac{9(d^2+4d-8)}{4d(d+2)^2}.
\]
For \(T=x_1(x_2^2-x_3^2)\), classify the unordered support pair of a root. The gradient squared equals \(1/8\) on \(\{1,2\}\) or \(\{1,3\}\), equals \(1/4\) on \(\{2,j\}\) or \(\{3,j\}\) for \(j\ge4\), and is zero otherwise. Thus
\[
\frac1{|R_d|}\sum_{R_d}\|\nabla_ST\|^2=\frac{2d-5}{2d(d-1)}.
\]
For \(Q=x_1x_2x_3\), the tangential gradient has squared norm \(1/4\) precisely when a root has two active coordinates among \(\{1,2,3\}\), yielding
\[
\frac1{|R_d|}\sum_{R_d}\|\nabla_SQ\|^2=\frac3{2d(d-1)}.
\]
Dividing these three exact sample energies by \(3(d+1)\) times the corresponding spherical moments gives \(\lambda_Z,\lambda_T,\lambda_Q\) and the multiplicities above. Their differences factor as
\[
\lambda_Z-\lambda_T=\frac{(d+4)(d+14)}{24(d+1)},\quad
\lambda_Z-\lambda_Q=\frac{(d-4)(d+4)^2}{8(d-1)(d+1)},\quad
\lambda_T-\lambda_Q=\frac{(d+2)(d+4)(2d-17)}{24(d-1)(d+1)}.
\]
Consequently \(\lambda_T\) is smallest for \(3\le d\le8\) and \(\lambda_Q\) is smallest for \(d\ge9\); the largest is \(\lambda_Q\) at \(d=3\), shared by \(Z,Q\) at \(d=4\), and \(\lambda_Z\) thereafter. This proves the displayed sharp condition number. The middle formula strictly decreases with real \(d\ge4\), because its derivative is
\(-9(3d^2-4d+16)/((d+2)^2(2d-5)^2)\). The last formula strictly increases in \(d\); comparison of \(d=8,9\) gives the unique minimum \(12/5\) at \(d=8\). The transverse eigenvalue increases with \(d\ge3\); the squarefree eigenvalue decreases to \(1/2\), proving the universal lower bound \(35/192\).

At \(d=4\), every coordinate of a root lies in \(\{0,\pm1/\sqrt2\}\). Thus \(Z_i(x)=x_i(x_i^2-1/2)=0\) at every root, although its tangential gradients do not vanish. This verifies the asserted repair of a value-sampling blind sector.

## Verification
The standalone `check.py` constructs all harmonic cubic basis polynomials over exact rationals, evaluates every tangential-gradient Gram entry on the actual root orbit, and independently computes Dirichlet Gram entries from exact spherical monomial moments. It checks the full pairwise identity for \(d=3,4,5,6,7\) and all diagonal entries for \(d=8,9\). These finite checks corroborate, but do not replace, the all-dimensional proof above. Run with `python check.py` (Python standard library only). The exact numerical dimensions and sample counts are printed by the script.

## Relationship to prior work
The type-\(D_4\) root shell and its design properties are studied by Hirao, Nozaki and Tasaka (2023); their concern is harmonic vanishing, design uniqueness, lattice shells and modular forms, not the derivative-observation Gram spectrum. Xiao and Zhuang (2023) study spherical designs, variational gradients and framelet transforms from point values, not tangential gradients of a target harmonic at type-\(D\) roots. Allasia, Cavoretto and De Rossi (2017) formulate Hermite–Birkhoff interpolation with derivative data on manifolds, using cardinal basis functions but no type-\(D\) cubic spectrum. Publicly indexed results on all-degree and cubic **value-only** sampling on type-\(D\) roots report root-orbit scalar evaluation spectra and a cubic \(d=4\) loss; such a scalar evaluation statement does not determine the gradient-only frame operator. The explicit three-sector derivative spectrum and dimension-eight sharp conditioning claim are the specific objects being compared here.

## Limitations
The classification is restricted to exact-degree-three real-sphere harmonics sampled by all tangential gradients at the equal-weight type-\(D_d\) root orbit. It does not classify erasures, point values jointly with gradients, higher jets or other node sets. A covering equivalent statement may exist in unindexed or inaccessible literature; publicly indexed value-sampling entries were available as summaries rather than full articles and were not certified absent in their complete text. The provided verification is computationally finite, while the proof is analytic for every integer \(d\ge3\).

## References
- G. Allasia, R. Cavoretto, A. De Rossi, *Hermite-Birkhoff interpolation on scattered data on the sphere and other manifolds*, arXiv:1705.01032v1, first public May 2, 2017, https://arxiv.org/abs/1705.01032.
- Y. Xiao, X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1, first public March 9, 2023, https://arxiv.org/abs/2303.05365.
- M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs and modular forms of the D4 lattice*, arXiv:2303.09000v1, first public March 16, 2023, https://arxiv.org/abs/2303.09000.
