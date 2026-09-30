# Quadrupole symmetry-breaking Jacobi gap for the spherical standard double bubble

## Context

The equal-volume standard double bubble in the round unit 3-sphere
$S^3(1)$ (volume $2\pi^2$) consists of two outer spherical caps plus one
minimal interface disc meeting along a triple circle $C$ at $120$
degrees, axisymmetric about a bubble axis. Axisymmetric stability tests
cannot detect faceting; the first dangerous symmetry-breaking direction
is the quadrupole azimuthal sector $|m|=2$, the lowest non-Killing
harmonic above the $m=0$ symmetric and $m=1$ isometry modes. Euclidean
Fourier analysis of double-bubble Jacobi fields is qualitative only
(kernel equals isometries, no constants), and spherical minimality
theorems compute no azimuthal sector spectra.

## Definitions

Let $v\in[0.05,0.30]$ and $\Sigma_v=\Sigma_1\cup\Sigma_2\cup\Sigma_0$ be
the equal-volume standard double bubble with each enclosed region of
volume $v\,\mathrm{Vol}(S^3(1))$. Each sheet is a disc of revolution with
coordinates $(s,\phi)$, metric $g_j=ds^2+\rho_j(s)^2\,d\phi^2$, where
$\rho_j(s)\ge 0$ is the rotation orbit radius. In the unit sphere every
rotation orbit has length $2\pi\rho_j\le 2\pi$, so
$0\le\rho_j(s)\le 1$ on every sheet. Normal fields decompose as
$u_j(s,\phi)=\sum_m f_{j,m}(s)e^{im\phi}$; the $|m|=2$ sector uses
$m=\pm 2$ with pole regularity $f_{j,\pm 2}=O(\rho_j^2)$. The $L^2$ inner
product $\langle u,w\rangle=\sum_j\int u_j\bar w_j\,d\mu_j$ with
$d\mu_j=\rho_j\,ds\,d\phi$ is rotation-invariant. Since
$\int_0^{2\pi}e^{2i\phi}d\phi=\int_0^{2\pi}e^{2i\phi}e^{\pm i\phi}d\phi=0$,
the $|m|=2$ sector is $L^2$-orthogonal to constants and $e^{\pm i\phi}$
(the angular dependence of ambient Killing fields), hence orthogonal to
all rigid motions. For $m\ne 0$,
$\int_0^{2\pi}e^{im\phi}d\phi=0$, so every $|m|=2$ field is automatically
first-order volume-preserving. Linearized triple-junction matching is a
$\phi$-independent linear relation on radial traces at $C$ (common
factor $e^{im\phi}$ cancels), so the same radial triple is admissible
for $|m|=1$ and $|m|=2$. The cluster Jacobi form is
$Q(u)=\sum_j\int(|\nabla u_j|^2-V_ju_j^2)\,d\mu_j+B(\mathrm{tr}_C u,
\mathrm{tr}_C u)$ with $\phi$-independent potential
$V_j=|A_j|^2+\mathrm{Ric}(N_j,N_j)$ and an order-zero triple-line form
$B$ with $\phi$-independent coefficients, hence $m$-independent.

## Result

For every $v\in[0.05,0.30]$, every admissible $|m|=2$
volume-preserving triple-junction-compatible normal field $u$ orthogonal
to Killing motions satisfies
$Q_v(u)\ge 3\,\lVert u\rVert_{L^2(\Sigma_v)}^2$,
hence uniformly $Q_v(u)\ge \tfrac1{10}\lVert u\rVert^2$
($\kappa_{\mathrm{quad}}=1/10$ certified; in fact $\kappa=3$).
Consequently no normalized admissible quadrupole field has
$Q_v(u)<0$, and no area-beating faceted competitor arises from this
channel at second order.

## Proof / evidence

For a single-mode field $u_j=f_j(s)e^{im\phi}$,
$|\nabla u_j|^2=|f_j'|^2+m^2\rho_j^{-2}|f_j|^2$, so
$Q^{(m)}(f)=Q_{\mathrm{rad}}(f)+m^2Q_{\mathrm{ang}}(f)$ with
$m$-independent $Q_{\mathrm{rad}}$ (including the order-zero junction
term, since $\int_0^{2\pi}|e^{im\phi}|^2d\phi=2\pi$ for all $m$) and
$Q_{\mathrm{ang}}(f)=2\pi\sum_j\int|f_j|^2\rho_j^{-1}\,ds$; cross terms
between distinct $m$ vanish. For identical radial profiles,
$Q^{(2)}(f)-Q^{(1)}(f)=3\sum_j\int|f_j|^2\rho_j^{-2}\,d\mu_j$.
Uniform stability: for $v\in[0.05,0.30]$ the exterior fraction is
$1-2v\in[0.40,0.90]\ge 0.10$, so by the Cotton-Freeman theorem the
equal-volume standard bubble is the global isoperimetric minimizer,
hence stable: $Q_v\ge 0$ on all admissible volume-preserving fields. The
transplanted $|m|=1$ field $f_j(s)e^{i\phi}$ is admissible
(volume-automatic, junction-preserved), so $Q^{(1)}(f)\ge 0$. The
pole-regularity mismatch (generic $O(\rho^2)$ quadrupole profiles are
only $C^1$ as $m=1$ fields) is repaired by $H^1$-density of profiles
vanishing near poles, using $H^1$-continuity of $Q^{(1)}$ (bounded $V$,
order-zero trace-continuous $B$). Finally, with $\rho_j\le 1$ so
$\rho_j^{-2}\ge 1$ (regular at poles by $O(\rho^2)$ vanishing),
$Q(u)-Q(\tilde u)=3\sum_j\int|f_j|^2\rho_j^{-2}\,d\mu_j
\ge 3\lVert u\rVert^2$ with $\lVert u\rVert=\lVert\tilde u\rVert$.
Hence $Q_v(u)\ge 3\lVert u\rVert^2\ge \tfrac1{10}\lVert u\rVert^2$
uniformly. The script `output/artifacts/verify_target.py` prints
`VERIFY_OK`: exterior fractions $\{0.90,\dots,0.40\}\ge 0.10$,
Fourier orthogonality, automatic volume preservation, and the
mode-difference identity on two model profiles (ratios $\approx 5.68$
and $10.26\ge 1$).

## Limitations

The argument uses the Cotton-Freeman equal-volume minimality theorem
(exterior $\ge 10\%$) as a black box for the $Q\ge 0$ stability input;
junction $m$-independence relies on the standard order-zero
triple-line form with $\phi$-independent coefficients; the
$H^1$-density cutoff repair is a proof sketch rather than a quantified
cutoff estimate; the verification script illustrates structural
identities on model profiles and does not enclose any PDE eigenvalue.

## Reproducibility

Run `python3 output/artifacts/verify_target.py` (expects `VERIFY_OK`).
The full analytic proof is self-contained in the Result and Proof
sections above modulo the cited Cotton-Freeman black box.

## References

- A. Cotton and D. Freeman, The double bubble problem in spherical and
  hyperbolic space, Int. J. Math. Math. Sci. 32 (2002), 641-699
  (equal-volume minimality with exterior $\ge 10\%$).
- E. Milman and J. Neeman, The structure of isoperimetric bubbles on
  $\mathbb{R}^n$ and $\mathbb{S}^n$, Acta Math. 234 (2025), 71-188,
  arXiv:2205.09102 (structural minimality, no sector spectra).
- G. Di Matteo, Nondegeneracy of standard double bubbles, Proc. AMS
  147 (2019) (Euclidean Fourier-ODE template, qualitative kernel only).
