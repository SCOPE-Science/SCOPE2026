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

# Verification
The three included Python 3 standard-library scripts must be executed from their containing directory:

```sh
python3 check_scattered.py
python3 check_rewrites.py
python3 check_independent.py
```

Each program contains assertions that fail on disagreement. `check_scattered.py` uses a pattern-oriented dynamic program; `check_rewrites.py` builds the SE exchange graph without subsequence counting; `check_independent.py` directly enumerates index subsets and checks exact equality of the complete observation and graph partitions. Their validated outputs contain \(2520\) words, \(180\) distinct undirected exchanges, \(2346\) fibers and the size histogram \(2184\) singleton fibers, \(156\) two-word fibers and six four-word fibers. No random sampling, numerical tolerance, unexplored search branches or external libraries are used. The finite verification does not establish a general rewriting theorem for longer words or other compositions.
