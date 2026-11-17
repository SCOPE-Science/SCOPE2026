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

# Verification

The standalone `verify.py` uses Python standard-library `fractions.Fraction` to differentiate **every actual summand** of the nonlinear model, including repeated triple indices. The run succeeded with:

```
VERIFY_OK complete_eigenvector_identities=880 barbell_quadratic_and_threshold_checks=90
Finite rational checks; the full finite-size classification and asymptotic limit use analytical proofs.
```

The complete-graph checks reproduce rotational modes, internal eigenspaces, and the relative eigenvalue for sizes two through eleven and both positive rational coupling choices. Those results corroborate a previously established comparison, not a new complete-graph claim. The barbell checks independently reconstruct signed-edge quadratic energies at sizes four through sixteen, attain the exact threshold equality via explicit witnesses, detect negative energy below, and demonstrate strict grounded positive definiteness above.

The proof for every barbell order uses the exact within-clique variance lower bound and an analytical quadratic minimization. No finite computation is presented as an exhaustive proof, no nonlinear stability is claimed at a nonhyperbolic equality boundary, and no independent audit has been performed.
