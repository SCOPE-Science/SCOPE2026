# Logarithmic-endpoint mixed-Poisson extremes and independent exceedance marks

## Finding

Fix \(c>0\) and \(\alpha>0\), and let the positive density \(h\) on \((0,1)\) satisfy
\[
h(u)\sim H(1-u)^{\alpha-1}\quad(u\uparrow1),\qquad H>0.
\]
For each integer \(n\ge2\), draw independent \(U_i\) from \(h\), independently draw \(X_{n,i}\mid U_i\sim\mathrm{Poisson}(cU_i\log n)\) for \(1\le i\le n\), and put \(M_n=\max_i X_{n,i}\). Write \(t=t_c>c\) for the unique solution of
\[
I_c(t)=t\log(t/c)-t+c=1,
\]
and set
\[
r=\log(t/c),\qquad a=t/c-1,\qquad \rho=c/t,\qquad
K=\frac{H\Gamma(\alpha)\sqrt t}{\sqrt{2\pi}(t-c)^{\alpha+1}},
\]
\[
b_n=t\log n-\frac{\alpha+1/2}{r}\log\log n+\frac{\log K}{r}.
\]
Then **uniformly for all integers** \(k=k_n\) satisfying \(k-b_n=O(1)\),
\[
 n\Pr\{X_{n,1}\ge k\}=e^{-r(k-b_n)}(1+o(1)). \tag{1}
\]
In particular, for every integer subsequence with \(k_n-b_n\to x\in\mathbb R\),
\[
\Pr\{M_n<k_n\}\longrightarrow\exp\{-e^{-rx}\}. \tag{2}
\]
This is a **lattice** extreme-value law; no unqualified continuous Gumbel weak limit is asserted. The coefficient of \(\log\log n\) in \(b_n\) is sharp: replacing \(-(\alpha+1/2)/r\) by any different fixed coefficient makes the expected number of exceedances at that candidate location tend to zero or infinity.

Further, with \(\Lambda_{n,1}=cU_1\log n\), conditionally on \(X_{n,1}\ge k_n\),
\[
\left(X_{n,1}-k_n,\ c\log n-\Lambda_{n,1}\right)
\ \Longrightarrow\ (G,A), \tag{3}
\]
where \(G\) and \(A\) are **independent**,
\[
\Pr\{G=j\}=(1-\rho)\rho^j\quad(j=0,1,\ldots),\qquad
 A\sim\operatorname{Gamma}(\alpha,\text{rate }a).
\]
For the uniform mixing density, \(c=\alpha=H=1\), the saddle is exactly \(t=e\), the correction is \(-\tfrac32\log\log n\), and the limiting latent-intensity deficit is exponential with rate \(e-1\).

## Assumptions and scope

The mixing density is fixed across rows after scaling, normalized to integrate to one, and has the stated strictly positive finite endpoint constant. No differentiability is assumed. Conditional counts are independent within each row. The ceiling/rounding convention is represented by the *integer* thresholds \(k_n\), rather than silently replacing integer maxima by a continuous random variable. Parameter \(c\) is fixed while the maximum possible intensity grows like \(c\log n\).

## Proof

