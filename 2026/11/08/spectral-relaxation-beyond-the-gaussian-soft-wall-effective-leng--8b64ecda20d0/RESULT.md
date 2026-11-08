# Spectral relaxation beyond the Gaussian soft-wall effective length

## Finding

For fixed \(L,\kappa_-,\kappa_+>0\), consider a one-dimensional Brownian diffusion with noise intensity \(T>0\) and a flat-bottom quadratic confining potential
\[
V(x)=\begin{cases}
\kappa_-x^2/2,&x<0,\\
0,&0\le x\le L,\\
\kappa_+(x-L)^2/2,&x>L.
\end{cases}
\]
Write \(\lambda_1(T)\) for the smallest strictly positive eigenvalue of the negative infinitesimal generator in the stationary weighted \(L^2\) space. Define
\[
C=\sqrt{\pi/2}(\kappa_-^{-1/2}+\kappa_+^{-1/2}),\qquad
B=\sqrt{\pi/2}(\log 2-\pi/6)(\kappa_-^{-3/2}+\kappa_+^{-3/2}).
\]
Then \(B>0\), and the exact stationary partition function is \(Z_T=L+C\sqrt T\). As \(T\downarrow0\),
\[
\boxed{\lambda_1(T)=\frac{\pi^2T}{Z_T^2}-\frac{2\pi^4B}{L^5}T^{5/2}+O_{L,\kappa_-,\kappa_+}(T^3).}
\]
Thus stationary mass alone predicts the eigenvalue through order \(T^2\), but systematically overestimates it at order \(T^{5/2}\). In the metric-projection case \(\kappa_-=\kappa_+=1\), the stationary effective length is exactly \(L+\sqrt{2\pi T}\), with the same strictly negative additional correction.

## Assumptions and scope

