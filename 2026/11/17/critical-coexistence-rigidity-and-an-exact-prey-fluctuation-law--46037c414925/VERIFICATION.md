---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: Direct differentiation of the given ODE yields (log y)dot=x-1 and Wdot=[log z-2a log y]dot=a(x-1)^2+a-b. Integrating gives exact finite-horizon identities and bounded endpoint terms under eventual positive compactness. If b<a, W grows at least linearly and cannot remain bounded. At b=a, W increases to a finite limit and integral (x-1)^2<infinity; bounded vector field derivatives give uniform continuity, Barbalat x->1 and derivative convergence xdot->0, hence y+az->1+c. Strict decrease of log[(1+c-Y)/a]-2a log Y then selects a unique limit Y,Z>0. Integrating nonnegative Wdot against any compactly supported invariant measure forces x=1 and its invariant support to the equilibrium line; ergodic measures are atoms. For b>a, the limiting moments Ebar(x)=1 and Ebar(x^2)=b/a, along with (M-x)(x-m)>=0, yield (M-1)(1-m)>=b/a-1 and AM-GM the amplitude bound. Independent rational-state substitution at hundreds of tuples confirms only the local algebra; infinite-time conclusions follow from compactness arguments, not trajectories numerics.

## originality

PASS

PASS qualified: The original model and its critical b/a=1 stability border are already known and explicitly excluded from novelty. Karim–Amen–Aziz’s accessible full integrability preprint concerns first integrals and Darboux polynomials, not this exact all-persistent-orbit Cesaro second moment, critical convergence or invariant-measure collapse. Related predator-prey systems with other nonlinearities do not transfer these log-coboundary formulas by renaming. Original 1988 Samardzija–Greller full article and expanded 2025 article were inaccessible; no claim of whole-paper noncoverage, risk retained.

## value

PASS

PASS: For an ecological flow known for complex recurrent/coexistence dynamics, exact prey variation independent of parameter c and of periodic versus chaotic behavior is a natural invariant. Critical global convergence to a continuum of nonhyperbolic equilibria and the supercritical necessary amplitude floor constrain possible persistent attractors and give quantitative consistency diagnostics; these are stronger than a local equilibrium stability border and not arbitrary computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
