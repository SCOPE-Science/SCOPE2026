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

The Fock Toeplitz coefficient identity gives m=int_B dmu and b=int_B z dmu with the stated first-argument-linear inner product. Two distinct quadratic ball-defining functions differ by an affine L, with L(1_B1-1_B2)>0 on the positive-measure symmetric difference; identical (m,b) would force its weighted integral to vanish. The convex Ψ is finite and differentiable at all parameters because the quadratic zero set is negligible; true data give its gradient, and strict two-ball injectivity plus m>0 excludes any other minimizer. Shape differentiation at positive r yields r^n λ^(n+1) det Cov_ν(ω)>0, with uniform boundary support. Invariance of domain supplies the continuous-observation lower bound. The d=1 I0/I1/I2 angular Bessel formula specializes to the stated determinant; centered R² direct calculation at r=1.1 gives positive 0.08540916030474. Assumption r>0, known contrast, indexed (not spectral) data, and lack of global conditioning all matter.

## originality

PASS

Best-of-knowledge PASS for the exact minimal first-Hermite ball reconstruction plus global convex inverse and Jacobian, not a novelty claim for sign separation or truncated moments generally. Gustafsson–He–Milanfar–Putinar reconstruct more general planar polynomial domains from a larger mixed-moment array; their hypotheses do not imply the stronger small-data Gaussian-ball assertion. Other identified Fock localization works concern spectra, Ky Fan/shape derivatives or eigenfunctions rather than this measurement map. Possible weighted centroid / inverse-moment folklore remains a genuine priority risk.

## value

PASS

A natural inverse Gaussian localization problem: the number of independent real center/radius parameters is 2d+1, and the theorem gives matching continuous data, constructive globally unique convex optimization, local analytic stability, and explicit degeneracy boundaries. These are useful exact sensing criteria rather than mere numerical recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
