---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Orthogonal projection at a fixed normalized site captures Q=e^{-|w|^2}|f_a(w)|^2, and ||f_a||^2=1+3a^2. For w=x+iy, u=|w|^2, the angular identity is (1+a/4)(1+au)^2-4a(x-(1-au)/4)^2. The upper radial envelope is uniquely maximized at u*=2-1/a when a>1/2. Stationarity at nonzeros, conjugate(w)f=f', forces u=u* and x=(1-a)/2 if y is nonzero. Thus y^2=-h(a)/(4a); the two simple positive roots give precisely the feasible saturation interval, with one point at each endpoint. Strict log concavity gives exactly one real maximum in each interval separated by the polynomial zeros, and the rightmost x3>1 violates the angular condition D=1-a*x^2-4x>=0. On the other two branches, the resultant is -a(a+4)h(a), and D=0 forces x=(1-a)/2 by factoring the stationary equation after substitution. This x lies on the middle branch at the lower root and the left branch at the upper root: at D=0, f=(a+4)x, determining its sign, and x<0 is left of the zeros if f<0. The resultant is a nonzero factor times the product of D over the three analytic stationary branches; simple resultant zeros and the unique common root ensure the corresponding D changes sign. Both branch values of D are positive for small a: x2~a, while x1~-1/sqrt(a) from the logarithmic stationarity equation x=1/(x-zeta_-)+1/(x-zeta_+), which bounds |x1-zeta_-| by 2/|x1|. Therefore the sole angular-admissible candidate in either outer regime is the claimed one. Evaluating the envelope gives M, and Taylor expansion at each simple root gives the square-root law. Replay `python /workspace/independent_checks.py 1` verified the exact stationary and angular identities, the resultant and the displayed decimals.

## originality

PASS

The strongest distinct indexed result has strikingly similar angular algebra but concerns the disk and another coefficient family; its inspected theorem gives one positive-real merger and cannot furnish the two Fock mergers. The cited primary Fock passages supply kernels and shifts, not the optimum classification. This judgment is bounded by inspected texts and retrievable indexed evidence.

## value

PASS

This balanced vacuum/one-quantum/two-quantum coefficient path exposes competition between the linear and quadratic terms in the optimal coherent approximation. It is a complete nonmonotone global example: a positive-real optimum splits into a conjugate pair and recombines on the negative real axis. Exact thresholds, endpoint coalescence speeds and captured norm make it a useful check on global coherent approximation or Husimi-peak calculations, beyond routine projection at a fixed site.

The dated certificate retains the supplied scientific assessment, sources and limitations.
