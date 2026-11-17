---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Beta(1,1) posterior threshold is u-v>=0, so a run ends at a first passage to -1. Catalan ballot counting gives f_p(z). Renewal equations G_A=s_a+f_a G_B and G_B=s_b+f_b G_A give the defective PGFs and exact majority-lock region. At a=1/2, expansion f(z)=1-sqrt(2(1-z))+O(1-z) and monotone Tauberian transfer yield the t^-1/2 tail constants and infinite mean. Independently checked algebraic win formula and exact (7/10,9/10)->3/5 witness; source checker inspected, but no infinite-time numerical certification is claimed.

## originality

PASS

Primary OA Meylahn–Searle paper specifies the same baseline reset-on-switch dynamics and Beta posterior, but inspected sections do not give the complete two-choice renewal solution, suboptimal-lock majority region, or critical tail constants. Earlier single-run quitting is a strict ingredient, not the alternating two-opinion stopping law.

## value

PASS

Sharp phase boundary, paradoxical more-likely fixation of an inferior option, and almost-sure-but-infinite-mean stabilization precisely characterize an explicitly motivated Bayesian opinion mechanism, beyond a generic gambler-ruin identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
