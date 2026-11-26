---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The normalized matrix is determined by the leaf entries u_i=√(w_i/W) appearing twice; duplicating entries has no effect on the maximum-entry norm. For m=1 the sole spoke entry is identically one and the modulus is zero. For m≥2, differentiating gives opposite signs on diagonal and other inputs, and the absolute row sum at a given w_i=x and S=Σ_{j≠i}w_j is [S+(m−1)x]/[2√x(x+S)^{3/2}]. Its S derivative has the sign of (5−3m)x−S<0, so equality in the reduction requires every other weight to be a. Taking z=x/a reduces the row maximum to g_m(z)/a. Integrating the derivative over segments gives the global upper bound, and sign directions at arbitrarily close interior points give the matching lower bound even when the maximizing profile is on the domain boundary. For each z>1 the ratio g_m(z)/g_m(1) increases strictly with m. The factorization at m=18 is positive after division by z−1 for z>1, by the stated square plus positive terms, so uniform is uniquely optimal there and at lower m≥2. At m=19, z=4 gives a negative squared-ratio comparison numerator −1107 for 1−[g_m(4)/g_m(1)]², and monotonicity excludes the endpoint for all larger m. The derivative numerator's two roots exceed one (for m≥19, (m−9)^2 minus the discriminant equals 48); the smaller is a local minimum and the larger r_m the only remaining maximum, since g_m tends to zero at infinity. Hence maximizing profiles for m≥19 are precisely the indicated profiles up to the choice of exceptional spoke. Dividing the radical by m gives r_m/m→1/2 and substitution gives aL_m(a)→1/(3√3). The optimizer switch concerns m≥2; at m=1 all conductances give the same constant matrix.

## originality

PASS

Degree normalization, filter robustness, and differentiating the normalized entries are prior or routine. The specific optimization over lower-bounded raw weights gives the sharp max-entry modulus and identifies the globally extremal profiles across all leaf counts; neither a covering formula nor an immediately implying stronger result was located in the inspected material.

## value

PASS

This is the complete sharp response of a canonical normalization under independently bounded conductance errors on a natural graph family. The uniform profile remains a local boundary maximum even after losing global optimality; the nineteen-leaf cutoff measures a genuine competition between profiles, not just the first appearance of a stationary point. The asymptotic imbalance producing a positive limit explains why increasing degree does not by itself cause this max-entry sensitivity to vanish. The exact modulus can be used as a baseline before analyzing any composite filter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
