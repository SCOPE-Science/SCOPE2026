# Scientific review

## Correctness — PASS
The result is anchored in the normalized radial beta moment identity and the exact Fourier coefficients of the squared quadratic. The sole sign-sensitive term is the three-frequency interference. A sharp AM–GM reduction leaves a strictly convex and coercive scalar optimization whose unique minimizer gives all equality cases. Strict monotonicity in the disk weight follows from explicit monotonic coefficients, and endpoint limits follow from uniform coercivity and convergence. `CHECK.py` passed 1,080 finite checks of formulas, signs, endpoint numbers and finite optimization diagnostics; none substitutes for the analytic global proof.

## Originality — PASS (best-knowledge)
The relevant random Bergman papers are Cheng–Fang–Liu (online 9 April 2021; DOI `10.1093/imrn/rnab018`) and Wang (Filomat 2023; DOI `10.2298/FIL2316215W`). Inspected Wang sections address qualitative randomization and continuity, not the sharp three-sign fourth-power constant. The closest related published published-finding corpus claims concern quadratic weighted Bergman `L4/L2` extremizers, not the sign-related `L4/L4` quotient. The Fourier interference identity does not automatically yield the new uniquely optimized constant or weight monotonicity. The 2021 paper and closest full repository texts remained inaccessible, so historical priority is provisional rather than independently certified.

## Value — PASS
This is a sharp, fully attained minimal-resonance unconditionality benchmark for a natural analytic-function Banach norm. It includes the exact finite-weight optimizer and all equality cases, a strict all-weight behavior law, and a nonzero Gaussian/Fock endpoint. It quantifies a distortion not seen on any two-monomial quadratic support and is relevant to finite-dimensional randomization stability.

## Scope and limitations
The theorem concerns only complex analytic degree-at-most-two polynomials, real sign multipliers, and power-weighted disk fourth norms. It does not solve the full Bergman monomial-basis unconditional constant or arbitrary unit-modulus multipliers. Full 2021 motivating-paper text and two relevant repository full texts were unavailable. Numeric tests are diagnostics only.

Self-review: passed. Independent audit: not yet performed.
