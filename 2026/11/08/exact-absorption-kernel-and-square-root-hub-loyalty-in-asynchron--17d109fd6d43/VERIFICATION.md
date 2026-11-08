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
# Verification of the exact friendship-graph absorption kernel

The following checks were executed with Python 3 and only standard-library modules:

- `python verify_absorption.py` — direct memoized exact rational recursion over all possible next changes, with no use of the proposed rank law, for each of the \(10,920\) labelled states at graph sizes \(1\leq k\leq6\). The computed complete absorption measures coincide with the rank/subset formulas, including zero-mass cases; their probabilities sum to one.
- `python verify_formula.py` — independent multinomial evaluation of the exact hub-switch law and an independent binomial-series calculation of unanimity. Exact rational checks cover specified sizes through \(k=160\), and \(\sqrt{\pi k}\,p_k\) reaches approximately \(0.9961\) at \(k=160\), consistent with but not establishing the limiting constant.

Outputs are included in `absorption_output.txt` and `formula_output.txt`. The argument establishing all sizes uses the exact relative order of eligible updates, the one-switch invariant, elementary binomial integration, and a normal limit with uniform integrability. Finite computation is not used as an infinite proof.

Scientific limits: no absorption-time distribution, no random tie-flipping dynamics, no unequal vertex-selection rates, no independent audit, and no guarantee against equivalent claims in all historical literature.
