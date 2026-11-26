---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Write U=2x−1 on Y; the uniform-U dyadic label g has mass 2^(−g−1), and after the right step and B+g doublings the returned coordinate 2^g U is uniform on Y conditional on both labels. Return-time choices of B are fresh. In the iid-environment extension the induced branches can be labeled by g and the full environment word consumed on that excursion. Conditional on each label, the return sends the branch to the product of uniform Y and an independent environment tail. This partition generates, since the coordinate inverse branches contract and the number of environment entries consumed tends to infinity. Hence the induced probability is ergodic and conservative. The return tower projects to the stated measure: for n≥1 a visit to I_n occurs iff B+G≥n, at most once and uniformly within that shell conditional on the labels. Its mass is E[2^(min(n,B)−n)]; n=0 is just the normalized base. Summing first for B=β gives β+2, and Tonelli applies even at infinite mean. Every positive point enters Y in finite forward time, so an absolutely continuous stationary probability has positive base mass, induces an absolutely continuous invariant law for the same exact full-branch return map, and must induce normalized Lebesgue measure. Kac's formula then excludes finite mass at infinite mean, and the return occupation formula determines the probability uniquely at finite mean. For J_0=1 the renewal transform is 1/(1−R(z)); weighting by π(Y)=1/m and centering gives the stated covariance transform. For B=1 its coefficient is (2/9)(−1/2)^n. Null boundaries and the zero atom do not affect these arguments. Independent branch, occupation and renewal calculations support the full claim. The frozen VERIFICATION.md and verification.py report 512 exact-rational finite checks; the script was inspected, not executed, and these diagnostics are not the proof for unbounded laws.

## originality

FAIL

A distinct indexed work states the core exact density, mass and iid return formulas for the identical model and parameter scope, and additionally gives density tomography. The covariance is not stated there, but it follows by the ordinary stationary renewal identity immediately from those exact inputs; the B=1 specialization is a partial fraction of the same identity. This is a finding of demonstrable current coverage and mechanical implication, not attribution of historical priority to the later-catalogued record or a claim that Inoue–Toyokawa gave the exact formulas.

## value

FAIL

An exact regenerative description of this model is useful and much stronger than shell orders. But the exact core is already available in the compared index, and the sole unstated observable result uses the ordinary renewal transform with no model-specific work beyond that core; its alternating example is a single substitution. There is no independently useful new exact invariant left to accept from this frozen finding on the audited evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
