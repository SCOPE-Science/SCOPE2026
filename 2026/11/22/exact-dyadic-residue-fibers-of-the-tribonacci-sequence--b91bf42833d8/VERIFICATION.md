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

# Reproducibility

Run `python3 verify_tribonacci_fibers.py`. The program constructs the recurrence and matrix independently, checks the first coefficients of the singular-branch expansions, lifts their critical parameters by exact modular arithmetic, and compares all residues for every exponent from \(4\) through \(14\), inclusive. The checked number of targets is \(32,752\). It additionally verifies the critical values \(\kappa_5\equiv1264\pmod{2048}\) and \(\kappa_7\equiv1791\pmod{2048}\).

These are finite checks. The all-level theorem depends on the written matrix congruences, contraction argument, and 2-adic isometries. No independent audit has been performed.
