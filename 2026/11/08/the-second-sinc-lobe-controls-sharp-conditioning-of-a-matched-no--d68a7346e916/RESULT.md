# The second sinc lobe controls sharp conditioning of a matched nonlocal diffusion preconditioner

## Finding
Let \(\rho(z)=1/2\) for \(|z|\le1\) and zero otherwise. For the translation-invariant one-dimensional nonlocal diffusion operator with horizon \(\delta>0\), set the comparison inverse preconditioner \(B_\delta=3(-\partial_{xx})^{-1}+\delta^2I/2\) on nonzero Fourier frequencies. The preconditioned multiplier is
\[
F(t)=\left(1-\frac{\sin t}{t}\right)\left(1+\frac6{t^2}\right),\qquad t=\delta|\xi|>0,
\]
with continuous endpoint \(F(0)=1\) and limiting value \(1\) as \(t\to\infty\). Define
\[
N(t)=(t^2+18)\sin t-t(t^2+6)\cos t-12t.
\]
The unique global maximum occurs at the unique root \(t_+\in(\pi,3\pi/2)\) of \(N\). The unique global minimum occurs at the unique root \(t_-\in(4\pi,9\pi/2)\). Explicit enclosed intervals and approximate values are
\[
3.7141548<t_+<3.7141551,\quad F(t_+)\approx1.644258263597434,
\]
\[
14.1206451<t_-<14.1206455,\quad F(t_-)\approx0.957152026310063.
\]
Thus the exact best frequency-uniform spectral-equivalence condition number is
\[
\kappa_*=\frac{F(t_+)}{F(t_-)}\approx1.71786531125703.
\]
In particular, the smallest multiplier occurs in the second positive-sine lobe \((4\pi,5\pi)\), not the first \((2\pi,3\pi)\). All extrema are independent of \(\delta\).

## Assumptions and scope
For Schwartz functions with Fourier support bounded away from zero, define the real symmetric energy operator via
\[
\mathfrak a_\delta(u,u)=\delta^{-3}\int_{\mathbb R}\int_{|y-x|<\delta}\frac12|u(y)-u(x)|^2\,dy\,dx.
\]
Its multiplier is \(a_\delta(\xi)=2\delta^{-2}(1-\sin(\delta\xi)/(\delta\xi))\). The preconditioner \(B_\delta\) has multiplier \(3/|\xi|^2+\delta^2/2\). Multiplying yields \(F\) above. The constant \(3\) matches the low-frequency diffusion coefficient, and the mass coefficient \(1/2\) matches the high-frequency inverse limit for the unit-mass box kernel. The nonzero frequency continuum is important: a finite periodic grid may not sample either extremizing frequency. Bounds concern the whole-space Fourier symbol; neither bounded-domain boundary conditions nor finite-element mass lumping are identified with this model.

## Proof
Differentiate directly:
\[
F'(t)=\frac{N(t)}{t^4},\quad N'(t)=(12-2t^2)\cos t+(t^3+8t)\sin t-12,
\]
\[
N''(t)=(t^3+4t)\cos t+(5t^2-4)\sin t.
\]
For \(t\in(\pi,3\pi/2)\), \(N''<0\), and \(N'(\pi)=2\pi^2-24<0\). Moreover \(N(\pi)=\pi(\pi^2-6)>0\), while \(N(3\pi/2)<0\). Hence there is exactly one zero, changing \(F'\) from positive to negative. On \((3\pi/2,2\pi)\), both \(\sin t\) and \(-\cos t\) are negative; therefore \(N<0\). Thus \(t_+\) is the unique maximizer over \([\pi,2\pi]\).

For \(0<t\le3/2\), the elementary alternating-series inequality \(\sin t\ge t-t^3/6\) gives \(F(t)\le1+t^2/6\le11/8<1.62\). For \(3/2\le t\le\pi\), the derivative bound
\[
|F'(t)|\le\left(\frac1t+\frac1{t^2}\right)\left(1+\frac6{t^2}\right)+\left(1+\frac1t\right)\frac{12}{t^3}\le10.1
\]
combined with a uniform outward-interval grid of \(20{,}000\) subdivisions establishes \(F(t)<1.62\); the actual verified upper bound including grid-cover radius is \(1.608342\). Finally, for \(t\ge2\pi\), \(F(t)\le(1+1/t)(1+6/t^2)\le(1+1/(2\pi))(1+6/(4\pi^2))<1.34\). Since \(F(t_+)>1.64425\), the first root is the unique global maximum.

