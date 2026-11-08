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

# Verification of the all-even-alphabet reverse-complement counting law

## Reproduction
Run `python3 verify.py` with Python 3; no external modules or files are required. The verifier reads no network resources. It counts all reverse-complement symmetric words by enumerating their unique half-words for alphabet sizes \(2,4,6,8\), with respective maximum half-lengths \(12,8,6,5\). It checks each direct arch index against the midpoint-cover identity, separately computes exact generating-function coefficients through inclusion-exclusion for surjections, and compares every resulting length-index histogram. Selected smaller instances are independently tested against the defining requirement that every target word of a specified length is a subsequence. It also checks all shortest-length coefficient formulas for \(1\le j\le5\) and each of the four even alphabet sizes.

The observed terminating status is:

`VERIFY_OK halfwords=189008 nonzero_cells=124 direct_subsequence_cases=368 shortest_profiles=20`

The symbolically simplified quaternary expression was additionally checked by exact rational-function algebra against the general formula. These finite experiments do not themselves establish the infinite-family theorem; the proof in `RESULT.md` does so using greedy-arch and surjection identities. No external or independent scientific certification is asserted.
