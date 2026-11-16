# Dimension-free first Slepian splitting for parity-orthant masks

## Finding

Fix integers \(m\ge2\) and \(d\ge2m\). On the sphere \(\mathbb S^{d-1}\) with normalized surface probability measure, define the checkerboard-orthant observation region
\[
\Omega_{d,m}=\big\{x\in\mathbb S^{d-1}:\prod_{j=1}^{2m}x_j>0\big\}.
\]
Let \(V_L=\bigoplus_{\ell=0}^{L}\mathcal H_\ell(\mathbb S^{d-1})\) denote the complex spherical-harmonic band through degree \(L\), and let \(T_{d,m,L}=P_{V_L}\mathbf1_{\Omega_{d,m}}\vert_{V_L}\) be its energy-concentration operator. Then:

1. For **every** \(0\le L<m\), \(T_{d,m,L}=\tfrac12 I\); every bandlimited signal has exactly half its energy in \(\Omega_{d,m}\).
2. At the **first nontrivial bandwidth** \(L=m\), the complete spectrum is
\[
\lambda_+=\frac{1+(2/\pi)^m}{2},\quad
\lambda_-=\frac{1-(2/\pi)^m}{2}
\quad\text{(each of multiplicity }\tfrac12\binom{2m}{m}\text{)},
\]
with all remaining eigenvalues equal to \(\tfrac12\), of multiplicity
\[
\binom{d+m}{m}-\binom{d+m-2}{m-2}-\binom{2m}{m}.
\]
3. Every extremal eigendirection is explicitly a linear combination of complementary squarefree monomials: choose one representative of each pair \(I,\{1,\ldots,2m\}\setminus I\), where \(|I|=m\). Write \(x_I=\prod_{i\in I}x_i\). The normalized vectors proportional to \(x_I+x_{I^c}\) and \(x_I-x_{I^c}\) give the \(\lambda_+\) and \(\lambda_-\) eigenspaces respectively.
4. The sharp ratio of maximal to minimal captured squared energy is
\[
\kappa_{d,m}=\frac{1+(2/\pi)^m}{1-(2/\pi)^m}.
\]
Both the noncentral eigenvalues and their multiplicities are **independent of ambient dimension \(d\)**; only the central multiplicity changes.

## Assumptions and scope

All dimensions are integral, \(m\ge2\), \(d\ge2m\), and the sign-product set uses exactly \(2m\) *distinct* orthonormal coordinate directions. Coordinate hyperplanes have zero surface measure, so their assignment to either side does not affect the operator. The complex Hilbert inner product is \(\langle f,g\rangle=\int_{\mathbb S^{d-1}}f\overline g\,d\sigma\) with \(\int d\sigma=1\). The sphere is the standard real unit sphere. The result is for cumulative harmonic bands, not for isolated degrees beyond the critical bandwidth or arbitrary masks.

## Proof

**1. Sign-selection rule.** Set \(\chi(x)=\prod_{j=1}^{2m}\operatorname{sgn}(x_j)\). The observation indicator satisfies \(\mathbf1_{\Omega_{d,m}}=(1+\chi)/2\) almost everywhere. Reflection of any selected coordinate changes the sign of \(\chi\) while preserving spherical measure, so \(\int\chi=0\) and \(\sigma(\Omega_{d,m})=1/2\).

For every monomial \(x^\alpha\) of total degree less than \(2m\), at least one selected coordinate has an even exponent. Reflecting that coordinate proves \(\int\chi x^\alpha\,d\sigma=0\). Consequently, for any polynomials \(f,g\) of degree at most \(L<m\), the sign-weighted integral \(\int\chi f\overline g\,d\sigma\) is zero. This proves assertion 1, including all mixed-degree terms.

**2. The only possible critical monomial.** At \(L=m\), each monomial term of \(f\overline g\) has total degree at most \(2m\). For its \(\chi\)-weighted integral to be nonzero, every one of the first \(2m\) exponents must be odd. Degree counting forces the exponent vector to have a \(1\) on precisely those first \(2m\) coordinates and \(0\) elsewhere. Thus only the squarefree monomial \(x_1\cdots x_{2m}\) survives sign integration. In particular, only pairs of degree-\(m\) squarefree terms \(x_I\) and \(x_{I^c}\) can couple; the lower harmonic degrees are annihilated by the compressed multiplier \(J=P_{V_m}\chi\vert_{V_m}\).

