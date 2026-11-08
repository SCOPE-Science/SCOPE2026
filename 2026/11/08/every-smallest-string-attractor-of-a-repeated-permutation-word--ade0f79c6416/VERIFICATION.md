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

# Computational reproducibility

Execute `python3 verify.py` from the directory containing the
standalone source. The program requires Python 3's standard library
only. It directly enumerates every distinct nonempty contiguous
factor and all its occurrences, rather than using the theorem's
factor classifications to determine attraction.

For each parameter pair within its explicit finite bounds, all
\(k^q\) one-position-per-symbol selections are checked. It compares
its direct answer with the predicted endpoint condition and then
checks the exact enumerator \(k^q-k^{q-2}\). Its verified successful
output is:

```text
PASS: 31 complete (q,k) parameter cases, 204695 candidate sets, maximum word length 35.
For each candidate, tested every distinct factor against all its occurrences.
```

These are finite stress tests; they do not claim to prove the theorem
for arbitrary \(q,k\). The complete proof is the interval argument in
`RESULT.md`. The use of \(q=2\) regression cases checks compatibility
with the previously known binary boundary and is not a priority claim.
No independent audit is reported.
