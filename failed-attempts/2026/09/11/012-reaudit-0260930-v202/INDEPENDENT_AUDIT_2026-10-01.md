---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"failed"}
---

# Independent mathematical audit

## Final claim

For Z_694: Br(Z_694)=Br_1(Z_694); all six Bright pair-ratios have squarefree part -119; the tangent-section rulings at [1:1:1:1] are defined only over Q(sqrt(-119)); and the stated bounded point/line and 3-adic checks hold.

## Correctness — PASS

The central Brauer-group implication is valid: for the normalized coefficients, exact fourth-power-class arithmetic gives {2,3,5} disjoint from H_D, and the cited diagonal-quartic theorem then yields Br(Z)=Br_1(Z). Independent rational recomputation also gives squarefree part -119 for all six pair-ratios and tangent discriminant -1904=-16*119. The boxed point/line statement is only the stated finite search, not a global absence theorem.

Checked sources: artifacts/hd_check.py (blob 0f7deef2f59f21a77f71749435344c513477218d); artifacts/fibration_attempt.py (blob 0f02eba3b58201fc987e3831dfc94dc7b1db50d4); artifacts/qline_search12.py (blob 8e97d614c23893b59edf28d9f9feb6a6cf00899d); Ieronymou-Skorobogatov-Zarhin, arXiv:0912.2865, Corollary 3.3

Residual risks: The finite box search does not rule out rational points or lines outside the box.; The 3-adic logged family was not needed for the headline conclusion.

## Originality — FAIL

The headline transcendental-free statement is a direct special case of a published criterion once the elementary H_D membership calculation is made. The -119 tangent/ruling calculation is an elementary instance computation and does not rescue the central claim from coverage.

### Equivalent formulations

The package uses exactly this criterion with a1=7/2, a2=4, a3=-17/2. Evidence: Corollary 3.3 defines H_D from -1,4,a1,a2,a3 and states that disjointness from {2,3,5} implies Br(D)=Br_1(D).

### Broader coverage

A general theorem dominates the instance-level Brauer-group assertion. Evidence: The cited theorem applies to the whole diagonal-quartic class, not merely this named surface.

### Exact database or table

Exact-tabulation novelty cannot overcome direct theorem implication. Evidence: No separate table was needed because theorem-level coverage is decisive.

### Claim versus prior implication

The prior result logically implies the headline claim after a short arithmetic check. Evidence: The package proves precisely the hypothesis of the published corollary.

### Source inspections

- **On the Brauer group of diagonal quartic surfaces** — https://arxiv.org/abs/0912.2865. Trigger: Same diagonal-quartic object class and the exact H_D criterion cited by the package. Material read: Statement of Corollary 3.3 and surrounding definitions/proof context. Method: Primary full-text inspection. Assessment: COVERING. Evidence: Corollary 3.3 states that if {2,3,5} is disjoint from H_D then the full Brauer group equals its algebraic part.

Checked sources: https://arxiv.org/abs/0912.2865

Residual risks: No priority claim is made for the auxiliary -119 arithmetic observation by itself.

## Scientific value — FAIL

For this particular coefficient tuple, the headline is obtained by plugging elementary fourth-power-class arithmetic into an existing general criterion. The remaining boxed search and tangent discriminant are bounded/routine instance checks without an independently motivated new structural consequence.

Checked sources: Ieronymou-Skorobogatov-Zarhin general criterion; package instance calculations

Residual risks: A broader arithmetic application using this surface could be valuable, but such an application is not part of the audited final claim.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and scientific value.
