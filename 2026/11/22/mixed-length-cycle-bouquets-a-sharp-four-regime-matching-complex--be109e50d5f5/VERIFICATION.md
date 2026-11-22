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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.8 or newer; only the standard library is required. The executable enumerates all independent graph-edge subsets from the definition of the cycle bouquet, forms signed simplicial boundary matrices, computes mod-2, mod-3, and mod-5 ranks, and compares the resulting reduced homology profiles to the closed four-case theorem. Its recorded execution is embedded as `verify_output.txt`.

The experiment verifies 48 distinct two-/three-petal length tuples drawn from lengths three through eight and with no more than 19 total graph edges, including contractible cases and all three noncontractible classes. All three field ranks agree. It does **not** determine integral torsion, certify infinitely many instances computationally, or replace the full homotopy proof. Torsion-freeness, the recurrence, all allowed petal lengths, and the exact wedge decomposition are proved mathematically in `RESULT.md`.

The independent audit channel is not performed. No external expert or formal prover has certified this result.
