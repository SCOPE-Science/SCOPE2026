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

The standalone `verify.py` uses only the Python standard library. Running `python verify.py` exhaustively checks all labeled ranking profiles with (alternatives, voters) = (3,2), (3,3), (4,2), (4,3), totaling 14,652 profiles, against the block-reversal construction and the literal-reversal zero-unanimity criterion. It separately enumerates all ranking profiles on three alternatives for 2 to 5 voters and verifies the two exact overlap probabilities as rational numbers.

Critical universal proof steps independent of computation: (i) unanimous matching blocks preserve unanimous orientations in both outputs and reverse all cross-block orientations; (ii) the six extreme-element events on three alternatives have total probability \(6\cdot3^{-n}-6\cdot6^{-n}\); (iii) disjoint candidate-pair comparisons have independent relative-order information; (iv) incident pair indicator products have expectation \(2\cdot3^{-n}+2\cdot6^{-n}\); (v) the cited dependency-neighborhood Poisson approximation theorem yields the displayed vanishing error. Finite checks cannot themselves prove these claims for arbitrarily many voters or candidates.
