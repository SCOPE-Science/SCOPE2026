# Exact all-degree squarefree spherical-harmonic concentration on fixed sign-count regions

## Finding

Let integers \(d\ge 2k\), \(k\ge1\), and \(0\le s\le d\) be fixed. On the unit sphere \(S^{d-1}\) with normalized rotation-invariant measure \(\sigma\), consider the natural region
\[
R_{d,s}=\{x\in S^{d-1}: \#\{j:x_j>0\}=s\}
\]
and the space \(\mathcal Q_{d,k}=\operatorname{span}_{\mathbb C}\{x_S=\prod_{j\in S}x_j: S\subseteq[d],\ |S|=k\}\). This is the \(\binom dk\)-dimensional **squarefree** subspace of pure degree-\(k\) spherical harmonics: every spanning monomial is harmonic because it is multilinear. No claim is made for the entire pure-degree space. Define the concentration operator by
\[
\langle Cf,g\rangle_{S^{d-1}}=\int_{R_{d,s}}f\overline g\,d\sigma,
\qquad f,g\in\mathcal Q_{d,k}.
\]

Put \(c=2/\pi\), \(w=2^{-d}\binom ds\), \(q=d-s\). Binomial coefficients outside their natural integer range are zero. For every even integer \(m\in[0,2k]\) define the sign-shell correlation
\[
\rho_m(d,s)=\frac{1}{\binom dq}\sum_{j=0}^{m}(-1)^j\binom mj\binom{d-m}{q-j}.
\]
For \(r=0,\ldots,k\), set \(b_r=c^{k-r}\rho_{2(k-r)}(d,s)\); for \(\ell=0,\ldots,k\), set
\[
a_\ell=\sum_{r=0}^\ell(-1)^{\ell-r}\binom\ell r b_r.
\]
Then **every eigenvalue of \(C\)**, with multiplicities, is given by the \(k+1\) explicit levels
\[
\boxed{\displaystyle\lambda_i=w\sum_{\ell=i}^k a_\ell\binom{k-i}{\ell-i}\binom{d-\ell-i}{k-\ell},\qquad
M_i=\binom di-\binom d{i-1},\quad 0\le i\le k.}
\]
For numerical equalities between levels, combine multiplicities. In particular, \(0<\lambda_i<1\) for all \(i\), and \(\sum_i M_i\lambda_i=\binom dk w\). Hence the sharp concentration and leakage bounds on this space are exactly the minimum and maximum of the displayed finite set.

Two consequences distinguish the continuous spherical problem from a discrete sign-shell restriction. For \(k=1\), let \(t=2s-d\). The two levels reduce to
\[
\lambda_0=w\left[1+c\frac{t^2-d}{d}\right],\qquad
\lambda_1=w\left[1-c\frac{t^2-d}{d(d-1)}\right],
\]
with multiplicities \(1\) and \(d-1\). Thus the entire linear-harmonic space concentrates **isotropically**, meaning \(C=wI\), precisely when \(d=m^2\) for an integer \(m\ge2\) and \(s=(d\pm m)/2\). There are no additional equality parameters. The two regions are complementary under global sign inversion.

For \(k=2\) and every \(d\ge4\), **no** sign-count region gives a scalar quadratic-squarefree concentration operator. Indeed scalarity would imply simultaneously \(\rho_2=0\) and \(\rho_4=0\); the first equality forces \(t^2=d\), whereas
\[
\rho_4\bigm|_{t^2=d}=-\frac{2}{(d-2)(d-3)}\ne0.
\]
More precisely, at any integer-square dipole-isotropic parameter \(d=m^2\ge4\), \(s=(d\pm m)/2\), the three squarefree-quadratic eigenvalues have the particularly simple form
\[
\boxed{\displaystyle
w(1-c^2)\quad[1],\qquad
w\left(1+\frac{2c^2}{d-2}\right)\quad[d-1],\qquad
w\left(1-\frac{2c^2}{(d-2)(d-3)}\right)\quad\left[\frac{d(d-3)}2\right].}
\]
Here square brackets denote multiplicity, not exponentiation. For \(d=4\), the first and last values agree and their multiplicities are added. For \(d\ge9\), the displayed levels are distinct.

## Assumptions and scope

Every integer parameter is quantified in the first paragraph, with \(d\ge2k\). The surface measure is a probability measure; the area of \(R_{d,s}\) is \(w\). Boundary sign ambiguities occur only on coordinate great spheres of measure zero. Scalars and functions may be complex. The concentration operator is the compression of multiplication by \(\mathbf1_{R_{d,s}}\) to **only** the homogeneous, multilinear (squarefree) degree-\(k\) harmonics. Eigenvalue multiplicity refers to this \(\binom dk\)-dimensional subspace. The isotropy statement for \(k=1\) has nontrivial square-dimension solutions starting at \(d=4\). Positivity and strict subunit bounds refer to all the specified integer regions, including the all-positive and all-negative single orthants.

## Proof

**1. Exact sphere/sign factorization.** Let \(Z_1,\ldots,Z_d\) be independent standard real Gaussians and \(X=Z/\|Z\|\). Its coordinate signs are independent symmetric Rademacher variables, independent of the absolute coordinate magnitudes. A sign vector belongs to \(R_{d,s}\) precisely when it has \(q=d-s\) negative entries. For a fixed set \(E\subseteq[d]\) of size \(m\), averaging \(\prod_{j\in E}\operatorname{sgn}X_j\) over that sign layer gives the displayed finite hypergeometric sum \(\rho_m\). It is the parity average of the number of negative signs selected in \(E\).

For distinct \(k\)-subsets \(S,T\), write \(r=|S\cap T|\), \(h=k-r\). The absolute-moment identity for normalized Gaussians (or Dirichlet coordinate squares) gives
\[
\begin{aligned}
\mathbb E_{S^{d-1}}x_S^2&=\frac{\Gamma(d/2)}{2^k\Gamma(d/2+k)},\\
\mathbb E_{S^{d-1}}\bigl|x_Sx_T\bigr|&=\frac{\Gamma(d/2)}{\Gamma(d/2+k)}\left(\frac12\right)^r\left(\frac1\pi\right)^h.
\end{aligned}
\]
If \(S\ne T\), the full-sphere inner product of \(x_S,x_T\) vanishes because some coordinate occurs to the first power; for \(S=T\), it equals the first displayed positive constant. Thus the normalized \(x_S\) form an orthonormal basis. Restricting to the sign layer, the signed product has \(2h\) odd-power coordinates, so its conditional sign average is \(\rho_{2h}\). Consequently the **exact continuous concentration matrix** is
\[
\boxed{C_{S,T}=w\,c^{k-|S\cap T|}\rho_{2(k-|S\cap T|)}(d,s).}
\]
This formula includes the diagonal, which is \(w\).

**2. Johnson incidence spectral resolution.** Let \(W_\ell\) denote the inclusion matrix from \(\ell\)-subsets to \(k\)-subsets, with \((W_\ell)_{S,U}=\mathbf1_{U\subseteq S}\). Then \((W_\ell W_\ell^{\mathsf T})_{S,T}=\binom{|S\cap T|}{\ell}\). Binomial inversion of the coefficients in step 1 proves the operator identity
\[
C=w\sum_{\ell=0}^k a_\ell W_\ell W_\ell^{\mathsf T}.
\]
The standard Johnson inclusion decomposition is recalled here to fix its normalization. Let \(V_i=\operatorname{im}W_i\ominus\operatorname{im}W_{i-1}\), with \(W_0\) the constant columns and \(\operatorname{im}W_{-1}=0\). For \(d\ge2k\), incidence raising is injective up to rank \(k\), so
\[
\dim V_i=\binom di-\binom d{i-1}.
\]
On \(V_i\), the positive-semidefinite operator \(W_\ell W_\ell^{\mathsf T}\) acts by zero for \(\ell<i\) and by
\[
\binom{k-i}{\ell-i}\binom{d-\ell-i}{k-\ell}
\]
for \(\ell\ge i\). One direct proof works on a coefficient array annihilated by the rank-lowering incidence map and lifts it from level \(i\) to \(k\); applying \(D_{r+1}U_r-U_{r-1}D_r=(d-2r)I\) successively establishes the scalar, and orthogonality yields the full decomposition. Alternatively these are precisely the known Johnson inclusion eigenvalues in Ghareghani–Ghorbani–Mohammad-Noori (2009), Lemma 14. Substituting in the preceding matrix identity gives exactly \(\lambda_i\) and \(M_i\); all \(\binom dk\) dimensions are accounted for.

**3. Sharpness and bounds.** For any \(f\in\mathcal Q_{d,k}\), the Rayleigh quotient is a convex combination of the eigenvalues and every eigenvalue is attained by a nonzero vector in its eigenspace. Both \(R_{d,s}\) and its complement contain nonempty open spherical sets whenever \(d\ge2\) and \(0\le s\le d\). A nonzero spherical polynomial is real analytic and cannot vanish on either open set. Thus \(0<\int_R|f|^2<\int_{S^{d-1}}|f|^2\), which proves \(0<\lambda_i<1\). The trace is the sum of \(\binom dk\) equal diagonal entries \(w\), proving the stated identity and sharp bounds.

**4. Linear isotropy and quadratic obstruction.** Because signs are exchangeable with fixed sum \(t=2s-d\), their two-coordinate correlation is
\[
\rho_2=\frac{t^2-d}{d(d-1)}.
\]
For \(k=1\), the concentration matrix has diagonal entries \(w\) and constant off-diagonal \(wc\rho_2\); its constant-vector and coordinate-sum-zero eigenspaces give the two formulas. It is scalar iff \(t^2=d\). Since \(t\) is an integer of the same parity as \(d\), this holds exactly when \(d=m^2\) and \(t=\pm m\), giving \(s=(d\pm m)/2\). For \(d\ge2\), the first valid square is \(d=4\).

For \(k=2\), matrix entries for pairs sharing one coordinate equal \(wc\rho_2\), while entries for disjoint pairs equal \(wc^2\rho_4\). Both kinds of off-diagonal pairs exist when \(d\ge4\), so scalarity forces both correlations to vanish. The fixed-sign fourth correlation follows by expanding \(t^4\) in sign products or evaluating the fourth Krawtchouk polynomial:
\[
\rho_4=\frac{t^4-(6d-8)t^2+3d(d-2)}{d(d-1)(d-2)(d-3)}.
\]
Putting \(t^2=d\) yields \(-2/((d-2)(d-3))\), never zero. At these parameters, the quadratic Johnson matrix is \(C=w(I+c^2\rho_4 A_0)\), where \(A_0\) is the adjacency matrix of disjoint pairs. The three adjacency eigenvalues of this Kneser graph are \(\binom{d-2}{2}\), \(-(d-3)\), and \(1\), with multiplicities \(1,d-1,d(d-3)/2\). Substituting \(\rho_4=-2/((d-2)(d-3))\) gives the displayed three spectral levels. Their ordering and equality statements follow immediately.

## Verification

The accompanying independent program `verify_sign_layer.py` constructs each full concentration matrix by explicitly enumerating the appropriate sign vectors and independently integrating the Gaussian absolute moments. It compares all eigenvalues to the binomial-inversion/Johnson formula, verifies trace identities, and checks the linear isotropy characterization. Thirty-seven full matrix cases for dimensions \(4\) through \(8\), degrees through \(4\), and varying sign-counts passed with maximum absolute eigenvalue discrepancy \(7.8\times10^{-16}\). The dipole equality test also passed for every integer \(2\le d\le39\) and \(0\le s\le d\). Run `python3 verify_sign_layer.py` with NumPy. A separate standard-library program `verify_exact_signs.py` checks the two exact sign-correlation identities and quadratic obstruction in rational arithmetic over all dimensions and sign-counts through \(200\). These finite checks corroborate, but are not substitutes for, the all-parameter proof.

For instance, \(d=9\), \(s=3\) or \(6\) has \(w=84/512\). The linear squarefree concentration is exactly \(wI\). On the quadratic squarefree space, the three values are \(0.0975704732\ldots\) (multiplicity \(1\)), \(0.1830602219\ldots\) (multiplicity \(8\)), and \(0.1608962130\ldots\) (multiplicity \(27\)); isotropy cannot extend to these quadrupoles.

## Relationship to prior work

The general spherical spatiospectral concentration framework dates to Simons–Dahlen–Wieczorek (2006). Gerhards–Huang (first public preprint 2023-08-07) develop polynomial-bandlimited Slepian concentration on Euclidean balls, including spectral asymptotics and other regions; neither source states the continuous, fixed-sign-count **squarefree harmonic** spectrum above. The Johnson inclusion eigenvalues used in step 2 are classical, and specifically available in Ghareghani–Ghorbani–Mohammad-Noori (2009), Lemma 14; they are not claimed as new. Existing Boolean Walsh concentration results for Hamming shells and nonbinary Hamming spheres concern discrete character spaces and can have nontrivial kernels. In contrast, the present real-sphere matrix carries the gamma-moment factor \((2/\pi)^h\), is strictly positive definite, and has the displayed sharp all-degree spectrum. The new contribution claimed here is this assembled **continuous** harmonic operator, its exact spectrum for all admissible \((d,k,s)\), and the linear-isotropy/quadratic-obstruction classification, not generic association-scheme theory or an assertion that sign correlations are newly discovered.

## Limitations

The result does not cover nonsquarefree pure harmonics, the entire degree-\(k\) harmonic space, mixed-degree polynomial bands, arbitrary weighted orthant masks, or discrete sampling. It does not claim that the square-dimensional arithmetic or Johnson incidence diagonalization alone is novel. Related discrete Hamming-layer results supply much of the combinatorial structure, so priority would change if an earlier source explicitly identifies the continuous spherical compression with this kernel or a stronger operator family implying it. No independent mathematical audit is claimed.

## References

1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, SIAM Review 48 (2006), DOI: https://doi.org/10.1137/S0036144504445765.
2. C. Gerhards and X. Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543, first public version 2023-08-07, https://arxiv.org/abs/2308.03543.
3. N. Ghareghani, E. Ghorbani, and M. Mohammad-Noori, *Intersection matrices revisited*, arXiv:0902.4367 (2009), https://arxiv.org/abs/0902.4367.
4. *Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-dimension-spectral-resonances-for-quadratic-band-walsh-co--7e1319aedf95.
5. *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-all-degree-spectral-law-for-fourier-sampling-on-q-ary-hamming--f3d01cadaa90.
6. *Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-quadratic-spherical-orthant-concentration-and-a-sharp-dime--043aca2fd738.