For the global minimum, on \(0<t<\pi\) use \(\sin t\le t-t^3/6+t^5/120\). Since \(\pi^2<14\), multiplication by \(t^2+6\) proves \((t^2+6)\sin t\le6t\), hence \(F(t)\ge1\). On \((\pi,2\pi)\) and \((3\pi,4\pi)\), \(\sin t<0\), and thus \(F(t)>1\). On \([2\pi,3\pi]\), the same derivative bound is less than \(0.30\); a \(20{,}000\)-subdivision outward-interval grid, including the covering-radius correction, rigorously gives \(F(t)>0.957484\).

On \((4\pi,9\pi/2)\), \(N''>0\), \(N(4\pi)<0\), and \(N(9\pi/2)>0\), hence exactly one zero \(t_-\) (convexity and a negative starting value rule out two positive crossings). On \([9\pi/2,5\pi]\), \(N>0\): if \(-\cos t\ge1/2\), the term \(-t(t^2+6)\cos t\) exceeds \(12t\); otherwise \(\sin t\ge\sqrt3/2\), and \((t^2+18)\sin t>12t\). Therefore \(t_-\) is the unique minimizer in \([4\pi,5\pi]\). A direct enclosed evaluation at \(t=14.12\) yields \(F(14.12)<0.9572\), strictly below the certified first-lobe floor.

For \(t\ge5\pi\), use \(\sin t\le1\) to obtain \(F(t)\ge H(t)=(1-1/t)(1+6/t^2)\). The derivative \(H'(t)=(t^2-12t+18)/t^4\) is positive there, and \(H(5\pi)>0.95910>F(t_-)\). All other intervals have just been excluded. This proves both global extrema and their uniqueness. The spectral condition number is their ratio because Fourier multiplication by \(F\) is positive and self-adjoint.

## Verification
Run \(\texttt{python check.py}\) with the publicly available \(\texttt{mpmath}\) package. It uses outward-rounded interval evaluations of \(\sin\) and \(\cos\), analytic global derivative envelopes, and finite covering radii. The checks enclose the signs of \(N\) at both roots, provide rigorous margin separation between the first and second positive sine lobes, verify the far-frequency tail, and independently recompute the Fourier multiplier. The proof supplies global monotonicity and interval exclusions; the finite grid alone is not being treated as an infinite proof.

## Relationship to prior work
Lu, Nie, Zhang and Zhang (2026) establish mesh- and horizon-independent spectral equivalence for additive local-Poisson-plus-mass preconditioning of nonlocal diffusion and motivate the kernel-mass coefficient. Their continuum estimates do not identify the sharp extrema of the present one-dimensional uniform-kernel Fourier multiplier. Earlier work on two-level Toeplitz \(\tau\)-preconditioners studies a different discrete construction; its general spectral interval does not imply the precise whole-space second-lobe selection or value of \(\kappa_*\). This is a specialization to a calibrated Fourier model, not a claimed replacement of the cited finite-element robustness theorem.

## Limitations
The exact constant belongs only to a translation-invariant one-dimensional uniform box kernel with the explicitly matched multiplier \(3/|\xi|^2+\delta^2/2\). It does not certify a sharp condition number for a finite mesh, bounded-domain discretization, practical multigrid approximation, or other kernel shapes. Historical priority for a previously unindexed equivalent sinc-extremum computation remains a possibility; numerical brackets depend on the stated interval program and its mpmath arithmetic.

## References
- J. Lu, Y. Nie, H. Zhang, P. Zhang, *A mesh- and horizon-robust preconditioner for finite element discretizations of volume-constrained nonlocal diffusion problems*, arXiv:2609.24143, submitted 2026-09-21, https://arxiv.org/abs/2609.24143.
- J. Zhang, T. Sun, H. Sun, J. Zhang, *Spectral Analysis of τ-Preconditioners for Two-Level Toeplitz Systems with Applications in Nonlocal Diffusion Models*, Journal of Scientific Computing 106 (2026), article 21, https://doi.org/10.1007/s10915-025-03150-2.
