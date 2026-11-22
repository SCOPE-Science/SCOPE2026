# A monotone strong-resetting escape frontier for symmetric stable flights

## Finding

**Theorem (strong-resetting escape frontier).** Let \(0<\alpha<2\), \(L>0\), \(\sigma>0\), and let a one-dimensional symmetric \(\alpha\)-stable Lévy flight start at \(x\in(-L,L)\). Absorption occurs at the first exit from \((-L,L)\). At rate \(r>0\), independently of the trajectory, the flight is instantaneously reset to the same starting point \(x\), conditional on not yet having exited. Let \(M_r(x)\) denote its expected exit time, and \(M_0(x)\) the expected exit time without resetting. Set \(v=|x|/L\). Then

\[
\frac{\lim_{r\to\infty}M_r(x)}{M_0(x)}
 =\frac{C_\alpha}{\cosh(\alpha\operatorname{artanh}v)},
\qquad C_\alpha=\frac{\pi\alpha}{2\sin(\pi\alpha/2)}>1.
\]

There is exactly one \(v_c(\alpha)\in(0,1)\) at which this ratio equals one:

\[
 v_c(\alpha)=\tanh\!\left[\frac1\alpha\operatorname{arcosh}\!\left(\frac{\pi\alpha}{2\sin(\pi\alpha/2)}\right)\right].
\]

For \(v>v_c(\alpha)\), sufficiently rapid **finite** Poisson resetting strictly improves the mean exit time relative to no resetting; for \(v<v_c(\alpha)\), all sufficiently rapid resetting strictly worsens it. At equality the limiting mean times coincide, with no finite-rate sign asserted. **The function \(\alpha\mapsto v_c(\alpha)\) is strictly increasing on \((0,2)\)**, and obeys the sharp endpoint laws

\[
\lim_{\alpha\downarrow0}v_c(\alpha)=\tanh\!\left(\frac\pi{2\sqrt3}\right),
\quad v_c(1)=\sqrt{1-\frac4{\pi^2}},
\quad v_c(\alpha)=1-\frac{2-\alpha}{2}+o(2-\alpha)\ \ (\alpha\uparrow2).
\]

The strong-resetting classification concerns the sign of the **infinite-rate limit relative to no resetting**; it is not a global classification of all finite reset rates.

## Assumptions and scope

The Lévy flight is normalized by

\[
 \mathbb E[e^{i\xi(X_t-X_0)}]=e^{-t\sigma^\alpha|\xi|^\alpha}.
\]

The resetting epochs form an independent homogeneous Poisson process; each reset completely regenerates the process at \(x\), incurs zero delay, and does not alter the absorbing interval. Exit includes jumps crossing either boundary, not just boundary hits. All conclusions are pointwise in the fixed parameters \(\alpha,L,\sigma,x\), with \(r\to\infty\); uniformity as \(\alpha\to2\) or as \(x\to\pm L\) is not claimed.

## Proof

**1. Short-time escape and the high-rate mean.** The Lévy jump measure is \(\nu(dz)=c_\alpha\sigma^\alpha|z|^{-1-\alpha}\,dz\), where

\[
 c_\alpha=\frac{\alpha2^{\alpha-1}\Gamma((1+\alpha)/2)}{\sqrt\pi\,\Gamma(1-\alpha/2)}.
\]

For a start strictly within the interval, the known short-time exit theorem for Lévy processes gives \(\Pr_x(\tau\le t)=\lambda_x t+o(t)\), with the **two-sided** exit-jump intensity

\[
 \lambda_x=\int_{\{z\colon x+z\notin(-L,L)\}}\nu(dz)
 =\frac{c_\alpha\sigma^\alpha}{\alpha}
 \bigl[(L-x)^{-\alpha}+(L+x)^{-\alpha}\bigr]>0.
\]

Here \(\tau\) is the exit time of an unreset excursion. Writing \(q(r)=\mathbb E_x e^{-r\tau}\), integration by parts, or the elementary Abelian theorem for the exit distribution, gives \(q(r)=\lambda_x/r+o(1/r)\) as \(r\to\infty\). The renewal identity for a Poisson restart is

\[
 M_r(x)=\frac{1-q(r)}{r q(r)},
\]

and hence \(\lim_{r\to\infty}M_r(x)=1/\lambda_x\). Existence of finite \(M_r\) follows because every independently restarted excursion has positive success probability \(q(r)>0\).

**2. Dimensionless comparison.** The established stable-flight free exit mean is

\[
 M_0(x)=\frac{(L^2-x^2)^{\alpha/2}}{\sigma^\alpha\Gamma(1+\alpha)}.
\]

Therefore

\[
 \frac{1/\lambda_x}{M_0(x)}
 =\frac{\alpha\Gamma(1+\alpha)/c_\alpha}
 {[(1-v)^{-\alpha}+(1+v)^{-\alpha}](1-v^2)^{\alpha/2}}.
\]

Since \((1+v)/(1-v)=e^{2\operatorname{artanh}v}\), the denominator of the final fraction is \(2\cosh(\alpha\operatorname{artanh}v)\). Gamma reflection and duplication show

\[
 \frac{\alpha\Gamma(1+\alpha)}{2c_\alpha}
 =\frac{\pi\alpha}{2\sin(\pi\alpha/2)}=C_\alpha.
\]

