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

# Exact reproducibility

Run `python3 verify.py` with a Python 3 standard-library installation. `results.txt` contains the actual deterministic output from this package. The verifier visits all \(q^n\) vertices in each of four cases, constructs every predecessor of length at most \(t\) from all radix-\(q\) prefixes, independently reconstructs the same balls by reverse-edge breadth expansion, and checks nonempty pairwise distinct code signatures and exact prefix-class counts. No optimization solver, probabilistic test or external dataset is needed.

Verified cases: \((q,t,n,|S|)=(3,3,5,162),(4,3,5,768),(3,4,7,1458),(4,4,7,12288)\). Full-domain finite verification does not imply the same property for any untested \(q,t\). The SHA-256 strings printed by the checker are fingerprints of exhaustively constructed identification sets, not independent mathematical certification.
