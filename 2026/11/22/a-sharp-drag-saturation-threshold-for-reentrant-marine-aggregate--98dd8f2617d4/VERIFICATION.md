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

The numerator g is strictly concave, positive at zero and tends to −∞. Its unique positive zero x_b has g′<0, hence H(x_b)<0; the displayed cutoff is the positive root of the multiplied quadratic. V′ has the sign of H and the positive factor (1+x)^3 turns H′ into Q with Q′<0. If Q(0)≤0 then H falls throughout; otherwise it rises to exactly one maximum at z and falls thereafter. Q(0)>0 implies b>c; x₀=√(b/c)−1 lies below x_b and H′(x₀)=(1+ηx₀)g″(x₀)<0, so z<x_b. The exact two-root test is then H(0)<0, Q(0)>0, H(z)>0; H(0)=0 is a boundary, not a first interior extremum. If H(z)=0, H′(z)=0 and H″(z)=Q′(z)/(1+z)^3<0: V′ is negative on both sides and V‴(z)<0, giving a stationary inflection. At or below η=2/(1−α), Q(0)<0 for all b,c>0. Above it choose b/c large enough for Q(0)>0 and first set a₀=(b−c)/(αη); then H(0)=0 and H(z)>0. A small positive perturbation of a makes H(0)<0 while preserving H(z)>0, proving realizability for each α,η above the frontier. Independent symbolic reconstruction of the stationary polynomial and exact signs at 0, 1/10 and 2 gives two roots below the buoyancy cutoff in the witness. The α=1/3 threshold is strictly η>3.

## originality

PASS

The exact result is for a specified rational excess-mass response and power-law volume drag, not general Stokes terminal velocity or the existence of competing physical effects. The checked alternate saturation models optimize different maps; the inspected physical model resolves different constitutive variables. No confirmed stronger theorem gives this family and two-root criterion. This is a best-of-knowledge judgment, with the closest motivating articles' unavailable passages explicitly retained as risks, not counted as exclusions.

## value

PASS

Opposing buoyant loss, saturating mass gain and size-dependent drag motivate asking whether a load–speed curve can reverse slope twice before flotation. The work gives a strict universal exclusion/realizability boundary controlled by the ratio of the saturation and drag-load scales, and a usable necessary and sufficient coefficient test that includes the tangency. It is more informative than a numerical reentrant example or a slope calculation at zero. It provides a benchmark for evaluating this explicitly assumed response law; it does not make an ocean-wide prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
