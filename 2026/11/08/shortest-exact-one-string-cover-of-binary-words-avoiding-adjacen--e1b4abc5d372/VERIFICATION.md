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

# Reproduction and checks

Run `python3 checker.py` with Python 3, no external modules or downloads. It enumerates every legal k-mer and graph vertex for \(2\le k\le13\), verifies the potential drop bound and sum of negative-vertex run weights, constructs all required duplicate edges, checks the Eulerian imbalance and verifies the final spelled string realizes exactly the admissible factor spectrum with the stated length. An independent breadth-first search of all legal factor masks establishes the exact shortest single-word lengths for \(2\le k\le5\). Successful replay prints `All bounded checks passed; infinite proof is in RESULT.md.`

These are bounded reproducibility checks, not an exhaustive or formal proof for all integers \(k\). The all-parameter argument is in RESULT.md. Independent mathematical validation and final priority assessment have not been performed.
