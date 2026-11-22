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

# Verification

The RESULT proof is analytic: transform each nightly visit into an orbital-phase arc, unwrap the full span (strictly shorter than a phase period), characterize the at-least-\(r\) coverage by intersections of consecutive blocks, and optimize the two piecewise-linear expressions divided by \(1\pm\delta\). All inequalities and strictness follow from \(N\ge2r\), \(r\ge2\) and \(0<w<1/(2N)\). No numerical experiment is used to prove the universal statements.

Reproduce exact-rational diagnostics with `python3 check.py`. The program independently partitions orbital phase circles into cells using arcs modulo \(P\), counts covered cells, and compares against the claimed expression. It passed 29,988 Fraction-based assertions in the reviewed execution, including boundary values, varying window counts, both sides of the daily alias and grid optimality comparisons. These are finite checks and do not certify unexamined parameter ranges. Model limitations and literature-comparison residual risks are disclosed in RESULT.md and REVIEW.md.
