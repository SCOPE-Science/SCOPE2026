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

Reconstructed the operator from its interpolation definition (RESULT.md lines 23–42) and verified the normalization and the three coefficient limits. With x=δ₂u, y=δ₃u and δ₁u=0, the first quadratic panel supplies the terms (2t−1)x/[ε(1+ε)] at both s₂ and s₃. At s₂, dominated convergence with the integrable majorant (1−t)^(−α) yields Jα(1)=1/(1−α)−2/(2−α)=Aα, and the current linear coefficient is O(ε^(−α)), hence disappears after multiplication by ε. At s₃, the first-panel limit is Jα(1+σ)=Bα, positive by reflecting half the interval against the strictly increasing kernel. The short second panel gives O(1) to the x coefficient and O(ε²) to the y coefficient since its kernel stays bounded and its derivative coefficient for y is O(ε). The third linear panel gives the positive finite constant σ^(1−α)/(1−α) to the y coefficient. Thus εΓ(1−α)B₃→Aα x²+Bα xy. Setting y=1 and x=−Bα/(2Aα) yields the stated strict negative constant, and the x=0,y=1 direction is positive for small ε. This is for each fixed 0<α<1, not a uniform endpoint assertion. Inspected both packaged checkers and outputs without executing them. Independent replay `python3 /workspace/replay/check_assignments.py 3` uses Lagrange interpolation and analytic moments, reproduces −3075.1592734497714868379217449 for the normalized half-order integer witness, and checks the scaled limits numerically at α=0.2,0.5,0.8. The replay is supplementary rather than the all-order argument; Decimal antiderivative evaluation is high precision, not exact radical arithmetic.

## originality

PASS

The same normalized unrestricted increment-energy form is studied in prior work, but the strongest inspected statements ensure positivity under ratio conditions. A collapsing middle cell is outside those conditions; the exact negative leading law for all fixed fractional orders neither follows from those sufficient conditions nor conflicts with them. The strongest exact catalogue hit is the bound record itself, not a distinct result. Pass is limited to the all-order fixed-increment obstruction and its exact asymptotic, not to the operator definition or conditional stability theory.

## value

PASS

This explicitly answers the unrestricted-positivity issue for the standard form with only three steps, a witness fixed independently of the collapsing length, and a sharp nonzero blow-up coefficient. It identifies which historical interpolation coefficient creates the obstruction rather than merely selecting a mesh outside a known theorem or reporting a floating-point negative value. This is directly useful when evaluating whether a proof relying on the unmodified increment-energy estimate can avoid mesh constraints. It is not a PDE instability, a maximum-principle violation, or an optimal ratio condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
