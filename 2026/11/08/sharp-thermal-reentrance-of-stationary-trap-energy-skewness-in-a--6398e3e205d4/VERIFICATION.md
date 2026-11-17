---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: The polynomial generator for Y=|X|^2, Z=X dot N at a=gamma/kappa has stationary recursion (2p+q+a)M_pq=2pM_(p-1,q+1)+qM_(p,q-1)+a E_new[Z^q] when q even. The stated first three radial moments give cum3(Y)=8aP_d(a)/[d^2(a+1)^3(a+2)(a+3)(a+4)(a+5)]. The polynomial P_d has negative constant, all positive nonconstant coefficients for d>=1; it crosses exactly once, a_1=a_2=1, and P_d(1/2)=-9(6d-1)/8, P_d(1)=2(d-1)(d-2). For real d>=2, rewriting P=(4a-2)d^2+(3a^2-3a-6)d+a(a+1)^2 makes da_d/dd<0 at its zero. Independent symbolic cumulant factorization and numerical root checks reproduce the stated asymptotic limits. Independent thermal Gaussian convolution gives cum3(E)=cum3(Y)+12h Var(Y)+24h^2 E[Y]+8dh^3. For d=3 the cleared-degree-seven polynomial has strictly positive constant and degrees >=2 for h>0; only linear coefficient can be negative, so Descartes gives at most two positive roots. Strict increase with h, positive endpoints for h>0, and a nonempty negative interval at h=0 force a unique critical coalescence. Solving K=K_a=0 independently gives (0.13982748204004,0.01962977632358); finite checks only corroborate the analytical all-parameter argument.

## originality

PASS

Qualified PASS for the complete sign and thermal-reentrance classification, not the underlying raw moments or Gaussian convolution. Frydel, Sun–Ye–Podgornik, Guéneau–Majumdar–Schehr provide moments/position laws and convolution; no inspected older exact theorem classifying stationary potential-energy third centered moment at all tumble rates, dimensions, and positive thermal-noise coalescence. Primary full text inaccessible: priority risk remains.

## value

PASS

PASS: The sign of stationary squared-radius (trap-energy) skewness is a motivated observable of non-Gaussian active confinement. A dimension-dependent exact sign flip and a thermal noise-induced two-zero reentrant interval, with a single annihilation threshold, are structurally meaningful phase boundaries rather than merely recomputing a raw moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
