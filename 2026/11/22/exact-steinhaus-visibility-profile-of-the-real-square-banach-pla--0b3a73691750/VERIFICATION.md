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

For a>=1, z=-x attains the reverse triangle bound for every pair. For 0<=a<=1 write delta=||x-y||_infty and h(u)=max(1-a,|u|). The increment h(u+delta/2)-h(u-delta/2) is odd and nondecreasing by evenness and convexity, and at u=a it is min(delta,max(0,2a+delta/2-1)). On a shared facet z_1=-a and the sign of z_2=±a chosen according to the pair midpoint give at least this increment in absolute value. On adjacent facets the two pertinent square corners yield min(2a,alpha) and min(2a,beta), where alpha and beta are the coordinate gaps; their maximum dominates the desired bound. On opposite facets delta=2 and a shift toward one facet and toward the other point's transverse coordinate gives 2a. These cover boundary corners as well. The lower bound is nondecreasing in delta. For the centered pair (1,±d/2), fixing z_2 makes the norm difference nonincreasing in the common floor |1+z_1|, so the maximum is at z_1=-a and then |z_2|=a. This proves equality including a=0, d=2 and the regime endpoints. The displayed real map is a surjective isometry since (|u+v|+|u-v|)/2=max(|u|,|v|).

## originality

PASS

The distinct claim is the entire absolute-value modulus in the real square, not the qualitative failure of property (S). The frozen comparison with Johnson–Kania should not call their definition the exact same modulus: their Definition 1.1 uses a signed norm difference. This attribution imprecision does not change the mathematically explicit Finding. For example, at d=1 and a=2/5, the signed modulus of the square would be zero (take ordered x=(1,0), y=(1,1), so ||x+z||=|1+z_1|<=||y+z|| throughout the ball); the absolute-value modulus here is 3/10.

## value

PASS

A qualitative counterexample to property (S) leaves open how much perturbation is needed to distinguish two norm profiles or to recover their full separation. This natural atomic model gives both sharp thresholds, the intervening slope, and a uniform extremizing pair. The result provides a quantitative benchmark not supplied by qualitative atomic obstructions or small-radius estimates in other geometries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
