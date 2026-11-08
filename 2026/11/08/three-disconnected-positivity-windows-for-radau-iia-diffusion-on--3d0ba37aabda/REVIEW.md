# Scientific review: Radau IIA star positivity windows

## Correctness

**PASS.** The theorem fixes the unweighted combinatorial Laplacian, the exact completed two-stage Radau IIA stability function and all quantifiers. Orthogonal projectors for eigenvalues \(0,1,m+1\) give four closed-form entry types. Every positive-step off-diagonal is positive, reducing full entrywise nonnegativity to two diagonal-polynomial inequalities. A discriminant determines the hub threshold, while a concavity argument in \(m\) and the explicit strictly positive polynomial certificate at \(m=10\) settle all smaller stars. At \(m\ge11\), an exact negative evaluation at \(h=8\), endpoint signs and Descartes' rule give exactly two simple positive leaf roots. The root ordering and asymptotic laws follow analytically. Standard-library exact-rational tests give additional cross-checks but are not the infinite proof.

## Originality

**PASS on the compared evidence, with remaining literature risk.** The Radau method and its scalar stability function are not new. Brugnano–Iavernaro–Magherini (2013) concern its efficient implementation, Flaig (2013) its use in parabolic optimal control, Bresten et al. (2013) sufficient/necessary SSP restrictions for different explicit multistep formulas, and Kovács–Li–Lubich (2015) maximal regularity of A-stable schemes. None of the materially inspected relevant sections supplies the exact two-star-diagonal sign calculation or the three disconnected endpoint-positivity intervals. Known analyses of alternative methods on stars and Radau IIA on double-stars do not imply these exact method–graph thresholds by parameter substitution. Query comparisons tested Padé [1/2], Radau IIA star, star diffusion positivity and nonnegative transition matrices. The literature search cannot exclude unindexed equivalent results.

## Value

**PASS.** Positivity (mass-preserving nonnegative transport from nonnegative input) is a meaningful numerical safety constraint distinct from \(A\)- and \(L\)-stability. The sharp threshold at eleven leaves separates unconditional positivity from two distinct, nonmonotone failure windows. The exact safe-step set provides an implementable, all-step criterion; the hub and leaf failures show that a larger step can restore positivity, but another later range can lose it again. The asymmetric asymptotic scaling of the two windows is structurally informative rather than a routine single-timestep check.

## Evidence and limits

The core algebra is recorded in `RESULT.md`, and `verify.py` checks the rational matrix equation and the polynomial identities directly, yielding `VERIFY_OK 2228`. The result is restricted to uniform unweighted star graphs and completed two-stage Radau IIA endpoints. No assertion is made about internal stages, other graphs or higher-stage methods. Literature-search coverage is incomplete, and verification remains same-model, not independent.

Self-review: passed. Independent audit: not yet performed.
