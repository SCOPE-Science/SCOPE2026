---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify_broom.py` using Python 3 and the standard library. The checker reconstructs the variance polynomial from the root-leaf and path contributions. For small graphs, it independently enumerates all open/closed edge states with exact rational probabilities; it also verifies the closed-form and moment identities, derivative endpoint identities, correction inequalities, and selected large-parameter sign brackets.

# Analytic versus finite checks

The theorem holds for every integer \(L\ge14\) and \(136\le m\le149\) by the rational bounds and decreasing-correction argument in RESULT.md. The finite examples in the checker do not constitute the infinite proof and do not establish a globally smallest graph. The use of Descartes' rule counts positive roots with multiplicity, so three disjoint sign brackets imply exactly three simple roots, without numerical root solving.

# Scope

All transmission edges are mutually independent. No claim is made about heterogeneous, dependent, or random-duration SIR dynamics; no independent external validation has been completed.
