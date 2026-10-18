---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

FAIL

The rank-one counterexample is correct: atoms f_i=sqrt(3)2^(-i)e1 form a Parseval K-frame for K=P_e1, U=[[1,1],[1,1]]≥0, S e1=(2,1), and x=(1,−2) annihilates all transformed atoms while ||K*x||²=1. For K≠0 the universal synthesis-range equivalence follows from testing Parseval (Ke_i) and applying Douglas; η is the largest domination factor. However the printed theorem quantifies over all bounded K and does not exclude K=0. For K=0, η=+∞ (the supremum of all nonnegative η for 0≤0), so the stated transformed lower frame bound Aη is not a finite valid frame bound as conventionally defined. A separate K=0 convention or restriction is necessary for the quantitative claim; the main range/counterexample statements do not have this flaw.

## originality

FAIL

A distinct published mathematically broader K-g-fusion-frame theorem derives EXACT R(K)⊂R(AK) for every invertible transport A and supplies the same 2×2 rank-one-failure mechanism; setting W_i=H and Λ_i(x)=⟨x,f_i⟩ reduces that theorem to all ordinary K-frame atomwise transports S=I+U. Classical Douglas supplies the operator domination and sharp η trivially, so this claim is covered at the implication level even without matching the target theorem number.

## value

FAIL

Correctness of a counterexample is meaningful but the exact frame-transformation obstruction is already explicitly established for the broader K-g-fusion-frame class in a published record; the candidate’s extra quantitative η is routine Douglas inequality optimization. No mathematically unaddressed source-specific structural consequence remains beyond identifying another theorem with the same generic defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
