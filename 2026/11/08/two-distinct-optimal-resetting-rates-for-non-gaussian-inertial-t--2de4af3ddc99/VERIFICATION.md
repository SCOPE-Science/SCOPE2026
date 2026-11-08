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

# Reproduction and scientific limitations

Run `python verify.py` using SymPy. The code recomputes the Laplace-exponential reward identities from elementary moments, checks the centered renewal reward formula and both rational fourth-order expressions, checks exact derivative polynomial factorizations, and verifies strict rational brackets for the two real maximizers. It then independently obtains the asymptotic fourth cumulant from a Laplace-transformed Markov-generator hierarchy for three exact rational reset rates. The script exits with an assertion error on any mismatch and prints the two positive polynomial roots on success.

The analytical proof in `RESULT.md` is required for the infinite-time limiting statements and for uniqueness on all positive rates. Finite algebraic checks and numerical roots alone do not certify the general theorem. The exponential renewal-reward variance law assumes finite second moments of the centered cycle reward and control of the residual incomplete cycle; both hold because exponential clock intervals have moments of all orders and the reward grows at most linearly in duration.

The principal priority limitation is that the model and general renewal generating-function framework were already published. This package assesses only the exact global two-optimizer claim and supplies no independent external validation.
