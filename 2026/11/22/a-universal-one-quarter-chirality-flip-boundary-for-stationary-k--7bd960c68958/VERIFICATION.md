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

Run `python verify.py` with Python 3 and SymPy installed. The code constructs the generator recurrence through total degree four, checks the complete rational identity by symbolic cancellation, and checks the exact critical polynomial factorization. It then independently integrates chronological Fourier-mode two-state Markov resolvents for the second and fourth radial moments. The prepared program completed the symbolic identities, 37 parameter triples, and the listed one- and two-crossing sign examples successfully.

The analytic correctness argument is in `RESULT.md`, including exact domains, strictly positive denominators and the elementary real-quadratic classification. The numerical integrations are finite corroboration, not proof of the all-parameter theorem. No experimental measurement, independent review, or independent audit is claimed.
