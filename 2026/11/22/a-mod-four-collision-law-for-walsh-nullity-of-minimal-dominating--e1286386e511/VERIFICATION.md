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
# Verification and limits

Run `python3 verification_mindom.py` with Python 3 (no third-party dependencies). The program independently obtains inclusion-minimal dominating sets using adjacency and all vertex subsets; compares their derived support to the combinatorial description; forms the unnormalized integer Walsh transform; compares every coefficient to the closed formula; checks the rank/nullity count, the parity criterion, the spectral norm and the smallest positive singular value. Its full finite scope is \(2\le a,b\le7\), \(a+b\le12\), and its observed outcome was **PASS: 33 graph shapes, 30901 exact assertions**.

The proof in `RESULT.md` derives the all-size formulas independently of numerical enumeration. Exact finite testing is not an infinite proof or an exhaustive check of every shore size. No independent review, external certification or human validation is claimed. The cited archival sources establish context, not an absolute uniqueness certificate.
