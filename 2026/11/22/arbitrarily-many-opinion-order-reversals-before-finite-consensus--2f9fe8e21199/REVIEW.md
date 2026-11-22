# Scientific review

## Correctness: PASS
The fixed-step directed-confidence rule and strict threshold semantics are stated explicitly. Exact rational powers of the one-way three-cycle matrix establish a sign flip every six updates and a similarity scaling every twelve. The minimum of all twelve phase gaps is exactly \(1/2916\), so the declared positive reverse thresholds cannot activate prematurely. The full base orbit has a verified five-stage gate sequence and reaches exact consensus for the first time at update 17, with value \(236213/708588\). Scale-conjugacy proves the precise stopping time \(12m+17\) and unanimous value for every nonnegative integer \(m\), while a nonnegative scalar difference multiplier excludes strict reversals for two agents. All supporting finite computations were reproduced by exact-rational `checker.py`; its finite tests are cross-checks, not a substitute for the scaling proof.

## Originality: PASS, subject to historical priority risk
The 2026 Huang–Ma–Shi–Chen article supplies the edge-heterogeneous update model and sufficient separated-cluster convergence theorems, but not the stated arbitrarily many temporary rank inversions with all confidences positive, exact switching timetable, or minimal three-agent boundary. General stochastic-matrix spectral ideas predict oscillatory transients, and bounded-confidence theory establishes other finite-consensus mechanisms; neither generic fact is presented as original. The closer published records on three-agent adaptive confidence and rank reversals under varying influence concern different update laws or a varying parameter rather than temporal order along one fixed-threshold trajectory. Relevant primary full HTML was inspected, and the accessible abstracts/records were compared by hypotheses and implication rather than by title alone. An earlier general lemma could still subsume the result; searches cannot certify uniqueness, and inaccessible full texts are identified in the structured audit.

## Value: PASS
The construction identifies a sharp population-size boundary for unstable **relative ranking** in a model that nonetheless reaches **exact finite-time consensus**, with a constructive logarithmic delay as the smallest strictly positive trust bound vanishes. Exact activation and consensus-time formulas separate transient repeated reversals from genuine periodic disagreement. That matters when analyzing time-series instability or assessing finite-time predictions from final consensus alone; it is not a claim about empirical social-media behavior.

## Closest literature and limitations
- Huang, Ma, Shi and Chen, *Future Internet* 18 (2026), 355: founding model and sufficient convergence, not the transient ranking theorem.
- Li, Luo and Porter, *SIAM J. Appl. Dyn. Syst.* 24 (2025), 994–1041: adaptive-confidence updates and convergence-time observations; not the fixed positive directed-threshold family.
- 2023 *Automatica* bounded-confidence survey: generic finite-consensus material, accessible excerpts only.
- Published mathematical records on a three-agent adaptive confidence transition, and rank reversals as influence strength varies: distinct claims; full files were not accessible during comparison.

This is a deliberately explicit family, not a complete classification of all possible reversal counts. Priority remains literature-bounded. No empirical causal or independent scientific certification is asserted.

Self-review: passed. Independent audit: not yet performed.
