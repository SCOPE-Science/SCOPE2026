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

The proof uses the classical weighted Szegő theta quotient, the product identity \(\Theta(Qu;Q)=-\Theta(u;Q)/u\), and the argument principle. On any multiplicative fundamental annulus the two circular images of \(F'\) differ by a constant, hence have the same winding. The unique double pole gives precisely two derivative zeros counted with multiplicity. The strict real inequality \(F''(x)>0\) on \(Q<x<1\), endpoint signs and conjugate pairing establish one positive and one negative simple orbit. Uniformly on compact rescaled sets, \(F'(\sqrt Q u)=1-1/(tu^2)+2\sqrt Q(u-1/(tu^3))+O_t(Q)\). The resulting roots and physical radius test prove the shrinking-hole trichotomy, including the equality boundary.

A standalone finite check is available as `check_stationary.py` (Python 3, `mpmath>=1.3`). Executing it produces `WEIGHTED_ANNULUS_CRITICAL_PASS theta_identities=6 root_and_phase_checks=10`. It checks theta identities and sample root/count cases; it is not a substitute for the all-parameter argument and does not certify historical originality. Only self-review has occurred, not independent audit.
