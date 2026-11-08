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

# Verification of the finite cograph threshold

The embedded source `verify.py` uses only the Python standard library. Reproduction command, from the directory containing the embedded files:

```sh
python3 verify.py
```

Its final line is `VERIFY_OK 21101`, and it writes `census.json`. The program asserts exact agreement of two refinement algorithms on every generated graph and checks the completeness-supporting canonical cotree counts \(1,2,4,10,24,66,180,522,1532,4624,14136\). The complete per-order distribution of strict refinement rounds is in `census.json`.

The direct witness \(W\) and its complement each have rank-by-rank class-count sequence \(1,3,5,6,7\), stable afterwards. The only eleven-vertex maximizers are the canonical cotrees recorded in `census.json`; one has a union root and the other a join root. The verifier checks that the cotrees are exchanged by complementation and that both graphs contain an induced four-cycle.

**Proof limits:** The computation is exhaustive only through eleven vertices, justified by the reduced cotree decomposition, and does not certify the maximum refinement depth at larger orders. Agreement between two implementations reduces implementation risk but is not independent mathematical validation. The uniqueness and finite cutoff additionally rely on the correctness of the cotree-to-graph and integer partition enumeration code, which is provided in full for inspection.
