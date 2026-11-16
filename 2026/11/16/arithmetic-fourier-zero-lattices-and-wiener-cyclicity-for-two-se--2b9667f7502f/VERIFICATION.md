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

Run `python check.py` using Python 3's standard library. The observed output was:

```
CHECK_OK finite_rational_frequency_tests= 9000  plus exact overlap checks
```

The script compares exact rational membership in the three proposed Fourier-zero families with the direct complex endpoint-exponential expression on a 9,000-point rational test grid. It also checks explicit simultaneous-root and distinct resonance instances. It is a finite check only; it does not test every real parameter or replace the following analytical argument.

Exact integration gives a bracket formed from two sine amplitudes and one unit complex phase. If both amplitudes vanish, the common lattice follows. Otherwise the equality of absolute sine values forces an integral sum or difference of the phases; the required sign leads respectively to the gap/integer or midpoint/odd-parity lattice. Conversely, substitution shows that each lattice is contained in the exact zero set. At non-common zeros the derivative has a nonzero imaginary term; at common zeros it is nonzero for unequal lengths. Equal lengths factor into a sine times cosine, and overlapping simple factor zeros yield exactly double roots. Rational arithmetic characterizes the nonemptiness of each lattice. Wiener's classical \(L^1\) and \(L^2\) translation theorems supply the stated cyclicity consequences.

Scientific limits: strict positivity of interval widths and their separating gap; continuous real frequencies; no assertion about complex zeros, discrete translates, multi-interval unions or uniform Fourier lower bounds. The closest motivating manuscript was accessible only through its abstract and indexed scientific description, not complete full text. An older equivalent arithmetical classification cannot be ruled out by the available search evidence. No independent mathematical audit or validation has been performed.
