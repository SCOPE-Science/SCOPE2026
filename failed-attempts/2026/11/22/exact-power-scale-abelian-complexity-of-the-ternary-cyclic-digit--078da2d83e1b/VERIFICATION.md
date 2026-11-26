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

The fixed point contains all letters, and each aa and a(a+1) occurs inside an image while (a+1)a occurs across the images of aa, so all nine block pairs occur. Splitting a length-3Q window into boundary pieces of combined length Q and two full Q blocks gives the upper bound H_{k+1}≤H_k+2 max W_k. For the lower bound take a maximizing letter c at scale k and an extremizing factor in one of the two pairs (c−1,c),(c,c+1). In the expanded pair U_k(c−1)^2 U_k(c)^3 U_k(c+1), either old suffix/prefix window can be extended by inserting two full c blocks. The inequality W_{k+1}(c)≥W_{k+1}(c+1) allows the new maximizing letter to be c−1 or c, so the adjacent-pair invariant continues; k=0 begins with a single letter. Applying the recurrence to the zero weight and its negative, and using one-step changes of at most one in a binary window count, yields the increment 2g_k. The centered letter-count vectors obey v̄_{k+2}=−3R²v̄_k, so g_{k+2}=3g_k, g_0=1, g_1=2. Telescoping gives the formula including k=0; the substitution also directly gives the base-three digit recursion. Independent bounded enumeration with `independent_check.py` checked all nine pairs at each scale through k=8 and 189 weighted recurrence instances. This corroborates the proof but does not address lengths outside exact powers or regularity of the full sequence.

## originality

FAIL

The exact two-repeat closed form was not found verbatim in earlier sources. However, a distinct October 26 record already gives the exact power-scale recurrence and Fourier spread formula for the same cyclic family, using derivations that apply at r=2 without any new case argument. The r≥4 restriction matters to the later irrational-phase and nonregularity results, not to its derivation of those exact formulas. Evaluating those formulas at r=2 and summing a geometric progression leaves no independently established distinct mathematical contribution in the frozen finding.

## value

FAIL

The object and power-length question are natural, and the closed form is correct. But in this case the full novelty asserted beyond the earlier extremal and spectral derivations amounts to evaluating them at r=2 (a phase of π/6) and summing the resulting two-step geometric progression. This is a convenient specialization, not a newly needed structural or extremal result independent of that proof. The finding contains no separate arbitrary-length classification or full regularity result that might survive as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
