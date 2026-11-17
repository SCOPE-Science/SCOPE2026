---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The displayed overlap exclusion test checks precisely all newly appended suffix periods p with length 2p+1, and square-suffix detection computes each curling symbol exactly because overlap-free sources are cubefree. Prefix-hereditary DFS with restricted-growth alphabet labels exhausts all source orbits. A separately written independent C++ enumeration of every restricted-growth prefix through length 85 produced 1008 canonical length-84 words, exactly two terminal image strings P1/P2 with multiplicities 672/336, no length-85 words; all length-84 sources have three letters, hence 6048 labeled source words and fiber sizes 4032/2016. The independent source code and run output are attached. This finite exhaustive proof makes no infinite assertion.

## originality

FAIL

FAIL: the already-published October 26 full RESULT proves verbatim the two transform images, their common 83-symbol prefix P, the exact labeled 4032/2016 and canonical 672/336 multiplicities, and the 1008 classes, plus a stronger all-three-or-none extension theorem at length 83. Its definitions use identical direct-prefix curling transform and ternary simultaneous overlap-freeness. Both conclusions and even the literal 83 digits match. The current final claim has no new asserted mathematical remainder beyond that earlier theorem.

## value

FAIL

FAIL: a repeat of the entire already published terminal fiber classification is not an additional unknown invariant or worthwhile distinct boundary. Re-enumerating the same terminal words, even with an alternate program, reproduces an existing table; the stronger earlier complete result subsumes the submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
