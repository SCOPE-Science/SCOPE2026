# Sharp zero-intensity tails at infinitely flat spectral edges

## Finding

Let \(S\in L^\infty(\mathbb R)\) be a nonzero, nonnegative power spectral density, supported in a compact interval \([a,b]\) with \(a<b\). Consider stationary circular complex Gaussian noise and the short-time Fourier transform with unit-normalized Gaussian window \(\varphi(t)=2^{1/4}e^{-\pi t^2}\). Write \(\rho_S(\omega)\) for the expected density of spectrogram zeros per unit time and unit frequency. The density is independent of time.

Define the spectral-edge condition at \(b\) using \(u=b-x\). In the *infinitely flat* case, suppose that for some \(\delta>0\), \(\alpha\ge0\), \(\kappa>0\), \(\beta>0\) and positive function \(h\) on \((0,\delta)\), continuous at zero with \(h(0)>0\),
\[
S(b-u)=u^\alpha h(u)\exp(-\kappa/u^\beta),\qquad 0<u<\delta.
\]
Then, as \(R\to\infty\),
\[
\boxed{\rho_S(R)\sim \frac{1}{\beta+1}\left(\frac{\kappa\beta}{4\pi}\right)^{\!1/(\beta+1)}R^{-(\beta+2)/(\beta+1)}},
\]
and the total expected zero intensity beyond \(R\), per unit time, satisfies
\[
\boxed{\int_R^\infty\rho_S(\omega)\,d\omega\sim
\left(\frac{\kappa\beta}{4\pi R}\right)^{\!1/(\beta+1)}}.
\]
These leading terms depend only on the infinitely flat cutoff, not on \(\alpha\), \(h\), the opposite edge, or the interior of the spectrum. Identical formulas hold at \(a\) for \(\rho_S(-R)\) and \(\int_{-\infty}^{-R}\rho_S\), with the parameters of the left edge.

For comparison, if instead \(S(b-u)=u^\alpha h(u)\) with \(\alpha\ge0\) and \(h(0)>0\), the algebraic-edge law is
\[
\rho_S(R)\sim\frac{\alpha+1}{4\pi R^2},\qquad
\int_R^\infty\rho_S(\omega)\,d\omega\sim\frac{\alpha+1}{4\pi R}.
\]
The corresponding formulas hold independently at the left edge. These are comparison baselines; the distinguishing result here is the continuously varying sharp exponent and coefficient for infinitely flat cutoffs.

Irrespective of edge regularity (provided \(a,b\) are the essential extreme support points), the exact mass identity is
\[
\boxed{\int_{-\infty}^\infty\rho_S(\omega)\,d\omega=b-a}.
\]
In the infinitely flat regime the observed tail exponent \(\gamma\in(1,2)\) and leading coefficient \(C>0\) identify the edge parameters by
\[
\beta=\frac{2-\gamma}{\gamma-1},\qquad
\kappa=\frac{4\pi}{\beta}\bigl((\beta+1)C\bigr)^{\beta+1}.
\]
This is a population-intensity identifiability statement, not a finite-sample statistical guarantee.

## Assumptions and scope

All formulas concern **pure stationary, circular complex Gaussian noise**, not a deterministic signal superimposed on noise. The power spectral density \(S\) is a measurable, bounded, nonzero function supported in the specified compact interval. The edge equalities above are assumed almost everywhere on some interval of positive length next to the relevant endpoint. No smoothness inside \((a,b)\), nor connectedness of the interior support, is required. The two endpoints can have different edge types and independent parameters. The integral of \(\rho_S\) is per unit time; integrating over any time interval of length \(L\) multiplies the mean number of zeros by \(L\).

## Proof

