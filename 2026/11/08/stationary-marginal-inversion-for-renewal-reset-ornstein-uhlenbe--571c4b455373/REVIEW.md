# Scientific review: stationary one-time inversion in renewal-reset Ornstein–Uhlenbeck dynamics

## Correctness — PASS

The equilibrium-age density is the renewal-reward identity. The Ornstein–Uhlenbeck propagator from zero is Gaussian with variance \(\frac D\kappa(1-e^{-2\kappa a})\); transforming the age to \(u=e^{-2\kappa a}\) gives the stated probability mixture and normalized even moments. Hausdorff moment uniqueness on a compact interval identifies the mixing law. The monotone left-continuous endpoint criterion is both necessary and sufficient to recover a proper strictly positive finite-mean reset-time distribution. Compact smooth derivatives supply exact finite-moment aliases while preserving the monotone survival constraint. A separate high-frequency perturbation of the mixing density has vanishing total variation yet its derivative—and the induced smooth reset-time density—retains a positive limiting total-variation difference. Exact-arithmetic diagnostics support special calculations but do not establish infinite limits.

## Originality — PASS, qualified

Eule–Metzger (arXiv:1510.07876), Lapeyre–Dentz (arXiv:1903.08055) and Masoliver–Montero (Physical Review E 100, 042103) establish the *forward* stationary renewal-mixture machinery. Olsen (arXiv:2310.04840) treats Poisson reset intervals and variable reset *positions* for harmonic-trap moments, while explicitly pointing to non-Poisson timing as further work. Jolakoski (arXiv:2605.30059) characterizes equilibrium-age Laplace transforms as gradient-flow spectral filters over varying curvature; it does not provide the single-OU-snapshot inverse image and smooth fixed-mean inverse instability. The present contribution is the combined nonparametric one-marginal characterization and its two complementary obstructions (finite moment aliases and strong smooth instability), not a claim to first discover Gaussian mixtures, the equilibrium-age identity or compact moment determinacy. Primary full texts and comparable published research records were inspected, with no identified dominating theorem. Because the inverse principle is built from known components, prior-priority risk from an unindexed general Gaussian-mixture inverse result remains real.

## Mathematical value — PASS

For a physically natural harmonic confining dynamics with non-Poisson reset clocks, the result answers which reset histories can be distinguished from a single equilibrium position marginal. It separates ideal mathematical identifiability from finite-moment experimental nonidentifiability, and proves that severe total-variation inverse instability persists even without atoms or an unknown reset mean. The smooth-law instability and exact admissibility criterion give concrete constraints on physical inference and inverse calibration that forward reset distribution formulas alone do not resolve.

## Closest literature and residual limitations

The full source comparison includes Eule–Metzger (2015), Lapeyre–Dentz (2019), Masoliver–Montero (2019), Olsen (2023) and Jolakoski (2026). It does not claim a global novelty certificate; general inverse Gaussian-mixture literature could contain an equivalent instability theorem. The theorem does not infer unknown physical coefficients, produce finite-sample error guarantees, or cover dependent and infinite-mean resets.

Self-review: passed. Independent audit: not yet performed.
