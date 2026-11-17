---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the specified self-inclusive asynchronous minority rule every active vertex flip makes same-color edge energy E nonincreasing. E>=m, equality exactly when each triangle nonmonochromatic; from every E>m state some monochromatic triangle permits a strict peripheral energy decrease. At E=m, for each fixed hub color the m independent edge-neutral peripheral coordinates form P3^m; hub may flip exactly when all m coordinates are corners, with 2^m matching cross-layer edges and therefore one irreducible 2*3^m-state class. Symmetric transition rates 1/(2m+1) imply uniform stationary law; fraction (2/3)^m of corners gives rate (2/3)^m/(2m+1). Starting from stationarity conditioned on one hub layer, union bound on hub crossings gives TV >=1/2-t r_m and lower mixing bound ceil(1/(4 r_m)). Independent exhaustive enumeration m=1..4 recovered energy structure, recurrent connectivity, cross-layer counts and stationary rate. Does not establish any matching upper bound on mixing time.

## originality

PASS

Best-of-knowledge originality: older Rouquier–Regnault–Thierry self-inclusive minority analysis has the same update and monotone energy but examines cliques, paths, cycles and tree cases, not the product geometry or windmill bottleneck. Published stochastic-minority bottleneck on K_m,m,m is for a different graph and yields a six-hypercube attractor, not the 2*3^m two-P3^m structure. Synchronous windmill minority results with numerically equal counts are not asynchronous recurrence. No identified publication implies the exact 2^m cross-layer matching, stationary hub-switch rate or F_m bound.

## value

PASS

The exact rare hub-flip mechanism supplies a motivated natural family where one recurrent class and uniform stationary law coexist with exponentially slow cross-layer mixing. The two-layer Cartesian product decomposition, stationary transition rate and rigorous conductance lower bound are mathematically useful even without a sharp upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
