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

# Reproduction and boundaries

The attached `verify_kummer_flags.py` is a standalone Python 3 standard-library program. With `kummer_flag_spectra.csv` in the same working directory, run:

```sh
python verify_kummer_flags.py kummer_flag_spectra.csv
```

Successful output: `KUMMER_96_FLAGS_720_SIX_POINT_ACTIONS_11_TYPES_SHARP_THREE_EXTENSIONS_VERIFIED`.

The verifier independently builds all \(16\) nodes, \(16\) tropes, and \(96\) flags from the explicit incidence rules. It tests all \(720\) elements of \(S_6\), compares orbit sizes and fixed points with the formula, and checks the eleven distinct signature triples, the unique two-extension collision, and the exact nine node/trope spectra. It rewrites `kummer_flag_spectra.csv` deterministically; its bytes are supplied and independently hashed in the archive. The program has no external software dependencies.

The mathematical proof of the global finite-field theorem is the characteristic-not-two Kummer incidence identification plus the equivalence between Frobenius classes on a six-element finite étale set and partitions of six. Exhaustive finite-group computation closes the remaining finite decision problem. The field realizability argument uses irreducible polynomials over finite fields, not finite sampling.

**Scope:** No characteristic-two statement, no moduli/invariant reconstruction beyond six branch-factor degrees, and no independent audit. Historical uniqueness is not established by these tests.
