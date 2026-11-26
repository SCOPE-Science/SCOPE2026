---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Any nonempty antipalindromic subsequence has opposite end bits and equal-length complementary mirror runs. A cut of the circle has at most five runs, so the subsequence has two or four. In the two-run case both colors cannot use both of their source runs: those four source runs alternate in circular order. Thus one color contributes at most one run, and all four candidate capacities are achieved by choosing a boundary cut and skipping the intervening unwanted run. A four-run subsequence uses all four source runs: omission leaves at most two circular color transitions. With all four used, the circular runs of the subsequence correspond one-to-one to the original ones; a split source run cannot contribute at both linear ends, since those ends are opposite. The two possible adjacent pairings give the two terms of Q. In the balanced case the exact half-length is max(s/2+U,s-U+V), where U and V are respectively the larger and smaller absolute deviations of a and b from s/2. Averaging gives 3s/4+V/2, and integrality gives the ceiling. In the stated construction s=4m+r, U=m+r/2 and V is 0 or 1/2, so both terms are at most 3m+r and the first equals it. The s=2,3 cases attain s. For 4 dividing s, equality forces V=0 and U=s/4, giving exactly the stated cyclic run profiles.

## originality

FAIL

A distinct indexed Resultary record gives the same six-term exact formula for arbitrary positive four-run lengths, the same rounded balanced minimum, and the same equality profiles. Splitting its maximum into four two-run terms and two four-run terms recovers the frozen P and Q verbatim up to order. No distinct mathematical remainder was identified. This is confirmed catalog coverage, not a finding of chronological priority: the matching path is dated later than the assigned path, and derivation or publication priority is unresolved. Earlier primary literature also explicitly gives the divisible-by-four upper-bound example, as the frozen record acknowledges.

## value

PASS

As mathematics the complete four-run invariant is useful: it resolves the first nontrivial fixed-run case of the separated matching problem exactly, including the finite rounding and classification of divisible-by-four extremizers. This assessment is of the result's mathematical utility, not a claim that duplicating it adds a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
