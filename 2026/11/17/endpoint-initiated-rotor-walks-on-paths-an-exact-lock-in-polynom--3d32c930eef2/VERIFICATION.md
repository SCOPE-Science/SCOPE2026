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

# Verification protocol and limits

The proof is complete in `RESULT.md`; the checks below are auxiliary finite tests.

With Python 3 standard library, run:

```sh
python3 endpoint_exhaustive.py
python3 full_graph_recurrence.py
python3 polynomial_check.py
```

The scripts compare exact states and integers; no randomness, external data or platform-specific library is used. The corresponding recorded outputs are `endpoint_output.txt`, `graph_output.txt`, and `polynomial_output.txt`. Endpoint simulation covers every initial rotor string through \(n=18\). The separate full-graph computation computes periodic nodes through \(n=14\) by indegree elimination without invoking the proposed recurrence criterion. Polynomial enumeration covers all subsets through \(m=17\). None of these finite bounds constitutes a proof for larger sizes. The all-length proof is the excursion decomposition, rooted-rotor recurrence criterion, and standard probability argument.

The original Algorithmica article was accessible in abstract only, so historical priority was not independently certified; this affects originality confidence rather than correctness of the mathematical derivation. No external independent audit is claimed.
