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

# Reproduction and verification

Run `python3 check_distance.py` and `python3 check_components.py` from the directory containing these files. They need only Python 3's standard library and exit with failure upon any mismatch. The distance-based program enumerates the entire \(2^{16}\)-set space, checks every vertex pair using the explicit rook-product distance, separately computes weak \(2\)-resolution on all six-sets, and calculates five symmetry orbits by generating automorphisms. The second program independently constructs the spanning incidence graph and verifies its two local leaf conditions plus the connected-component obstruction, checking each against direct distances on five small boards.

Observed successful markers: `DIRECT_DISTANCE_CHECK_OK`, `COMPONENT_CHARACTERIZATION_CHECK_OK`. The first program prints 45,605 total resolving sets, 2,016 six-set optima, orbit sizes 96, 192, 576, 576, 576, and weak-2-only/both/total-only/neither counts 1,168/864/1,152/4,824. The second program prints total counts 0, 13, 274, 1,952, and 45,605 for boards \(2\times2\), \(2\times3\), \(3\times3\), \(3\times4\), and \(4\times4\), respectively.

The general equivalence is proved algebraically in `RESULT.md`; the finite scripts are not substitutes for that proof. The prior-publication comparison is provisional, and independent human validation has not been performed.
