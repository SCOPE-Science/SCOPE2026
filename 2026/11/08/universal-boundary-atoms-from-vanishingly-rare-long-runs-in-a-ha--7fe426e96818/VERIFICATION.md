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

# Verification and replay

Execute `python verify.py` from the extracted package. The script requires only the Python standard library; it checks exact rational enclosures for the exponential used in the strict positive-cumulant claim, the explicit finite-\(L\) bound, the deterministic-orbit density and moments by quadrature, and independent finite-\(L\) moment recursion diagnostics.

The proof of the general renewal-limit statement is in `RESULT.md`, steps 1–4. Finite diagnostics are not an infinite proof, a publication-priority certificate or an independent scientific audit. This file describes the self-review only.
