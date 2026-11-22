# Sharp moving-frequency blindness and spectral separation of generalized Watson tests

## Finding

Consider the full generalized Watson statistics \(U_n^{[m]}\), indexed by an integer \(m\ge 1\), of Hwang and Kuriki [1]. Fix \(0<\varepsilon<1\). For any integer sequence \(k_n\to\infty\), observe \(n\) independent samples from the smooth, positive density
\[
 f_n(x)=1+\varepsilon\cos(2\pi k_nx),\qquad 0\le x<1.
\]
The scale of a single oscillatory alternative is \(s_n=n/k_n^{2m}\). Writing \(Z_1,Z_2,\ldots\) for independent standard normal random variables, define the continuous null law
\[
 Q_m=\sum_{j=1}^{\infty}\frac{Z_{2j-1}^2+Z_{2j}^2}{(2\pi j)^{2m}}.
\]
**The moving-frequency law** is, for every fixed \(m\ge1\): if \(s_n\to s\in[0,\infty)\), then
\[
 U_n^{[m]}\ \xrightarrow{\mathcal D}\ Q_m+\frac{\varepsilon^2s}{2(2\pi)^{2m}};
\]
if \(s_n\to\infty\), then \(U_n^{[m]}\to\infty\) in probability. Thus the exact detection boundary for this family is \(k_n\asymp n^{1/(2m)}\), including the nontrivial *translated-null* distribution at critical scale. With a fixed asymptotic upper-tail critical value \(c_{m,\alpha}\) of \(Q_m\), the limiting rejection probability at finite \(s\) is
\[
 1-F_{Q_m}\!\left(c_{m,\alpha}-\frac{\varepsilon^2s}{2(2\pi)^{2m}}\right).
\]
Here \(0<\alpha<1\), \(F_{Q_m}\) is the continuous CDF (defined to be zero on nonpositive arguments), and \(F_{Q_m}(c_{m,\alpha})=1-\alpha\). Infinite \(s\) gives limiting power one.

There is a **strict hierarchy between these published statistics**. For \(k_n=\lfloor n^{1/3}\rfloor\), the classical \(m=1\) Watson test has power tending to one, while *every fixed* higher-order statistic \(m\ge2\) has power tending to its nominal level \(\alpha\). Yet the total-variation distance between the full \(n\)-sample alternative and its uniform-null distribution tends to one exponentially fast. The same strongly separated sequence is therefore detectable by the first-order member and asymptotically invisible to each higher-order member.

An exact finite-sample companion identity is
\[
 \mathbb E_{f_n} U_n^{[m]}
 =\frac{2\zeta(2m)}{(2\pi)^{2m}}
 +\frac{(n-1)\varepsilon^2}{2(2\pi k_n)^{2m}}.
\]

## Assumptions and scope

The null is the fully specified continuous uniform law on \([0,1)\), with periodic identification of endpoints. The integer order \(m\ge1\), oscillation amplitude \(0<\varepsilon<1\), and nominal level \(0<\alpha<1\) are fixed as \(n\to\infty\); only the positive integer frequency \(k_n\) varies. Sampling is independent within each row of the triangular array. No nuisance parameters are estimated. We study the **full** statistic, not the eigenvalue-truncated statistics \(U_n^{*[m]}\) also discussed by Hwang and Kuriki [1].

Use the ordinary Bernoulli polynomial \(B_{2m}\) and \(b_{2m}=B_{2m}/(2m)!\). Equation (74) in [1] states
\[
 U_n^{[m]}=\frac1n\sum_{a,b=1}^n (-1)^{m-1}b_{2m}(|X_a-X_b|).
\]
The absolutely convergent Fourier expansion of this periodic Bernoulli kernel, for all \(m\ge1\), gives the **exact**, nonasymptotic identity
\[
 U_n^{[m]}
 =2n\sum_{j=1}^{\infty}\frac{|\widehat\phi_n(j)|^2}{(2\pi j)^{2m}},
 \qquad \widehat\phi_n(j)=\frac1n\sum_{a=1}^n e^{2\pi i jX_a}.
\]
This normalization agrees with the null spectral law in Theorem 3.2 of [1].

## Proof

