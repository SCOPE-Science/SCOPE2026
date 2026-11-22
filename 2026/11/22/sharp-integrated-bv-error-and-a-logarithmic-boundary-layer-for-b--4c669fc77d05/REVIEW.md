# Scientific review: sharp integrated BV error for Baskakov point sampling

## Correctness — PASS

The representation of any right-continuous Jordan-BV input as an integral of one-jump functions reduces the exact operator norm to step responses. On a sampling cell, negative-binomial tails are beta-prime CDFs; the integrated error is strictly convex in jump location and therefore maximizes at the cell ends (with one-sided limits included). The full-line absolute-moment identity and a uniform gamma-ratio central limit bound give the leading norm constant. The beta-prime Gaussian moderate tail balances the loss in the local standard deviation and gives the \(\sqrt{2}\) coefficient of logarithmic jump retreat. The accompanying script confirms 324 tail evaluations, 81 original-integral checks, and 81 cell endpoint checks; these are finite consistency tests, not the proof of the limiting theorem.

## Originality — PASS, qualified

Abel–Gupta–Ivan (2002) derive pointwise BV rates and discontinuity limits for Baskakov–Kantorovich integral variants. Gupta–Abel (2004) use a Durrmeyer integral modification, and Patel–Mishra (2014) describe a modified integral operator and BV derivatives. No inspected theorem subsumes the exact integrated identity-error norm of classical negative-binomial point sampling, its finite beta-prime formula, or the sharp logarithmic retreat of its norming jump. The previously known Poisson/Szász–Mirakjan–Kantorovich integrated window law is analogous, but its operator, endpoint variance and normalization differ. The Gupta–Govil (2006) original was not fully accessible and leaves a genuine historical-priority risk. Actual indexed and historical-claim comparisons are recorded in `AUDIT.json`.

## Value — PASS

The boundary placement of a discontinuity determines how much binomial-type averaging error is visible inside a finite observation window. The exact degree-wise formula gives an executable benchmark, and the asymptotic law identifies a nonstandard logarithmic transition (rather than only a leading order of convergence) with a kernel-dependent variance constant. This is a structural, motivated operator-norm fact, not only a numerical rate estimate.

## Limitations

The input must have a chosen right-continuous point representative; only the classical Baskakov point sampler with \(n\ge2\), the observation interval \([0,1]\), and whole-half-line Jordan variation are covered. No all-degree winning-cell classification or general norm attainment is claimed. Moderate-deviation calculations establish asymptotic but not explicit finite-n error bounds. Some relevant historical sources were read only in part or at the bibliographic level; independent originality and correctness checks remain outstanding.

Self-review: passed. Independent audit: not yet performed.
