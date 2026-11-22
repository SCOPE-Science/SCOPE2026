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
# Verification notes

The analytical proof uses a one-variable exact Cauchy brightness identity, a known isolated global maximizing-direction switch, a direct computation of the negative oblique second derivative, the analytic Morse superlevel-length expansion with an odd-order cancellation, the envelope theorem, and a second-order expansion of the competing local maximum. The conditional total-variation limits follow from rescaling intervals whose endpoints converge; the underlying absolute axial cosine density is exactly uniform. The mathematical proof is independent of the finite checker.

Run `python3 verify.py` after installing NumPy and SciPy. Actual execution returned `CONE_RANDOM_BRIGHTNESS_CRITICAL_TAILS_OK`, with k_c near 2.641402552, d near 0.7767760421, κ near 3.667631058, and β near 0.1898838274. The script reconstructs projection areas from 4,096-gon convex hulls, tests the exact brightness and curvature, uses bounded roots to compute the true one-dimensional upper-tail measure, and checks fixed-aspect and both moving-aspect regimes.

A numerical check at finitely many parameters does not establish uniformity, mathematical independence, or historical priority. No automated proof certificate, independent audit, or exhaustive literature search is claimed. Historical risk is discussed separately in REVIEW.md and AUDIT.json.
