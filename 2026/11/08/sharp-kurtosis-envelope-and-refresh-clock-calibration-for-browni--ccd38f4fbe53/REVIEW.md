# Scientific review

## Correctness — PASS

The model assumes an autonomous Poisson-refresh rate environment, with the position reset but not the rate at particle-reset events. The stationary generator gives the exact conditional Fourier measure and independently gives second/fourth moment balances. The excess-kurtosis identity and derivative formulas are dimensionally consistent and use valid differentiation for every positive refresh rate. Explicit strictly signed square expectations prove monotonicity and convexity for all nondegenerate laws. The upper bound is attained by a precisely specified endpoint law, and its equality conditions were checked. The code repeats 228 rational cases, but the infinite-family assertions rely on the written proof.

## Originality — PASS (qualified)

The 2025 Arutkin–Reuveni paper supplies the complete stationary Fourier transform, so the derived moments themselves are covered; they are not presented as the advance. The new mathematical comparison is a simultaneous strict monotonicity/convexity theorem for *normalized* fourth moments across refresh speeds, plus a sharp support extremizer and exact inverse calibration. The inspected paper discusses density crossovers, not these global normalized-shape and equality laws. A known localization-order theorem for the same model orders unnormalized radial moments; such ordering cannot establish a ratio comparison. Alternative refractory and viscoelastic reset mechanisms have different retained variables. The Fourier formula does determine all moments and therefore poses a real corollary-priority risk, particularly if these inequalities were previously observed elsewhere.

## Value — PASS

Normalized kurtosis isolates non-Gaussian shape from the diffusion scale, making the excess above the exponential fixed-rate benchmark a meaningful signature of refresh disorder. Strict decrease with positive curvature supports one-observable calibration of a known rate environment. The exact extremal envelope specifies the maximal feasible non-Gaussian enhancement given an intensity range and identifies the unique maximizing two-rate mixture. These are model-wide structural and calibration statements, not a single numerical evaluation or an arbitrary parameter slice.

## Residual limitations

The inference statements require knowledge of the intensity law, and stationary fourth moments may be difficult to measure at small refresh rates. The original Fourier solution already implies each fixed-parameter moment. No first-passage conclusion, transient claim, or independent validation is supplied. Literature coverage cannot exclude unindexed equivalent calculations.

Self-review: passed. Independent audit: not yet performed.
