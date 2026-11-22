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

# Verification of the exact constrained universal-cycle enumeration

Run `python3 verify_switch_universal.py` in this extracted directory. It requires Python 3 standard library only.

For every \(n=2,\dots,10\), the program enumerates the permitted length-\(n\) words, independently constructs the directed overlap Laplacian, computes the root-minor determinant exactly by Bareiss elimination, and checks both the word count and \(2^{n-2}\) tree count. For every \(n=2,\dots,7\), it also independently enumerates all Euler tours with the distinguished edge `0...0` first and verifies the actual distinct cyclic factors against the claimed set. These tests were executed from the actual packaged script and printed `VERIFY_OK`.

The proof for arbitrary orders is the reduced-graph classification and BEST theorem given in RESULT.md. Finite enumeration cannot establish that infinite theorem, cannot establish publication priority, and is not an independent external mathematical audit.