**1. Fourier moments and exact expectation.** Under \(f_n\), trigonometric orthogonality gives, for each positive integer \(j\),
\[
 \theta_n(j)=\mathbb E e^{2\pi i jX_1}
 =\frac\varepsilon2\mathbf1_{\{j=k_n\}}.
\]
For any i.i.d. unit-modulus complex variables, direct expansion of the squared empirical mean yields
\[
 \mathbb E\big[n|\widehat\phi_n(j)|^2\big]
 =1+(n-1)|\theta_n(j)|^2.
\]
Multiplication by the nonnegative Fourier weights and Tonelli's theorem prove the displayed finite-sample expectation. In particular, for every \(j\ne k_n\), \(\mathbb E[n|\widehat\phi_n(j)|^2]=1\), independent of \(n\).

**2. Joint fluctuations of finitely many low modes.** Fix \(J\ge1\). Eventually \(k_n>2J\). For all \(1\le j,\ell\le J\), the expectations of \(e^{2\pi i(j-\ell)X}\) and \(e^{2\pi i(j+\ell)X}\) are identical to those under uniformity: their frequencies have absolute value at most \(2J\), where the only nonzero population Fourier coefficient is the constant coefficient. Therefore the \(2J\)-dimensional real vectors
\[
 \bigl(\cos(2\pi jX),\sin(2\pi jX)\bigr)_{j=1}^{J}
\]
have mean zero and covariance \(\tfrac12 I_{2J}\). Their norms are bounded uniformly in \(n\), so the multivariate Lindeberg central limit theorem for row-wise i.i.d. triangular arrays applies. It follows jointly that
\[
 \bigl(\sqrt{2n}\,\operatorname{Re}\widehat\phi_n(j),
 \sqrt{2n}\,\operatorname{Im}\widehat\phi_n(j)\bigr)_{j=1}^{J}
 \xrightarrow{\mathcal D}(Z_1,\ldots,Z_{2J}).
\]
Consequently the first \(J\) terms of the Fourier statistic converge in law to \(Q_{m,J}=\sum_{j=1}^{J}(Z_{2j-1}^2+Z_{2j}^2)/(2\pi j)^{2m}\).

**3. Uniform control of the other high modes.** Exclude the exceptional mode \(k_n\) and the first \(J\) modes. By positivity and the expectation computed above,
\[
 \mathbb E\!\left[2n\!\sum_{j>J,\ j\ne k_n}
 \frac{|\widehat\phi_n(j)|^2}{(2\pi j)^{2m}}\right]
 \le 2\!\sum_{j>J}(2\pi j)^{-2m}\ \xrightarrow[J\to\infty]{}0.
\]
Since \(2m\ge2\), the tail is summable. Markov's inequality makes the contribution of all nonexceptional high frequencies uniformly negligible in probability. Also \(Q_{m,J}\uparrow Q_m\) almost surely, as its expectation series is finite. The standard truncation/converging-together argument yields \(Q_m\) as the limiting nonexceptional component. This is stronger than merely asserting fixed-frequency Gaussian convergence; it controls the whole infinite series uniformly in the moving alternative.

**4. Exceptional moving mode.** At \(j=k_n\), the population Fourier mean is \(\varepsilon/2\), and a bounded-variables variance calculation gives
\[
 \widehat\phi_n(k_n)=\frac\varepsilon2+O_{\mathbb P}(n^{-1/2}).
\]
The corresponding nonnegative term is
\[
 2n\frac{|\widehat\phi_n(k_n)|^2}{(2\pi k_n)^{2m}}
 =\frac{2s_n}{(2\pi)^{2m}}
 \left|\frac\varepsilon2+O_{\mathbb P}(n^{-1/2})\right|^2.
\]
If \(s_n\to s<\infty\), the term converges in probability to \(\varepsilon^2s/[2(2\pi)^{2m}]\). Combining with Step 3 and Slutsky's theorem proves the translated-null law, including \(s=0\). If \(s_n\to\infty\), the special term alone diverges in probability since its squared factor tends to \(\varepsilon^2/4>0\). All other terms are nonnegative, so the full statistic diverges.

**5. Rejection probability and sharp separation.** The series \(Q_m\) has a continuous distribution and positive density on \((0,\infty)\): isolate its first squared-Gaussian pair, which has a strictly positive exponential density on \((0,\infty)\), and convolve with the independent nonnegative remainder. The weak limits therefore imply convergence of right-tail rejection probabilities at every fixed upper quantile. For \(k_n=\lfloor n^{1/3}\rfloor\), \(s_n\sim n^{1-2m/3}\), which diverges at \(m=1\) and tends to zero for each fixed \(m\ge2\).

