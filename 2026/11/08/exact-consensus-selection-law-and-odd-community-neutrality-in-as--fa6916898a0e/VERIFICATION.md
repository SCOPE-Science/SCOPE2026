---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

With ties retaining the present bit, each actual strict-majority flip reduces the bichromatic-edge count, so no nontrivial recurrence. Fixed states are unanimous colors or (only for both even parts) jointly tied counts; a one-part tie is broken deterministically by the other part's strict majority. For opposite initial strict majorities, exactly a initial one-vertices on the first shore and c=n-b initial zero-vertices on second shore are eligible; their first individual update times form a uniformly ordered permutation. First shore loses strict positive majority after r=a-floor(m/2) flips, second gains positive majority after s=ceil(n/2)-b flips. The second shore reaching s first corresponds to a winning prefix with j<r first-shore flips and yields the displayed finite sum of falling factorial weights. Exact color-complement handles reverse orientation. Order statistics show odd-odd polarization symmetry and even-sided tie advantages; fixed-n limit follows from binomial tails. Independently solved rational Markov count-state equations for 729 initial macrostate cases for m,n<=6; tests include even-even ties. Finite checks do not prove all m,n.

## originality

PASS

PASS but heavily qualified: odd-odd complete initial-profile hypergeometric kernel is already published by the 2 November Resultary theorem and is NOT independently new; all-size polarized two-opposing-unanimous-camp parity and rate-race results are also published by a separate 8 November Resultary theorem and are NOT independently new. The surviving full statement includes arbitrary mixed initial profiles when one or both part sizes are even, the exact all-parity kernel and complete nonconsensual doubly-tied fixed-state classification. These are a natural extension of the race to genuinely new cases not covered verbatim by those earlier scoped results, although the mathematical derivation is close and a broader unindexed theorem remains plausible.

## value

PASS

The full all-initial-configuration exact fixation kernel for arbitrary community parities, including a nonconsensus trap classification, is a coherent natural completion of previously odd-only and fully polarized partial results. Useful to predict strict-majority fixation in arbitrary bipartite communities without assuming odd degree; value is restricted to that completion, not the already known fairness or polarized result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
