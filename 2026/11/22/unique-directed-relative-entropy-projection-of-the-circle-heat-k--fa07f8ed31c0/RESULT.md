# Unique directed relative-entropy projection of the circle heat kernel onto Poisson kernels

## Finding
For every heat time \(t>0\), the normalized circle heat density \(H_t\) has exactly one globally best Poisson approximation for **forward** Kullback–Leibler divergence \(D(H_t\Vert P)\), including freely chosen concentration and center. The optimal center agrees with the heat center and the optimal radius is uniquely fixed by a strictly monotone scalar equation. Its small-time radius has the universal Gaussian–Cauchy scale \(1-r_t\sim c_*\sqrt t\), while matching the first Fourier moment gives a divergent excess information loss rather than a finite limit.

The constants are \(c_*=0.86550319873261586\ldots\) and \(K_*=0.18275830866970635\ldots\). The precise claims and boundaries appear below.

## Assumptions and scope
Let \(d\mu=d\theta/(2\pi)\) denote Haar probability measure on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Define
\[
H_t(\theta)=\sum_{n\in\mathbb Z}e^{-tn^2}e^{in\theta},\qquad t>0,
\]
and
\[
P_{r,\phi}(\theta)=\frac{1-r^2}{1-2r\cos(\theta-\phi)+r^2},\quad 0\le r<1,\quad \phi\in\mathbb T.
\]
Both densities have integral one against \(\mu\), and \(H_t\) is smooth and strictly positive. Define \(D(p\Vert q)=\int p\log(p/q)\,d\mu\). We minimize this directed divergence over the *entire* Poisson family; the reverse divergence and generic circular densities are not within scope. When \(r=0\), all \(\phi\) represent the same uniform density.

## Proof
**Fourier identity and center.** Absolute convergence of the Poisson logarithm and the heat Fourier series gives
\[
D(H_t\Vert P_{r,\phi})=\int H_t\log H_t\,d\mu-\log(1-r^2)-2\sum_{n=1}^{\infty}\frac{e^{-tn^2}r^n}{n}\cos(n\phi).
\]
For any \(r>0\), every Fourier weight is positive, so this is uniquely minimized at \(\phi=0\pmod {2\pi}\) (the first harmonic makes equality strict). The right derivative at \(r=0\) is \(-2e^{-t}<0\), so no minimizer is uniform.

**Unique radius.** Put \(s=-\log r>0\), \(A_t(s)=\sum_{n\ge1}e^{-tn^2-sn}\) and \(B(s)=\sum_{n\ge1}e^{-2sn}=(e^{2s}-1)^{-1}\). The derivative with respect to \(r\) of the radial objective has the sign of \(B(s)-A_t(s)\); thus stationarity means \(A_t(s)=B(s)\). Let \(R_t(s)=A_t(s)/B(s)\). As \(s\downarrow0\), \(R_t(s)\to0\), and as \(s\to\infty\), \(R_t(s)\sim e^{s-t}\to\infty\). Under normalized weights \(e^{-sn-tn^2}\), the mean index is strictly below the mean under geometric weights \(e^{-sn}\), by the monotone likelihood-ratio order. Therefore
\[
\frac{d}{ds}\log R_t(s)=2\mathbb E_{B,s}n-\mathbb E_{A,t,s}n
>\frac{2}{1-e^{-2s}}-\frac{1}{1-e^{-s}}
=\frac1{1+e^{-s}}>0.
\]
Consequently there is exactly one critical radius, which is globally minimizing since \(D\to+\infty\) as \(r\uparrow1\) for fixed \(t>0\). At \(s=t\), the strict inequalities \(e^{-tn^2}<e^{-tn}\) for \(n\ge2\) show \(A_t(t)<B(t)\), whence \(s_t>t\), i.e. \(r_t<e^{-t}\). For fixed \(s\), \(A_t(s)\) strictly decreases with \(t\); implicit differentiation of the unique crossing proves that \(s_t\) is smooth and strictly increasing in \(t\).

**Sharp small-time scale.** For any fixed \(c>0\), set \(s=c\sqrt t\). Riemann-sum convergence gives
\[
\sqrt t\,A_t(c\sqrt t)\longrightarrow\int_0^\infty e^{-x^2-cx}\,dx,
\qquad \sqrt t\,B(c\sqrt t)\longrightarrow\frac1{2c}.
\]
Multiplying by \(2c\), the first limit increases strictly from zero to one as \(c\) increases from zero to infinity, since its substitution \(u=cx\) becomes \(2\int_0^\infty e^{-u-u^2/c^2}\,du\). Thus it equals one for exactly one \(c=c_*>0\); monotonic crossings bracket \(s_t/\sqrt t\) and prove convergence. Equivalently, \(c_*\) satisfies the stated Gaussian integral equation.

