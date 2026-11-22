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
# Verification of the spatial weak-resetting transition

The exact backward equations and boundary data in `RESULT.md` constitute the analytic proof. Replay with `python check.py`. The script constructs the first and second moments from their integral representations, checks the reaction and wall conditions, independently reproduces Eq. 113 in arXiv:2310.04016 for uniform launch, proves algebraic identities for the endpoint susceptibility and Bernstein differences, and spot-checks signs/roots numerically for several strictly positive rate pairs. The executable report is **61 passed assertions**. The Descartes sign-variation theorem and strict monotonicity in the text justify the continuous, infinite-domain quantifiers; neither a numerical test grid nor Monte Carlo is used as an exhaustive proof.

The weak-reset theorem assumes a fully renewed position/direction and independent new target-capture Bernoulli events. At a vanishing first-order susceptibility the finite-rate sign remains undetermined. No independent scientific audit has been performed.
