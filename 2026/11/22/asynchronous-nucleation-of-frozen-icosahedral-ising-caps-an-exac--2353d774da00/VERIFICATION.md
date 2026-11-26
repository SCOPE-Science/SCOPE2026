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

A successful flip at a vertex with d≥3 disagreeing neighbors changes the cut size by 5−2d<0. In a nonabsorbing state at least one flippable clock is active, giving a finite exponential wait and equal next-flip probabilities among the eligible vertices. At most 30 flips can occur, giving almost-sure absorption, with no update-order or stationarity assumption beyond the stated clocks. I independently formed the icosahedral graph from the golden-ratio coordinates, using exact squared distances, and exhausted all 4096 states. The only fixed masks were the two constant states and the twelve closed neighborhoods, with complementary caps. The simultaneous majority map has exactly one incoming mask per cap, its own. For asynchronous dynamics I propagated 13 channels of initial mass forward on the cut-decreasing graph in exact fractions, confirming the full size-resolved vector and every polynomial coefficient, and checked all 220 three-spin starts by a local exact path sum (160 zero and 60 with 1/30). In the supplied labels, the displayed path adds 0, 3, then 5, each with at least three positive neighbors; the successful seed is therefore among the 60. The one-half value is 10067037913/87091200000 and the ratio to 12/4096 is 10067037913/255150000. The polynomial has positive coefficients in q and is at least 2q³, strictly exceeding 12q⁶ for 0<q≤1/4, with the maximum unique at p=1/2. Replay: `python /workspace/review-evidence/reproduce.py 3`, using only the standard library on Python 3.10 or newer.

## originality

PASS

The icosahedral equilibrium census and synchronous singleton cap basins are exact prior coverage and already credited. The distinct checked contribution is the asynchronous, rate-one icosahedral absorption polynomial and three-seed law, hence its quantitative contrast with those synchronous basins. Exact asynchronous analogues on other graphs are credited for the method and theme, but do not give these numbers or the fixed-graph comparison.

## value

PASS

The finite graph and invariant are natural: the same two scheduling protocols share all equilibria, yet one forbids cap nucleation while the other can grow a six-spin cap from three positives. The full initial-density law, the exact seed probabilities, and the more than 39-fold difference at the unbiased start quantify that mechanism on a canonical graph. This is more than recounting static fixed points and is a useful benchmark for stochastic majority calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