Because \(0<\sin t<t\) for \(0<t<\pi\), \(C_\alpha>1\). The denominator \(\cosh(\alpha\operatorname{artanh}v)\) increases strictly and continuously from \(1\) to infinity as \(v\) rises from zero to one. This proves the unique threshold, the sign classification, and the formula. For strict inequalities, continuity of the limiting convergence ensures the same sign for all sufficiently large finite \(r\).

**3. Strict monotonicity across every stable index.** Put \(t=\pi\alpha/2\in(0,\pi)\), \(h(t)=\log(t/\sin t)>0\) and \(F(h)=\operatorname{arcosh}(e^h)\). The argument of the outer hyperbolic tangent in the threshold is

\[
 \frac{F(h(t))}{\alpha}=\frac\pi2\cdot\frac{F(h(t))}{\sqrt{h(t)}}\cdot\sqrt{\frac{h(t)}{t^2}}.
\]

Both variable factors are strictly increasing in \(t\). To prove this for the second factor, Euler's product for sine gives the convergent positive series

\[
 \frac{h(t)}{t^2}
 =\sum_{n=1}^\infty\frac{-\log(1-t^2/(n\pi)^2)}{t^2}.
\]

For each \(n\), the summand equals \((n\pi)^{-2}\varphi(t^2/(n\pi)^2)\), where \(\varphi(u)=-\log(1-u)/u\) is strictly increasing on \((0,1)\), as follows from its positive-coefficient series. Hence \(h(t)/t^2\) is strictly increasing.

For the first factor, let \(z=F(h)>0\), so \(h=\log\cosh z\). The derivative of \(z/\sqrt{\log\cosh z}\) has the sign of \(2\log\cosh z-z\tanh z\). That expression vanishes at zero and its derivative is \(\tanh z-z\operatorname{sech}^2z>0\) for \(z>0\), because \(\sinh(2z)>2z\). Thus \(F(h)/\sqrt h\) strictly increases with \(h\), and \(h(t)\) strictly increases. Both factors therefore increase strictly. Applying the increasing function \(\tanh\) establishes strict monotonicity of \(v_c(\alpha)\).

**4. Endpoints.** As \(t\downarrow0\), \(t/\sin t=1+t^2/6+O(t^4)\) and \(\operatorname{arcosh}(t/\sin t)=t/\sqrt3+O(t^3)\), giving the small-index limit. At \(\alpha=1\), \(C_1=\pi/2\), so \(\tanh(\operatorname{arcosh}(\pi/2))=\sqrt{1-4/\pi^2}\). Finally, with \(\varepsilon=2-\alpha\downarrow0\), \(C_\alpha\sim2/\varepsilon\), \(\operatorname{arcosh}C_\alpha=\log(4/\varepsilon)+o(1)\), and \(1-\tanh z\sim2e^{-2z}\); these give \(1-v_c(\alpha)\sim\varepsilon/2\). This completes the proof.

## Verification

The standard-library script `checker.py` independently evaluates the Lévy-measure normalization and the two-sided escape intensity, compares the direct mean ratio against the hyperbolic-cosine expression on a broad finite parameter grid, checks the strict sign change and sampled index ordering, and compares the Cauchy and small-index endpoints. Running `python3 checker.py` produces 6,359 successful finite consistency assertions. No numerical finite sample is used to certify the all-index monotonicity, which is proved above.

## Relationship to prior work

Żbik and Palmowski (2026), Sections II–III, provide the Poisson-restart renewal identity and the symmetric stable-flight short-time/large-interval/strong-reset mean formulas for general initial positions. Their strong-reset mean is **not** claimed here. Żbik and Dybiec (2024) provide the free mean and analyze the weak-reset coefficient-of-variation benefit region. The present contribution is the *sharp all-index comparison frontier and its strictly monotone dependence on the stability index*, including endpoint constants. The earlier weak-reset criterion is a different asymptotic regime and must not be identified with the strong-reset frontier; the two index trends need not agree. The short-time exit step rests on the result of Figueroa-López and Tankov (2014), as used in Żbik–Palmowski. The main frontier formula is an explicit consequence of these prior ingredients; the nontrivial monotonicity is proved independently above.

## Limitations

This theorem does not assert a globally optimal finite reset rate, any exact boundary for existence of benefit at *some* unspecified reset rate, or a finite-rate sign at the crossover. It excludes the Brownian endpoint \(\alpha=2\) and the boundary starting points \(|x|=L\); neither can be substituted into the limit by continuity without checking order of limits. Its strictness is within the idealized instantaneous full-restart model. Its originality is qualified by the possibility that equivalent all-index ordering is implicit in wider renewal literature, even though the underlying asymptotic mean is known.

## References

1. B. Żbik and Z. Palmowski, *Asymptotic behaviour for escaping an interval by Lévy flights under stochastic resetting*, arXiv:2610.20410, first public version 14 October 2026. https://arxiv.org/abs/2610.20410
2. B. Żbik and B. Dybiec, *Lévy flights and Lévy walks under stochastic resetting*, *Physical Review E* **109**, 044147 (2024), arXiv:2311.16014. https://arxiv.org/abs/2311.16014
3. J. E. Figueroa-López and P. Tankov, *Small-time asymptotics of stopped Lévy bridges and simulation schemes with controlled bias*, *Bernoulli* **20** (2014), 1126–1164, Theorem 2.1. https://arxiv.org/abs/1203.2355
4. R. K. Getoor, *First passage times for symmetric stable processes in space*, *Transactions of the American Mathematical Society* **101** (1961), 75–90 (classical stable-flight exit moments).
