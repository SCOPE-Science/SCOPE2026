---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For C f(x)=x^{-1}∫0^x f(t)/(1−t)dt, the coordinate commutator has kernel 1_{t<x}(x−t)/[x(1−t)], bounded by 1 and hence Hilbert–Schmidt. Shifted Jacobi weighted orthogonality and unitary multiplication from L²(x²dx) or L²((1−x)²dx) give two complete orthonormal bases u_n,v_n. Terminating Jacobi hypergeometric coefficients prove ∫0^x(x−t)P_{n−1}^{(2,0)}(2t−1)dt=x² P_{n−1}^{(0,2)}(2x−1)/[n(n+1)] for every n, yielding T v_n=[n(n+1)]⁻¹u_n and the full singular system, not merely a subset. Independently checked this exact integral identity symbolically for n=1,...,6. Telescoping gives trace norm 1, partial fractions give HS²=π²/3−3, and n⁻² singular asymptotics give Schatten p>1/2. Pointwise |T^j f|≤V^j |f| for Volterra integration V and ∥V^j∥≤1/j!, establishing quasinilpotence despite nonzero singular spectrum.

## originality

PASS

An exact complete Jacobi singular system for the coordinate commutator of the real-variable (1−t)⁻¹ Cesàro operator was not established in the inspected founding operator text or related Hardy–Volterra literature. These objects have different kernels even if their n⁻² decay is similar. Best-of-knowledge with residual risk of a broader Jacobi weighted-integration theorem.

## value

PASS

The complete exact singular basis and entire Schatten ideal membership for a natural commutator of an explicitly studied real-variable Cesàro operator fill a concrete spectral gap. The contrast between compact quasinilpotent spectrum {0} and explicit positive singular sequence is mathematically instructive; all-degree Jacobi integration is harnessed nontrivially to solve an operator SVD.

The dated certificate retains the supplied scientific assessment, sources and limitations.
