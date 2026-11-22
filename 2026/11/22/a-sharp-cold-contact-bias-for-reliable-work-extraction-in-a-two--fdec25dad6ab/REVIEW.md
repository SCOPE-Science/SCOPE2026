# Scientific review: exact bath-time allocation in a Gaussian Otto engine

## Correctness — PASS

The mathematical claim is restricted to an overdamped, one-dimensional harmonic engine, in its unique period-stationary Gaussian law, with two instantaneous stiffness changes, a fixed sum of bath-contact times and exactly equal coordinate-decay rates in the two baths. The period-stationary variance recursion and the hot-contact cross-covariance determine the full bivariate Gaussian pair at the work jumps. Gaussian fourth-moment identities give the single-cycle mean and variance of work; factoring a difference of squares into a product of two jointly Gaussian linear forms gives the *exact*, not approximated, positive-work probability. Its strict monotonicity in reliability is algebraically proved. The derivative of squared reliability has the sign of an explicitly exhibited cubic, which has exactly one positive root. The source algebra, boundary behavior, strict cold-biased location, and both asymptotics are checked in the proof and in `verify.py`. Numerical checks are corroborative, not infinite certification.

## Originality — PASS, qualified

The closest openly inspected sources are: Zheng, Hänggi, and Poletti, *Phys. Rev. E* 94, 012137 (2016), particularly the model and Sections III–V, including quantitative optimization of bath allocation for *mean work and efficiency* in a quantum Otto engine; Iida, Negoro, and Yamada, *PTEP* 2022, 043A02 (full accessible article), on second moments and a Gaussian proxy for success in a different continuously breathing Brownian engine; and Shastri and Venkatesh, arXiv:2204.04782, especially Sections II–V and appendices, on reliability optimized by varying finite-time unitary-work-stroke asymmetry, with hot/cold thermalization split fixed to one-half in principal examples. The latter paper explicitly presents a systematic study of thermal-stroke asymmetry on power and fluctuations as a follow-up. Published general covariance methods are credited. None of the inspected works supplies the exact global cubic allocation with strict separation from the mean optimum plus co-optimization of the *actual* sign probability for the restricted overdamped engine. Separately queried semantically related mathematical-research records concern reset optimization, inertial work pulses, long-run fluctuation laws, or information-distance goals, not this exact theorem.

The residual risk is that a separate prior work or an implicit consequence of a broader control theorem establishes the same conclusion. Search and full-text comparison are evidence of non-coverage in the inspected material, **not a proof of absolute publication priority**. Related models differ, and there is no assertion that the published generic covariance law is new.

## Mathematical value — PASS

The result separates two experimentally meaningful single-cycle objectives: maximizing average work and maximizing either its signal-to-noise ratio or its exact positive-extraction chance. For every finite cycle time it gives a *unique* optimum with a strict, all-parameter cold-bath contact bias; a cubic characterizes it without numerical optimization, and the short- and long-cycle laws establish its design scale. The non-Gaussian sign probability is co-optimized exactly, avoiding the normal-approximation caveat in related Brownian-engine treatments. This is a structural phase-free classification for a motivated optimization problem, not simply re-evaluating known second moments.

## Boundaries and residual risks

The conclusion applies to one-cycle (not long-run time-series) reliability in periodic steady operation. Equality of coordinate-relaxation rates is a substantial, explicitly stated restriction and might require varying mobility; mechanical switching and auxiliary bath-control costs are excluded. The work-stroke durations are idealized to zero. None of the proofs cover nonlinear traps, inertia or unequal decay rates. Originality remains a same-author scientific assessment without independent priority confirmation.

Self-review: passed. Independent audit: not yet performed.
