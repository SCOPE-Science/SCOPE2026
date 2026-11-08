---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The analytic proof computes the exact two-aliased-frequency matrix with the \(1/\sqrt2\) downsampling factor, evaluates its trace and determinant, and proves monotonicity of both singular-value squares in the alias separation. The spectral collision at \(\cos\theta=0\) blocks a positive frame lower bound on the full Fourier band for any finite number of diffusion times. A uniform bound \(0\le c^{-2}A_c(t)\le t^2e^{-t}\), for \(0<c\le1/2\), justifies passing the maximum over observation time through the small-gap limit.

Run `python CHECK.py` with NumPy and SciPy. It tests 49 combinations of spectral notch and heat time using an independently constructed two-by-two matrix, compares the asserted extremal eigenvalues against 1001-point frequency sweeps, and constructs actual spatial Fourier measurements on periodic chains of 128 and 256 sites. It also tests the limiting optimal-lag constant numerically. These finite computations are not an infinite-dimensional proof and make no independent validation claim. Source inspection limitations and originality risks are described in REVIEW.md and AUDIT.json.