For \(\theta=\sqrt t\,x\), the properly rescaled heat *Lebesgue* density tends to \(g(x)=e^{-x^2/4}/\sqrt{4\pi}\), and the rescaled optimally centered Poisson Lebesgue density tends to \(q_c(x)=c/[\pi(c^2+x^2)]\). These follow from Poisson summation and the small-angle denominator expansion. Gaussian tails and the bounded-domain logarithmic singularity permit truncation and dominated convergence for relative entropy, giving
\[
K_*=D(g\Vert q_{c_*})=\log(\pi/c_*)-\tfrac12\log(4\pi e)+\mathbb E\log(c_*^2+X^2),\quad X\sim N(0,2).
\]
The derivative of \(D(g\Vert q_c)\) is \(c^{-1}(2\int_0^\infty e^{-u-u^2/c^2}\,du-1)\), proving again that its global minimizer is precisely \(c_*\).

**Moment matching and large heat time.** The first nonconstant Fourier coefficients are \(e^{-t}\) for \(H_t\) and \(r\) for \(P_r\). Thus moment matching fixes \(r=e^{-t}\). At scale \(\theta=\sqrt t x\), the ratio of the heat density to this narrower Poisson density has logarithm \(-\tfrac12\log t+\tfrac12\log\pi-x^2/4-\log2+\log(x^2+t)+o(1)\) away from the origin. Uniform integrability of the logarithmic term near the origin under Gaussian weights, plus exponential tails, yields
\[
D(H_t\Vert P_{e^{-t},0})=\tfrac12\log(1/t)+\tfrac12\log\pi-\log2-\tfrac12-\gamma+o(1).
\]
Indeed \(\mathbb E\log X^2=-\gamma\) for \(X\sim N(0,2)\). Finally write \(q=e^{-t}\) and solve the unique radius equation as a convergent analytic implicit series near \(q=0\); its first terms give \(r_t=q-q^3+3q^5+O(q^7)\). The leading unmatched second Fourier coefficient is \(-q^2+o(q^2)\), so the quadratic expansion of relative entropy at the uniform density yields \(\min D(H_t\Vert P)=q^4(1+o(1))=e^{-4t}(1+o(1))\).

## Verification
The independent executable arithmetic checks in `checker.py` numerically solve the scalar crossing, quadrature for \(c_*\) and \(K_*\), evaluate direct circle KL integrals and test both asymptotic regimes and angular/radial optimality in finite examples. The checker reports 92 passed diagnostics. These diagnostics are **finite numerical checks**, not proofs of global uniqueness or of asymptotic limits; the analytic derivations above supply those proofs.

## Relationship to prior work
Bailey's publicly deposited thesis treats wrapped normal and wrapped Cauchy models, and its Appendix C1 includes numerical grid comparisons under KL divergence for *mixtures* of wrapped normal distributions; its main theorem uses squared \(L^2\) discrepancy. The current claim is instead an exact globally unique **single wrapped-normal-to-wrapped-Cauchy forward-KL projection** with sharp small-time information-loss asymptotics. The later Bailey–Codling paper motivates comparison of wrapped models, while the Otani–Matsuda article treats circular distribution projections under Wasserstein loss and gives individual other-family KL expressions; none of the inspected passages states the current classification. The key novelty is not elementary Fourier expansion alone but its global monotonicity consequence and singular information-theoretic limit for all heat times.

## Limitations
Only forward KL and a centered unimodal circular heat source are treated. Results do not cover mixtures, reverse KL, alternate losses, or non-heat Fourier sequences. Numerical constants are approximate evaluations of analytic characterizations; publication-priority claims remain provisional because no literature search guarantees exhaustion. The available Bailey–Codling accepted journal text was not fully inspectable; the original publicly available thesis chapter and appendix were inspected directly. No independent external mathematical validation is claimed.

## References
- J. D. Bailey, *Modelling and Analysis of Individual Animal Movement*, University of Essex PhD thesis (public repository deposit 8 January 2020), chapter 6 and appendix C1. https://repository.essex.ac.uk/26383/1/Thesis_2%281%29.pdf
- J. D. Bailey and E. A. Codling, *Emergence of the wrapped Cauchy distribution in mixed directional data* (2020). https://doi.org/10.1007/s10182-020-00380-7
- J. González-Pérez, *Hölder classes via semigroups and Riesz transforms* (2022). https://doi.org/10.1007/s00209-022-02982-0
- N. Otani and T. Matsuda, *Wasserstein projection estimators for circular distributions* (2026), especially the relative-entropy comparison in the appendix. https://link.springer.com/article/10.1007/s41884-026-00214-6
