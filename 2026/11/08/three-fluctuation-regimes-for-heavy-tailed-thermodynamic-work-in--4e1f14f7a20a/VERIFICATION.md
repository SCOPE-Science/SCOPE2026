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

## Mathematical verification
The cycle identity and Gaussian conditional moments follow directly by expanding the squared displacement. The compensated tail calculation isolates a regularly varying product \(T(\kappa D Z^2-v)\) and shows the remaining Gaussian cross term has a strictly higher finite moment than the tail index; the two-sided coefficients therefore follow by product regular variation. Ordinary and generalized central limit theorems are applied only after identifying the exact dependent reward-and-duration pair, and random-index replacement is justified by the functional limit theorem. The equilibrium renewal age is tight because cycle durations have finite mean. The proof does not rely on the numerical tests to establish asymptotic limits.

## Reproducible computation
Run `python check.py` with Python, NumPy and SciPy installed. The checker computes independent normal-integral expressions, finite-cycle second-moment identities, a Lomax-clock tail limit for a concentrated initial state, and the raw-work lower bound. It passes 87 deterministic assertions under the tested environment. The initial-state-zero tail calculation checks the leading constants but is only an auxiliary diagnostic; the theorem allows arbitrary positive Gaussian initial variance and proves the perturbation negligible.

## Boundaries
The return phase uses exact independent Gaussian thermalization, not an asserted finite-time solution of the unmodified Ornstein–Uhlenbeck relaxation equation. The work observable counts completed switch pairs. The analytic statement requires the exact survival tail equivalence and independent renewal cycles. Neither an independent audit nor an external certification has been carried out.
