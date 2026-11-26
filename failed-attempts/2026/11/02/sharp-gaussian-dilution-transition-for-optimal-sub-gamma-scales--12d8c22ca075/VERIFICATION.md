---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For positive jump weight the MGF boundary forces c≥β. With x=βt and K(t)=Vt²F(x)/2, rearrangement gives c/β≥(1−1/F(x))/x; when x≥β/c this constraint is automatic. Coefficients of Hα are at most one for α≤1, so c=β is feasible, including α=1 and w=1. For α>1 the reciprocal of F at x=1−δ is o(δ) for fixed positive w, forcing c>β. At fixed α>1, writing ε=(2w/[α²(α+1)])^(1/(α−1)) and δ=εu yields the uniform compact limit u−u^α/α for the scaled excess above one. Away from x=1 the objective is O(w) uniformly, since (Hα−1)/x extends to zero. If δ/ε tends to zero the scaled excess cannot be positive in the limit; if δ→0 and δ/ε→∞ then δF(1−δ)≤δ+O(wδ^(1−α))→0 so the objective is below one. Thus all maximizers converge to u=1, giving the stated location and coefficient. For α=2 the objective in δ is w(1+3δ)/(w+2wδ+3(1−w)δ²); differentiation gives the sign of w−(1−w)(6δ+9δ²). The unique interior root moves to δ=1 at w=15/16; at and above that weight the maximum is an endpoint limit, also at w=1. Substitution yields both scale branches. The uploaded checker was inspected, not executed; its recorded finite checks are not the basis of the proof.

## originality

FAIL

A distinct indexed Resultary record with the same mixture and variance-exact objective states the shape-one threshold, the same fixed-shape singular coefficient and maximizer asymptotic, and both exact Erlang-two branches with the same 15/16 transition. Its result is broader for α>1. This is demonstrated mathematical coverage, not a claim of historical priority or attribution.

## value

FAIL

The sharp calibration and nonuniform Gaussian limit are meaningful mathematical facts, but this record contributes no independently useful uncovered invariant or regime beyond the existing stronger Resultary record. The Erlang expansion and optimizer uniqueness are direct consequences of its explicit objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
