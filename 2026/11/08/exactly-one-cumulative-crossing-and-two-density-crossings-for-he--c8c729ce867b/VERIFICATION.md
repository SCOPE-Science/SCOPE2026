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

# Verification scope

The proof's decisive global step is strict convexity of \(K(s)\), together with two endpoint signs and one negative interior value implied by \(\Delta'(z)\). This yields exactly two simple density roots; the derivative sign pattern implies exactly one cumulative crossing. Jensen convexity/concavity yields the strict support bracket. A uniform second-order expansion at \(D=\mu\) yields the weak-disorder roots; finite sampling alone would not prove any of these statements.

The self-contained script `verify_crossings.py` was executed using NumPy, SciPy and SymPy. It checked both analytical complementary-error-function derivative identities and solved 185 representative laws (one two-atom prototype, 180 seeded random discrete laws with 2 through 7 atoms, and four Gauss–Legendre discretizations of the continuous uniform law). The run passed 1,852 deterministic symbolic and finite-numerical assertions. A second high-precision weak-disorder calculation was used to confirm the root-limit scaling, but that experiment is not a substitute for the Taylor proof.

For a two-atom law with equal weights at diffusivities 1 and 4 and starting distance 1, the density crossings are approximately 0.041349063 and 0.461690201, with the unique cumulative crossing at approximately 0.076433483. This lies strictly between the support-derived bounds 0.041666667 and 0.166666667. All times use the convention \(dX_t=\sqrt{2D}\,dB_t\).

These checks were carried out as self-review only. No external or independent audit has been performed.
