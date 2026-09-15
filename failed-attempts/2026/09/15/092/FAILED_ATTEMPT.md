# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-sided graded Betti numbers of symmetric mixed ladder determinantal ideals via diagonal degeneration
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20313
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** Groebner degeneration and liaison linkage analysis

## Problem

Let K be an algebraically closed field of characteristic zero, X=(x_ij) the n×n generic symmetric matrix, L a symmetric (mixed) ladder in the sense of Gorla, Definition 1.3, R=K[x_ij:(i,j) in L^+] standard-graded, and I_t(L) ⊂ R the associated symmetric mixed ladder determinantal ideal for an admissible minor-size vector t. Fix a diagonal term order < and put J=in_<(I_t(L)). Determine, for every fixed (n,L,t) and all homological degrees i and internal degrees j, the graded Betti numbers β_{i,j}^R(R/I_t(L)): prove a closed two-sided combinatorial formula in terms of the ladder data (inside/outside corners) and t, and decide whether β_{i,j}^R(R/I_t(L))=β_{i,j}^R(R/J) holds for all i,j.

## Attempted claim

Let K be an algebraically closed field of characteristic zero, X=(x_ij) the n×n generic symmetric matrix, L a symmetric (mixed) ladder in the sense of Gorla, Definition 1.3, R=K[x_ij:(i,j) in L^+] standard-graded, and I_t(L) ⊂ R the associated symmetric mixed ladder determinantal ideal for an admissible minor-size vector t. Fix a diagonal term order < and put J=in_<(I_t(L)). Determine, for every fixed (n,L,t) and all homological degrees i and internal degrees j, the graded Betti numbers β_{i,j}^R(R/I_t(L)): prove a closed two-sided combinatorial formula in terms of the ladder data (inside/outside corners) and t, and decide whether β_{i,j}^R(R/I_t(L))=β_{i,j}^R(R/J) holds for all i,j.

## Research outcome

Target blocked: no general closed two-sided Betti formula or general Betti-equality theorem was proved. Bounded recovery tests verified Betti(R/I)=Betti(R/in(I)) on two instances (5-variable ladder t=2; full 3x3 symmetric t=2) with Groebner and Euler checks, but this instance evidence cannot close the general claim; clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No general closed corner-and-t Betti formula was proved and no mapping-cone minimality theorem was established; the mixed minor-size vector case was not tested; computations are over F_32003 (characteristic-zero lift justified only by monic integral Groebner bases) and cover just two small instances, so they are evidence, not a theorem.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No general closed corner-and-t Betti formula was proved and no mapping-cone minimality theorem was established; the mixed minor-size vector case was not tested; computations are over F_32003 (characteristic-zero lift justified only by monic integral Groebner bases) and cover just two small instances, so they are evidence, not a theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
