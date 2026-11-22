---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For odd n curvature radius rho=w(1+sgn(cos ntheta))/2 gives only odd-n multiple harmonics; support Fourier coefficients decay as 1/[j(n²j²-1)], and Parseval area deficit is positive weighted square of 3-phase Fourier sums. The odd-harmonic pair kernel F_n(t)=sum cos(jt)/[j²(n²j²-1)] has the exact closed expression on [0,pi], and derivative pi/4*(1-cos((pi/2-t)/n)/cos(pi/(2n)))<0 inside (0,pi). A three circular-gap minimizer cannot have a gap >=pi; equal derivative for three interior gaps forces equal gaps, and all collision boundaries are strictly worse by sin(3s)<3sin(s). The maximum deficit is positive because modes j divisible by 3 survive. Taylor expansion F_n(2pi/3)>0 gives the stated local stability. Independently summed Fourier series and closed kernel for n=3,5,9,19, checked exact deficit and a 61x61 phase grid, finding only expected equal-spaced phase pairs on grid; finite mesh corroborates rather than proves global rigidity.

## originality

PASS

Falcó–Myroshnychenko classify minimum-area invariant constant-width shapes, not optimal three independent rotations of a fixed shape. Bogosel treats Reuleaux mixed area with a special opposite copy. Prior exact two-copy Reuleaux triangle phase area, random-rotation means and smooth two-mode nonmonotonicity do not state the constrained three-gap minimization or strict n-general equality classification. Best-of-knowledge novelty is subject to older three-point energy literature.

## value

PASS

The exact deterministic three-copy phase-optimization and strict noncircular residual is a natural sharp geometric symmetrization question, distinct from prior body-shape minimization or two-copy complementary-rotation disk construction. Explicit asymptotic and Hessian rigidity quantify the failure of three-copy averaging to reach the disk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
