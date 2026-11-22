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

# Reproducibility and mathematical limits

The standalone standard-library Python 3 script `check.py` was executed against its delivered contents and returned `VERIFY_OK 9993 finite and exact checks`. It reconstructs digit carry matrices, the full tensor-square transfer and the exact vector identity \(T^2w_0-26Tw_0+90w_0=0\); these matrix identities imply the collision recurrence at every depth, independently of the finite checks. It verifies the rational stationary carry distribution and output frequencies. The script checks all finite target fibers through \(3^8\) and direct ordered triple counts through \(3^4\), along with the first ten energy values from the transfer.

The almost-sure digit frequency assertion rests on the standard finite-state irreducible aperiodic Markov ergodic theorem; finite computations do not establish such a limit. The dimension follows from the exact recurrence and cylinder-mass identity, not extrapolation. No theorem for arbitrary convolution orders or nonuniform input digits is asserted, and independent mathematical auditing has not occurred.
