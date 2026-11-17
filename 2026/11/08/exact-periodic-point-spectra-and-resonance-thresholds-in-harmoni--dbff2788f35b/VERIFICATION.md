---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The statement only concerns the two explicitly named tangent-intersection periodic families for integer n≥6 and 0<ε<n^(−2); it does not count all outer-billiard periodic orbits. From γ(t)=e^{it}+εe^{int}, the speed, curvature and radius at extremal tangencies give ρ_s=(1+snε)^2/(1+sn²ε) and tangent half-length ℓ_s=(1+sε)tan(2π/(n−1)). The co-rotating Jacobian K_s=R(−2θ) [[−1,−2ρ_s/ℓ_s],[0,−1]] is determinant one and has the exact stated trace after factorizing (1+snε)^2−(1+sε)(1+sn²ε)=−s(n−1)^2 ε. The positive-elliptic and hyperbolic trace inequalities and monotonicity hold throughout the open convexity range; jπ/k<φ_* is necessary and sufficient for scalar K_+^k=(-1)^jI. The smaller quadratic root, strictly increasing resonance list, small-ε square roots and logarithmic hyperbolic boundary law follow by exact algebra. Independently computed resonance parameters for n=6,7,8,9,10,11,15,20,40,100 satisfy the original trace equation and ε∈(0,n^(−2)); finite checks are not proof of global monotonicity, which was verified symbolically.

## originality

PASS

Best-of-knowledge PASS: Bialy–Mironov–Shalom introduced this exact harmonic curve family and symmetric tangent-intersection cycles, including geometric elliptic/hyperbolic examples. The inspected original Section 4 does not present the present rational all-ε Floquet traces, exact primitive return multipliers, finite scalar-monodromy parameter census or logarithmic exponent divergence at ε→n^(−2). Ramírez-Ros 2006 addresses perturbation of resonant invariant curves (Melnikov breakup), not the exact linear monodromy of these named discrete periodic orbits. Generic area-preserving Jacobian formula is background, not the claimed contribution.

## value

PASS

The all-parameter stability spectrum and exact resonance thresholds of geometrically natural symmetric periodic orbits answer a motivated bifurcation/stability question for the classical harmonic family. Exact scalar-monodromy exceptions and rigorous boundary exponent are useful precise invariants not implied by descriptive orbit pictures; no nonlinear KAM/bifurcation conclusions are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
