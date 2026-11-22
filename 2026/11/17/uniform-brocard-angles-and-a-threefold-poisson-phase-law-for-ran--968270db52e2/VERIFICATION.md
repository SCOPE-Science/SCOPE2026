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

A random oriented cyclic triangle has angles (A,B,C) with (A,B) uniform density 2/π² on A>0,B>0,A+B<π, by the Dirichlet(1,1,1) boundary-gap law. With x=cot A,y=cot B,z=cot C, identity xy+yz+zx=1 and K=x+y+z yield an exact radius-s cotangent circle s²=K²−3. The parametrization x=(K+2s cos φ)/3, y=(K+2s cos(φ+2π/3))/3, z=(K+2s cos(φ+4π/3))/3 bijects the positive-angle simplex except its equilateral point. Its two-dimensional Jacobian |∂(x,y)/∂(K,φ)|=(x+y)/√3 gives |∂(A,B)/∂(K,φ)|=9√3/[2(K³+9K−s³ cos3φ)]. Multiplying 2/π² gives the joint density. Direct algebra verifies (K³+9K)²−(K²−3)³=27(1+K²)²; integrating 1/(a−b cos 3φ) gives f_K=6/[π(1+K²)]. Since dK/domega=−(1+K²), omega is uniform on (0,π/6). Normalized conditional kernel has r=b/(a+√(a²−b²)) and its weak limits r→0 and 1. Density tail ~k^-2 establishes moments p<1. Independent centered finite-difference Jacobians at (K,φ)=(2.1,0.1),(4,1.3),(10,2.5) agreed with exact Jacobian within ~10^−9 relative; this corroborates, but the distribution proof is analytic.

## originality

PASS

Best-of-knowledge PASS for the evaluated random-circle Brocard marginal and its exact marked cotangent-circle phase conditional law. Deterministic Brocard identities, uniform triangle-angle simplex, fixed-Brocard side-ratio constraints and Poisson-kernel integration are acknowledged inputs; the particular pushforward is not implied by the inspected published statements.

## value

PASS

An exact, unexpectedly uniform nonlinear geometric angle law for the simplest natural random cyclic triangle, plus the full correlated marked shape distribution, supplies reusable closed-form sampling and conditional law beyond textbook cotangent identities. The exact first-moment and moment cutoff are natural consequences; the substantive value is the evaluated joint probability law, not numerical simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
