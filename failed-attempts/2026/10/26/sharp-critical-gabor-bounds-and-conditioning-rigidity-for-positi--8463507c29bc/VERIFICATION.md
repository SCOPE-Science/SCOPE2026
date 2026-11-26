---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With the stated Fourier convention the pole at -iu gives -2 pi i exp(-2 pi u xi) for xi>0 and zero for xi<0. Bochner integration is justified by the positive lower cutoff and finite mass. The physical lattice dilation gives the squared normalization alpha^(-1). On the unit Zak cell the Fourier series is a positive mixture of r^omega/(1-r exp(2 pi i x)), apart from a common phase and 2 pi. The modulus is bounded above by the integral of 1/(1-r). The real-part inequality follows by clearing denominators, with numerator r(1-r)(1+cos(2 pi x)); together with r^omega>=r it gives the integral of r/(1+r) below. The corner limits (0,0+) and (1/2,1-) come from positive-measure neighborhoods by dominated continuity, verifying essential sharpness. The identity for the ratio follows exactly by completing the square in [1+r-kappa r(1-r)]/(1-r^2). Positivity makes the integral vanish precisely at the given single height. The universal barrier is sharp allowing any positive lower cutoff; for a prescribed cutoff above the optimizer it remains valid but equality is excluded. The frozen checker and its recorded output were inspected, not executed.

## originality

FAIL

The stronger October 25 causal completely monotone theorem already gives exactly the two sharp bounds by the unitary Fourier transform, with the same hypothesis on the image and even weaker decay assumptions allowed. The remaining universal optimum and quadratic deficit are mechanically obtained by completing the square in the ratio of those known formulas; there is no independent sharp mixture-conditioning classification beyond this scalar identity. This is verified coverage plus a direct algebraic implication, not an inaccessible-source verdict.

## value

FAIL

Sharp reconstruction bounds for a class of windows are useful, but here the two bounds and their full generality are transferred from earlier bounds by a standard unitary symmetry. The proposed remaining invariant is ratio optimization by one scalar quadratic completion of those bounds, without an additional independent technical result. This does not supply a valuable distinct repaired remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
