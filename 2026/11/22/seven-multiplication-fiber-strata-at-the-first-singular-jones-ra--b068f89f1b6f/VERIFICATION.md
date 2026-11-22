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

# Verification and reproducibility

Run the standard-library Python program `check_jones.py` with `python3 check_jones.py`. Its captured stdout is `CHECK_OUTPUT.txt`, ending in `ALL_CHECKS_PASS`. The checker builds all prescribed rank-\(n-2\) factors, forms their products by three-row union-find graph gluing, independently inspects the resulting cap/cup geometry, and compares the exact target fibers and their complete multiplicity census for \(3\le n\le10\). It also constructs all Catalan planar perfect matchings for \(3\le n\le8\) and checks that the rank-\(n-2\) factor class is exhaustive.

The proof, not these finite computations, covers all integers \(n\ge4\). Its critical exact checks are the enumeration of the four possible upper and lower gluing branches, the fact that any three of the four \(D,D\) equality events force the fourth, and the complete inclusion-exclusion counts \(S_1=m(m+1)^2\), \(S_2=5m(m+1)/2+m\), \(S_3=4m\), and \(S_4=m\), with \(m=n-3\). Weighted multiplicity totals are \((n-1)^4\). At \(n=3\) the theorem's low-rank class is empty and the direct checker treats this as a boundary case.

Source comparisons are made for unrestricted two-factor product fibers versus rank-preserving principal-factor adjacency, ideal-generation theorems and idempotent-only enumeration; none of the inspected sections provides the full stated prescribed-target law. This is a self-review, not an independent audit or historical novelty certificate.
