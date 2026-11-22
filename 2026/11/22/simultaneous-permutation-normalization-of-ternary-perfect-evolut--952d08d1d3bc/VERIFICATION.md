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

# Reproducibility and checks

Run `python3 verify.py` using Python 3 standard library. The script verifies the integer centralizer formula for every partition through dimension five and evaluates all seven fifth-dimensional conjugacy contributions. It separately exhausts every invertible \(1\times1\), \(2\times2\), and \(3\times3\) ternary structure matrix, computes all its signed permutation automorphisms, checks whether one coordinate sign vector simultaneously removes all automorphism signs, and computes the monomial orbit counts directly.

Expected terminal marker: `TERNARY_EVOLUTION_CHECKS_PASSED`. The five-dimensional exact result uses an all-partition enumeration with exact integers and fractions, not a random sample. The finite checks do not prove the unrestricted-dimensional normalization theorem; the fixed-space proof in `RESULT.md` does. The centralizer formula relies on standard finite-module facts explained there. No independent audit, expert review, or formal certification has taken place.
