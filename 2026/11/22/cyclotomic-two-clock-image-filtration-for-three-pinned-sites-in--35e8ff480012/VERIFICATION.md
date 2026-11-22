---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

## Scope and exact argument

The claim concerns every triple of distinct integer input sites for the bilateral binary three-tap map and every nonnegative time. The algebraic proof supplies exact \(\mathbb F_2[z,z^{-1}]\) divisibility calculations, a character-duality identification of image subgroup index, and a sharp worst-span witness; it does not infer infinite conclusions from finite rank tests.

## Executed standalone checks

- Command: `python3 verify_cyclotomic_clocks.py`.
- Exact polynomial-valuation vs analytic first-full-time comparison: 8,910 tested triple masks.
- Independent binary image-matrix rank deficiency vs analytic index formula: 3,002 tested mask/time combinations.
- Every pair spacing through 80 checked against the binomial valuation.
- Sharp diameter law checked through span 120, exhaustively through span 55.
- The program uses only Python's standard library and terminates with assertions on any mismatch.

## Limits

Finite computations verify only their enumerated domains. The continuous bilateral full-shift conclusions follow from the written proof. No independence, external certificate, or independent mathematical audit is claimed. Historical equivalence under another description of additive cellular automata remains a residual risk.
