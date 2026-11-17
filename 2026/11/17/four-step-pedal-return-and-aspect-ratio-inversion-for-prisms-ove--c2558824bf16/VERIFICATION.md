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

# Verification details

The full proof checks all facet equations through polar duality, both apex signs, and the equal-radius constraint on every original vertex. The first two-step formula is exact; the four-step formula follows by substituting the inverted aspect ratio. The strict two-step resonance condition is \(h=a\), and \(0<\Gamma<1\) follows for all positive parameters with \(R\ge a\).

The included `verify_pedal.py` independently enumerates facet hyperplanes using numerical convex hulls, projects the origin onto these planes, and compares the unordered predicted and actual vertex sets for both a regular pentagonal prism and a nonregular tetrahedral-base prism. It reports floating-point residuals and tests them at tolerance \(2\times10^{-6}\). Finite diagnostics are not proofs for unrestricted dimension or parameters. There is no independent mathematical audit or external certification.
