---
audit_date_utc: 2026-10-01
status: failed
record_id: SCOPE-20260915-009
---

# Scientific audit

## Final claim

No single Delsarte polynomial of degree at most 10 can prove the unconditional \(48\)-dimensional \(T_1\)-avoiding bound \(52416000\) while attaining equality at the known extremal support; equality forces the displayed degree-10 polynomial, whose Gegenbauer coefficients in degrees 3 and 4 are negative.

## Correctness — PASS

The equality-support argument was reconstructed from the Delsarte LP conditions. The eight required support zeros, together with even multiplicity at the two interior sign-change-free zeros, exhaust degree 10 and force the polynomial up to scale. Exact rational recomputation gives \(P(1)/P_0=52416000\), \(f_3=-8507/67651200\), and \(f_4=-25333/60134400\), so the unconditional nonnegative-coefficient condition fails.

Checked sources: artifacts/exact_certificate.py; Boyvalenkov--Cherkashin, arXiv:2312.05121

Residual risk: The statement concerns the single-polynomial Delsarte method with equality at the known support; it does not exclude higher-degree or stronger methods.

## Originality — FAIL

The audited obstruction is a mechanical corollary of the published LP equality conditions and the same paper's degree-11 construction. The paper explicitly says that a simple zero at \(-1\) does not work and therefore doubles that zero; removing one \((t+1)\) factor gives precisely the forced degree-10 candidate. The uniqueness step is elementary degree counting from the published support and sign conditions, so the result is covered as an implication even though the exact negative pair \(f_3,f_4\) is not tabulated there.

### Equivalent Formulations

Searches: degree ten Delsarte impossibility 48 dimensional T1 avoiding 52416000; simple zero at -1 degree 10 Boyvalenkov Cherkashin

Evidence: Theorem 3.1 gives equality-support zeros; Theorem 5.1 constructs the degree-11 polynomial and states that the simple \(-1\) zero does not work.

Reasoning: The degree-10 candidate is the published degree-11 polynomial divided by one \((t+1)\) factor.

### Broader Coverage

Searches: T-avoiding spherical codes linear programming 48 dimensions; universal optimality T-avoiding 48

Evidence: The published 48-dimensional LP paper supplies the stronger surrounding theorem and all equality data.

Reasoning: No separate new theorem is needed to derive the degree-10 barrier.

### Exact Database Or Table

Searches: 52416000 Gegenbauer degree 10 negative coefficient

Evidence: No separate table was needed because the covering implication is direct.

Reasoning: Absence of a table does not restore originality.

### Claim Vs Prior Implication

Searches: Theorem 5.1 arXiv 2312.05121 equality support

Evidence: Published support nodes plus sign multiplicity force the unique candidate, and the paper already records failure of the simple \(-1\) choice.

Reasoning: Prior results mechanically imply the audited impossibility.


### Source inspections

- **COVERING** — 2312.05121 (https://arxiv.org/pdf/2312.05121): Full primary PDF, especially Theorems 3.1 and 5.1 and the displayed degree-11 polynomial. Evidence: Theorem 5.1 explicitly states that a simple zero at \(-1\) does not work and uses a double zero instead; equality conditions supply the remaining forced zeros.
- **CONTEXT** — 2501.13906 (https://arxiv.org/abs/2501.13906): Primary abstract and scope statement for later \(T\)-avoiding optimality work. Evidence: Later work broadens the \(T\)-avoiding program but is not needed for the decisive coverage.

Checked sources: https://arxiv.org/pdf/2312.05121; https://arxiv.org/abs/2501.13906; artifacts/exact_certificate.py

Residual risks: The exact negative coefficient pair is an explicit recomputation rather than a number printed in the source, but the scientific implication is already determined by the published construction.

## Value — FAIL

As a standalone final claim this is a routine method-obstruction corollary of the published equality analysis rather than a new structural boundary. The exact coefficient calculation is reproducible and useful diagnostically, but under the stated value bar that is insufficient once the obstruction is mechanically implied by the primary source.

Checked sources: https://arxiv.org/pdf/2312.05121

Residual risk: A genuinely new barrier for all higher-degree LPs or for SDP methods could be valuable, but it is not claimed here.

## Disposition

**FAILED**. Acceptance requires PASS on correctness, originality, and value.
