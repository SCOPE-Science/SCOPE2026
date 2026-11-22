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

The all-parameter proof is the complete Rule 90 kernel classification plus a case-by-case analysis of exclusion-compatible kernel differences. The cyclic gap composition count supplies the source cardinality, and parity-mask orbit counting supplies the complete inverse-fiber distribution.

The included `verify.py` uses only the Python 3 standard library. From the package directory, execute `python3 verify.py`. It exhaustively enumerates all indexed binary sources and their observed outputs for 57 parameter pairs, with \(1\le r\le6\) and ring lengths up to \(20\), and checks alternating-output witnesses in four noninjective intermediate cases. Its observed output starts with `VERIFY_OK parameter_pairs=57`.

This finite experiment does not prove any statement outside the enumerated range; the infinite claims rest on the proof in `RESULT.md`. No independent mathematical audit or external certification has been performed.
