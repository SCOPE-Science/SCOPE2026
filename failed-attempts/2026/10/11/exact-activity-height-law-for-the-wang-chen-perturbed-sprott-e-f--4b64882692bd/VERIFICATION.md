---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the printed polynomial vector field xdot=yz+a, ydot=x²-y, zdot=1-4x, compact invariance gives E[x]=1/4, E[y]=E[x²], E[yz]=-a. The exact square A=E[(1-4x)²]=16 E[x²]-1 implies E[y]=(1+A)/16 and y-weighted mean E_nu[z]=-16a/(1+A). Complete bounded trajectories give y>=0 by variation of constants and normalization >0. A=0 forces x=1/4 on invariant support, then y=1/16 and z=-16a by invariance; only the equilibrium δ_Q remains. At a>0, all other invariant measures have strict weighted height in (-16a,0). Algebraic generator identities and the rigidity step were checked independently, not inferred from the saved VERIFY_OK log.

## originality

FAIL

FAIL: An already published 2026-10-04 primary mathematical record proves this IDENTICAL exact y-weighted height contraction E_nu[z]=-16a/(1+A), same zero-defect equilibrium rigidity, same a>0 strict interval, and an additional stronger conditional stationary law E[yz|x]=-a for the identical vector field. The submitted claim is contained within that result, even when its wording and presentation differ; the extension of the displayed identity to all real a uses the same stationarity algebra.

## value

FAIL

FAIL: The present package repeats a covered activity/height invariant and its equilibrium equality characterization without an uncovered structural theorem. Rechecking exact coordinates is reproducible but supplies no separately needed new conclusion beyond the stronger prior result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
