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

## Reproducibility
Run `c++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` and `python3 verify_support.py`. Both use only standard runtime libraries. `CHECKS.txt` contains the executed output of these sources.

The direct verifier uses closed-neighborhood bitmasks of every vertex of \(J(5,2)\), \(J(8,2)\), and \(J(9,2)\). It checks all path pairs at the last two orders and all single paths for \(n=5\). The \(n=8\) total is an extra non-tight test and is **not** asserted as an all-order closed formula. The \(n=9\) direct enumeration independently confirms the disjoint-four-support classification and tests the degree on 30 sampled optimizers. The second verifier independently counts root-path possibilities and block partitions for \(n=5,9\), then checks the factorial expressions at larger orders without exhaustive graph search. These finite checks are corroborative only; the proof in `RESULT.md` establishes the infinite statement.

## Verification limits
No outside referee, formal proof assistant, or independent audit was used. The historical-priority comparison is supported by actual searches and source text but is not exhaustive. The count convention is subgraph paths with a chosen middle vertex; three-vertex-support identification is a different invariant.
