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

# Verification and scientific limitations

Run `python checker.py` with a Python 3 standard-library runtime. The checker enumerates all nonempty allowed subsets for \(16\) ring/blockade pairs, confirms exact counting by excitation number and the pinned exceptional-gap coefficient, and performs a small set of independent numerical root/probability checks. The observed output is `PASS: 16 exhaustive ring sizes, 1194 assertions`.

These finite enumerations verify the pinned-gap bijection on tested finite instances only. The thermodynamic partition ratio is proved separately by the dominant simple pole of the exact rational generating functions. The large-blockade law follows by asymptotic analysis of the positive root. The theorem applies to equilibrium weighted counts, not dynamic random sequential adsorption, and specifies the order of limits. The exact pinned-defect priority beyond the inspected literature has not received an independent audit.
