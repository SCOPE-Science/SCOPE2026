---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every a,p,q,alpha>0 and y0,z0>0 at b=1, positivity and u_(n+1)>=u_n+q imply z_n=O(1/n) and y_n<=a z_(n-1)->0. The exact successive-coordinate ratio gives orbitwise y_n=a z_n+d z_n^2+O(z_n^3), d=aq+a^2(alpha-1-p). Reciprocal expansion gives u_(n+1)-u_n=c+k z_n+O(z_n^2), c=q+alpha a, k=alpha a[2q+a(3alpha/2-1-p)]; the z_n^2 remainder is summable. Two summations yield 1/z_n=cn+(k/c)log n+C_initial+o(1), and n y_n->a/c. Zero correction occurs exactly at p=3alpha/2-1+2q/a when positive. Independent direct iteration with (a,q,alpha)=(2,1,1) and p=1,3/2,4 up to n=250000 verified both signs, vanishing k, quadratic slaving and stabilization of the corrected finite part; these finite checks do not prove universal asymptotics.

## originality

PASS

The same two-population recurrence is studied by Li and Zhang (2026), but its published local origin tests, positive fixed-point conditions and geometric interior-attraction results do not imply the global b=1 parabolic reciprocal expansion with explicit logarithmic coefficient/cancellation. Other related parabolic predator–prey findings concern different maps. Best-of-knowledge claim of a model-specific nonstandard critical-rate calculation, not priority certification.

## value

PASS

At b=1 the population extinction equilibrium has a neutral multiplier, so linearization does not supply the long-time extinction clock. The exact cancellation hypersurface and sign-changing second-order law distinguish natural parameter regimes with identical leading 1/n decay; this is a motivated quantitative boundary classification rather than a textbook renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
