---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Re-derived the projected ellipse (semiaxes 1,c) and on-minor-axis projected apex hs, and integrated their maximum support function with no factor-of-two ambiguity. In the active interval (α,π−α), cot α=z=√(h²−(1+h²)c²) and s cos α=z/√(1+h²). Moving-boundary terms cancel, giving ∂hP=2z/√(1+h²) and, after division by 2c, the stated J+J₀−B for the c derivative. The h derivative is strictly below the side-on derivative for every c>0, including at activation, so the continuous positive-at-zero difference crosses strictly once and tends to −∞ for fixed c>0 by P≤4E+2hs. In the short-cone argument the derivative of B² as a function of x=c² has sign h²−1−(1+h²)x, so B≤1/√2<π/4≤J for 0<h≤1. NIST DLMF 19.12.2 with complementary modulus k′=c gives the stated expansion; the analytic incomplete-arc correction is uniformly O(c²) on compact positive height intervals. Therefore h_c tends to ∞ at c=0 (use positivity at each fixed large height and the strict crossing), and a continuous crossing family attains its minimum; 1 cannot be the minimizer in c since a nearby inactive ellipse beats the axial tie at h₁. Attainment in the interior then gives the strict height bounds, and the uniform side-on penalty rules out oblique winners near c=0 at the switch. Axial views are excluded at all positive heights by the inactive ellipse comparison. A separate 35-digit support-quadrature calculation obtained the stationary tie c≈0.795726767064798, h≈1.601499304498265; it is not a global or interval certificate. Packaged checker inspected but not executed; the result does not assert uniqueness of the oblique latitude or a certified decimal.

## originality

PASS

Best-of-knowledge pass for the global directional perimeter phase switch paired with local side-on persistence. The support integral and the elliptic singular expansion are classical ingredients; neither is itself novel. Same-cone projection literature is relevant and public full-text access to Vickers–Brown was not obtained independently, as detailed below.

## value

PASS

Minimizing the perimeter of an orthogonal silhouette is natural for a canonical convex body. The global jump with strict local persistence on the losing side is stronger than a one-view ellipse formula or a numerical aspect-ratio estimate; the normalized logarithmic barrier explains the qualitative difference from the bicone. The theorem remains useful without a count of oblique minima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
