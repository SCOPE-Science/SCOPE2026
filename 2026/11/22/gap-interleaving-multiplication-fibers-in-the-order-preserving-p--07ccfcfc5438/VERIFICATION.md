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

# Computational and proof verification

Reproduce with `python3 CHECKER.py`. The accompanying `CHECK_OUTPUT.txt` contains all successful assertions and enumerated spectra. The code directly enumerates ordered pairs in the monoid and independently evaluates the gap-coefficient formula for \(1\le n\le4\), covering 4, 36, 400 and 4900 products respectively. It separately enumerates every pair of rank-\(n-1\) factors and each target for \(2\le n\le12\), tests the exact closed fiber formula and predicted class multiplicities, checks the \(n\)-factorization rank-\(n-1\) class, and checks totals.

The proof's universal ingredient is the four-set gapwise bijection with disjoint intermediate extras; the corank-one multiset transform supplies its full spectrum. No finite enumeration by itself proves these unbounded statements. No independent audit was performed.
