# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Definite BDP toric nonvanishing input for 43a1 over Q(sqrt(-11)) mod 31
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1210
- **Disposition:** NO_RESULT
- **Domain:** anticyclotomic BDP p-adic L-values
- **Method:** Brooks finite toric sum over class number 1 with inert/split local corrections

## Problem

Let E/Q be the elliptic curve 43a1 given by y^2+y=x^3+x^2 of conductor 43, let K=Q(sqrt(-11)) of discriminant -11, and let p=31. Preliminary gate (failure is NO_RESULT, not disproof): verify p is good ordinary by counting E(F_31), verify 43 is inert in K and p splits in K by Kronecker symbols, and verify mod-31 irreducibility by explicit traces. Decided claim (single definite analytic input for the bipartite Euler-system step, no tower): let chi_0 be the explicit unramified anticyclotomic character of K of smallest conductor and order whose twisted root number is +1, determined in-hour from the root-number formula. Decide whether the BDP toric period value at chi_0 is nonzero modulo 31, computed via the Brooks finite toric sum over Pic(O_K) (class number 1, single term) with the explicit local correction factors at the inert prime 43 and the split-31 ordinary stabilization. A complete answer proves nonvanishing with the certified nonzero residue, or rigorously disproves it by certifying vanishing to proven precision with a Waldspurger cross-check that converts the zero into a forced definite-Selmer rank jump with explicit witnesses.

## Attempted claim

Let E/Q be the elliptic curve 43a1 given by y^2+y=x^3+x^2 of conductor 43, let K=Q(sqrt(-11)) of discriminant -11, and let p=31. Preliminary gate (failure is NO_RESULT, not disproof): verify p is good ordinary by counting E(F_31), verify 43 is inert in K and p splits in K by Kronecker symbols, and verify mod-31 irreducibility by explicit traces. Decided claim (single definite analytic input for the bipartite Euler-system step, no tower): let chi_0 be the explicit unramified anticyclotomic character of K of smallest conductor and order whose twisted root number is +1, determined in-hour from the root-number formula. Decide whether the BDP toric period value at chi_0 is nonzero modulo 31, computed via the Brooks finite toric sum over Pic(O_K) (class number 1, single term) with the explicit local correction factors at the inert prime 43 and the split-31 ordinary stabilization. A complete answer proves nonvanishing with the certified nonzero residue, or rigorously disproves it by certifying vanishing to proven precision with a Waldspurger cross-check that converts the zero into a forced definite-Selmer rank jump with explicit witnesses.

## Research outcome

Preliminary gate for 43a1 over Q(sqrt(-11)) at p=31 fully verified (good ordinary, inert/split, mod-31 irreducibility) plus maximal order and three T_2 stable planes, but the BDP toric-period residue step proved unfinishable in this pass, so the outcome is an honest NO_RESULT with CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The BDP toric-period residue was not computed: the class set, right orders, unit groups, Brandt eigenvector, Gross point, and stabilized mod-31 residue were not completed to auditable standard. Only the preliminary gate and the maximal-order plus T_2 stable-plane prefix are verified by exact scripts; the Waldspurger cross-check and the nonvanishing-vs-vanishing decision were never reached.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The BDP toric-period residue was not computed: the class set, right orders, unit groups, Brandt eigenvector, Gross point, and stabilized mod-31 residue were not completed to auditable standard. Only the preliminary gate and the maximal-order plus T_2 stable-plane prefix are verified by exact scripts; the Waldspurger cross-check and the nonvanishing-vs-vanishing decision were never reached.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
