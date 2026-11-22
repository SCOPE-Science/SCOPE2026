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

A complete proof of the infinite-set theorem and its boundary cases is supplied in `RESULT.md`. The standalone `verify.py` reconstructs supported relations on four named-parameter sizes, constructs finite instances with three interchangeable anonymous elements, computes all-pairs distances directly, and checks the stated normal-form formulas. Cases for up to three parameters are exhaustive over every allowed orbit bit, including self-loops and missing interfaces. Four-parameter checks are deterministic-seeded samples. The sharp family is checked through seven parameters.

Observed program output: `VERIFY_OK 135132 exhaustive m<=3, sampled m=4; sharp examples m=0..7`.

Finite computations do not prove the theorem for arbitrary infinite atom sets: orbit transitivity and path normalization provide the proof. The named-pair case includes equal endpoints via reflexive distance zero. The generic diagonal bit is intentionally ignored by reflexive distances. The cutoff is acknowledged as separately inferable from general orbit-iteration techniques; the specific exact distance formulas remain the novel claim subject to historical-priority uncertainty.
