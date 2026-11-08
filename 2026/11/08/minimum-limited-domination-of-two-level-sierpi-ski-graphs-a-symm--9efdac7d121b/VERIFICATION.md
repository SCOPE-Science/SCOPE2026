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

# Reproducibility and limits

Run `python verify.py` using an ordinary Python interpreter. The verifier builds the graph from base-clique and cross-row edges, independently tests domination and the condition of at most \(k\) omitted neighbours per selected vertex, and then separately enumerates symmetric binary matrices by upper-triangular bits. Every minimum-size row-profile candidate is checked for \(2\le m\le5\); every vertex subset at \(m=2,3\) is checked to exclude smaller sets. A third calculation uses the labelled path/cycle component recurrence for \(k=2\).

Observed final output ends in `VERIFY_OK`. Counts are \(N_{2,1}=2\); \(N_{3,1}=N_{3,2}=4\); \(N_{4,1}=N_{4,3}=10\), \(N_{4,2}=18\); \(N_{5,1}=N_{5,4}=26\), \(N_{5,2}=N_{5,3}=112\). The unrestricted theorem rests on the exact proof in `RESULT.md`, not on finite sampling. No outside certification, computer proof assistant, or independent mathematical audit is claimed.
