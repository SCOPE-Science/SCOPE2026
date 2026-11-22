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

# Exact verification and boundaries

The complete standalone artifact `verify_tetrads.py` uses only the Python standard library. Execute `python3 verify_tetrads.py tetrad_spectra.csv`. The script regenerates `tetrad_spectra.csv` and reports a successful enumeration of the \(16\)-node symplectic space, \(35\) plane directions, \(60\) Göpel and \(80\) Rosenhain affine planes, and \(720\) branch permutations. Independent four-subset versus direction/coset constructions agree exactly. It verifies all \(11\) partition spectra, independent fixed-coset counts, the unique pairwise collision, and the node/trope spectrum comparison.

The mathematical argument does not infer infinite facts from sampling: every smooth genus-two curve in odd characteristic has the specified symplectic six-branch action, every branch permutation is among the enumerated \(720\) elements, and the polynomial realization argument is uniform in the finite field. The table concerns geometric Frobenius acts, not Hasse–Weil curve point counts. Independent audit has not been performed.
