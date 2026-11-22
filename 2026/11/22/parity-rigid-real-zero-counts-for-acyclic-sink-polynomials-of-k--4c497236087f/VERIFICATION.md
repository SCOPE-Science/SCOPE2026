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

# Reproduction and scientific limits

Run the standalone Python-standard-library checker with `python verify.py`. It iterates all \(4^n\) directed-edge assignments for every integer \(2\le n\le8\), separately detects acyclicity using indegree elimination and counts sinks from outdegrees, and compares each coefficient to the closed formula. It additionally checks exact integer coefficient-sign inequalities and the positive-test-point identity up to \(n=200\).

Expected successful output:

```
INDEPENDENT_FULL_ORIENTATION_CENSUS_PASS n=2..8
EXACT_SIGN_PATTERN_AND_WITNESS_CHECK_PASS n=2..200
VERIFY_OK
```

The mathematical proof does not rely on checking finitely many degrees. Its non-computational steps are the exhaustive four-state acyclic characterization, the exact orientation counting correction for configurations without receiving states, the exclusion inequality for \(-2\le z<0\), and Descartes' upper bound together with the uniform sign witness for odd parameters. The explicit small boundaries \(n=2,3\) are included.

A passed self-review is not an independent audit, external certification or proof by exhaustive computation of infinitely many cases. The possible existence of older algebraically equivalent work remains a scientific priority limitation.
