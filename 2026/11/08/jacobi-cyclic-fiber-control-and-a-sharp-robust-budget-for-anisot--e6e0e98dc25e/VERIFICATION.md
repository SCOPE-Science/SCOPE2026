---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The PBH test reduces the exact coordinate-input minimum to injectivity on each eigenspace of the symmetric Kronecker sum. Irreducible Jacobi recurrence gives u_i(k)=u_i(0)p_k(alpha_i), with nonzero endpoint values, degree-k polynomials and leading coefficient (-1)^k/(c_1...c_k). Cyclicity of the B-root means simple beta_j and v_j(h) nonzero. Each repeated sum alpha_i+t beta_j uses distinct i and j; the s×s consecutive-fiber determinant is the Vandermonde times those nonzero endpoint factors. Rank s is attained and <s is impossible. For square-grid gamma_i=2-2cos(pi*i/n), at t=1 the n-1 pairs i,n-i (1<=i<n) yield eigenvalue 4. Multiplicity n at any t would force order-reversed pairing; endpoints force t=1, but gamma_1+gamma_(n-2)-gamma_(n-1)=4cos(pi/n)(cos(pi/n)-1)<0, contradicting it. Thus fixed n-1 boundary actuators control for all t>0, n>=3. An independent spectral check showed the claimed n-1 resonance for n=3..7; finite checks are not proof.

## originality

PASS

No inspected prior result asserts both the arbitrary rooted cyclic second-factor sharp placement and the fixed all-positive-anisotropy n−1 budget. The earlier path-grid determinant framework is credited; an implicit generalization in existing spectral controllability theory remains a genuine originality risk.

## value

PASS

A sharp parameter-uniform actuator budget saves one boundary actuator beyond full-row zero forcing in an entire nontrivial anisotropic square-grid family, and the Vandermonde construction supplies the missing attainment of the maximal eigenspace-multiplicity lower bound for general Jacobi⊗cyclic-root networks. This is a motivated spectral/control structural theorem rather than a raw numerical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
