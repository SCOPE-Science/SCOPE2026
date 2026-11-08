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
# Verification record

The theorem is proved by a side-and-matched-index back-and-forth strategy plus explicit separating sentences. The programs only check small finite cases and do not constitute independent mathematical validation or an infinite proof.

`refinement_check.py` implements noncounting replacement **sets** on ordered tuples, not multisets, and tested 217 pair/width cases; `refinement_output.txt` is its recorded stdout.

`extension_check.py` checked 15,286 one-point extension cases for the canonical index strategy, maximum independent-set sizes and the three-variable matching-deletion witness on ten finite model instances; `extension_output.txt` is its recorded stdout.

Both scripts are executable with Python 3 and the standard library. Reproduce from the package directory with:

```text
python refinement_check.py
python extension_check.py
```

The theorem's domain is all integers \(n\ge2\) and all widths \(k\ge1\), in a pure undirected loopless edge language, without counting. Verification is bounded to the enumerated graphs and widths. No external certificate, independent audit, or universal computational proof is asserted.
