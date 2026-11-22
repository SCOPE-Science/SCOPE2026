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

# Reproduction and mathematical limits

Run `python verify_cactus_chain.py` using Python 3.9 or later and its standard library. The supplied checker exhaustively enumerates the spanning trees of five small cactus flowers, including an example with a bridge. It constructs the cut-first chain independently from the graph's fundamental cuts using exact `fractions.Fraction` arithmetic, and checks the symmetric coordinate-product kernel and all character eigenspaces. For times 0, 1, 2, 3 and 5 it compares exact distributional chi-square with the full spectral multiplicity formula. It additionally computes exact-state-lumped finite-time total variation numerically for homogeneous and heterogeneous cycle families and compares with their analytical asymptotic curves.

The delivered script reports `PASS with mixed-profile tests 1818 assertions` when run as supplied. Its exact assertions concern finite graphs and transition matrices. Its floating-point checks concern finite examples and bounded numerical errors. The limiting theorems, including the central Gaussian profile, early-time separation, and discrete-to-continuous comparison, are instead established by the analytical proof in `RESULT.md`. The stated mixture profile and mixing-time dichotomy do not depend on Monte Carlo sampling.

All cycle lengths in the finite checks are small, whereas the theorem requires the explicitly specified exponentially growing cycle family. The test suite is not an exhaustive computational proof of every asymptotic regime. Independent mathematical audit has not been performed.
