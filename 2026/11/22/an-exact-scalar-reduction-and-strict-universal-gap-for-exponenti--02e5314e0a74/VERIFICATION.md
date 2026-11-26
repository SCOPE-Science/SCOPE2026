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

At a smooth exterior input tp+λv, p·v=0 and p,q,v (q the tangential part of p′ orthogonal to p) form an orthogonal basis. The input differential in the q direction has coefficient t+λe^r/||q||², whereas the output has coefficient t, since v′·q=e^r and v′·p=0. The invertible normal parametrization thus gives Jacobian eigenvalues 1, ρ, 0 in those directions. The polar projects to zero and the cone interior gives identity. For a nonzero flat-face output (-a,0,b), a,b≥0, a normal lies in the polar and is orthogonal to the output. A polar vector has first component ≥0 and third ≤0; orthogonality forces the first to vanish if a>0, or the third if b>0. If the third vanishes, testing on (r,1,e^r) as r→+∞ forces the first to vanish too. Testing r→−∞ then forces the second to be nonpositive. Hence this branch has input x≤0,y≤0 and projection (x,0,max(z,0)); the residual seams, cone boundary and polar boundary are null sets. Mollification propagates the a.e. row-norm bound globally. Conversely, at each fixed r the two endpoint Jacobians are limits at λ→∞ and λ↓0, furnishing lower bounds for the true Lipschitz constant. Maximizing coordinate row sums reduces to the stated R,H; the equality ratios follow from Cauchy–Schwarz in the two other coordinates and maximizing over the distinguished magnitude. Neither p(r) nor v(r) realizes these ratios: in particular (1−r)e^r≤1 for r≤1, equal only at 0. Both scalar functions tend to 1 at each end; R(1)>1 and H(0)=4/3, ensuring finite attainment separately and hence a strict uniform gap. An independent numerical evaluation gives 1.3660217223118953 at the stated radial witness and 1.3660254037844386 at the ceiling; the analytic proof, not the decimals or supplied grid, establishes strictness. The supplied checker was inspected, not executed.

## originality

PASS

Credit the known exponential-cone projection geometry, general projection sensitivity and universal non-strict bound. The surviving cone-specific results are the exact full-projector scalar norm formula and the proof that its optimal constant strictly misses the universal bound despite the close analytic lower witness.

## value

PASS

This gives a sharp global coordinate-error coefficient for a standard optimization cone, including branches near its singular face. The analytic scalar extremum is useful without a closed-form optimizer: it replaces a supremum over two inputs by explicit functions of one real variable. The narrow numerical interval is meaningful because it certifies near-worst-case coordinate amplification while distinguishing it from exact saturation, not because of extra decimal places or a tiny algorithmic improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
