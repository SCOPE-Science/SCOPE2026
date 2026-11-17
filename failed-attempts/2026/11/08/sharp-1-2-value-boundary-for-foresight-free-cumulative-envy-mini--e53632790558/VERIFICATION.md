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

The Bellman parity-step induction for integer imbalance z is valid: the next imbalance choices differ by an even number, parity monotonicity is preserved, and 0<=F_W(2)-F_W(0)<=2. The four-good (1,1,3,1) and (1,1,2,0) witnesses attain greedy/optimum totals 6/4 and 5/3 respectively, and the reverse-triangle bound rules out three-good failure. Independently checked all 1022 {1,2} words of lengths 1..9 with exact dynamic programming and both counterexamples.

## originality

FAIL

The complete October 25 published theorem proves the same arbitrary-horizon, arbitrary-fixed-order optimality for two agents and {a,2a}, exactly the same positive-integer alphabet barrier, and four-good shortest counterexample. The November 2 published theorem also covers the zero-valued boundary and the three-good nonnegative minimality. Thus the entire submitted claim follows from earlier results, not merely a similarly named paper.

## value

FAIL

Exactness would be a worthwhile optimization boundary if new, but both sharp cutoff and short failure witnesses have already been established in published complete proofs. Reproduction and an alternate Bellman invariant do not provide a separately motivated unknown invariant or mathematical advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
