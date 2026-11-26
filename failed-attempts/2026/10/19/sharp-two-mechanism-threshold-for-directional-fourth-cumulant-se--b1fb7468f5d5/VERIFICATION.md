---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the basis of symmetric and antisymmetric opposite-heading pairs, zI−Q has 2×2 blocks with determinants z(z+2s) and (z+s+2c)²+(a−b)². The diagonal tilt couples those blocks via diag(vk_x,vk_y); expanding the coupled determinant gives the stated quadratic tilt term (the antisymmetric entries cancel) and the positive quartic product v⁴k_x²k_y². Zero is simple and the other eigenvalues have strictly negative real part for all allowed rates. The analytic eigenprojection gives a nonzero generating-function amplitude near the origin and an exponentially smaller remainder, with bounded derivatives after taking the log and subtracting the dominant linear-in-time term. Rescaling to s=v=1 and writing R=1+2r, the quadratic eigenvalue coefficient is A=R/(2H) and the quartic B satisfies 2HB+(H+4R)A²−(R+1)A+cos²θ sin²θ=0. Hence 8H³B=N_ax−H²sin²(2θ). Here H²−N_ax=d⁴+(R²−2R)d²+2R³=N_diag, bounded below by 7/4. Restoring v and s and multiplying the coefficients by the factorials gives the asserted cumulant rates. The factorized axis term gives the transition including its equality cases, and the strictly negative diagonal term gives the stated sectors and zero rays. The c=0 rate ratio, the equal-turn threshold and the independent-Gaussian addition also follow. A separate exact symbolic derivation confirmed the determinant and coefficients; the frozen checker was inspected but not run.

## originality

FAIL

The distinct indexed result ec488e19dc0f states the full same phase and sector classification, including equal-chirality and reversal thresholds and strict diagonal negativity, on a wider rate domain. Its formulas specialize exactly to the assigned result. This is existing mathematical coverage at review, not proof of historical priority: the indexed broader record has a later listed date. The older same-model Mallikarjun–Pal resolvent encodes cumulants but is not the decisive basis of the failure.

## value

PASS

As mathematics this is a natural phase classification: a covariance measurement cannot distinguish axes and diagonals, while the connected fourth cumulant separates them and identifies distinct routes to a positive axial rate. The angular boundary gives precise projections for that contrast rather than just a numerical example. This usefulness is shared with the covering result and does not support an independent originality pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
