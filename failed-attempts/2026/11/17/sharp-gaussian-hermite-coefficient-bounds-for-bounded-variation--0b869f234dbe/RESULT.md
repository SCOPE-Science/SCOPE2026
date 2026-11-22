# Sharp Gaussian Hermite coefficient bounds for bounded-variation data, with parity-dependent corrections

## Finding

Let \(\gamma\) be standard Gaussian probability measure on \(\mathbb R\), with density \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\), and let \(\operatorname{He}_n\) denote the probabilists' Hermite polynomial. Define the normalized coefficient
\[
  c_n(f)=\int_{\mathbb R}f(x)\,\frac{\operatorname{He}_n(x)}{\sqrt{n!}}\,d\gamma(x),\qquad n\geq1.
\]
For the class \(\mathcal V\) of real functions having finite total variation on the whole real line (not necessarily integrable with respect to Lebesgue measure), set
\[
 M_n=\sup_{f\in\mathcal V,\;0<\operatorname{Var}(f)\leq1}|c_n(f)|.
\]
(The zero-variation constants are immaterial, as every positive-degree Hermite polynomial has Gaussian mean zero.) Then the following hold for every integer \(n\geq1\).

1. For odd \(n=2k+1\),
\[
 M_{2k+1}=\frac{1}{\sqrt{2\pi(2k+1)}}\sqrt{\frac{\binom{2k}{k}}{4^k}}.
\]
Among single-jump inputs, the sole maximizing jump location is zero.

2. For even \(n=2k\), let \(t_n\) be the smallest positive zero of \(\operatorname{He}_n\). Then
\[
 M_n=\frac{\phi(t_n)|\operatorname{He}_{n-1}(t_n)|}{\sqrt{n!}}.
\]
Among single-jump inputs, the only maximizing jump locations are \(\pm t_n\).

3. Set \(K=2^{-1/4}\pi^{-3/4}\). The sharp norm has the parity-dependent asymptotics
\[
 M_n=K n^{-3/4}\begin{cases}
 1+\dfrac{1}{8n}+O(n^{-2}),&n\text{ odd},\\[3pt]
 1-\dfrac{\pi^2-2}{16n}+O(n^{-2}),&n\text{ even}.
 \end{cases}
\]
Moreover, along even degrees,
\[
 t_n=\frac{\pi}{2\sqrt n}-\frac{\pi}{8n^{3/2}}+O(n^{-5/2}).
\]
All suprema \(M_n\) are achieved by a unit-height half-line indicator with its jump at a maximizing location.

## Assumptions and scope

We use ordinary total variation on the full real line: \(\mathcal V\) consists of functions whose distributional derivatives are finite signed measures and which have bounded representatives. The variation is the total mass \(|Df|(\mathbb R)\). We do not impose Lebesgue \(L^1\) integrability; half-line indicators belong to this class. This differs from conventions defining \(BV(\mathbb R)\) as a subspace of \(L^1(\mathbb R)\). Every \(f\in\mathcal V\) is bounded, so its Gaussian coefficient is defined. We do not impose a Gaussian weighted variation or a norm controlling the additive constant. The index is a positive integer, and Hermite polynomials are normalized to be orthonormal in \(L^2(\gamma)\). The statement concerns each coefficient separately, not the full Hermite series projection norm.

## Proof

**Step 1: the exact coefficient-functional norm.** Put \(h_n=\operatorname{He}_n/\sqrt{n!}\). Rodrigues' formula gives
\[
 \int_t^\infty\phi(x)h_n(x)\,dx=\frac{\phi(t)\operatorname{He}_{n-1}(t)}{\sqrt{n!}}=:F_n(t).
\]
For \(\mu=Df\), the Stieltjes decomposition and the vanishing Gaussian mean of \(h_n\) give \(c_n(f)=\int F_n(t)\,d\mu(t)\). Fubini is valid because \(\mu\) is finite and \(h_n\phi\) is integrable. Consequently
\[
 |c_n(f)|\leq\|F_n\|_\infty\,|Df|(\mathbb R),
\]
with equality for \(f=\mathbf1_{[t,\infty)}\) at a maximizer of \(|F_n|\). Hence \(M_n=\|F_n\|_\infty\).

