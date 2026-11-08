# Self-review

## Correctness — PASS

The statement applies to Brownian motion in one dimension, a regular lattice of nearest reset sites, and independent iid positive renewal intervals with finite second moment. The proof first obtains the variance rate by conditioning on the renewal intervals and applying renewal reward theory; no interchange of a finite experiment with an infinite limit is needed. The exact rounded-Gaussian second moment has two independently checkable expansions. A Gaussian Mills inequality proves increase of its variance/time ratio for \(\theta\le1/16\), and a decreasing alternating Fourier series proves strict concavity afterward, forcing a unique global optimizer. Equality for arbitrary clocks follows from the renewal length-biased average. The Poisson comparison is proved analytically by positive Taylor coefficients. The reproducible `check.py` passes 528 finite diagnostic assertions and is not the source of the global proof.

## Originality — PASS, with publication-priority qualification

Alston and Bertrand (2024, https://arxiv.org/abs/2401.12772) analyze nearest-site resetting with exponential clocks and obtain the Poisson-rate optimized diffusivity near \(1.16923D\). The new result optimizes over **every admissible independent renewal-clock distribution**, identifies its unique periodic extremizer, and establishes a sharp universal ceiling near \(1.33248D\). The accessible full text of Schneeweiss, Komlos and Ahmad (2006, https://epub.ub.uni-muenchen.de/1847/1/paper_479.pdf), Section 6, gives rounded-Gaussian moment formulas but does not establish the renewal optimization and the strict clock comparison. Tricker (1984, DOI 10.2307/2987741) is relevant prior normal-rounding literature, but its full text was not accessible; exact moment identities are explicitly credited. Broader unindexed variance/quantization inequalities could affect publication priority and require an independent literature audit. Targeted searches of published literature did not reveal a directly covering theorem; absence of a search hit is not novelty proof.

## Mathematical value — PASS

The natural experimental choice of binding/reset interval distribution cannot be inferred from the previously optimized exponential-clock model. The proof resolves the full unconstrained renewal-clock design problem with a sharp constant and uniquely optimal deterministic protocol. Its rigorous separation \(D_{\mathrm{eff}}^{\mathrm{periodic}}>5D/4>D_{\mathrm{eff}}^{\mathrm{Poisson}}\) demonstrates that allowing a different clock family materially changes the attainable physical transport, rather than merely reformulating a known Poisson rate. The exact rounded-normal moment by itself is known and is not offered as the new contribution.

## Scope and residual risks

Only iid, Brownian-independent positive renewal intervals with finite second moment and instantaneous nearest projection to a one-dimensional regular lattice are covered. Clock feedback, irregular arrays, slow returns, heavy-tailed intervals lacking the stated moment condition, and a general multidimensional analogue are unproved. The Tricker full-text access limitation, possible preexisting sharp rounded-Gaussian optimization inequalities, and absence of independent scientific assessment remain relevant.

Self-review: passed. Independent audit: not yet performed.
