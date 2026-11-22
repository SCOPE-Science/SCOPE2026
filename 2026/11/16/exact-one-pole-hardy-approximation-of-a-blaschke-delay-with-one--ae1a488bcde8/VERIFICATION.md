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

The normalized Hardy H2 distance to analytic type-(1,1) rationals reduces by orthogonality to maximizing (1-|p|²)|p|^(2N-4)|(p-a)/(1-ap)|². For a>0, differentiation with respect to cos(arg p) is strictly negative, forcing p=-r, and the radial logarithmic derivative L(r) strictly decreases from positive to negative, ensuring a unique global maximizer. The displayed coefficient and exact squared error follow from projection. Differentiating L establishes dr/da<0 while the pointwise radial objective strictly increases with a. Independent symbolic expansion of L(1-1/(2N)+b/N²) gives b=-(9a+1)/(8(1+a)), matching the claimed second term; log capture gives 1/(eN) with stated first correction. At a=0 rotational degeneracy and r²=(N-1)/N are correct. The inspected CHECK.py runs only supplementary finite consistency checks, not the infinite proof.

## originality

PASS

Baratchart et al. (arXiv:2603.16295) treat lower H2 rational-approximation bounds and pure delays, not this exact globally optimized one-displaced-zero type-(1,1) family. Wang and Qian give existence and a general Szegő-kernel projection approach, but no family-specific antipodal pole and exact error in the inspected material. Search also surfaced a related opposite-pole one-state system with a different model; its title and snippet alone cannot rule out equivalence, retained as priority risk. Older control theory may contain equivalent calculations.

## value

PASS

One-pole stable rational reduction of a delayed Blaschke transfer function is a motivated analytic benchmark. The uniquely determined global pole, exact error, movement under zero displacement and sharp 1/(eN) asymptotic calibrate one-state approximation beyond generic existence and lower estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
