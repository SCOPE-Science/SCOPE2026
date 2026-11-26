---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An exponential first-event race selects vertex i proportionally to its rate; removing its closed neighborhood leaves independent fresh clocks on the remaining graph by memorylessness. On a path the residual splits into two alternating subpaths; summing the two sides by reflection gives the displayed E, A, B equations. A separate graph-mask race over truncated exact fractions reproduced all three path expansions at k=4,5,6,7 and the particular A_3 and B_3 truncations for C10. After clearing the linear denominators, the candidate residual for each coefficient is quadratic or less for k≥5: short indices contribute constants and the remainder consists of sums of affine terms. At k=5,6,7 only confirmed lower indices occur, so the three zeros certify the residual identically; induction then covers all k≥4. For a cycle the remaining 2m−3 vertices form the path with both endpoint rates equal to that of the first accepted vertex. The separate mask calculation gives cycle coefficients through degree three of (2,0,0,0), (3,−3/2,15/4,−63/8), (4,−2,10/3,−49/18), and (5,−5/2,25/6,−595/144) for C4 through C10. C4 is exactly 2 since any maximal independent set there has size 2. The rational finite recurrences are regular at epsilon=0 and justify the fixed-m remainder, not a size-uniform one.

## originality

PASS

Pass is for the exact finite-cycle stabilization cutoff and the short-cycle exceptions, not for discovery of the stabilized coefficient as an infinite-chain coefficient. The strongest indexed law, for alternating-rate dimers, is in fact equivalent to the infinite-line monomer model via the line graph. Its explicit jammed coverage implies the matching third-order per-cell coefficient by Taylor expansion, even though it states only two terms. It does not give exact coefficient agreement with the infinite law at every finite C_(2m) for m≥5 or the three exceptional finite cycles. Those are the distinct findings supported by the comparison.

## value

PASS

The sharp finite-size onset determines exactly when the known bulk strong-bias approximation is already correct through degree three for the natural periodic finite model. The C8 third-order defect, despite agreement in the first two terms there, makes the size threshold nontrivial. This gives finite-size information a researcher cannot read off from a bulk coefficient or a handful of finite tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