The stochastic differential equation is \(dX_t=-V'(X_t)\,dt+\sqrt{2T}\,dW_t\) on the entire real line, with \(W\) standard one-dimensional Brownian motion. The potential is continuously differentiable with globally Lipschitz derivative, and is zero on \([0,L]\). The invariant probability is
\[
\pi_T(dx)=Z_T^{-1}e^{-V(x)/T}\,dx,
\quad Z_T=\int_{\mathbb R}e^{-V(x)/T}\,dx=L+C\sqrt T.
\]
The generator is \(\mathcal L_T=T\partial_x^2-V'(x)\partial_x\). It is symmetric on \(L^2(\pi_T)\), with Dirichlet form \(T\int |f'|^2d\pi_T\). All three geometric parameters are fixed while \(T\) tends to zero; the remainder constant may depend on them. The theorem is about the smallest nonzero \(L^2(\pi_T)\) eigenvalue, not a claimed total-variation mixing-time identity.

## Proof

**Discrete spectrum and nodal characterization.** Conjugating \(-\mathcal L_T\) by multiplication with \(e^{-V/(2T)}\) gives the one-dimensional Schrödinger operator \(-T\partial_x^2+V'(x)^2/(4T)-V''(x)/2\), with locally bounded potential quadratic and tending to infinity at both ends. Its resolvent is compact. The ground state is the positive constant before conjugation, with eigenvalue zero. By the one-dimensional Sturm oscillation theorem, the first nonconstant eigenfunction has exactly one real zero. Since \(V\) is \(C^1\), eigenfunctions and their first derivatives match continuously at the two soft-wall interfaces.

**Exact Gaussian tail logarithmic derivative.** Let \(\lambda=Tk^2\) and \(\nu_j=\lambda/\kappa_j\), for \(j\in\{-,+\}\). In the appropriate outward coordinate \(y=\sqrt{\kappa_j/T}\,\operatorname{dist}(x,[0,L])\), the eigenfunction satisfies
\[
g''-yg'+\nu_jg=0.
\]
The unique square-integrable solution against \(e^{-y^2/2}dy\) at infinity, up to scale, is \(g_{\nu}(y)=e^{y^2/4}D_\nu(y)\), where \(D_\nu\) is the parabolic-cylinder function. Its boundary logarithmic derivative equals
\[
Q(\nu)=\frac{g_\nu'(0)}{g_\nu(0)}
=\frac{\nu}{\sqrt2}\frac{\Gamma((1-\nu)/2)}{\Gamma(1-\nu/2)}
=\sqrt{\pi/2}\,\nu\big[1+\nu\log2+O(\nu^2)\big].
\]
The gamma expression follows from the standard origin values of \(D_\nu\); the expansion uses \(\psi(1/2)-\psi(1)=-2\log2\). For sufficiently small positive \(\nu\), the tail solution is strictly positive for \(y\ge0\). One direct check uses \(D_\nu(y)=yD_{\nu-1}(y)+(1-\nu)D_{\nu-2}(y)\) and the positive integral representations of \(D_{-a}(y)\), \(a>0\), for \(0<\nu<1\).

**Exact matching equation.** On \([0,L]\), eigenfunctions solve \(f''+k^2f=0\). Writing
\[
 r_j(k,T)=\frac{1}{k}\sqrt{\frac{\kappa_j}{T}}\,Q(Tk^2/\kappa_j),
\]
the outward tail solutions give Robin ratios \(f'(0)/f(0)=-kr_-(k,T)\) and \(f'(L)/f(L)=kr_+(k,T)\). These are equivalent, for the root near \(k=\pi/L\), to the exact phase equation
\[
kL+\arctan r_-(k,T)+\arctan r_+(k,T)=\pi.
\]
The implicit function theorem gives a unique root \(k(T)\) near \(\pi/L\). For sufficiently small \(T\), its inside eigenfunction is proportional to \(\cos(kx+\arctan r_-)\), with one zero in \((0,L)\). The exterior solutions have no zeros, so this is exactly the first positive eigenvalue, rather than merely a candidate eigenvalue.

**Three-term boundary phase.** Uniformly for \(k\) near \(\pi/L\), Taylor expansion of the gamma quotient and the inverse tangent yields
\[
\arctan r_j(k,T)=k\sqrt{\frac{\pi}{2\kappa_j}}\sqrt T
+k^3\sqrt{\frac\pi{2\kappa_j^3}}(\log2-\pi/6)T^{3/2}+O(T^{5/2}).
\]
Summing and using the root equation gives
\[
k(L+C\sqrt T)+Bk^3T^{3/2}=\pi+O(T^{5/2}).
\]
Let \(k_0=\pi/(L+C\sqrt T)\). The phase derivative with respect to \(k\) is \(L+O(\sqrt T)\), so
\[
k=k_0-\frac{Bk_0^3}{L+C\sqrt T}T^{3/2}+O(T^{5/2}).
\]
Squaring, multiplying by \(T\), and replacing the remaining \(L+C\sqrt T\) denominators in the order-\(T^{5/2}\) term by \(L\) introduces only \(O(T^3)\). This is precisely the displayed spectral expansion. Finally, \(\log2>2/3>\pi/6\), proving \(B>0\) (the first inequality follows from the positive series for \(\log 2=2\operatorname{artanh}(1/3)\)).

## Verification

Run `python check_spectrum.py` with Python 3.9 or newer and the public Python package `mpmath`. The script evaluates the exact parabolic-cylinder matching equation for five pairs of wall stiffnesses/interval lengths and six positive temperatures each; it tests the effective-width and refined \(T^{5/2}\) formulas, residuals of the secular equation, independent gamma/parabolic-cylinder origin derivatives and the gamma-quotient Taylor expansion. The included test suite gave **125 passed numerical assertions** at 75-digit working precision. These checks detect normalization or sign errors but are not substituted for the infinite-dimensional proof above.

## Relationship to prior work

Darapaneni (2026) studies exactly the unit-stiffness metric-projection diffusion (and arbitrary compact convex sets) and supplies the Gibbs law, reflected-Brownian weak limit and mixing-time bounds of order \(T^{-1}\) up to a logarithm. Its discussion explicitly asks whether the logarithmic mixing factor is necessary. The present theorem concerns a distinct spectral invariant and gives a higher-order expansion for one-dimensional intervals, including asymmetric wall stiffness; neither the reflected limit nor a coarse mixing bound determines its \(T^{3/2}\), \(T^2\), or \(T^{5/2}\) coefficients. The parabolic-cylinder and gamma-function identities used in the proof are standard, not claimed as new. Related one-dimensional diffusion spectral theory could potentially yield equivalent formulas and needs independent historical-priority review.

## Limitations

The result is for fixed positive interval length, fixed positive wall stiffnesses, and vanishing positive temperature. It does not cover higher-dimensional convex sets, simultaneous degeneracy of the wall stiffnesses, arbitrary nonquadratic exterior confinement, total-variation cutoff, or a universal mixing bound. The exact secular equation and asymptotics have not undergone independent mathematical audit; finite-precision tests do not certify the analytic proof or historical originality.

## References

1. N. Darapaneni, *Zero temperature versus long time for diffusions driven by metric projections onto convex sets*, arXiv:2610.35145v1 (first public submission 26 October 2026), https://arxiv.org/abs/2610.35145 .
2. NIST Digital Library of Mathematical Functions, Chapter 12, §12.1 and §12.2(ii), parabolic-cylinder notation and values at the origin, https://dlmf.nist.gov/12.2 .
3. NIST Digital Library of Mathematical Functions, Chapter 12, recurrence relations and asymptotic behavior, https://dlmf.nist.gov/12.8 and https://dlmf.nist.gov/12.9 .
