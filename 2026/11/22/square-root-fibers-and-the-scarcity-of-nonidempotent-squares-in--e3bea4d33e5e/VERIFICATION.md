---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Direct partial composition forces domain A∩(A−k) and displacement 2k. Nonempty targets split over the solutions of 2k=j and over their +k cycles; for the empty target the empty input is counted only once. A positive output edge forces both input endpoints to one, so a single zero between positive edges is impossible. For a zero run r=2 there is one forced interior zero; for r≥3 the two end-adjacent input vertices are forced zero and the r−3 free vertices form an independent-set path, giving F_(r−1). The all-one and independent-set-cycle all-zero branches include periods 1 and 2. The trace of the displayed two-bit transition matrix enumerates indexed (not rotation-quotiented) periodic words; its nonzero characteristic factor yields the recurrence. Odd n gives unique root displacement and φ(d) shifts of order d, hence the stated divisor sum with a single empty output. The disjoint-triple bound uses floor(d/3)/d≥1/5 for d≥3 and bounds the entire nonidentity displacement contribution exponentially relative to the monoid. The initial displayed counts also follow from the recurrence. A fresh direct tuple-composition enumeration checked all target fibers for n=1–8 and all local fibers through length 12; the direct image at n=9 was 1702. Direct images at n=1–9 were 2, 4, 16, 25, 96, 136, 428, 597, 1702. Replay the bounded check by enumerating tuples with defined entries x+k modulo n and undefined entries elsewhere, composing each distinct tuple with itself, and tallying outputs including the single empty tuple; enumerate binary words independently for the local check. The frozen checker was inspected, not run.

## originality

PASS

The supported distinct contribution is the individual square-map census, including even periods and empty target, and the exact odd-degree image and scarcity within this specific inverse monoid. The cyclic AND reduction and avoidance counts are not claimed as novel on their own. No inspected comparison covers this assembled claim, with the stated limits on source access.

## value

PASS

Squaring is a natural invariant of the cyclic inverse monoid. The result distinguishes root feasibility, exact multiplicity and image density, including the partial-identity mechanism responsible for the 1/n density. The explicit orbit formula avoids brute-force composition and shows scarcity of the genuinely nonidempotent image; this is more than recalculating the word sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
