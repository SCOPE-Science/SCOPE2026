# Strict dimensional convexity and universal high-intensity curvature for one-source branching walks

## Finding

For a continuous-time symmetric, finite-range, irreducible coordinate walk on \(\mathbb Z\), form its independent-coordinate products on \(\mathbb Z^d\). Add one branching source of positive net intensity \(\beta\) at the origin. Whenever the positive growth eigenvalues \(\lambda_d(\beta)\), \(\lambda_{d+1}(\beta)\), and \(\lambda_{d+2}(\beta)\) exist,
\[
\lambda_d(\beta)-\lambda_{d+1}(\beta)>
\lambda_{d+1}(\beta)-\lambda_{d+2}(\beta)>0.
\]
Thus the loss in growth rate from adding a coordinate is strictly diminishing, rather than merely nonnegative.

Write the one-coordinate jump rates as \(b_z=b_{-z}\ge0\) for \(z\ne0\), let \(c=\sum_{z\ne0}b_z>0\), and let \(B\) be the zero-diagonal convolution operator with off-diagonal rates \(b_z\). Define \(v=(B^2)_{00}=\sum b_z^2>0\), \(w=(B^3)_{00}\), and \(u=(B^4)_{00}\). For every fixed integer \(d\ge1\), as \(\beta\to\infty\),
\[
\lambda_d(\beta)=\beta-cd+\frac{dv}{\beta}+\frac{dw}{\beta^2}
 +\frac{du+(d^2-3d)v^2}{\beta^3}+O_d(\beta^{-4}),
\]
so in particular
\[
\lambda_d(\beta)-2\lambda_{d+1}(\beta)+\lambda_{d+2}(\beta)
 =\frac{2v^2}{\beta^3}+O_d(\beta^{-4}).
\]
The leading cross-dimensional curvature is universal: it depends only on the squared jump-rate sum \(v\), even when the walk admits three-step return loops.

For symmetric nearest-neighbor rate \(r>0\) in each direction, \(c=2r\), \(v=2r^2\), \(w=0\), and \(u=6r^4\). The stronger parity expansion becomes
\[
\lambda_d(\beta)=\beta-2rd+\frac{2dr^2}{\beta}
 +\frac{(4d^2-6d)r^4}{\beta^3}+O_{d,r}(\beta^{-5}),
\qquad
\lambda_d-2\lambda_{d+1}+\lambda_{d+2}
 =\frac{8r^4}{\beta^3}+O_{d,r}(\beta^{-5}).
\]

## Assumptions and scope

Take fixed positive, finite-range symmetric jump rates \(b_z\) on \(\mathbb Z\), with their support generating the additive group of integers. The generator of the one-dimensional walk is \(A_1=B-cI\). In dimension \(d\), let \(A_d\) act by the sum of \(d\) independent coordinate generators. The evolution operator for expected particle counts with a single branching site is
\[
H_{d,\beta}=A_d+\beta\lvert\delta_0\rangle\langle\delta_0\rvert
\quad\text{on }\ell^2(\mathbb Z^d).
\]
The positive isolated eigenvalue, if it exists, is denoted \(\lambda_d(\beta)\); it is unique. A probabilistic realization can use birth-only branching at the origin at rate \(\beta\), ensuring precisely this mean generator. The theorem applies separately to every fixed \(\beta>0\) at all triples of dimensions for which the positive eigenvalue exists, and to each fixed dimension in the stated strong-intensity asymptotics. It does not claim that positive eigenvalues exist at arbitrarily large dimension for fixed \(\beta\).

For the interpolation used in the proof, put \(q(t)=\Pr_0(X_t=0)\) for the one-coordinate walk, and
\[
\mathcal I_\beta=\Big\{x>0:\beta\int_0^\infty q(t)^x\,dt>1\Big\}.
\]
An infinite integral is allowed. The continuous interpolation \(\lambda(x)>0\) is defined uniquely on this open set by
\[
\beta\int_0^\infty e^{-\lambda(x)t}q(t)^x\,dt=1.
\]
For integer \(d\in\mathcal I_\beta\), this agrees with the positive eigenvalue of \(H_{d,\beta}\). Noninteger \(x\) is only an analytic interpolation, not a physical fractional-dimensional lattice.

## Proof

**Resolvent and product representation.** The rank-one resolvent formula says that \(\lambda>0\) is an eigenvalue of \(H_{d,\beta}\) exactly when \(\beta G_d(\lambda)=1\), where
\[
G_d(\lambda)=\langle\delta_0,(\lambda-A_d)^{-1}\delta_0\rangle
 =\int_0^\infty e^{-\lambda t}q(t)^d\,dt.
\]
The last identity uses independent coordinate semigroups. The integral is strictly decreasing continuously from \(G_d(0)\) to zero as \(\lambda\) increases, so a positive root is unique exactly when \(\beta G_d(0)>1\). The same argument defines \(\lambda(x)\) on \(\mathcal I_\beta\). Since \(0<q(t)<1\) for \(t>0\), the supercritical set is an initial interval, and it contains the intervening real dimensions whenever it contains two integers.