**1. Exact tilted-variance identity.** By the pure-noise specialization of the established Gaussian-spectrogram first-intensity formula [1], put
\[
F(\omega)=\int_{a}^{b}e^{-2\pi(\omega-x)^2}S(x)\,dx,
\quad
\rho_S(\omega)=1+\frac{1}{4\pi}(\log F)''(\omega).
\]
Let \(\mu_\omega\) be the probability measure on \([a,b]\) with density proportional to \(S(x)e^{-2\pi(\omega-x)^2}\); let \(m(\omega)=\mathbb E_{\mu_\omega}X\). Since the support is bounded, differentiation under the integral is justified at every finite \(\omega\). Direct differentiation yields
\[
(\log F)'(\omega)=4\pi(m(\omega)-\omega),\quad
m'(\omega)=4\pi\operatorname{Var}_{\mu_\omega}(X),\quad
\boxed{\rho_S(\omega)=m'(\omega)=4\pi\operatorname{Var}_{\mu_\omega}(X)}.
\]
In particular the intensity is nonnegative, and positive unless the underlying spectral measure is concentrated at a single point (impossible for a nonzero bounded density).

**2. Exact total mass and tail identities.** The tilted measure can equally be written as
\[
\mu_\omega(dx)=\frac{e^{4\pi\omega x-2\pi x^2}S(x)\,dx}{\int_a^b e^{4\pi\omega y-2\pi y^2}S(y)\,dy}.
\]
The exponential tilt concentrates at the essential right endpoint \(b\) as \(\omega\to+\infty\) and at the essential left endpoint \(a\) as \(\omega\to-\infty\), hence \(m(+\infty)=b\) and \(m(-\infty)=a\). Integrating the exact derivative identity gives the bandwidth mass. It also gives, for every \(R>0\), the *exact* tail identities
\[
\int_R^\infty\rho_S(\omega)\,d\omega=b-m(R)=\mathbb E_{\mu_R}(b-X),\qquad
\int_{-\infty}^{-R}\rho_S(\omega)\,d\omega=m(-R)-a.
\]

**3. Endpoint reduction.** For the upper edge set \(U=b-X\), \(t=4\pi R\), and \(q(u)=e^{-2\pi(b-u)^2}S(b-u)\). The tilted law of \(U\) at frequency \(R\) is proportional to \(q(u)e^{-tu}\,du\), for \(0\le u\le b-a\). Thus the desired intensity is \(4\pi\operatorname{Var}(U)\), while the integrated tail is \(\mathbb E U\). The contribution from any fixed interval \(u\ge\delta>0\) is exponentially negligible compared with the endpoint contribution, in both edge regimes below.

**4. Algebraic edge.** If \(q(u)=u^\alpha\widetilde h(u)\), with \(\widetilde h(0)>0\), Watson's elementary endpoint substitution \(v=tu\) gives, for \(k=0,1,2\),
\[
\int_0^{b-a}u^kq(u)e^{-tu}\,du\sim
\widetilde h(0)\Gamma(\alpha+k+1)t^{-\alpha-k-1}.
\]
Taking ratios yields \(\mathbb E U\sim(\alpha+1)/t\) and \(\operatorname{Var}(U)\sim(\alpha+1)/t^2\). Inserting \(t=4\pi R\) proves both algebraic formulas.

**5. Infinitely flat edge and its nonstandard concentration scale.** Now
\[
q(u)=u^\alpha\widetilde h(u)e^{-\kappa/u^\beta},\qquad
\widetilde h(u)=e^{-2\pi(b-u)^2}h(u),\quad \widetilde h(0)>0.
\]
The Laplace phase \(\Phi_t(u)=tu+\kappa u^{-\beta}\) has exactly one minimum at
\[
u_t=(\kappa\beta/t)^{1/(\beta+1)},\qquad
\Phi_t''(u_t)=(\beta+1)t/u_t.
\]
Its natural fluctuation width is
\[
\sigma_t=\sqrt{\frac{u_t}{(\beta+1)t}},\quad
\frac{\sigma_t}{u_t}=\big((\beta+1)tu_t\big)^{-1/2}\longrightarrow0.
\]
To verify *variance*, rather than only localization, set \(u=u_t+\sigma_t z\). Uniformly on each fixed bounded \(z\)-interval, Taylor expansion at the minimum gives
\[
\Phi_t(u_t+\sigma_t z)-\Phi_t(u_t)=\tfrac12z^2+o(1),
\qquad
\frac{(u_t+\sigma_t z)^\alpha\widetilde h(u_t+\sigma_t z)}{u_t^\alpha\widetilde h(u_t)}\longrightarrow1.
\]
The convex rescaling \(\Phi_t(u_t v)=tu_t(v+v^{-\beta}/\beta)\), with \(tu_t\to\infty\), has a unique nondegenerate minimum at \(v=1\). On a fixed neighborhood of \(1\) it supplies a uniform Gaussian bound in \(z\); outside that neighborhood the phase has a positive gap, while \(v\to0\) and \(v\to\infty\) have still stronger suppression. Together with boundedness of \(q\) away from the endpoint, these bounds justify convergence of the normalized zeroth, first, and second centered \(z\)-moments. Consequently
\[
\mathbb E U=u_t(1+o(1)),\qquad
\operatorname{Var}(U)=\sigma_t^2(1+o(1))
=\frac{(\kappa\beta)^{1/(\beta+1)}}{\beta+1}
 t^{-(\beta+2)/(\beta+1)}(1+o(1)).
\]
The exact identities from steps 1–2 and \(t=4\pi R\) give the stated sharp constants and exponents. Reflecting the spectral coordinate, \(x\mapsto-x\), proves every left-edge assertion. The inversion of exponent and coefficient is simple algebra.

## Verification

A standalone script `CHECK.py` numerically integrates the exact exponentially tilted spectral moments for the bounded compactly supported example
\[
S(x)=x^2\exp\!\left(-\frac1{(1-x)^\beta}\right)\mathbf1_{(0,1)}(x).
\]
For \(\beta\in\{1/2,1,2\}\), its right edge is infinitely flat with \(\kappa=1\), while its left edge is algebraic of order \(\alpha=2\). The script compares directly computed variances and endpoint means against the sharp predicted constants, and checks the exact derivative/variance identity by centered differences. It returns `EDGE_ZERO_TAIL_CHECKS_PASSED` with SciPy installed. These finite numerical tests are corroboration only; step 5 supplies the unrestricted asymptotic proof.

## Relationship to prior work

Escudero, Koliander, and Romero [1] give the Gaussian-spectrogram zero first-intensity formula used in step 1. Their slow-spectrum asymptotic assumes a positive, globally supported sub-Gaussian lower bound, so it does not establish the compact, infinitely flat spectral-edge regime. Feldheim [2], extending classical Wiener and Edelman–Kostlan formulas, gives a general zero-intensity formula for stationary Gaussian entire functions and explicitly treats the constant-density Paley–Wiener spectral interval. Thus the general derivative identity, total mass obtained by integrating it, and flat *algebraic-order-zero* boxcutoff are **not** claimed to be new. The distinguishing result is the precise infinitely flat edge asymptotic, including its continuum of tail exponents, exact constants, sharp integrated tail, and the edge-parameter recovery law. The proof requires the additional saddle concentration and variance analysis in step 5. Related spectral-equivalence results for equal full intensity profiles do not determine these edge asymptotics.

## Limitations

The results concern only the **population first intensity** of zeros of a pure-noise Gaussian-window spectrogram. They do not establish statistical rates for finite observations, the full distribution of the zero point process, or stability in recovering spectral-edge parameters from noisy intensity estimates. A more general old stationary-analytic-function result might imply an equivalent edge asymptotic after a nonobvious reduction; this remains the principal publication-priority risk. Weights with rapidly oscillatory or nonconvergent endpoint profiles need not satisfy the stated hypotheses; no general tail law is claimed for them.

## References

[1] L. A. Escudero, G. Koliander, and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689 (first public version 2026-09-16), Theorem 1.1 and Section 4, https://arxiv.org/abs/2609.18689.

[2] N. Feldheim, *Zeroes of Gaussian Analytic Functions with Translation-Invariant Distribution*, arXiv:1105.3929 (first public 2011), Theorem 1, equation (4), and Section 3.1, https://arxiv.org/abs/1105.3929.
