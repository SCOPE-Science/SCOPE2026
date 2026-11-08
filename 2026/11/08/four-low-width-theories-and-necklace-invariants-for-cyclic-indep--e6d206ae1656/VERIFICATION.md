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
The three Python 3 standard-library scripts in `verification/` were run directly from the package staging directory. Their observed outputs are included as `verification/pebble_output.txt`, `verification/necklace_output.txt`, and `verification/formulas_output.txt`.

`check_pebble.py` performs noncounting fixed-variable tuple-type refinement across finite pairs. This implements reachable **sets** of substitution colors at every coordinate, not multiplicity-counting colors, until a common global partition is stable. It compares empirical equivalence against all predicted small-sample cases at widths two, three and four, including the different-width fiber cutoff.

`check_necklaces.py` computes the directed adjacency matrices independently and verifies that equal out-neighborhoods define exactly the prescribed clone classes, that closed directed walk lengths are multiples of the quotient cycle length, and that the Burnside formula and coefficient polynomial agree with brute rotation orbits on small parameter ranges.

`check_formulas.py` directly evaluates the constructed first-order formula syntax with lexical variable rebinding, using `check_necklaces.py` from the same directory for graphs and cyclic words. It verifies 90 decorated cyclic-word sentences and 308 fiber-size color evaluations. This tests a separate proof-critical issue: locally shadowing a bound variable must not change the meaning of an enclosing formula.

All three programs were executed with their actual package paths; stored outputs are exact. These are reproducible **finite consistency checks**. They do not prove that arbitrary formulas are covered by any finite sample. Infinite scope is justified by the constructive formula and permanent-pebble proofs in `RESULT.md`. The novelty assessment is bounded by the inspected literature and publicly accessible research records. No independent mathematical audit is asserted.
