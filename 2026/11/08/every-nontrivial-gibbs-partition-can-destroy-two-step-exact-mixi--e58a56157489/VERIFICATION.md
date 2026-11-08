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

# Verification and reproduction

Run `python3 verify.py` in a standard Python environment; no external Python packages or network calls are needed. The program uses `fractions.Fraction` to verify the displayed three-state witness and exact matrix-power formula. It separately generates every nontrivial partition of sets with three through six elements and, for each, tests uniform and nonuniform rational stationary measures. For these finite cases it reconstructs positive, stationary rank-one perturbation kernels whose centered squares vanish, verifies nontrivial Gibbs-compressed eigenmodes, and verifies the exact weighted-Frobenius power law. The completed run reports `PASS: 13899 exact rational assertions; no simulation`.

The full theorem is established by the constructive proof in `RESULT.md`. Finite replay does not prove the universal statements over arbitrary state-set sizes or all stationary distributions, and it does not establish historical priority. Independent audit has not been performed.
