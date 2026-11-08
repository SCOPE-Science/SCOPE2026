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

The full argument is in `RESULT.md`. It explicitly verifies the Hardy Hankel finite matrix, phase-aligned Poisson-variance formula, strict-improvement discriminant, unique upper-branch maximum, low-degree boundary, exact equality set, cubic unique optimizer, and higher-degree local/global optimizer transition. The asymptotics are elementary consequences of the closed forms.

Run `python3 checker.py` with a standard Python 3 interpreter; no downloaded data or external packages are needed. It reports **454 finite diagnostic assertions passed**, checking degrees three through nineteen, arbitrary complex phases and magnitudes, the block norm and variance identities, analytic threshold ties, and sample strict inequalities above and below the transition. Sampled radii do not prove completeness or the general theorem. No independent validation or external certification has been carried out.

Unproved beyond this claim: general multi-frequency symbols; uniqueness and a formula for every subcritical higher-degree optimal radius; exhaustive publication priority against all possible alternative terminology.
