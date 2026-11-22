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

# Verification record

The theorem is proved by exact conjugation of the hard-rod transfer integral operator to a killed centered-exponential random-walk kernel, followed by a conditioned-bridge heat-trace limit and positive-spectrum Laplace-transform identification. The proof controls the *first two* eigenvalues, so the correlation-length coefficient is not inferred from only the dominant eigenvalue. The return density is an exact gamma density; its asymptotic follows from Stirling's formula. The finite-mesh program `check.py` is a numerical consistency test, not an independent proof of convergence.

## Reproduction

From the directory containing this document and `check.py`, execute `python check.py` with Python 3, NumPy and SciPy installed. It builds a distinct cell-integrated killed-walk discretization and tests four small positive spacing ratios, as well as three exact gamma return densities. Positive numerical evidence is not substituted for the analytic bridge and trace steps.

## Scientific limits

The result requires the specific hard-rod model, a fixed positive well width less than the particle diameter, one rod per site, and the stated order of thermodynamic and close-packing limits. It does not quantify finite-mesh numerical error, provide finite-chain relaxation-time conclusions or establish novelty against unpublished research. Independent audit has not been performed.
