---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The word ba^hba^j attains each four-case bound. The function F on full, one-hole and two-hole images increases by at most one per letter; rank monotonicity rules out returning from three holes. Checked every assigned pair by independently coded BFS on subsets for n=4..10 (161 total pairs), not just its checker. Thus exact distances and the histogram follow for every n>=4.

## originality

FAIL

FAIL: published separate Resultary 2026-11-08 codimension-two spectrum theorem already proves the identical four-case function for every n>=3 and exactly the same histogram. Interchanging names of cycle/merge letters does not change the automaton or the answer.

## value

FAIL

The exact pairwise spectrum is a natural mathematical invariant, but this submission supplies no new invariant or implication beyond a full previously published theorem. Recomputing the same table under a second proof is not a new valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
