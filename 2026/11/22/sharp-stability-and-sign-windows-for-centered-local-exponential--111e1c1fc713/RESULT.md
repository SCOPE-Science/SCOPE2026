# Sharp stability and sign windows for centered local exponential heat stencils

## Finding

For the one-dimensional heat equation \(u_t=\kappa u_{xx}\), set \(\mu=\kappa\Delta t/h^2\ge0\). Consider the centered \((2r+1)\)-node local matrix-exponential propagator obtained by exponentiating the exact second-differentiation matrix on the degree-\(2r\) Lagrange interpolation space and harvesting its center row. On any uniform periodic grid with at least \(2r+1\) distinct nodes, it defines a symmetric, mass-conserving finite convolution \(T_r(\mu)\).

For the first three odd stencil sizes, the exact positivity and uniform periodic \(\ell^2\)-contraction conditions are:

| Number of stencil nodes | Entrywise nonnegative exactly for | \(\ell^2\)-contractive on **every** admissible periodic grid exactly for |
|---|---|---|
| \(3\) | \(0\le\mu\le 1/2\) | \(0\le\mu\le1/2\) |
| \(5\) | \(\mu=0\), or \(1/6\le\mu\le2/3\) | \(0\le\mu\le2/3\) |
| \(7\) | \(\mu=0\), or \((5-\sqrt{10})/10\le\mu\le(5+\sqrt{10})/10\) | \(0\le\mu\le\mu_*\) |

Here \(\mu_*=0.841360228011148\ldots\) is the unique positive root of
\[
480\mu^3-600\mu^2+272\mu-90=0.
\]
The upper positivity threshold for seven nodes is \((5+\sqrt{10})/10=0.816227766016838\ldots<\mu_*\); hence a nonempty range of steps remains spectrally contractive but violates nodal positivity. In five and seven nodes, **arbitrarily small positive steps violate positivity**, even though the zero step is the identity. Both recovered positivity intervals are exact, not numerical estimates.

More generally, for **every** \(r\ge2\), there are positive constants \(\varepsilon_r,R_r\) such that \(T_r(\mu)\) has a negative entry whenever \(0<\mu<\varepsilon_r\) or \(\mu>R_r\). No centered polynomial-exponential stencil with at least five nodes is positive for all positive timesteps.

## Assumptions and scope

Fix \(r\ge1\), uniform spacing \(h>0\), constant diffusivity \(\kappa>0\), and periodic grid size \(N\ge2r+1\). For nodes \(j=-r,\ldots,r\), let \(\ell_j(x)\) be the Lagrange basis polynomial satisfying \(\ell_j(k)=\delta_{jk}\). Let \(D_r^{(2)}\) denote the matrix with entries \((D_r^{(2)})_{ij}=\ell_j''(i)\), indexed by these nodes (dimensionless coordinates). Define
\[
w_j^{(r)}(\mu)=\bigl[e^{\mu D_r^{(2)}}\bigr]_{0j}
=\sum_{a=0}^{r}\frac{\mu^a}{a!}\ell_j^{(2a)}(0),\qquad
(T_r(\mu)u)_k=\sum_{j=-r}^r w_j^{(r)}(\mu)u_{k+j\;\mathrm{mod}\;N}.
\]
The finite sum is exact: differentiation by twice is nilpotent on polynomials of degree at most \(2r\). A step is *positive* when it maps every componentwise nonnegative grid vector to another such vector, equivalently all convolution weights are nonnegative. *Uniform periodic \(\ell^2\)-contraction* means the operator norm is at most one for every admissible finite periodic grid. For necessity of an unstable Nyquist mode, even grids with \(N\ge2r+2\) suffice.

These are completed-step, constant-coefficient, centered-stencil statements; neither stagewise nor boundary-stencil positivity is asserted.

## Proof

**Conservation.** Since \(\sum_j\ell_j(x)=1\), all differentiated sums vanish and \(\sum_jw_j=1\). Reflection of the symmetric nodes gives \(w_{-j}=w_j\). Thus each periodic convolution is real symmetric and doubly stochastic exactly when its entries are nonnegative. Its Fourier eigenvalue is
\[
G_r(\theta,\mu)=w_0+2\sum_{j=1}^r w_j\cos(j\theta),\qquad \theta=2\pi k/N.
\]

**Three nodes.** The weights are \(w_0=1-2\mu\) and \(w_{\pm1}=\mu\); writing \(t=\sin^2(\theta/2)\in[0,1]\), the symbol is \(G_1=1-4\mu t\). This proves both exact bounds \(\mu\le1/2\).

**Five nodes.** Direct application of the truncated heat exponential gives
\[
w_0=\frac{6\mu^2-5\mu+2}{2},\qquad
w_{\pm1}=\frac{2\mu(2-3\mu)}3,\qquad
w_{\pm2}=\frac{\mu(6\mu-1)}{12}.
\]
The first weight is strictly positive (its quadratic discriminant is negative), and the other two weights are nonnegative simultaneously exactly for \(1/6\le\mu\le2/3\), apart from the identity at \(\mu=0\). The Fourier symbol is
\[
G_2(t,\mu)=1-4\mu t+\frac43\mu(6\mu-1)t^2.
\]
For \(1/6\le\mu\le2/3\), positivity of the weights implies \(|G_2|\le1\). For \(0\le\mu\le1/6\), \(G_2\) decreases in \(t\), and its value at \(t=1\) is \(1-16\mu/3+8\mu^2\ge1/3\). Conversely, if \(\mu>2/3\), then \(G_2(1,\mu)-1=(8/3)\mu(3\mu-2)>0\). An even periodic grid contains \(\theta=\pi\). This proves the uniform \(\ell^2\) frontier.

