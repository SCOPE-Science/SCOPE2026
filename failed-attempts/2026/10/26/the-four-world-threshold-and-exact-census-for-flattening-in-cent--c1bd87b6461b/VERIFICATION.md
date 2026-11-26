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

For nonempty X=A∩B the inclusion for all C is equivalent, by singleton consequents, to f(f(w,A),X)=f(w,X). Empty antecedents are automatic. Centering handles w in A and X=A, while singletons are forced; through three worlds these exhaust the cases. For n=4 only the outer triple omitting w and its inner pairs matter; choosing the triple winner forces its two pair choices, and the third pair supplies the stated compatibility condition. The indicated failure has left selection 3 and right 2, so C={3} witnesses failure. On the full Boolean algebra a singleton consequent also recovers each selection from the conditional, proving injectivity. Success, centering and consequent monotonicity yield P1–P4 and identity, and the two-valued derived negation yields the stated negation laws. An independent direct-table enumeration (without running the frozen checker) obtained n=1,2,3 valid totals 1,1,8 and n=4 total 331776, valid 138, invalid 331638, orbit sizes [6,12,24,24,24,24,24], and 138 distinct conditionals. Replay: python3 /workspace/branches/a5b6adf2-cc35-4ae2-9fe1-82a1ac21e56b/independent_census.py; output at the same directory's replay_output.txt. The calculation concerns only the stated finite total centered functional class.

## originality

FAIL

The principal threshold and census are explicitly covered by the earlier Tail-coherent rankings record in the identical semantic class. The strong-density-to-P5 translation is exact and already part of the underlying semantics. The independently reproduced orbit sizes refine already enumerated orbits by their cardinalities; they do not rescue novelty of the threshold/census finding.

## value

FAIL

The four-world obstruction and complete first nonautomatic layer would be meaningful if unresolved. Here they repeat an existing structural criterion and exact census, already independently cross-checked in the earlier work. Subtraction and sizing its seven known orbits do not provide a separately motivated mathematical result on this evidence. No substantive surviving claim warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
