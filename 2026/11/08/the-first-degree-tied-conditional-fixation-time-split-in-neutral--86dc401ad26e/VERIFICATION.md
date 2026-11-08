---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification instructions

The two exact, standalone scripts require only Python 3 and its standard library.

```text
python3 neutral_moran_census.py
python3 neutral_moran_path_interval.py
```

The exhaustive certificate iterates over all \(2^{\binom{n}{2}}\) labelled simple graphs for \(n=2,3,4,5\), retains connected graphs, groups isomorphism classes by the least relabelled edge mask, and evaluates fixation probabilities and conditional first moments by exact Fraction Gaussian elimination. Counts of connected classes are \(1,2,6,21\); counts with equal fixation chance but unequal conditional time are \(0,0,0,7\). The seven five-vertex canonical masks are exactly `29, 58, 62, 185, 187, 221, 254`.

The independent interval-state script does not reuse any functions or graph classifications from the census checker. It derives the transition law directly from the four boundary events for mutant intervals on the five-vertex path. Both checkers verify \(p(1)=p(2)=1/7\), \(\tau(1)=14650/329\), \(\tau(2)=26955/658\), and \(\tau(1)-\tau(2)=335/94\).

All computations are exact rational arithmetic, not floating-point estimates. The infinite-horizon probability and moment statements are justified by finite-state almost-sure absorption, the martingale argument and the resolvent recurrence in RESULT.md. The certificate does not attempt a result for six or more vertices or for non-neutral reproductive fitness.
