---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The root-to-vertex integration operator is unitarily equivalent (via derivative D on H^1 tree functions vanishing at the pendant root) to the compact embedding from the rooted H^1 energy space to L², so its singular values are reciprocals of positive square roots of the Dirichlet-at-root, Kirchhoff-interior, Neumann-at-leaves Laplacian eigenvalues. For 0<k<pi/2, stem eigenfunction C sin(kx), middle branches U cos(ky)+B_j sin(ky), and terminal Neumann profiles lead exactly to (cos²k-e sin²k)B_j=U(e+1)sin k cos k and C cos k=sum_j B_j. If cos²k!=e sin²k then B_j coincide and cos²k=(de+d+e)sin²k, giving simple k0=atan(1/sqrt(Q)). If equality holds then C=0 and sum B_j=0, giving k1=atan(1/sqrt(e)) of multiplicity d−1. These exhaust k<pi/2; Q>e ensures s1>s2>2/pi. Inverting Q=(d+1)(e+1)-1 and e gives ordered d,e; (2,7) and (3,5) collide in s1 and separate in s2. An independent conforming piecewise-linear finite-element assembly on actual graphs for (d,e)=(2,2),(2,7),(3,5) matched k0²,k1² within 1e-4, with second multiplicity d−1, only corroborative.

## originality

PASS

Metric-tree Laplacian reductions, equilateral graph characteristic functions, and full-spectra inverse problems have long-standing priority. The narrow best-of-knowledge contribution here is the explicit first-two Hardy singular values for a pendant-root, *Neumann-leaf* stem-plus-two-tier tree, their multiplicity, complete product-collision condition and recovery of (d,e) from only two numbers. The inspected regular star-tree paper instead imposes Dirichlet leaves and homogeneous branching; the 2023 full-spectrum inverse treatment uses a different data budget. A generic determinant method could readily reproduce the special formulas, which is a genuine residual risk; it does not by itself state this two-value inverse classification.

## value

PASS

A root-to-point Hardy operator on a natural stemmed two-generation branching tree has a structural spectral ambiguity: one leading norm sees only the product (d+1)(e+1), but the next eigenmode encodes e with multiplicity d−1 and eliminates collisions. The precise two-measurement inverse reconstruction is a natural and complete finite-parametric spectral rigidity fact, not an arbitrary numerical slice or a mere copy of a known table. General reductions provide method, while the particular minimal inverse data statement is motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
