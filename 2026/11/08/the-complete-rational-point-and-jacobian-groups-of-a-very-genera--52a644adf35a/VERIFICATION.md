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

# Reproducibility and limitations

Execute `python3 VERIFY.py` in any Python 3 environment; no optional packages are required. The program uses integer and exact rational calculations and prints `VERIFY_OK` on success.

It checks the determinant of the six nonidentity-component intersection matrix (\(16\)), the ten independent \((-2)\)-component contributions (\(2^{10}\)), the resulting trivial-lattice discriminant \(2^{14}\), the generic K3 discriminant \(2^6\), and the finite index \(16\). It also computes the rank of six ramification half-classes mod two and exhibits an explicit configuration with ten distinct finite collision parameters.

These are **exact consistency checks**. The generic Picard rank \(16\), the actual singular-fiber list, the two-blowup construction, and the Shioda quotient theorem are cited external mathematical inputs rather than results of a finite computation. Nothing in this program proves the very-general assertion independently of those theorems. The proof and references are in RESULT.md. Independent assessment remains unperformed.
