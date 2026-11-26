---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The displayed mathematical identities hold. The first two letters and the lag-two XOR derivative reconstruct the word; duplicating at site j inserts two zeros at derivative gap j. Two insertions give the same output precisely within the same zero run, for 1+wt(derivative) distinct outputs. Weighting the transitions of states 00,01,10 by u for a lag-two mismatch gives the three-state transfer matrix and the stated rational function. The initial polynomials give degrees 0,1,2 and top counts 3,2,1. In the recurrence the leading term comes only from u² A_{n-3} for n=0,1 mod 3 and also from A_{n-1} for n=2 mod 3, giving the stated extrema and counts, including n=2. A zero mismatch count gives exactly the three admissible two-periodic words. At u=1 the series counts Fibonacci words; differentiation gives the displayed derivative series. The prose 'summed descendant count' should read 'summed descendant count minus one per source': A'_n(1)=sum_w(B(w)-1). For the literal total add (3+2t)/(1-t-t²) to the displayed series. The frozen script was inspected, not executed; the all-length conclusion follows from the identities, not from finite checks.

## originality

FAIL

The full constrained degree spectrum is mathematically equivalent to the one in a distinct indexed two-burst-deletion record. This is stronger than proximity of topics or equality on a table: the deletion and duplication degrees are equal for every input by the same lag-two statistic, and exact-one duplication's degree formula was already known. Both records have the same displayed date; the evidence does not establish which was written or published first. Failure is for equivalent indexed coverage and no distinct surviving degree result, not a finding about historical priority or the equality of the output sets.

## value

FAIL

A sharp all-length forward-degree distribution for a natural constrained language would be useful if independently unknown. Here the equal pointwise deletion and duplication degrees transport the entire result from an indexed theorem, and the known sphere identity already supplies the channel-specific degree step. There is no new result about output sets, correction, or some other invariant that survives this equivalence. Correcting the first-moment wording would not change that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
