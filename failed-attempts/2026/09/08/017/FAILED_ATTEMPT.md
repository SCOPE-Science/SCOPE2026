# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified S8 extremal Kronecker multiplicity 17 and full containment in the tensor square of (4,2,1,1)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 94
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Representation Theory
- **Method:** Murnaghan-Nakayama character recursion with exact inner-product verification

## Problem

Let g(lambda,mu,nu) = (1/8!) * sum_C |C| chi_lambda(C) chi_mu(C) chi_nu(C) for partitions lambda,mu,nu of 8, with irreducible S8 characters chi computed by exact Murnaghan-Nakayama rim-hook recursion. Compute the full 22^3=10648-entry exact table over Z; prove (a) the global maximum is 17, attained uniquely up to S3 permutation at ((4,2,1,1),(4,2,1,1),(4,2,1,1)); (b) the tensor square [(4,2,1,1)]^{otimes 2} contains all 22 irreducibles of S8 with explicit multiplicities [1,1,2,2,4,4,4,4,5,5,6,6,6,6,8,12,12,13,13,14,14,17] in the order [(8),(1^8),(7,1),(2,1^6),(6,1,1),(4,4),(3,1^5),(2^4),(6,2),(2^2,1^4),(5,3),(5,1^3),(4,1^4),(2^3,1^2),(3,3,2),(4,2,2),(3,3,1,1),(5,2,1),(3,2,1^3),(4,3,1),(3,2^2,1),(4,2,1,1)]; (c) the S8 table has 5048 nonzero entries, and the S6/S7 companion maxima are 5 at ((3,2,1)^3) and 9 at ((4,2,1)^3) up to permutation. Every entry must pass exact-divisibility (8! divides the class sum), nonnegativity, S3 and transpose symmetries, hook-formula dimension cross-checks, and class-size sum 40320.

## Attempted claim

The S8 Kronecker maximum is exactly 17, uniquely (up to permuting the three arguments) at ((4,2,1,1)^3); the square [(4,2,1,1)]^{otimes 2} = sum_nu g_nu [nu] has all 22 coefficients >= 1 (min 1 at (8) and (1^8), full list as in problem_statement); the complete S8 table has 5048/10648 nonzero entries; companion certified maxima: S6 max 5 at ((3,2,1)^3) with 511/1331 nonzero, S7 max 9 with 1599/3375 nonzero (up to S3 permutation, S7 maximizer family includes ((4,2,1),(3,2,1,1),(3,2,1,1)) permutations). Proof by from-scratch Murnaghan-Nakayama plus exact inner product, independently replayed via a second character-table implementation (e.g. Sage SymmetricFunctions/GAP).

## Research outcome

Certified exact S6/S7/S8 Kronecker tables via two independent Murnaghan-Nakayama implementations: S8 max 17 unique at (4,2,1,1)^3 with 5048/10648 nonzero and a 22/22 full-containment square slice; companions S6 max 5, S7 max 9; 24-check verifier ALL PASS.

## Why this attempt failed

Failed axes: value.

value: FAIL under the unexplained-enumeration / textbook-method / parameter-substitution bars, even taking correctness and narrow novelty as given. Method is textbook Murnaghan-Nakayama rim-hook recursion plus the standard character inner product (DRAFT Sec.6 concedes method is the audit instrument and proof is purely computational with no analytic explanation of why (4,2,1,1) is extremal). Theorems T1-T4 are direct read-offs from the 10648-entry brute-force table: a global max, a row slice, companion maxima, and neighbour-slice nonzero fractions. The witness shape was selected retrospectively as the computer output, not motivated ex ante; generic GCT/quantum-marginal/Schur-positivity motivation does not single out n=8 or (4,2,1,1). The single n=8 full-containment datum (22/22, min 1) does not advance the staircase-Saxl or square programs it cites: n=8 admits no staircase partition, no infinite family, stability statement, formula, or technique is given, and the contrast data are further read-offs. The work repeats the census pattern of prior internal result SCOPE006 (n=12 vanishing/maximum census) at smaller n with the same instrument, i.e. a parameter-substitution-like smaller instance. Regression-oracle / test-bed utility is engineering convenience, not an independently retrievable research finding; the fallback's own framing as a regression dataset confirms this. This is exactly the 'unexplained enumeration even if correct and new' and 'textbook restatement / mere parameter substitution' category the value gate must reject.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Computational (not analytic) proof; second implementation is independent from-scratch MN, not Sage/GAP (unavailable in env); triage-level originality only, no priority claim; S7 argmax family confirmed as (4,2,1)^3 + 3 perms of ((4,2,1),(3,2,1,1),(3,2,1,1)).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
