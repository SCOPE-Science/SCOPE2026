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

# Mathematical and executable verification

The standalone `verify.py` is an ordinary standard-library Python 3 program. It enumerates every generic order chamber for path sizes two through eight and independently recovers all exact step-column profiles. It checks the finite maximum against directly evaluated profiles using five sets of integer weights per size and confirms the necessary half-weight boundary conditions with exact rational perturbations. It then tests 4,950 deterministic rational input pairs against the two-input bound, as well as the separate unweighted one-input variation inequality. It requires no external data, third-party software packages, or historical logs.

The proof, rather than these finite computations, establishes the theorem for all integers \(n\ge2\), all strictly positive real weights, and all real input pairs. It identifies the complete list of possible profiles and constructs strictly feasible perturbations that attain each branch. Generic-chamber bounds extend to ties by continuity. A finite checker cannot alone establish infinite-dimensional quantification or historical priority.

No independent scientific audit is represented by this verification document.
