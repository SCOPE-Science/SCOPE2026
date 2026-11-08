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

# Reproducibility and verification

Run `python3 verify.py` with a standard Python 3 interpreter. No third-party packages or network access are required.

The verifier implements both direct 2-adic indexing and recursive odd-position decimation of generalized paperfolding words. It covers 18 instruction sequences and 12 source lengths \(n\in\{8,12,16,20,24,28,32,36,40,48,64,96\}\). For each pair it computes the distinct factors of source length \(n\) and target length \(2n\), verifies exact cardinalities against the known \(4n\) factor law, constructs every even-start lift, and checks that the induced map on restricted rotation classes is bijective with exactly twice the size per target class.

Observed stdout:

```
VERIFY_OK instruction_sequences= 18 length_pairs= 216 base_cyclic_counts= [(8, 4), (12, 16), (16, 4), (20, 28), (24, 16)] n4_exception= (3, 4)
```

All executable checks passed when the packaged `verify.py` was run. The verification does not enumerate all possible infinite instruction sequences; the infinite statement is established by the mathematical proof. The known total factor complexity makes the particular finite factor-set enumerations complete once they contain exactly \(4n\) words.