Finally, put \(T_n=n^{-1}\sum_{a=1}^n\cos(2\pi k_nX_a)\). Under uniformity, \(\mathbb ET_n=0\); under \(f_n\), \(\mathbb ET_n=\varepsilon/2\). Each summand lies in \([-1,1]\). Hoeffding's inequality for the event \(T_n>\varepsilon/4\) bounds both the null false-positive and alternative false-negative probabilities by \(\exp(-n\varepsilon^2/32)\). Thus, if \(P_n\) is the product law under \(f_n\) and \(P_{0,n}\) the uniform product law,
\[
 \lVert P_n-P_{0,n}\rVert_{\mathrm{TV}}
 \ge1-2e^{-n\varepsilon^2/32}\longrightarrow1.
\]
This proves that higher-order blindness is a property of the chosen statistics rather than statistical inseparability of the full experiments. \(\square\)

## Verification

The included standalone script `verify_watson_frequency.py` uses NumPy and SciPy and has been executed successfully with **56 deterministic assertions**. It checks the Bernoulli-kernel and Fourier expressions for \(m=1,2\), exact trigonometric orthogonality by quadrature, the expectation formula for \(m=1,2,3\), and the critical scaling and normalization. Those finite calculations are supplementary; the uniform infinite-series bound and triangular-array central limit theorem above establish the asymptotic claims analytically.

## Relationship to prior work

Hwang and Kuriki [1] define the generalized Watson statistics, prove the exact kernel expression, identify the null Gaussian spectral law and compare numerical power for selected fixed low-frequency alternatives. **These are their results, not claimed here.** The present result addresses a different quantifier regime: a fixed-amplitude sinusoidal density whose frequency increases with sample size, and the joint power hierarchy across all orders. Neither the fixed-null spectral theorem nor numerical power at fixed frequencies itself states this triangular-array conclusion.

Henze and Nikitin [2] earlier studied integrated empirical-process Watson-type tests, including the second-order kernel, with local Bahadur efficiency for shift alternatives. The present finding does not claim priority for the second-order test or its Bernoulli kernel. García-Portugués, Paindaveine and Verdebout [3] analyzed directional Sobolev-test detection thresholds under local perturbations of fixed angular shapes and derivative constraints. Their results supply important broader context, but the source inspected does not give the present fixed-amplitude, diverging Fourier-frequency hierarchy or its translated-null critical law. Classical Fourier orthogonality, Hoeffding bounds and the multivariate CLT are used with their standard prior meanings.

## Limitations

The order \(m\) and amplitude \(\varepsilon\) are fixed; there is no joint limit with \(m\to\infty\) or \(\varepsilon\to0\). The frequencies are positive integers; nonintegral frequencies generally lose exact orthogonality. The result applies to Hwang–Kuriki's *untruncated* generalized Watson statistics for a completely known uniform null, not the truncated family, estimated-null tests or other Sobolev diagnostics. The separation statement is pointwise across each fixed \(m\ge2\), not uniform in growing \(m\). It does not imply that the underlying full observations are impossible to classify, and it does not claim minimax optimality. Historical priority beyond the inspected sources requires independent literature review.

## References

[1] H.-K. Hwang and S. Kuriki, *Integrated empirical measures and generalizations of classical goodness-of-fit statistics*, arXiv:2404.06040, first posted 2024-04-09, Theorems 3.2–3.3 and Section 3.4. https://arxiv.org/abs/2404.06040

[2] N. Henze and Ya. Yu. Nikitin, *Watson-type goodness-of-fit tests based on the integrated empirical process*, Mathematical Methods of Statistics **11** (2002), 183–202. Full text inspected via https://www.researchgate.net/publication/268315464_Watson-type_goodness-of-fit_tests_based_on_the_integrated_empirical_process

[3] E. García-Portugués, D. Paindaveine and T. Verdebout, *On a class of Sobolev tests for symmetry of directions, their detection thresholds, and asymptotic powers*, arXiv:2108.09874, first posted 2021-08-23. https://arxiv.org/abs/2108.09874
