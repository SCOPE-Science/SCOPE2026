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

The theorem was checked with `python verify.py` and `python verify_independent.py` from the published source package. Both scripts regenerate the four-letter universe and the single-adjacent-swap shadow sets rather than reading stored graph instances.

`verify.py` reports \(96\) balanced words, \(8\) fixed strands, \(44\) nontrivial reverse-complement orbits, \(40\) internally admissible orbits, \(100\) conflicts, and five connected components with exact independent-set size and count pairs \((2,3),(3,12),(2,3),(3,12),(1,4)\). A direct test verifies the displayed \(22\)-word construction. The program reports `PASS_ALL_EXHAUSTIVE_CERTIFICATES`.

`verify_independent.py` uses composition classes and a separate memoized inclusion/exclusion algorithm. It confirms the constrained optimum \(22\), the extremizer count \(5184\), and the unconstrained composition-only optimum \(25\). The program reports `ALTERNATIVE_COMPOSITION_DP_PASS`.

These checks are exhaustive finite mathematical computations, not statistical samples and not claims of independent scientific audit. The code does not model substitutions, deletion, sequencing reads, biochemical thermodynamics, or arbitrary transposition distance.