**Seven nodes.** The four independent weights are
\[
\begin{aligned}
w_0&=-\frac{60\mu^3-84\mu^2+49\mu-18}{18},\\
w_{\pm1}&=\frac{\mu(10\mu^2-13\mu+6)}4,\\
w_{\pm2}&=-\frac{\mu(20\mu^2-20\mu+3)}{20},\\
w_{\pm3}&=\frac{\mu(30\mu^2-15\mu+2)}{180}.
\end{aligned}
\]
For positive \(\mu\), both \(w_1\) and \(w_3\) are strictly positive (negative quadratic discriminants). The inequality \(w_2\ge0\) is equivalent to
\[
(5-\sqrt{10})/10\le\mu\le(5+\sqrt{10})/10.
\]
The center weight \(w_0\) is strictly decreasing in \(\mu\) because its derivative has a strictly positive opposite sign; at the upper endpoint it equals \((16-4\sqrt{10})/45>0\). Hence these are exactly the positivity steps outside the isolated identity.

For stability, an exact trigonometric reduction gives
\[
G_3(t,\mu)=1-4\mu t-\frac{4\mu(8t^3+15t^2)}{45}
+\frac{8\mu^2(2t^3+3t^2)}3-\frac{32\mu^3t^3}3.
\]
Equivalently, its derivative obeys
\[
\partial_tG_3=-\frac{4\mu}{15}H(t,\mu),\quad
H=120\bigl(\mu t-\tfrac{t+1}{4}\bigr)^2+\tfrac{t^2-10t+15}{2}\ge3
\]
for \(0\le t\le1\). Thus \(G_3\) decreases strictly from \(G_3(0,\mu)=1\) to its Nyquist value. The sole constraint for \(|G_3|\le1\) is \(G_3(1,\mu)\ge-1\), equivalently
\[
480\mu^3-600\mu^2+272\mu-90\le0.
\]
The cubic is strictly increasing on the real line, with derivative \(1440(\mu-5/12)^2+22>0\), and has exactly one positive root \(\mu_*\). At the upper positivity endpoint, \(G_3(1,\mu)=-(13+8\sqrt{10})/45>-1\); therefore the positivity interval ends strictly before the stability interval.

**All higher centered orders.** For \(r\ge2\), the classical centered Lagrange second-derivative weight at offset two is
\[
\frac{d}{d\mu}w_2^{(r)}(0)=-\frac{r(r-1)}{2(r+1)(r+2)}<0.
\]
Thus \(w_2^{(r)}(\mu)<0\) for all sufficiently small positive \(\mu\). At the opposite extreme, the leading coefficient of \(\ell_{r-1}\) is \(-1/(2r-1)!\), giving
\[
w_{r-1}^{(r)}(\mu)=-\frac{2r}{r!}\mu^r+O(\mu^{r-1})<0
\]
for all sufficiently large \(\mu\). These explicit coefficients prove the universal short- and long-step sign obstructions.

## Verification

The accompanying `verify.py` independently constructs each polynomial differentiation matrix, checks its nilpotency, reproduces the exponential center rows via both matrix powers and derivatives of Lagrange polynomials, and verifies the declared Fourier identities and exact root relations. It also checks periodic matrix eigenvalues against discrete Fourier symbols for a finite sample of rational timestep ratios. It executed successfully with `VERIFY_OK 90 algebraic and matrix checks`. The infinite-dimensional and all-parameter conclusions follow from the displayed proof rather than from sampled eigenvalues.

Reproduce by running `python verify.py` with Python 3, SymPy and NumPy available. Dimensionless coordinates make the same formulas valid for any positive physical spacing and diffusivity once \(\mu\) is fixed.

## Relationship to prior work

Bayona's local matrix-exponential propagator introduces the exact polynomial-interpolant exponential and demonstrates larger empirical stability envelopes; the original study does not give the complete positivity and uniform periodic contractivity intervals above. Standard interpolation-differentiation stencils and von Neumann analysis are classical; in particular the negative outer weights of high-order second derivatives and the three-point heat CFL bound are not new. The contribution here is the sharp joint classification for three successive centered stencil sizes, including the unexpected isolated identity and recovered positive-step windows, the seven-point Nyquist/positivity separation, and the general all-orders two-end sign obstruction.

This statement concerns local *finite polynomial* exponentials assembled into a banded periodic update. It is not the exact global exponential of the spatially assembled high-order heat generator, and it is not a backward-Euler, Runge–Kutta, or rational filtered heat step. These distinctions prevent equivalence with results on positivity of those different semigroups and numerical maps.

## Limitations

No claim is made for nonlinear equations, variable coefficients, nonuniform nodes, nonperiodic boundary harvesting, or higher-dimensional stencils. A single periodic grid of odd size may admit a larger spectral stability interval than the *uniform-over-all-grids* cutoff given here, because it does not include the Nyquist frequency. For \(r\ge4\), the sign obstructions are established but no exact intermediate positivity interval or stability threshold is claimed. Positivity and spectral contraction are discrete stability properties, not guaranteed accuracy for an arbitrarily large physical timestep. Independent mathematical validation has not been performed.

## References

1. V. Bayona, *Unifying Finite Differences and Semi-Lagrangian Schemes via Localized Matrix Exponentials*, arXiv:2603.15964, first version 2026-03-16, https://arxiv.org/abs/2603.15964.
2. P.-O. Persson, *Finite Difference Methods for PDEs*, Math 228B lecture notes, https://persson.berkeley.edu/math228b/html/finite_difference_methods_for_PDEs.html (classical stencil and Fourier-method background).
