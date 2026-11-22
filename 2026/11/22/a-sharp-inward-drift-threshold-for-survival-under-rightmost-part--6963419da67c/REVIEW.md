# Scientific review

## Correctness — PASS

The first-reset embedding is exact before absorption. Every cycle contributes the iid increment \(Y=-vT+\sqrt{2D}\max_jW_j(T)\), with mean \((v_c-v)/r\). Negative-mean and zero-mean cases are excluded by the strong law and centered finite-variance random-walk oscillation. For the positive-mean case, the present-cycle downward drawdown has finite exponential moment, so a union bound over previous cycle increments yields a finite exponential bound on capture from large launch positions; a positive-probability first-cycle route gives noncapture from all positive launch positions. Strong laws and within-cycle maximal control prove the conditional speed. The coefficient \(\sqrt{\pi Dr/2}\) is checked algebraically from the mean square root of an exponential clock. Numerical checks in `check.py` independently test the Gaussian maximum and mean cycle displacement; none are used as infinite-time proof. Limitations: continuous first-hitting, first group member only, Poisson clock, constant inward drift, independent Brownian coordinates.

## Originality — PASS, qualified

The full HTML text of the April 2026 group-first-hitting paper and extracted sections and appendices of its 2026 theoretical precursor were inspected. The prior papers study a harmonic potential or stationary group-reset kernels rather than the full constant-drift noncapture/capture threshold. A full older arXiv article on one lattice walker returning to its **historical** maximum was inspected: its ballistic law does not identify the current-maximum Brownian group absorption threshold. The accessible prior ledger includes the zero-drift group-escape subcase; that special case is not represented as new. Actual search queries included `rightmost group reset Brownian particles drift absorbing boundary critical velocity`, `first-group-hitting Brownian extreme selection reset drift v critical`, `reset to maximum multi particle Brownian drift critical survival`, and `conditional noncapture ballistic speed in rightmost resetting Brownian group`. No stronger covering result was identified. Negative search results alone are not proof of priority; equivalent unindexed results remain a risk.

## Value — PASS

The sharp drift frontier distinguishes positive-probability permanent avoidance from almost-sure eventual first-hit, including the delicate critical equality, in the exact collective-reset protocol motivating current first-passage work. The frontier scales nontrivially like \(\sqrt{r\log N}\), yields an explicit two-particle threshold, and identifies the ballistic speed *conditioned on survival*. It determines the condition under which group selection can overcome a constant restoring force, rather than merely computing another stationary moment or a narrow arbitrary parameter table. The previously known zero-drift phenomenon is a boundary case, not the mathematical point of the extension.

## Closest literature and residual risks

- Lee, Yang and Lizana (2026), arXiv:2604.24406: exact protocol, harmonic confinement and first-hitting observables, not the drift-controlled transience phase boundary.
- Lee, Yang, Park and Lizana (2026), arXiv:2412.02524: general kernel and harmonic stationary observables, no exact first-hitting critical drift.
- Majumdar, Sabhapandit and Schehr (2015), arXiv:1509.04516: historical-maximum lattice walker rather than synchronized resetting of multiple instantaneous Brownian positions.
- Residual: unindexed equivalent threshold, or an extension of general renewal kernels not recognized as a prior theorem. Other drift forces and finite-time absorption statistics are not established here.

Self-review: passed. Independent audit: not yet performed.
