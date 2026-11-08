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

# Reproduction and limits

The self-contained `verify.py` script runs with the standard Python 3 library:

```sh
python3 verify.py
```

It generates the complete coined walk amplitudes on all occupied sites through the third step, independently of the closed origin formulas. It also enumerates the corresponding independent-increment classical return probabilities, compares the exact polynomial-difference identities using rational parameters, checks parameter-phase boundaries and samples the constrained renewal-policy triangle using fixed-seed pseudorandom convex coefficients.

The recorded execution passed 8,307 bounded checks with switching parameters approximately \(0.140013678738\), \(1.608554344652\), and \(6.701562118716\). A clean reproduction should produce the corresponding `PASS` output. Passing finite tests does not prove all-parameter statements, which instead follow from the explicit finite-step recurrence, exact polynomial factorization, Descartes' sign bound and the complete feasible-polytope argument in `RESULT.md`.

No external formal proof certificate is claimed. This is a scientific consistency check and accompanying analytical derivation, not independent validation or a publication-priority certification.
