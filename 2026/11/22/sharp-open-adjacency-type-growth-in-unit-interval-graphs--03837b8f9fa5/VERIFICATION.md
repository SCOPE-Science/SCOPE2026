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

In a unit representation the full pattern at x contains exactly the marked coordinates within distance one. Count the 2m entries/exits individually, entries before exits at a simultaneous event. Every actual closed-window pattern is visited, and both end states of the walk are empty, giving at most 2m patterns even with repeated coordinates. An unmarked open trace is a full pattern, and each mark adds at most its own diagonal-deleted pattern; together with the Boolean ceiling this proves the open bound. Spacing marks by 3/4 gives 2m distinct full patterns: all events differ, the windows have connected union, and the nonempty index blocks cannot repeat because their boundaries sweep monotonically. The marks form an induced path. Interior marks yield distinct noncontiguous pairs; endpoint marks yield singleton traces on interior indices, unavailable from full patterns because the query windows of the two neighbors cover that index's window. Thus for m≥4 all m deleted patterns are new, and the m marks plus 2m probes all have distinct open traces. At m=3 the endpoint traces coincide, so the six full and two extra traces shatter all three marks; at m=1,2 the full patterns exhaust the subsets; at m=0 a nonempty host has one trace. This also proves the two distinct VC dimension thresholds and both linear densities. One trace per vertex gives the claimed minimum order where asserted.

## originality

PASS

The supported distinct claim is the simultaneous sharp open-versus-closed comparison for unit/proper hosts, in particular the open formula and its minimum witnesses. The 2m closed bound is elementary from the standard representation; it serves as the comparison, not a separate priority claim. Both distinct general interval Resultary results were checked on their actual statements; they neither give the unit formula nor realize their full query witnesses with unit-length probes in general. No equivalent unit-host theorem was demonstrated by the bounded primary checks.

## value

PASS

The exact unit-host maximum reveals a sharp fifty-percent increase in the eventual number of patterns when self-adjacency is omitted, and a shift of one in VC dimension without a density change. The diagonal deletion mechanism and hosts meeting the one-trace-per-vertex lower bound explain when that increase is fully realizable. This is a natural comparison, not just a restatement of linear growth or the usual closed sweep bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
