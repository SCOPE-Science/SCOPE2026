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
Run `python verify.py` with Python 3.8 or later. No external packages or downloaded data are required. The program computes the associative Nijenhuis identity directly on an algebra basis for all \(q^{(n+1)^2}\) linear operators when \((q,n)=(2,1),(3,1),(2,2),(3,2)\); it checks the explicit normal form in both directions and the exact total. Independently of those equation tests it enumerates actual algebra-automorphism conjugacy orbits using all invertible matrices for the same pairs and \((2,3)\), and compares each answer with the Euler-product coefficient. The raw counts are \(6,15,56,459\), and the orbit counts for the five test pairs are \(6,12,18,48,46\). A successful run prints `VERIFY_OK`.

The program uses prime fields for finite execution. The printed finite checks are not a proof for arbitrary \(n\) or nonprime fields; the general proof is in `RESULT.md`. No independent external validation has been performed.
