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

The reproducible standard-library checker is `verify.py`. The test computes \(I_r,J_r\) from modular inverses and independently evaluates Frobenius numbers by directly testing whether each multiple of \(p\) belongs to \(\langle a,a+h\rangle\), using the least residue of the second generator's coefficient modulo \(a\). It tests \(1{,}920\) admissible parameter triples with \(2\le p\le20\) and \(1\le h\le10\), and verifies zero-class branch uniqueness for each tested coprime pair. The conjectural all-parameter claim is not inferred from these finite computations: it follows from the proof in `RESULT.md`, including a CRT argument handling the restricted domain.

Expected final messages:

```
EXACT_INDEPENDENT_DIRECT_CHECK_OK cases= 1920 p=2..20 h=1..10
ZERO_RESIDUE_RIGIDITY_CHECK_OK all tested p,h
INFINITE_PERIOD_PROOF_REQUIRED true
```

No independent audit is asserted. No computation over a finite range can certify that the period is minimal for all parameters; that conclusion is analytical.
