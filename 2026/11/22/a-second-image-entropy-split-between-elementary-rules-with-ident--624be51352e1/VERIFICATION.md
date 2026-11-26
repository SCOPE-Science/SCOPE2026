---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Use the bit convention indexed by 4a+2b+c. An n-letter path in the labeled radius-t de Bruijn graph corresponds to an input block of length n+2t, and any such block extends to the full bilateral shift. The subset DFA counts distinct output words, not paths in the nondeterministic presentation. Closing the one-step product gave 15 reachable pairs with no acceptance mismatch in either direction; equality of languages implies equality of the compact image subshifts. At time two the product reached mismatches at 10111101 (only Rule 22) and 1010111 (only Rule 104). Independently reconstructing the reachable automata gives 360 and 418 states, and SCC sizes 350 plus ten singletons for Rule 22 and one component of 418 for Rule 104. Every state is reachable and accepting, so eA^n1 has exponential rate equal to the largest SCC spectral radius; singleton SCCs here have radius at most one. Both strict integer inequalities at each of the 768 vector coordinates in spectral_witnesses.json were checked against the reconstructed components. The resulting intervals (1.86746,1.86748) and (1.83426,1.83428) are disjoint. Direct finite-block enumeration checked the full first-loss sets as well as length-11 counts 1788 and 1770, and truth-table complementation gives Rules 151 and 233. Replay: the frozen verify.py and spectral_witnesses.json are in the same package directory. The script was inspected, not executed; the separate computation built the automata from length-3 and length-5 truth tables, explored the synchronized products, used Kosaraju SCCs, and read the bundled vectors only as data. The infinite conclusions use the finite automata and Perron argument, not extrapolation from word counts through length 11.

## originality

PASS

One-step equality, the per-rule loss timings, the selected words as individual first-to-second losses, and the Rule 22 entropy are all covered or implied by identified prior/companion results. The claim worth evaluating is the cross-rule separation, principally the strict upper bound for Rule 104 below the known Rule 22 value, with explicit two-sided cross witnesses. That comparison was not found or implied by the inspected sources. The separate Rule 22 calculation supplies the identical rational band and should be explicitly cited alongside the prior art in the finding, not merely acknowledged in its supporting review. It is not part of the claimed novelty. This assessment does not resolve historical priority of all finite-time graph calculations.

## value

PASS

The rules are a naturally singled-out class with an identical first-image language, not an arbitrary pair selected for a small numerical inequality. The certified second-step order shows that even within this class an earlier obstruction can coexist with strictly greater asymptotic spatial block growth. The extra quantitative bound and opposing cross-language witnesses make this a useful exact benchmark for finite-time image invariants, independent of the already known horizons and Rule 22 rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
