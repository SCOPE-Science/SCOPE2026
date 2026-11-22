# Scientific review: quadratic resonances and nonexponential mean relaxation

## Correctness — PASS

The claimed dichotomy follows from the explicitly specified regenerative process. Conditioning on its last reset yields the renewal convolution in RESULT.md, with a two-point duration law. If the durations have a common maximal span, the elementary recurrence has a rational generating function. Coprimality makes \(1\) its only unit-circle singularity; other poles lie strictly beyond the unit disk and the renewal weights approach the reciprocal mean duration exponentially. The resulting finite atomic law has exact total mass one and the stated sawtooth mean, including the after-reset boundary convention.

For irrational duration ratio, the directly Riemann integrable single-flight test kernel permits the classical nonarithmetic key renewal theorem and gives uniform weak position limits. Finite-time atomicity is immediate from the positive minimum duration. The mean's Laplace transform has an explicitly computed numerator; continued-fraction approximants, an analytic implicit-function expansion, and a noncancellation estimate give genuine poles tending to the imaginary axis. Analytic continuation then excludes exponential decay for the mean itself. The critical quadratic root coefficient and normalization were reconstructed and checked.

The standalone checker passed 19,578 finite exact-arithmetic and complex-root consistency assertions. These tests neither prove weak convergence nor certify infinitely many roots; those statements rely on the analytical arguments. The mathematical assumptions and quantifiers are explicit, with no use of simulations as proofs.

## Originality — PASS, with a stated priority risk

The initiating full paper by Das–Majumdar–Pal (arXiv:2611.16733v1, 12 November 2026) gives the ballistic resetting renewal formula, uniform invariant spatial occupation for continuous speed distributions, and the single-speed periodic limit. The assessed claim is the *irrational two-speed mean-position nonexponential theorem* with a quadratic noncancelling pole formula. The arithmetic phase formula is standard lattice-renewal context and is **not** counted as the new result. The irrational mean-observable pole statement was not found in the inspected Sections II–III and VII–VIII, including the original results and conclusion. The present work does not claim the general renewal theorem or the single-speed result as new.

Boyer (arXiv:1506.07625), especially Section 2.2.2 and Proposition 4.7, provides established higher-level Diophantine renewal-spectral theory and general obstructions to exponential renewal convergence. This is the strongest comparator: it may imply parts of the qualitative story when specialized. The exact physical mean-observable noncancellation and quadratic curvature of its poles are established directly here and were not identified there; ordinary rational phase weights are not assessed as novel. Searches also compared other resetting and renewal papers and published mathematical records by mathematical implication rather than title only. No exact table or published result covering the combined assertion was identified. **Residual risk:** specialized classical renewal literature may contain an equivalent two-point formula or implicit pole expansion; failed searches do not certify historical priority. Independent expert priority checking remains necessary.

## Value — PASS

The simplest genuinely random atomic velocity distribution exhibits a discontinuous arithmetic distinction overlooked by the continuous-density versus deterministic-speed dichotomy: commensurate draws retain a periodic atomic phase ensemble, whereas incommensurate draws relax weakly to uniform occupation but not at any exponential rate in even the mean coordinate. The result gives exact phase-resolved weights and a computable high-frequency resonance scale, explaining why random velocity selection alone does not guarantee ordinary exponential mixing. This is a natural boundary for the original physical model, not an arbitrary parameter slice. It also clarifies why total variation cannot capture weak mixing of atomic trajectories to a continuous invariant law.

## Closest literature and limitations

- Das, Majumdar and Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, https://arxiv.org/abs/2611.16733 , Sections II–III and VII–VIII; original renewal construction, density-based uniformity and deterministic periodic law.
- Boyer, *The speed of convergence in the renewal theorem*, https://arxiv.org/abs/1506.07625 , Sections 2 and 4; general Diophantine spectral theory and non-exponential convergence obstructions.
- Classical arithmetic and nonarithmetic key renewal theorems are credited as proof tools.

The statement is restricted to exactly two atomic flight durations, deterministic travel between instantaneous resets, and zero observation noise. It proves no optimal rate within the nonexponential class and is not a theorem about continuous-velocity distributions or broad renewal kernels.

Self-review: passed. Independent audit: not yet performed.