**3. Orthogonal decomposition.** Every \(x_I\) with \(|I|=m\) and \(I\subseteq\{1,\ldots,2m\}\) is harmonic (each variable occurs at most linearly). Distinct \(x_I\) are orthogonal, because the product has an odd coordinate exponent. Moreover, for a homogeneous degree-\(m\) polynomial, the spherical inner product with \(x_I\) extracts only its \(x_I\)-coefficient times \(\|x_I\|^2\): a different degree-\(m\) monomial cannot have the same pattern of odd exponents as \(x_I\). Therefore the span \(W\) of these \(\binom{2m}{m}\) monomials is an orthogonal summand of \(\mathcal H_m\), and the compressed sign multiplier vanishes on its orthogonal complement in \(V_m\).

**4. Two exact spherical moments.** If \(X\) is uniform on \(\mathbb S^{d-1}\), the vector of squared coordinates has Dirichlet parameters \((1/2,\ldots,1/2)\). Therefore, for every subset \(I\) of size \(m\),
\[
q_{d,m}:=\mathbb E X_I^2=\frac{\Gamma(d/2)}{2^m\Gamma(d/2+m)},
\quad
b_{d,m}:=\mathbb E\prod_{j=1}^{2m}|X_j|=\frac{\Gamma(d/2)}{\pi^m\Gamma(d/2+m)}.
\]
The normalized complementary coupling is exactly
\[
\rho_m=\frac{b_{d,m}}{q_{d,m}}=\left(\frac2\pi\right)^m.
\]
Consequently, on the orthonormal squarefree basis \(x_I/\sqrt{q_{d,m}}\), the operator \(J\) acts by \(Jx_I=\rho_m x_{I^c}\), and vanishes on \(W^\perp\). Complementation has no fixed point when \(m\ge1\), hence its plus and minus eigenspaces both have dimension \(\binom{2m}{m}/2\). Since \(T=(I+J)/2\), this establishes the asserted noncentral spectrum, eigenvectors, and strict positive lower bound.

**5. Remaining multiplicity and sharpness.** The dimension of \(V_m\) is the standard harmonic-polynomial count \(\binom{d+m}{m}-\binom{d+m-2}{m-2}\). Subtracting \(\dim W=\binom{2m}{m}\) gives the central multiplicity. Both extremes are attained by the displayed complementary monomial combinations, proving the sharp condition ratio. As \(2/\pi<1\), all eigenvalues lie strictly between zero and one and the noncentral splitting decays exponentially with the parity depth \(m\). This proves all assertions.

## Verification

The separate `ParitySpectrumChecker.py` forms nullspace bases of homogeneous polynomial Laplacians (without assuming the proposed complementary-pair decomposition), calculates unconditional and parity-weighted spherical monomial moments, constructs the full cumulative-band Gram and sign matrices, and solves their generalized Hermitian eigenproblems. It verifies eight ambient-dimension/parity-depth cases, including \((d,2m)=(4,4),(5,4),(6,4),(6,6),(7,6)\); the largest computed spectral discrepancy is below \(6\times10^{-16}\). The exact theorem is proved algebraically above; numerical agreement in finite dimensions is supporting evidence, not an infinite-dimensional certificate.

## Relationship to prior work

The classical Slepian formulation and general finite-dimensional concentration-eigenproblem are established in Simons–Dahlen–Wieczorek (2004/2006). Speckbacher–Hrycak (2019) derive large-sieve estimates for bandlimited spherical harmonics, while Michel–Plattner–Seibert (2021) develop commuting-operator methods for cap regions. None of the inspected theorems gives the checkerboard-orthant spectrum above. General reflection symmetry forces eigenvalue pairing around one-half, but it does not determine the *first* noncentral bandwidth, the exact pair multiplicities, or the ambient-dimension-independent \((2/\pi)^m\) splitting. Discrete cube-vertex Walsh interpolation is a distinct sampling model, not a restriction-energy calculation over positive-measure spherical regions.

## Limitations

The result treats exactly one even-parity constraint on \(2m\) selected coordinate signs and the cumulative harmonic bandwidths through \(m\). It does not classify odd numbers of constrained signs, higher bandwidths, unequal orthant weights, or arbitrarily rotated sign patterns lacking orthogonality. The lower-band half-energy identity follows from elementary sign symmetry; its inclusion identifies the first meaningful bandwidth for the new exact spectral classification. Historical priority is provisional because specialized older signed-orthant harmonic moment identities could conceivably imply the result. No independent mathematical audit has been performed.

## References

1. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, first posted 31 August 2004, https://arxiv.org/abs/math/0408424 .
2. M. Speckbacher and T. Hrycak, *Concentration estimates for band-limited spherical harmonics expansions via the large sieve principle*, arXiv:1909.01670, first posted 4 September 2019, https://arxiv.org/abs/1909.01670 .
3. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first posted 26 March 2021, https://arxiv.org/abs/2103.14650 .
