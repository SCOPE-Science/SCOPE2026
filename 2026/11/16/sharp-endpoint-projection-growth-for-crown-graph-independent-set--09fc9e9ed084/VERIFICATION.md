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

# Mathematical and computational verification

Run `python check_crown.py` using Python 3 standard library. The script constructs independent sets without using the closed formula, transforms their indicator using exact-integer butterflies, checks all 21,824 Fourier multipliers at \(n=3,4,5,6,7\), and independently obtains the full projection kernel by inverse Walsh transform of the zero-frequency indicator at \(n=3,5\). It compares every kernel entry with the closed Krawtchouk expression and verifies exact operator norms by summing absolute kernel values. It also checks the central Krawtchouk identity and the spectral gap.

Expected terminal line: `CROWN_WALSH_PROJECTION_EXACT_PASS coefficients= 21824`.

The enumeration is a finite consistency check, not an exhaustive argument for all \(n\). The all-length conclusions are justified in RESULT.md by explicit algebraic steps and a translation-averaging proof. The exact projection norm is on finite real or complex \(\ell^1\)/\(\ell^\infty\) with counting measure. Independent audit has not been performed.
