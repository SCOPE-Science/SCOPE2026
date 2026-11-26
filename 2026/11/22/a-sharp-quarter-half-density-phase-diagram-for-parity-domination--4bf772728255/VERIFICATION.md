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

All four neighbors are distinct for m,n≥3, so the indicator problem is exactly Ax=1 over F₂, with A=S+S⁻¹+T+T⁻¹. An independent short route to the decisive identity verifies the polynomial proof: U=ST and V=ST⁻¹ commute and (I+U)(I+V)=SA. If Ax=1, multiply the resulting (I+U)(I+V)x=1 by the two length-a geometric sums in U and V. Each sum fixes the constant-one vector because a is odd. Thus (I+Uᵃ)(I+Vᵃ)x=1. When m divides 2a, I+S²ᵃ cancels in this product, so Sᵃ(Tᵃ+T⁻ᵃ)x=1, or (I+T²ᵃ)x=1. This verifies the asserted shift and normalization for every feasible solution. If 4 divides neither dimension, the order of T²ᵃ is n/gcd(n,2a), odd; iteration is impossible. In the mixed case the shift pairs selected and unselected sites and gives exactly mn/2. The column-only 0011 series is feasible when 4 divides n; the two neighbors in the fixed coordinate agree, while those in the varying coordinate have opposite membership. When both lengths are fourfold, incidences give |D|≥mn/4. In the period-4 witness rows 0 and 2 contain complementary adjacent column pairs, rows 1 and 3 are empty, each vertex in an occupied row sees one horizontal selected neighbor, and each in an empty row sees one vertical selected neighbor. The pattern therefore attains equality, including length 4; swapping coordinates proves the other asymmetric case.

## originality

PASS

The full odd-open phase diagram and forced complementation are the distinct claims supported by the comparison. The both-fourfold quarter-density branch by itself is covered: prior existence of parallel total perfect codes gives equality in the four-regular incidence bound. No originality credit is assigned to that branch in isolation. Perfect open domination results do not settle the affine parity problem in the other regimes, where the number of selected neighbors may be three.

## value

PASS

Feasibility, exact support, and a constraint on every configuration on a standard periodic graph are useful beyond the known perfect-code case. The odd factor of a circumference forces a translation to exchange selected and unselected sites, explaining why the mixed regime cannot approach domination density one quarter and why the other regime is empty. This is a structural classification, not a re-computation of the fourfold code or a small finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
