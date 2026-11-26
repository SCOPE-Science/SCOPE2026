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

The coupled passive vector has norm sqrt(W); its orthogonal complement is exactly a dark direct summand. Eliminating the three bright leaf coordinates gives lambda - 2t^2 lambda/(lambda^2+gamma^2) - W/lambda = 0; clearing denominators as a polynomial gives the stated quartic. The squared-energy roots have product -W gamma^2, so for positive W and gamma there are four simple bright roots and m-1 semisimple dark zeros. At gamma=0 the bright polynomial is lambda^2(lambda^2-S): the whole matrix is Hermitian and the zero multiplicity is m+1. The four-simple-root statement is read in its stated positive-gain setting. For x=beta^2 the root equation is x^2+(2t^2+W-gamma^2)x-W gamma^2=0; evaluation at 0 and gamma^2 brackets it and implicit differentiation gives positive derivative. The equation divided by W proves the upper limit, and the quadratic formula gives the lower limit. The 2-by-2 active-leaf minor at uncoupled criticality is nonzero; the nilpotent 3-by-3 trimer therefore has rank 2 and a single size-three block, with the uncoupled neutral zeros separate. Near W=0 the small squared root is given by the constant term divided by the persistent root; at criticality lambda^4-W lambda^2-2t^2W=0 gives the stated leading constant and a square root in the hopping norm, not an EP4. The frozen numerical checker was read, not executed; its nearest-eigenvalue test is not a multiplicity certificate, which the block proof supplies.

## originality

PASS

The generic thresholdless onset and the uncoupled path threshold are already known. The surviving claim is the exact arbitrary-weight open-star classification over the entire positive-gain axis, including no reentrance or exceptional point and the singular weak-spoke limit. A same-day adjacent record contains the identical unit-spoke polynomial in its zero closing-link limit; this is genuine partial algebraic overlap, not a competing derivation of the variable passive-weight weak-coupling classification. No inspected earlier source covers the surviving combination.

## value

PASS

A pendant conservative channel is a minimal physical perturbation of a standard gain–loss trimer. Distinguishing immediate local breaking from permanent failure of an all-real regime and simultaneous disappearance of all exceptional points is a meaningful exact classification. The amplitude scaling at the former EP distinguishes a structured coupling to an independent zero mode from an EP4 and quantifies its effect beyond the generic degeneracy argument. Applicability is the specified finite weighted, zero-detuning one-particle family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
