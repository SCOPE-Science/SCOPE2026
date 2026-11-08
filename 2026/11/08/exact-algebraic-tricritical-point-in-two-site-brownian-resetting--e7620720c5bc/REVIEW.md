# Scientific review: algebraic tricritical coordinate in two-site resetting

## Correctness — PASS

The physical Brownian-ring renewal expression in arXiv:2605.08414, equation (31), becomes the dimensionless formula in RESULT.md when the antipodal and nearer resetting angles are inserted and the initial distribution matches the resetting distribution. Independent formal-series division gives the stated polynomials \(P_1,P_2\). The exact polynomial elimination identity forces \(p=(5b-2)/(3b^3)\) and the cubic \(Q(b)=0\). Monotonicity of \(Q\) and the sign restriction \(0<p<1\) leave precisely one physical zero-rate simultaneous derivative root. The cubic Taylor coefficient is strictly positive by an exact rational root bracket and a quadratic sign certificate; the local-coordinate Jacobian is nonzero. A Taylor/implicit-function argument establishes the small-rate local square-root branch. `verify.py` was executed and passed the symbolic identities and rational sign certificates. The proof does not infer any universal claim from finite numerical tests.

## Originality — PASS (qualified)

The nearest same-object source is Julián-Salgado et al., arXiv:2605.08414v1, section V.2 and Table 1: it introduces the zero-rate tricritical derivative conditions and gives approximate coordinates obtained numerically, without an exact algebraic polynomial, proof of uniqueness in the physical rectangle, positive cubic coefficient, or transverse local square-root coefficient. Its September 2026 accepted version is the same work, not a second independent result. The earlier arXiv:2311.11897 treats a half-line instead of a circle and gives different critical behavior, not this geometric polynomial. A search of public indexed mathematical findings and available historical claims found no equivalence or broader implication covering the present exact classification. Because indexed and full-text coverage is not exhaustive, independent priority investigation remains advisable.

## Value — PASS

The source treats its tricritical coordinates as mathematically difficult enough to compute numerically. The exact cubic, proof that precisely one branch lies in the physical probability range, and nonzero third rate correction convert an approximate point in a real phase diagram into a reproducible algebraic invariant. The local onset law specifies the singular scaling of the emergent minimizing rate. Both quantities are directly tied to the phase-boundary structure of the stochastic-search model; they are not arbitrary finite samples, substitutions, or a repackaging of an already exact table.

## Closest literature and limitations

- P. Julián-Salgado et al., *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1 (2026-05-08), especially equations (28), (31), (38) and Table 1. The general renewal law, phenomenon and numerical tricritical coordinates are prior work.
- The same authors, *Critical and tricritical transitions in diffusion with stochastic resetting on a ring*, accepted 2026-09-29, DOI:10.1103/2fsc-jkq8. Its accessible accepted-paper page supplies only abstract-level detail, so changes in final full text remain a priority risk.
- P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023-11-20): related half-line two-site restart analysis, not a closed-ring algebraic tricritical classification.

The claim is limited to zero-rate tricritical derivatives for the specified diametric geometry and its reflected counterpart. The emerging positive-rate minimizer is certified locally, not globally; arbitrary resetting distributions and independent validation are out of scope.

Self-review: passed. Independent audit: not yet performed.