**Strict convexity.** Put \(a(t)=-\log q(t)\) and give \(T\in(0,\infty)\) the probability density \(\beta e^{-\lambda(x)t}q(t)^x\). Derivatives of the implicit root are justified locally by exponential integrability: \(0\le a(t)\le ct\), because \(q(t)\ge e^{-ct}\). Differentiating once and twice gives
\[
\lambda'(x)=-\frac{\mathbb E[a(T)]}{\mathbb E[T]}<0,
\qquad
\lambda''(x)=\frac{\operatorname{Var}(a(T)+\lambda'(x)T)}{\mathbb E[T]}.
\]
For strict positivity, \(q'(0)=-c\) and \(q''(0)=c^2+v\), hence \(a''(0)=-v<0\). Thus \(a(t)\) cannot be affine in \(t\); the variance above is strictly positive because the tilted distribution has a positive density on every positive interval. Consequently \(\lambda(x)\) is strictly decreasing and strictly convex throughout \(\mathcal I_\beta\). Applying the strict slope inequality at successive integer points proves both strict inequalities in the finding.

**High-intensity expansion.** Let \(B_d\) be the sum of the commuting zero-diagonal coordinate operators and put \(s=\lambda+cd\). Its first five diagonal moments are
\[
(B_d^0)_{00}=1,\quad (B_d)_{00}=0,\quad
(B_d^2)_{00}=dv,\quad (B_d^3)_{00}=dw,\quad
(B_d^4)_{00}=du+3d(d-1)v^2.
\]
The last identity counts either all four steps in one coordinate or a pair of two-step returns in each of two distinct coordinates, with six interleavings. Since \(B_d\) is bounded, its Neumann resolvent expansion at large \(s\) is
\[
G_d(\lambda)=\frac1s+\frac{dv}{s^3}+\frac{dw}{s^4}
 +\frac{du+3d(d-1)v^2}{s^5}+O_d(s^{-6}).
\]
Solving \(G_d(\lambda)=1/\beta\) by power-series reversion gives
\[
s=\beta+\frac{dv}{\beta}+\frac{dw}{\beta^2}
 +\frac{du+(d^2-3d)v^2}{\beta^3}+O_d(\beta^{-4}).
\]
Subtracting \(cd\) and then taking a second difference yields the universal \(2v^2\) coefficient. In the nearest-neighbor case, odd diagonal moments vanish by bipartite parity; the remainder in the eigenvalue series improves to \(O_{d,r}(\beta^{-5})\), and substitution of the stated moments gives the explicit nearest-neighbor formula.

## Verification

`CHECKER.py` independently enumerates one- through four-step closed walks for four finite-range symmetric jump kernels in dimensions one through four, verifies the universal moment identities, and checks the formal resolvent-series reversion symbolically. It also solves the nearest-neighbor Green-function equation numerically for \(\beta\in\{10,20,40,80\}\), dimensions \(2,3,4\). All 84 embedded checks passed; `CHECKER_OUTPUT.txt` records the values. The numerical dimension curvatures are positive and their \(\beta^3\)-multiples tend toward the predicted value \(8\) for rate one. These finite diagnostics are not substitutes for the implicit-differentiation and resolvent arguments proving the universal statements.

## Relationship to prior work

Yarovaya, *Supercritical Branching Random Walks on Nested Lattices* (2026), Theorem 4 establishes strict **monotonicity** of the positive growth eigenvalue as the lattice dimension rises, and Theorem 5 provides a first-order strong-source expansion for a broader nested-lattice setting. Neither theorem states strict discrete curvature or the jump-rate-universal third-order coefficient above. The present theorem deliberately assumes independent coordinate products rather than claiming curvature for arbitrary nested lattices.

The earlier paper by Gusarov and Yarovaya (2026) treats precisely symmetric nearest-neighbor lattices and determines eigenvalues using successive approximations. Its publicly available abstract was reviewed, but its full text could not be inspected; a potentially stronger implicit or explicit comparison remains an originality risk. Yarovaya (2015), *Positive Discrete Spectrum of the Evolutionary Operator of Supercritical Branching Walks with Heavy Tails*, establishes the rank-one Green-function eigenvalue framework used here, not a cross-dimensional curvature law. No historical-priority uniqueness is asserted.

## Limitations

The result applies only to independent-coordinate product walks with finite-range symmetric jump rates, not arbitrary dimension-consistent random walks. It concerns the positive eigenvalue of the expected-particle evolution operator, not sample-path almost-sure growth, extinction or survival probabilities. The expansion is at fixed integer dimension as \(\beta\to\infty\); its error is not claimed uniform over growing dimension. An uninspected relevant full text or a stronger general result could affect priority, notwithstanding the direct mathematical proof. This work has not undergone independent audit.

## References

1. E. Yarovaya, *Supercritical Branching Random Walks on Nested Lattices*, arXiv:2610.27129, first publicly submitted October 19, 2026. https://arxiv.org/abs/2610.27129
2. A. S. Gusarov and E. B. Yarovaya, *Estimation of particle number growth in a supercritical branching random walk by the method of successive approximations*, Teor. Veroyatnost. i Primenen. 71 (2026), 473–495, public July 23, 2026. https://doi.org/10.4213/tvp5912
3. E. Yarovaya, *Positive Discrete Spectrum of the Evolutionary Operator of Supercritical Branching Walks with Heavy Tails*, arXiv:1511.07217, first publicly submitted November 23, 2015. https://arxiv.org/abs/1511.07217
