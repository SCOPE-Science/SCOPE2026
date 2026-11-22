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

The packaged `verify_picard_f5.py` executes as `python3 verify_picard_f5.py` with no third-party dependencies. It checks the complete finite set of \(125\) normalized coefficient triples, including squarefreeness, independent quartic discriminants, two representations of \(\mathbb F_{25}\), direct cubic fibers and the eighth-power character test, and the exact eleven-stratum table. The algebraic odd-extension and Weil functional-equation arguments are written in RESULT.md; the code verifies only the finite census and consistency with the known rank equation. No independent audit, proof assistant or external certification is claimed.
