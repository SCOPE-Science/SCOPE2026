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
# Verification

Run `python CHECK.py` from the same directory. The checker uses only Python's standard library and no external files or network. It passed 33092 rational and finite-grid checks in the packaged source. It verifies the exact source and sink equilibrium equations, gain identity, positive dispersal-rate derivative bound, numerical signs of the biomass derivative, full zero/critical examples, and the mutant-invasion determinant identity. The formulae hold for all admissible real parameters by the separate mathematical proof in `RESULT.md`; the checker does not verify an infinity of cases. The example gives \(r_*\approx0.197948831886174\), \(u_*\approx0.582216113146922\), and \(T_*\approx4.272179643843490\). No independent review has been conducted.
