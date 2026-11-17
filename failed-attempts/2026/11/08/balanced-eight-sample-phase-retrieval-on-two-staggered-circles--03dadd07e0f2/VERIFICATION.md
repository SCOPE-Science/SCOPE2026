---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Reconstructed the 3x3 Hermitian lifting: two independent first-harmonic radial equations kill h10,h21; two independent angular Nyquist equations kill h20 exactly if sin(2phi) is nonzero; remaining two DC equations give kernel spanned by diag(r^2 s^2,-(r^2+s^2),1), which has rank 3. Difference of two coefficient rank-one Gram matrices has rank <=2, hence is zero. Explicit aligned-grid and equal-radius pairs establish necessity. For <=7 arbitrary measurements the 9-dimensional Hermitian kernel is at least 2-dimensional, and an odd determinant argument yields a nonzero singular indefinite kernel element when measurements span C^3. Independently recalculated real lifting ranks 8,7,5 for generic, aligned, equal-radius examples. Gaussian convolution uses exact transform, known positive channel factors, and invertible three-tone coefficient rescaling; does not assert L2 periodic signals.

## originality

FAIL

Published October 18, 2026 general theorem gives exactly this necessary-and-sufficient balanced two-circle criterion simultaneously for every polynomial degree d>=1. Taking d=2 and angular base phi1=0,phi2=phi yields the entire submitted phase-retrieval theorem, with the same 4+4 samples, identical boundary obstructions, and even an explicit full-intensity reconstruction. Published November 1 all-degree theorem independently dominates the same d=2 claim. The lifting kernel is a direct linear-algebra unpacking of the already-proved Fourier de-aliasing, and eight-measurement lower bound is known; the Gaussian three-tone corollary is an invertible Gaussian Fourier rescaling, not a surviving independent result.

## value

FAIL

The constrained 4+4 phase-retrieval classification is well motivated but has already been solved for all polynomial degrees; a special-case kernel certificate and routine channel-rescaling corollary do not add a distinct valuable mathematical problem or new obstruction. Correctness does not recover scientific value after exact prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
