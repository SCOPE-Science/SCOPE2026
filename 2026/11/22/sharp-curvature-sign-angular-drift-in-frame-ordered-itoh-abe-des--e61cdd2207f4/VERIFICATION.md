---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In normal coordinates the Hessian of half the squared distance has radial and transverse eigenvalues 1 and q=rS'_K/S_K. Expanding the coordinate quotients gives G=g+Bu+O(‖u‖²) with B=H/2 plus the skew term (H_12/2)J, J taking E_1 to E_2. The local implicit displacement is −hg+h²Bg+O(h³). Since g=−r e_r is an eigenvector of H and H_12=(q−1)sinθ cosθ, the inward-to-azimuthal skew term is exactly r(1−q)sin(2θ)/4. A radial exponential displacement changes no azimuth, so the leading angular increment is the transverse displacement divided by S_K, with error O(h³). The recurrence r_{j+1}=r_j−hr_j+O(h²) on a compact annulus slightly larger than [r_0 exp(−T),r_0], still in the smooth region, gives a uniform O(h) deviation by bootstrap and discrete Gronwall. Summing angular increments and dividing by h gives the integral in (10); (r/S_K)'=(1−q)/S_K and r'=-r give exactly (1). The opposite strict monotonicities of r/S_K in the two curved cases, and its constant value in the flat case, give the exact signs and maximizing angles. Reversing the coordinate order negates the skew term, proving O(h²) fixed-time angular error for the average. At θ=π/4 the intermediate exponential images for a radial candidate are radial-meridian reflections, with equal objective values, and the two components telescope to the radial secant −r+δ/2. Solving δ=h(r−δ/2) gives (2), with 0<δ<r for 0<h<2 and agreement with the locally unique small-h branch.

## originality

PASS

Credit both the Riemannian ordered Itoh–Abe construction and its same-center symmetrization, including the known general order context. The supported distinct content is the explicit sharp signed, frame-relative fixed-time angular coefficient for the specified radial objective and the exact finite-step bisector radial branch. The examined primary passages and published index did not establish these specializations; this is a bounded coverage assessment, not a priority certificate.

## value

PASS

Even on a canonical objective whose exact trajectory has no angular motion, the ordered dissipative scheme can accumulate a signed first-order azimuth bias, reversed by curvature and by frame order. Its sharp coefficient measures an error invisible in radial dissipation or a generic convergence order. The exact bisector identity is a useful separate benchmark for the established symmetric variant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
