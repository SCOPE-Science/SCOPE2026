---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

Every active spectral mask occurs on an open set of DCT coefficient space; the continuous piecewise-affine map has global seminorm Lipschitz constant equal to maximum mask projection seminorm. Step decomposition h=h_0*1+sum differences*H_a reduces the seminorm to single-step images. The product of DCT step coefficient and its first difference is (2/n) sin(pi*k*a/n) sin(pi*k*b/n), exactly the DST-I projection kernel. Orthogonality yields the sqrt(n-1) column bound. Independent fair-mask signs and the fourth-moment inequality E|X|>=sqrt(E X²)/sqrt(3), together with the sine squared-product sum >=n/4, establish the explicit lower bound. Local open-cell pairs attain the maximum. Independent exhaustive masks n=2..8 and DST orthogonality tests passed; finite checks are not a substitute for the all-n proof.

## originality

PASS

The exact nonlinear two-input DCT-II BV coefficient is mathematically equivalent to the unconditional DST-I spectral-mask column-norm problem. Full Strang DCT analysis supplies the transform but not nonlinear shrinkage in path variation; Durand–Froment wavelet-TV reconstruction concerns another transform and optimization. The indexed prior Haar/Walsh BV thresholds have different bases and growth rates; no exact DCT-II law or dominating bound was identified. A general unconditional basis theorem could cover the Theta(sqrt n) rate and is a material residual priority caveat.

## value

PASS

The operator is Euclidean nonexpansive but amplifies the natural ordered signal graph variation by Theta(sqrt n). A sharp *attained* finite mask formula and all-dimensional rate characterize a substantive stability boundary for classical coefficient denoisers; this is more than a computational toy or generic norm equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
