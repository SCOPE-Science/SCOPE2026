---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Only four square corners can contribute when R<1; the third-smallest distance squared is 1/2+s²+t²+|s−t| and the largest is 1/2+s²+t²+s+t. Folding contributes constant density four and independent fair quadrant signs. The linear inverse map has Jacobian ε^{3/2} for the cap and ε² for the four-point event, with no further truncation in the stated ε range; a diagonal segment beyond the four-point region has an open neighborhood with exactly three corners. The exact supports are nested in the limits. The cap's excluded wedge has area √ε/2+O(ε^{3/2}); the upper boundary changes its integrated area by O(ε), using a square-root difference bound by a constant times ε/√(1−|y|) and bounding the O(ε) endpoint interval separately. For the four-point region write r+q=ρ, r/ρ=a; the radial cutoff solves ρ+ερ²[a²+(1−a)²]=1 and the Jacobian is ρ. Uniform first-order expansion gives area 1/2−2ε/3+O(ε²). Removing the four-point region costs √ε times this area in cap coordinates. The nested-uniform TV identity yields the three coefficients with the stated event distinctions. The radial limit is √2X and the width 2(1−2x²) gives its density after normalization. Own finite quadrature in the original folded coordinates corroborates all three coefficients (python /workspace/checks/reproduce.py 2); it is not the proof.

## originality

FAIL

Demonstrable prior implication, not an access-based failure. The earlier result 1098c654ec0a gives exact spatial supports in anisotropic diagonal-lens and diamond coordinates, not merely scalar occurrence probabilities. Folding and rescaling those sets gives the exact conditional uniform laws, the limiting shapes and all three TV formulas by a direct change of variables, uniform normalization and one elementary Taylor coefficient. No separate historical claim about the wording of the conditional laws is needed for that implication.

## value

FAIL

The conditional spatial description is clear and potentially useful exposition, but the earlier record already isolates the two spatial scales by its exact lens/diamond equations. All claimed quantitative improvements follow by routine normalization, marginalization or differentiating its explicit areas. No non-covered, independently valuable mathematical remainder was established; no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
