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

Discarding the null endpoint 1, write x=t+kd uniquely with 0≤t<d. Residues t<r have m+1 positions and the remaining residues have m, each position carrying measure dt. On odd chains let S contain even positions and B odd positions. A successful distance-d edge from S must enter B, so for any coupling the success mass is at most 1−λ(S)+λ(B). The difference λ(S)−λ(B) is the residue measure of odd chains, r for even m and d−r for odd m. This uses no disintegration or graph assumption about a competing copula. The adjacent-pair swap is a measurable, measure-preserving involution (piecewise translations, with odd tails fixed), inducing an exchangeable coupling with exactly this failure mass. Positive distances have perfect success only at even reciprocals; at an odd reciprocal 1/k with k≥3 the one-sided slopes −(k+1) and k−1 give a strict local minimum with mass 1−1/k. The boundary cases follow from identical variables at d=0 and zero endpoint mass at d=1. Separate finite assignment reproduction checked all 28 grid size/step cases through size 8 by exhaustive permutations and verified the formula and construction for 8,128 cases through size 128, with exact reciprocal checks. This is not the proof for all real d. The uploaded checker was read, not executed.

## originality

PASS

The distinct supported claim is the evaluated all-distance envelope and an exchangeable deterministic involution that attains it, with the parity classification. General capacity duality covers the variational problem, not an evaluated envelope. The closest indexed two-distance result raises substantial partial-overlap risk, but its available statement under restricted support does not establish the optimum over all couplings. Priority is provisional at the access limits stated below.

## value

PASS

The maximized atom is a natural sharp dependence bound for two fixed marginals even though every independent continuous coupling has zero mass there. The result supplies an exact capacity, a coupling that attains it for every real d, and a complete account of perfect feasibility and alternating cusps. This is an explicit geometric evaluation, not just an invocation of capacity duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
