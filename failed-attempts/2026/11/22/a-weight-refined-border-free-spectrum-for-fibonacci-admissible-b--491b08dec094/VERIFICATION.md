---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The shortest border is itself unbordered. If its length exceeded half the word length, two shifts by the corresponding period would give a shorter positive border; thus the two copies can be separated by a legal middle. For distinct endpoints exactly one of the two junctions forces a zero on a nonempty middle, giving M=1+zT=1/(1-z-tz²), and the empty middle is legal. For a singleton border 0 there is no extra constraint; for 1 the middle is nonempty with both ends 0 (the one-letter middle 0 serves both ends). These cases give (1) and induction gives uniqueness. The scalar recurrence, convolution and limit then follow by coefficient extraction and Binet. In the convolution the conjugate-root error summed with u_k≤phi^{k+1} is O(phi^{-n/2}), as is the omitted tail. Recomputing gives a K=10 lower bound about 0.13695 and the displayed density to double precision; the analytic enclosure in (4) controls further digits. Replay via RESULT.md (5)–(6) and the tail estimate; both checkers and VERIFICATION.md were inspected, not executed. The claim is about linear no-11 words and contiguous borders only.

## originality

FAIL

Verified distinct same-date catalogue coverage, not an inference about chronological priority: the golden-mean periodic-cylinder record proves that full period n is precisely this unbordered event, gives the exact oriented scalar recurrence and the same positive density, and strengthens the convergence error to a signed parity expansion. Its proof gives the same exact sandwich decomposition of the oriented word sets, not merely scalar counts. Marking a 1 by t in that decomposition gives the whole proposed bivariate equation directly, as detailed below. The bivariate formula was not printed in the inspected companion passage, but is a mechanical consequence of its stronger word-level decomposition and the elementary regular-language weight series. The frozen claim thus does not establish a distinct result against this matching coverage.

## value

FAIL

The inventory is a natural useful quantity in isolation, but its scalar law and positive density are already available with a sharper asymptotic, and the proposed weight refinement is direct marking of an already explicit word-level decomposition. The frozen result does not supply a further nonmechanical invariant, weighted asymptotic, or independently motivated cutoff. Finite checks and the elementary tail enclosure do not remedy that gap. No surviving independently valuable claim was found that could be repaired merely by narrowing the scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
