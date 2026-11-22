# Scientific review

## Correctness (PASS)

The parity difference of short signed-binary strings obeys the stated even/odd signed recurrences with explicitly checked base cases and the excluded leading pair accounted for. The eight disjoint sign states are invariant under both unimodular digit transitions, and their rational series yield the exact positive-sign frequency. First and second moment formulas follow from rigorously telescoped adjacent products and the boundary values at powers of two. The standalone verifier checks the independent finite examples, without relying on those examples for the infinite proof.

## Originality (PASS, inspected-evidence scope)

The 2023 Anders--Dawsey--Gupta--Vandehey paper proves the *unweighted* representation count; OEIS A145865 already records the signed recurrence. Monroe's 2021 analysis weights *fixed-length* representations by zero digits. The 2026 Fibonacci zero-set result proves exact parity-balanced indices but merges positive and negative imbalance signs in one ratio state and does not state the dyadic sign count or energy. Those earlier claims are neither misattributed nor reproduced as new. The eight-state refinement and exact moments are the claimed additions. A possible earlier unindexed signed-moment calculation is a residual priority risk.

## Mathematical value (PASS)

The statistic arises naturally when the signed representations of an integer are separated by the parity of the number of negative digits. The result settles a sharp all-depth sign-classification question and the exact fluctuation size: a positive class of exactly half of dyadic integers coexists with a Fibonacci exceptional set, a logarithmically small aggregate difference, and a mean square growing exponentially. This complements the previously known total and zero-set counts and is not a small arbitrary finite refinement.

## Limits

Dyadic cutoffs only; the results give no full distribution by absolute value, no bound at arbitrary cutoffs, and no independent validation.

Self-review: passed. Independent audit: not yet performed.
