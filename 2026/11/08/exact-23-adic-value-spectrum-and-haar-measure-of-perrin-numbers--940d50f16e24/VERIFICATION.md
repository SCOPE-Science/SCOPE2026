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

The reproduction file `verify_perrin23.py` uses only the Python standard library. Execute it with `python3 verify_perrin23.py` from the extracted package directory. It checks the integer matrix trace identities modulo \(23\) and \(23^2\), the complete \(22\)-branch finite certificate, exact grouping of the \(211\) residue targets at precision \(529\), all \(13\) uniquely represented critical nodes, and the period/image sizes through \(23^4\). Infinite-level square normal form uses the analytic argument in RESULT.md; finite tests are not a proof for unbounded exponents. The run output terminates `VERIFY_OK base_rows=22 base_groups=15 full_lift_classes=198 quadratic_classes=13 prime_power_levels=4`.
