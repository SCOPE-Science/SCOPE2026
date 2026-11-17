---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The first-fit algorithm is unambiguous for each of the n! equally likely labelled orders. Fresh independent enumeration of all 720 orders on P6 and the explicitly defined degree-three T6 produces exact X histograms P6 {5:350,6:370}, T6 {4:30,5:330,6:360}, hence 397/72 and 131/24 and strict 1/18 reversal. For n<=5, the Prufer bijection gives exactly n^(n-2) labelled trees (1,1,3,16,125 for n=1..5), and full orders for each yield exact minima equal to paths, including n4=15/4 and n5=14/3. This is exhaustive finite enumeration of precisely the stated finite-size minimum-order claim, not finite data extrapolated into a purported theorem for larger n. Two supplied algorithms (permutation and multiplicity-preserving state DP) were inspected and agree.

## originality

PASS

The primary source Krivelevich–Mészáros–Michaeli–Shikhelman proves path minimality for the first GREEDY independent-set class but explicitly asks in Section 9 whether the first TWO classes together are minimized by the path. It does not contain this six-vertex counterexample or the exact minimum-order certificate. Other greedy-colouring source concerns connected arrival orders and different extrema. Resultary alternatives for one-class or tree shift notions do not imply the two-class reversal.

## value

PASS

This is a smallest-order exact counterexample to a specific published extension question in random greedy coloring. The endpoint n=6 and gap 1/18 are not arbitrarily sliced statistics; the exhaustive Prufer certificate gives a meaningful finite boundary, and the counterexample changes the correct mathematical expectation of path extremality. A finite witness can carry standalone scientific value without an infinite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