**Step 2: global maximizing jump locations.** Write \(y(x)=\phi(x)\operatorname{He}_{n-1}(x)\). Hermite differentiation yields
\[
 y'(x)=-\phi(x)\operatorname{He}_n(x),\qquad y''(x)+xy'(x)+ny(x)=0.
\]
Its Sonin-type energy \(E(x)=y(x)^2+y'(x)^2/n\) satisfies
\[
 E'(x)=-\frac{2x}{n}y'(x)^2.
\]
Thus \(E\) decreases strictly across every nondegenerate positive interval and is even in \(x\). At a critical point of \(y\), the energy is \(y^2\); because \(y\) tends to zero at infinity, successive positive critical amplitudes decrease strictly. For odd \(n\), \(y\) is even and the point zero is itself critical and globally maximal in modulus. For even \(n\), \(y\) is odd, vanishes at zero, and the first positive critical point is the smallest positive zero \(t_n\) of \(\operatorname{He}_n\), uniquely maximizing its modulus on the positive half-line. Reflection gives the two claimed locations. This argument also applies to \(n=1\) and \(n=2\).

**Step 3: exact odd coefficient.** The recurrence gives \(\operatorname{He}_{2k}(0)=(-1)^k(2k)!/(2^kk!)\). Inserting this into \(F_{2k+1}(0)\) gives the claimed central-binomial formula.

**Step 4: exact even coefficient and local asymptotics.** For even \(n\), \(y(0)=0\) and \(y'(0)=-\phi(0)\operatorname{He}_n(0)\ne0\). Define
\[
 z_n(s)=\frac{\sqrt n\,y(s/\sqrt n)}{y'(0)}.
\]
Then
\[
 z_n''(s)+\frac{s}{n}z_n'(s)+z_n(s)=0,\quad z_n(0)=0,\quad z_n'(0)=1.
\]
Variation of constants on every fixed compact interval yields, uniformly together with the first derivative,
\[
 z_n(s)=\sin s+\frac{w(s)}n+O(n^{-2}),\qquad
 w(s)=-\int_0^s\sin(s-u)u\cos u\,du.
\]
The first positive zero \(s_n\) of \(z_n'\) therefore tends to \(\pi/2\), with no earlier zero, and the implicit-function expansion yields
\[
 s_n=\frac\pi2+\frac{w'(\pi/2)}n+O(n^{-2})
 =\frac\pi2-\frac\pi{8n}+O(n^{-2}).
\]
Here \(w'(\pi/2)=-\pi/8\) and \(w(\pi/2)=1/4-\pi^2/16\), so
\[
 z_n(s_n)=1+\frac{1/4-\pi^2/16}{n}+O(n^{-2}).
\]
Since \(t_n=s_n/\sqrt n\) and \(M_n=\phi(0)|\operatorname{He}_n(0)|z_n(s_n)/\sqrt{n\,n!}\) in absolute value, the even-degree asymptotic follows.

**Step 5: both parity corrections.** Stirling's formula gives
\[
 \frac{\binom{2k}{k}}{4^k}=(\pi k)^{-1/2}\left(1-\frac1{8k}+O(k^{-2})\right).
\]
Substituting \(n=2k+1\) in Step 3 gives the odd correction \(1/(8n)\). Substituting \(n=2k\) in Step 4 gives the even prefactor correction \(-1/(8n)\), which combines with \(w(\pi/2)/n\) to produce \(-(\pi^2-2)/(16n)\). Both yield the constant \(K\).

## Verification

Run `python3 verify.py` (Python standard library only). It checks Hermite recurrence and differentiated identities with exact integer polynomials, independently finds every positive critical root and compares critical amplitudes for degrees 1 through 30, checks attainment by half-line steps, and compares the two-term parity asymptotics and even-root expansion at increasing degrees. These finite checks corroborate, but do not substitute for, the preceding unrestricted analytical argument.

## Relationship to prior work

The Hermite orthogonality and Rodrigues identities are classical and are specified in NIST DLMF §18.3. Krasikov (2004) studies extremal values of the physicists' Hermite polynomial under the *square-root Gaussian weight* \(e^{-x^2/2}\), with maxima in a distant turning-point region. The present coefficient problem instead has the **full Gaussian density** times a degree-shifted polynomial; its energy identity forces the maximizer into the central region. The two optimization problems are not equivalent by a change of Hermite normalization, and Krasikov's extremal statement does not imply the present localization or parity correction. Vemuri (2008) studies exponential decay of Hermite-function coefficients under Gaussian bounds on a function and its Fourier transform, not sharp Gaussian-polynomial coefficients under a BV seminorm.

A published Laguerre-coefficient BV result offers an analogous primitive-maximization technique for a different weight and polynomial family; its indexed summary does not supply a Hermite theorem. Such analogies motivate a direct overlap search but do not constitute priority certification. No claim is made that other unindexed sources cannot contain equivalent observations.

## Limitations

The statement is for one-dimensional standard Gaussian polynomial coefficients and the ordinary (unweighted) variation seminorm on globally finite-variation functions without a Lebesgue-integrability requirement. It does not address multivariate Gaussian chaos, generalized Gaussian weights, Hermite *functions* in Lebesgue \(L^2\), simultaneous bounds for many coefficients, or Hermite-series approximation errors. Novelty remains conditional on the accessible literature comparisons; independent external audit has not been performed.

## References

- I. Krasikov, *New Bounds on the Hermite Polynomials* (first public arXiv submission 2004-01-23), https://arxiv.org/abs/math/0401310 .
- M. K. Vemuri, *Hermite expansions and Hardy's theorem* (first public arXiv submission 2008-01-15), https://arxiv.org/abs/0801.2234 .
- NIST Digital Library of Mathematical Functions, §§18.3, 18.5, 18.8, 18.15–18.16, https://dlmf.nist.gov/18.3 and https://dlmf.nist.gov/18.16 .
