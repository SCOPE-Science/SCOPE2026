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

The two standalone Python programs can be run using `python3 check_girth.py` and `python3 check_witness.py` in the extracted directory. They use only the standard library and have corresponding saved outputs.

`check_girth.py` builds 40 actual finite bipartite incidence graphs and independently computes the cycle rank and shortest cycle. `check_witness.py` constructs sparse arithmetic supports and tagged patterns for \(2\le r\le12\), verifies the \(77\) prescribed translate counts \(2,\ldots,r+1\), and finds additional translates with counts zero and one. These computations are supplemental finite checks. They do not certify the infinite family or general theorem, which are established by the finite-subgraph cycle-rank argument, named published implications, and maximum-weight proof in RESULT.md.

The first public source date is the original arXiv posting on 2026-09-23, not the later revision. The result has not undergone independent validation.
