---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For odd n>=3 with fair independent letters (rotation plus defect 0->1) and specified initial pair {1,(n+1)/2}, the exact unordered-pair Markov-chain first-step equations produce E T=(n-1)(2n^2-n-1)/2 and Var T=n(n-1)(4n^4-8n^3+3n^2+7n-14)/6. Submitted second-moment telescoping agrees algebraically with published earlier explicit recurrence. Independent rational inversion of the actual absorbing pair transition matrix confirmed mean/variance (14,142) at n3, (88,5320) at n5, (270,49294) at n7. The bounded-mean Markov tail argument plus uniform fourth moments supplies nonconvergence in probability, not only a nonzero CV. All-n variance is analytical, independent finite checks do not certify it.

## originality

FAIL

DECISIVE SAME CLAIM COVERED. The publicly published 2026-10-25 full mathematical result Exact random-input pair-merging variance in odd Černý automata already establishes, for precisely the same model and initial pair after stated state conjugacy/letter renaming, identical mean, variance and asymptotic CV sqrt(2/3). A second full result published 2026-11-08 repeats the same all-odd-n formula. We read both full RESULT.md proofs, including pair transition graph and explicit telescoping. This is mathematical identity, not merely matching keywords. Submitted additional nonconvergence argument is a routine tail/uniform-integrability consequence here and does not rescue novelty of the claim.

## value

FAIL

The exact fair-input synchronization variance is a meaningful invariant, but it was already completely evaluated before this submission, including the same nonvanishing relative fluctuations. This submission is a recomputation of the known invariant with no distinct motivated unsolved parameter, classification or strong new structural conclusion. Mathematical value as a NEW finding therefore fails even though the formula is correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
