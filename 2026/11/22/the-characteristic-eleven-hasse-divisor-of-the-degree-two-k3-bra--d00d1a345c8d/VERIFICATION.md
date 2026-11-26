---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact checks and scope

Run `python3 check_character_ranks.py`. The program constructs the marked monomial matrix by repeated sparse multiplication, compares the supporting permutation with the characters, checks the iterated polynomials through the third twist, and tests the local-minor order lists and the Hasse coefficients of the four previously exhibited elliptic factors. The proof of the scheme structure uses the sparse polynomial form over the smooth parameter line for all iterates, not a finite test extrapolation. The determinant and numerical ranks are not claimed independently of the prior decomposition. The assertions concern the branch curve's coherent cohomology, not the K3 surface.
