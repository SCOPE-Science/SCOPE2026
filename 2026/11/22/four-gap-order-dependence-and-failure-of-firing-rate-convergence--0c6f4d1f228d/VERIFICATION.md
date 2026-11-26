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

Both aligned length-14 cells contribute four opportunities and one outgoing gap of each length 2, 3, 4, and 5. At an arbitrary cutoff an incomplete cell adds only a bounded discrepancy. Starting from the cell origin, the offsets selected before the next origin in the four successive threshold bands are (0,2,5,9)/(0,2,6,9), (0,5,9)/(0,6,9), (0,5,9)/(0,6), and (0,5)/(0,6). In each case the next eligible offset after those is 14, and the right endpoint is included in each band because eligibility is weak. Thus the exact count follows by induction across arbitrary cell words. When c is in (3,4], the ratio differs from (3-N_B(m)/m)/14 by o(1); alternating doubly exponential runs have negligible total past length relative to each final run, so the averages approach zero and one along the two types of endpoints. Their vanishing one-step jumps ensure every intermediate value is a limit point. Outside the band and within (0,5] the cell counts are independent of the letters. For periodic clocks the projected map on phases is a finite deterministic map with fixed elapsed time on each phase transition, giving a limiting density. Greedy earliest selection in each finite window is maximum-cardinality by replacing any competitor's first event by the first available event and inducting. Translation changes the finite-window maximum by bounded endpoint errors, and reflection of a whole-period window exactly preserves separated subsets. Every permutation of at most three gaps is dihedral, and the four-gap witness is strict. The expression 'each block of four' is read in its construction/proof sense of aligned cells, not arbitrary sliding windows (which can straddle a switch). No claim is proved for c>5 on this nonperiodic family.

## originality

PASS

Pass for the four-gap order obstruction and its exact fixed-marginal nonconvergence construction. The projection law, greedy cardinality argument, and the order-invariance lower bound for three periodic gaps do not independently clear prior-coverage checks. The three-phase catalogue theorem already gives that invariance for thresholds below one period, and the other thresholds add only a trivial case. This does not cover the exhibited four-gap order dependence or the sharp nonconvergence band and full interval of limit points.

## value

PASS

Exact agreement of the entire one-gap empirical distribution, not just average clock speed, is a natural regularity hypothesis for a deterministic firing limit. This counterexample sharply disproves it while giving bounded discrepancy, minimal periodic motif length, exact threshold endpoints, and the entire interval of output limit points. The result explains why order information is necessary; it does not claim such failure is generic or model an empirical population.

The dated certificate retains the supplied scientific assessment, sources and limitations.
