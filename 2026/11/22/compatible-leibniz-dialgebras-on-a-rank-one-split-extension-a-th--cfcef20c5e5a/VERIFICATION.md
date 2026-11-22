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

# Verification of the claimed theorem

The proof in `RESULT.md` establishes the full all-field classification and finite-field formulas. It is not dependent on bounded enumeration. The checked scientific source is Uzakbaev, arXiv:2611.00109v1, specifically the definition of Leibniz dialgebras and the six three-dimensional models.

To reproduce the finite tests, run `python check.py` with a standard Python interpreter. `CHECK_OUTPUT.txt` contains the recorded successful run. The code enumerates all matrices for its selected small prime-field dimensions, checks the four idempotent equalities and orbit-count multiplicities, and checks all five identities on every basis triple for every classified product. For two-dimensional underlying algebras over the two prime fields, it additionally enumerates *every* bilinear second product and checks all five identities. The final line must be `VERIFY_OK`.

Verified small cases: \((d,q)=(1,2),(1,3),(2,2),(2,3),(3,2)\). Total compatible products respectively: \(3,3,21,39,339\). For the first two cases every possible bilinear second product is also tested. The checker implements prime-field arithmetic, not arithmetic in all extension fields; finite-field uniformity comes from the proof, and its tests do not certify infinite quantifiers.

Scientific limitation: historical priority remains provisional. An independent mathematical audit has not been performed.
