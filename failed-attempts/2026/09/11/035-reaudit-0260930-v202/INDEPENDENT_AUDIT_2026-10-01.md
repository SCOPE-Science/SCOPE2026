# Independent audit — 2026-10-01

## Final scientific disposition

**FAILED**

## Correctness (C): PASS

Independent arithmetic checks confirm 10069 is prime, 10069 is 7 modulo 9, D=3·10069=30207, the Mordell coefficient is -394183950768, and the cubic-residue Euler value is 5363 with cube 1 modulo 10069 but value not 1. These data satisfy the contrapositive hypothesis of Das–Jha Proposition 2.7, which proves rank zero/non-cube-sum in this family.

## Originality (O): FAIL

Das–Jha Proposition 2.7 already states that for n=3l with prime l congruent to 7 modulo 9, cube-sum implies cubic residue symbol (3/l)_3=1, and its proof establishes the contrapositive by rank zero. The record's l=10069 case is therefore a direct finite specialization of a published general theorem.

The comparison included equivalent formulations, broader coverage, exact-instance searches, and direct implication from prior theorems.

## Value (V): FAIL

The exact integer 30207 is selected from an arbitrary narrow numerical strip and the conclusion is mechanically implied by the general criterion after one modular exponentiation. No separate structural boundary or motivated exact invariant is established.

## Sources inspected

- https://arxiv.org/abs/2508.05361
- https://arxiv.org/abs/2207.12487

## Residual risks

- The arithmetic specialization is correct, but correctness and reproducibility do not overcome direct prior implication.
