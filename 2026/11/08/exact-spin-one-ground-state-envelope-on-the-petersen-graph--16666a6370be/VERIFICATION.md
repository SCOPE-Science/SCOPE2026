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

The claim is established by exhaustive **finite** state classification and an exact rational dominance certificate, not by extrapolation. `enumerate_direct.py` checks all \(3^{10}=59049\) configurations, every distinct exchange-energy/occupancy/magnetization sector, all \(36\) nonnegative-magnetization sector minima, each rational convex coefficient row, and all seven strictly exposed phase witnesses. `enumerate_shell.py` independently constructs the same sector counts from two five-site rings and five spokes. Both programs completed successfully on the bundled `certificate.json`.

The rational dominance inequality applies to all real crystal-field values and all nonnegative absolute magnetic fields, closing the continuum of model parameters. Spin reversal supplies negative fields. Two zero-field coexistence multiplicities are verified by exact integer enumeration. No independent scientific audit, thermodynamic limit, finite-temperature dynamics, or external experimental validation is claimed.
