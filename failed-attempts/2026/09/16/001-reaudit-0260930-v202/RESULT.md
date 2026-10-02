# Arithmetic no-point-spectrum window for the kappa=2 mosaic almost-Mathieu operator

## Setup

Consider the kappa=2 mosaic operator
\[
(H_{\lambda,\alpha,\theta}u)_n=u_{n+1}+u_{n-1}+V_nu_n,
\qquad
V_{2m}=2\lambda\cos 2\pi(\theta+2m\alpha),\quad V_{2m+1}=0,
\]
with irrational \(\alpha\) and \(\lambda\ne0\).  Write
\[
\beta(\omega)=\limsup_{q\to\infty}-\frac{\log\|q\omega\|_{\mathbb R/\mathbb Z}}q.
\]
Assume \(0<\beta(\alpha)<\infty\).

## Exact two-step reduction

For \(E\ne0\), group the transfer matrices in pairs.  If
\[
A(\varphi)=\begin{pmatrix}E-2\lambda\cos(2\pi\varphi)&-1\\1&0\end{pmatrix},
\qquad
B=\begin{pmatrix}E&-1\\1&0\end{pmatrix},
\]
then with
\[
P=\begin{pmatrix}1&0\\-1&E\end{pmatrix}
\]
one has the exact identity
\[
PBA(\varphi)P^{-1}
=
\begin{pmatrix}
E^2-2-2\lambda E\cos(2\pi\varphi)&-1\\
1&0
\end{pmatrix}.
\]
Thus the even-sublattice equation is an almost-Mathieu equation with frequency \(2\alpha\), effective coupling \(\lambda_{\rm eff}=\lambda E\), and effective spectral parameter \(E'=E^2-2\).

On spectral energies this also gives the familiar mosaic Lyapunov exponent
\[
L_{\rm mosaic}(E)=\frac12\max\{0,\log|\lambda E|\}.
\]

## Arithmetic exponent under frequency doubling

The elementary inequalities
\[
\beta(\alpha)\le \beta(2\alpha)\le2\beta(\alpha)
\]
hold.  For the upper bound use \(\|2q\alpha\|=\|q(2\alpha)\|\) and compare the limsup along the subsequence \(2q\).  For the lower bound, along a sequence realizing \(\beta(\alpha)\), use \(q/2\) when q is even and \(\|2q\alpha\|\le2\|q\alpha\|\) when q is odd.

## Corrected theorem

Define the open arithmetic window
\[
W=\{E\ne0:1<|\lambda E|<e^{\beta(2\alpha)}\}.
\]
Then for **every phase \(\theta\)**, the mosaic operator has no \(\ell^2\) eigenvalue in \(W\).

Indeed, an eigenfunction at \(E\in W\) would induce an \(\ell^2\) solution of the effective almost-Mathieu equation with frequency \(2\alpha\) and coupling satisfying
\[
1<|\lambda_{\rm eff}|<e^{\beta(2\alpha)}.
\]
The sharp frequency-arithmetic transition theorem for the almost-Mathieu operator places this regime on the singular-continuous side and in particular excludes point spectrum.

Since the mosaic Lyapunov exponent is positive on \(W\), standard Kotani/Ishii-Pastur theory excludes absolutely continuous spectrum in the ergodic sense; consequently, for the phases for which that conclusion is applied, any spectral mass in \(W\) is singular continuous.  The all-phase statement asserted here is only the no-point-spectrum conclusion above.

## Important limitation

This record does **not** prove that \(W\cap\sigma(H_{\lambda,\alpha,\theta})\) is nonempty for an arbitrary \((\lambda,\alpha)\). Therefore the theorem by itself is not a counterexample to a localization statement unless one separately verifies that the proposed energy window actually intersects the spectrum.  What it proves unconditionally is the arithmetic absence of eigenvalues at every spectral energy that lies in \(W\).

## Reproducibility

`artifacts/mosaic_window.py` now checks the exact two-step matrix identity numerically and constructs finite continued-fraction approximants whose next-denominator growth illustrates a prescribed positive arithmetic exponent.  It explicitly labels all finite approximants as rational and does **not** report a finite-sample value as \(\beta(\alpha)\).  `artifacts/mosaic_window.json` records those finite-scale checks.

## References

- A. Avila, J. You, Q. Zhou, *Sharp phase transitions for the almost Mathieu operator*, Duke Math. J. 166 (2017), 2697–2718, arXiv:1512.03124.
- W. Liu, *Distributions of Resonances of Supercritical Quasi-Periodic Operators*, IMRN 2024 (2024), 197–233.
- Y. Wang et al., *One-Dimensional Quasiperiodic Mosaic Lattice with Exact Mobility Edges*, Phys. Rev. Lett. 125 (2020), 196604.
- J. He, Y. Shan, Y. Wang, *Cantor Spectrum via a Reducibility-Duality Bridge for the Mosaic Almost Mathieu Operator*, arXiv:2606.23422.