**1. Unique saddle.** Since \(I_c(c)=0\), \(I'_c(t)=\log(t/c)>0\) for \(t>c\), and \(I_c(t)\to\infty\), there is exactly one \(t>c\) with \(I_c(t)=1\). In particular \(r,a>0\) and \(0<\rho<1\).

**2. Uniform Poisson-tail factor.** Put \(\ell=\log n\), \(L=c\ell\), and \(k=t\ell+O(\log\ell)\), so that \(L/k\) stays below a fixed number strictly less than one. With \(p_k(\lambda)=e^{-\lambda}\lambda^k/k!\), a factorial-series expansion gives, uniformly for \(0\le\lambda\le L\),
\[
\Pr\{\operatorname{Pois}(\lambda)\ge k\}
=p_k(\lambda)\left[\frac1{1-\lambda/k}+O(k^{-1})\right]. \tag{4}
\]
Indeed, write the tail-to-mass ratio as \(\sum_{j\ge0}\prod_{v=1}^j\lambda/(k+v)\). Its difference from \(\sum_{j\ge0}(\lambda/k)^j\) is bounded by a constant times \(k^{-1}\sum_{j\ge0}j(j+1)q^j\) for a fixed \(q<1\); this proves the uniform error.

**3. Endpoint Laplace calculation.** Write \(s=L-\lambda\). For every fixed \(s\ge0\),
\[
\frac{p_k(L-s)}{p_k(L)}=e^{s}(1-s/L)^k\longrightarrow e^{-as},
\qquad \frac{h(1-s/L)}L\sim Hs^{\alpha-1}L^{-\alpha}.
\]
Choose a fixed small \(\delta>0\). On \(0\le s\le\delta L\), the density satisfies \(h(1-s/L)\le C(s/L)^{\alpha-1}\), after adjusting constants, and
\[
\frac{p_k(L-s)}{p_k(L)}\le e^{-a's}
\]
for some \(a'>0\). Hence dominated convergence applies to the locally rescaled integral. On \(\delta L<s\le L\), Poisson upper tails are uniformly at most a fixed multiple of \(p_k((1-\delta)L)\), whose ratio to \(p_k(L)\) decays exponentially in \(\ell\); integrating the mixing density gives at most this exponentially small quantity. Consequently (4) yields
\[
\Pr\{X_{n,1}\ge k\}
\sim p_k(L) H L^{-\alpha}\int_0^\infty
 \frac{s^{\alpha-1}e^{-as}}{1-\rho}\,ds
=p_k(L)\frac{H\Gamma(\alpha)t}{(t-c)^{\alpha+1}\ell^\alpha}. \tag{5}
\]
This argument also gives uniform relative error for bounded shifts of \(k\) around the stated \(b_n\).

**4. Large-deviation expansion and maxima.** Stirling's formula and Taylor's theorem at \(t\), with \(k-t\ell=O(\log\ell)\), imply
\[
p_k(L)=\frac{e^{-\ell I_c(t)-r(k-t\ell)}}{\sqrt{2\pi t\ell}}(1+o(1))
=\frac{n^{-1}e^{-r(k-t\ell)}}{\sqrt{2\pi t\ell}}(1+o(1)).
\]
Substituting in (5) proves (1), including its constant. Since \(\Pr\{M_n<k\}=(1-\Pr\{X_{n,1}\ge k\})^n\), (2) follows. If an alternative centering has coefficient \(d\) for \(\log\ell\), its expected exceedance count behaves like a positive constant times \(\ell^{-\alpha-1/2-rd}\), with the unique nonvanishing finite exponent \(d=-(\alpha+1/2)/r\). This establishes sharpness.

**5. Independent exceedance marks.** For each fixed integer \(j\ge0\) and \(s>0\), the unnormalized joint density of the event \(\{X_{n,1}=k+j\}\) and the intensity deficit \(s\) is
\[
 \frac{h(1-s/L)}L p_{k+j}(L-s).
\]
After division by \(H L^{-\alpha}p_k(L)\), it converges pointwise to \(s^{\alpha-1}e^{-as}\rho^j\). The same endpoint domination and a fixed geometric bound for \(p_{k+j}(\lambda)/p_k(\lambda)\) give tightness in \(s\) and \(j\) and permit normalization by the sum-integral \(\Gamma(\alpha)a^{-\alpha}/(1-\rho)\). The normalized limit factors into the stated Gamma density and geometric probability mass, proving their independence in (3).

## Verification

The accompanying standalone `mixed_poisson_endpoint_checker.py` evaluates exact uniform-mixture upper tails, the identity
\[
\Pr\{X\ge k\}=\Pr\{\operatorname{Pois}(L)\ge k\}
-\frac{k}{L}\Pr\{\operatorname{Pois}(L)\ge k+1\}
\]
for uniform \(\Lambda\) on \((0,L)\), the saddle equation and finite-parameter asymptotic ratios. It also numerically checks the factorization of the conditional mark density at a large logarithmic sample size. Its 50 numerical assertions passed at 175-decimal precision. These finite checks are diagnostics, not substitutes for steps 1–5.

## Relationship to prior work

Valiquette, Toulemonde, Peyhardi, Marchand and Mortier (2023), Theorems 2.5 and 2.8 and Section 3.3, analyze Poisson mixtures with a **fixed** mixing endpoint and the associated rapidly decreasing far tail, and display maxima for fixed endpoints. Those results do not give the present moving-endpoint asymptotic in which the count threshold and upper intensity are both proportional to \(\log n\). Anderson, Coles and Hüsler (1997) study Poisson and other triangular-array maxima, principally the regime permitting normal/Gumbel calibration for growing Poisson means; they do not state the explicit mixed-endpoint tail factor, shape-dependent \(\log\log n\) correction, or Gamma/Geometric latent exceedance law derived here. The large-deviation and endpoint-Laplace methods are standard; the specific combined classification and constants are the contribution.

## Limitations

The theorem requires an absolutely continuous mixing law with a power-law density at the endpoint, fixed positive \(c\) and \(\alpha\), independent rows, and conditional Poisson sampling. It does not cover an endpoint atom, varying power exponents, dependent observations, or uniformity over \(c\) approaching zero or infinity. Due to lattice effects, a single continuous Gumbel limit without subsequence alignment is false. The status of historical priority beyond the sources compared remains subject to independent scholarly review.

## References

1. S. Valiquette, G. Toulemonde, J. Peyhardi, É. Marchand, F. Mortier, *Asymptotic tail properties of Poisson mixture distributions*, arXiv:2305.17095v1 (first posted 26 May 2023), https://arxiv.org/html/2305.17095v1 .
2. C. W. Anderson, S. G. Coles, J. Hüsler, *Maxima of Poisson-like variables and related triangular arrays*, Annals of Applied Probability 7 (1997), 953–971, https://doi.org/10.1214/aoap/1043862420 .
3. S. Coles and F. Pauli, *Extremal limit laws for a class of bivariate Poisson vectors*, Statistics & Probability Letters 54 (2001), 373–379, https://doi.org/10.1016/S0167-7152(01)00102-X .
