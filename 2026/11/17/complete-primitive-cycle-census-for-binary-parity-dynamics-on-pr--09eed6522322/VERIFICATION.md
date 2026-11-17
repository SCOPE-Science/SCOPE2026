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
# Reproducible finite checks

The proof is in `RESULT.md`. Run with Python 3 standard library:

```
python verify_prism.py
python verify_prism_states.py
python verify_power_two.py
```

`verify_prism.py` builds the binary adjacency matrix of the prism from distinct neighbours and checks the claimed polynomial-GCD formula for \(\ker(F_n^t-I)\) against matrix computations for \(3\le n\le44\), \(1\le t\le34\). It additionally tests ranks to guard against implementation errors. Its output is in `verify_prism.out`.

`verify_prism_states.py` independently simulates all \(87{,}360\) labelled initial configurations for \(3\le n\le8\), identifies terminal orbits, and compares exact periodic-point counts with direct polynomial calculations. Output is in `verify_prism_states.out`.

`verify_power_two.py` uses polynomial gcd computations for \(n=2^k\) and \(n=3\cdot2^k\) (for simple graphs) to independently check \(A_j\) and the implied cycle counts through \(k=8\). It does not enumerate all those large state spaces. Output is in `verify_power_two.out`.

All programs were run from copies of the embedded source files. These tests establish exact equality for the stated finite ranges only, not completeness of the literature comparison or an independent audit.
