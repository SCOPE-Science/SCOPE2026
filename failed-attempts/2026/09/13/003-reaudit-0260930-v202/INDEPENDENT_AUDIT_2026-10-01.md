# Scientific audit — 2026-10-01

## Final claim

Binary-cubic discriminant conormal excess at triple-root orbit: Tor-amplitude [0,1], excess rank 1, length 2

## Correctness — FAIL

The local derivative computations are correct: at p=x^3 the discriminant gradient vanishes, the Hessian has only the dd entry -54, and on the transverse slice f=-4c^3-27d^2 the Jacobian quotient is the Jacobian quotient with relations c squared and d of length 2. But that quotient is the critical locus of f, not the defined intersection W=Y x_{T*Y} N^*(D/Y). Calaque's conormal-intersection formula identifies the zero-section/conormal fiber product with the (-1)-shifted cotangent of D (for n=0), so its classical truncation contains D rather than being the isolated length-2 Jacobian scheme. Equivalently, classically the conormal intersection has equations Delta=0 and lambda dDelta=0 and contains the entire lambda=0 discriminant. Thus the claimed W≃Crit(Delta), finite length w=2, and ensuing excess identity are false for the stated W.

## Originality — PASS

Resultary returned only this record for the exact binary-cubic triple-root computation. Calaque and PTVV provide the general shifted cotangent/conormal and Lagrangian-intersection framework, but no inspected source states the record's exact local numerical package. Originality of the intended local example is therefore plausible, though it cannot rescue the false identification.

## Scientific value — PASS

A correctly formulated first singular binary-cubic discriminant example with nontrivial stabilizer is a natural test case for shifted conormal intersections and excess geometry. The object, orbit, and A2 cusp are mathematically canonical rather than arbitrary. The scientific rejection is correctness, not lack of motivation.

## Sources inspected

- **Damien Calaque, Shifted cotangent stacks are shifted symplectic** (https://arxiv.org/abs/1612.08101): DECISIVE_CORRECTNESS_CONTRADICTION. The paper defines the shifted conormal and states that the fiber product of two shifted conormals is the shifted cotangent of the corresponding fiber product; taking one map to be the identity yields the negative-one shifted cotangent of D, not Crit(Delta).
- **Pantev-Toen-Vaquie-Vezzosi, Shifted Symplectic Structures** (https://arxiv.org/abs/1111.3209): GENERAL_BACKGROUND. Supports the general shifted-symplectic setting, not the record's finite-length identification.

## Residual risks

- The local A2 Jacobian length 2 is genuine but belongs to a different derived critical-locus construction.
- A substantive repair would require redefining W and changing RESULT/SLOGAN, so no audit-only repair is valid.

## Disposition

**failed** — at least one required scientific axis does not pass. The original scientific files are preserved unchanged as evidence.
