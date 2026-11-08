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

# Reproducible verification

Execute the following standalone Python 3 scripts from the directory containing this file:

```
python3 verification/verify_bruteforce.py
python3 verification/verify_histogram.py
python3 verification/verify_formula.py
```

The exact captured standard output for each script is bundled in the adjacent output text file of matching stem.

`verify_bruteforce.py`: checks every labelled chip vector in the finite confined box for each \(2\le b\le7\), including \(3,211,264\) vectors at \(b=7\). The update is the literal graph-rule update; a state counts iff it returns after four updates but not after two. All mass counts match the polynomial.

`verify_histogram.py`: independently reduces the right side to histograms and weights them by exact multinomial counts, through \(b=12\), with separate update and count implementations. This reaches all bounded configurations without listing every labelling explicitly.

`verify_formula.py`: checks the polynomial simplification by exact integer coefficients and the endpoint and total-count identities for each \(2\le b\le50\).

The proof uses Jiang's equal-period firing-count and complementary confinement properties and Jiang–Scully–Zhang's non-clumpiness theorem; these are scientific inputs, not computational certificates. Finite computations do not prove correctness for all \(b\); the full argument appears in `RESULT.md`. No independent audit has been performed.
