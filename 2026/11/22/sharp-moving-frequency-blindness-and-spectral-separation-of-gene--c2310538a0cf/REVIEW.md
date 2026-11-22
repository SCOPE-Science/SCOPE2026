# Mathematical review

## Correctness — PASS

The claim concerns the full untruncated periodic generalized Watson statistics and a row-wise independent array of exact positive sinusoidal densities. Equation (74) of Hwang–Kuriki yields the exact periodic Bernoulli-kernel identity; its absolutely convergent Fourier expansion fixes the normalization and eliminates arbitrary Fourier truncation. All nonexceptional Fourier coefficients have zero mean, uniformly giving the exact second moment \(\mathbb E[n|\widehat\phi_n(j)|^2]=1\). For each finite low-frequency block, \(k_n>2J\) makes the covariance exactly the null covariance, allowing the bounded triangular-array CLT. A summable tail bound controls all higher nonexceptional modes, and the single exceptional mode converges to the translated mass or diverges. Continuity of the null spectral CDF transfers these limits to rejection probabilities. Hoeffding's inequality independently verifies exponential separation of the complete experiments. The included standalone numerical checker passed 56 assertions; no simulation is used as a replacement for the infinite-dimensional proof.

## Originality — PASS (with residual priority risk)

The nearest primary source, Hwang–Kuriki (arXiv:2404.06040), establishes the statistic and its null kernel/eigenstructure; Section 3.4 numerically compares alternatives with selected fixed low modes. The new result is not its spectral identity alone: it is a precise triangular-array phase diagram and a same-alternative cross-order power separation. Henze–Nikitin (2002) already covers the higher integrated Watson kernel at order two and local shift efficiencies, which are expressly excluded from the priority claim. García-Portugués–Paindaveine–Verdebout (arXiv:2108.09874) studies Sobolev detection thresholds for different fixed-form angular local alternatives. None of the inspected relevant statements supplies the fixed-amplitude, growing-harmonic translated-null theorem. Additional historical literature could still dominate the result; this is a residual priority risk, not a proof of uniqueness.

## Value — PASS

The exact threshold \(k_n\asymp n^{1/(2m)}\) quantifies the loss of high-frequency sensitivity as the integration order grows. Choosing the single natural frequency scale \(k_n\asymp n^{1/3}\) proves a substantive separation: one published diagnostic is consistent, all higher fixed orders retain only nominal asymptotic power, and the full experiments have total variation approaching one. The critical law is a translated Gaussian quadratic series rather than a routine fixed-mode noncentral chi-square law. This is a concrete calibration/design consideration for practitioners using increasingly smoothed goodness-of-fit diagnostics, even without a minimax theorem.

## Risks and limits

Fixed order, fixed amplitude and exact integer harmonics; no claim about truncated, estimated-null, growing-order or minimax versions. The original exact kernel and null law are credited, and historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
