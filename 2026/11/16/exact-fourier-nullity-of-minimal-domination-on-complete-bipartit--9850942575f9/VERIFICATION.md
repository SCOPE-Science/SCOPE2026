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

# Verification of the minimal-domination Fourier classification

Use `python3 check.py` from the same directory. The program requires only Python 3's standard library.

The finite exact test first enumerates all dominating sets on \(K_{m,n}\), checks minimality by deleting each selected vertex, and compares the resulting supports with the two entire shores and all cross-shore pairs. For each \(2\le m,n\le6\), it then computes the Walsh sum over those independently enumerated supports at every character and compares with the closed formula. It also verifies the exact zero counts, least nonzero multiplier, and maximal multiplier. This comprises 15,376 distinct integer Walsh coefficients.

A second check uses independent binomial-weighted frequency summation, without enumerating supports, to test the exact nullity and gap formulas for all 1,521 ordered pairs \(2\le m,n\le40\). The test emits `MINIMAL_DOMINATION_BICLIQUE_WALSH_PASS` if every assertion succeeds.

These tests are finite and do not prove the result for untested orders. The general proof is an exact support classification and arithmetic case division. No independent mathematical validation is claimed.
