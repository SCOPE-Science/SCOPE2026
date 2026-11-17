---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For every unit x the constraint <x,y>=q gives exact support q|<Tx,x>|+sqrt(1-q²)sqrt(||Tx||²-|<Tx,x>|²). Compact K tends to zero on geometric weakly null tails, yielding w_q(S+K)≥1, with w_q≤||T||. If ||T||>1 choose a finite-support v with ||Tv||>1, mix it with a far geometric tail at fixed small mass δ, and continuously vary its ratio r from 0 to R<1 until |<Tx,x>|=q. Uniform tail compactness suppresses cross terms; the mixed ||Tx||² tends to δ||Tv||²+(1-δ)>1. The support formula gives w_q>1. At q=1, the exact telescoping quadratic form isolates the 2×2 boundary matrix positive semidefinite iff t≤sqrt(2); geometric tail witnesses strictness when t>sqrt(2). These arguments cover every compact K without assuming weighted shift structure.

## originality

PASS

Prior one-edge Hilbert numerical-radius threshold sqrt(2) was explicitly published and is not original; its endpoint claim is covered. Earlier general scaled-q dilation abstracts and periodic weighted shift q-radius descriptions do not establish the universal unscaled criterion in read material. The most on-point 2007/2008 specialist full texts were inaccessible, so originality is best-of-knowledge, not absolute priority; the entire all-compact criterion survives within current checked evidence.

## value

PASS

The difference between a general compact perturbation’s operator norm and its constrained q-numerical radii is a natural operator-theoretic detection question. The strict interior-versus-endpoint dichotomy is a motivated stability/rigidity theorem with genuinely infinite quantification, not a finite numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
