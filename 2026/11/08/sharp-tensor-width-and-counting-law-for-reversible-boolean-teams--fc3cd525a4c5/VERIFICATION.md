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

PASS: any two distinct assignments in a team satisfying all dep(p_i,p_j) differ in every coordinate, hence are complementary. Each lax cover piece is contained in an antipodal pair, yielding width = occupied pair classes. Independent four choices per pair give (1+(2u+u²)z)^{2^{d-1}}. Coordinate fibers have <=1 point per class and at least half total team; equality ratio 2 iff one vertex per occupied class and every coordinate balanced. d2 any two noncomplementary classes share a coordinate; four even parity points witness d>=3, with no smaller balanced class-free nonempty team. Proof for every d>=2 not extrapolated from the d2,d3 finite checker.

## originality

PASS

PASS best-of-knowledge: known Boolean team syntax and lax tensor semantics do not by themselves supply a stated minimal piece count, full size-width generating polynomial, or exact sharp coordinate-fiber ratio transition d=2 vs d>=3. The complete Barbero et al paper treats labelled proof systems and terminating proof search, not this quantitative fixed-formula family; scanned theorem/formula text has no antipodal or tensor-width theorem.

## value

PASS

PASS: reversible dependence is a natural logical constraint; exact minimum tensor-piece count and its joint size distribution quantify model decomposability rather than repackage a single satisfiability check. The d2-to-d3 equality threshold is a sharp structural boundary across all Boolean dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
