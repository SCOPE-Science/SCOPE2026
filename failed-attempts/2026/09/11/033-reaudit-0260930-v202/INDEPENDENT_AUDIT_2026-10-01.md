# Independent audit — 2026-10-01

## Final scientific disposition

**FAILED**

## Correctness (C): UNRESOLVED

The finite motif, incidence and square-class arithmetic are internally consistent, but the final lifting and Grothendieck-Witt conclusions invoke Markwig–Payne–Shaw under a standing 2-divisible-value-group hypothesis. The stated field Q((t)) has value group Z. The package asserts an unramified-part extension but does not prove a replacement theorem, so the 0-rational-lift and 14H conclusions are not fully justified for the stated field.

## Originality (O): FAIL

The substantive mathematical mechanism is already supplied by the cited primary literature: Cueto–Markwig classify the bitangent shapes, while Markwig–Payne–Shaw give the twist-based rationality criterion, the 0-or-4 theorem, and Theorem A.2 assigning 2H to shapes A, B and C. The chosen coefficients and the radicand -2 are a finite specialization of those published rules rather than an implication-independent theorem.

The comparison included equivalent formulations, broader coverage, exact-instance searches, and direct implication from prior theorems.

## Value (V): FAIL

The package explicitly presents a single-quartic fallback and leaves the cone-wide census open. The exact initial coefficient choice is engineered to produce a nonsquare twist and is not independently motivated as a natural boundary, classification case, or invariant needed downstream.

## Sources inspected

- https://arxiv.org/abs/2207.01305
- https://arxiv.org/abs/2004.10891
- https://arxiv.org/abs/1710.10126

## Residual risks

- A separate theorem extending the cited tropical lifting/GW machinery from 2-divisible value groups to Q((t)) could repair correctness, but it would not remove the direct-specialization originality problem.
