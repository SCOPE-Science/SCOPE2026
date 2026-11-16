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

# Exact computational verification

## Dependencies and commands

Python 3 and NumPy are required. From the folder containing the three standalone files `verify_asm.py`, `verify_independent.py` and `kernel_certificate.json`, run:

```
python verify_asm.py
python verify_independent.py
```

## Checks performed

The first program constructs order-two through order-five ASMs by allowed alternating rows and column-prefix constraints; it verifies their respective counts 2, 7, 42, 429. It forms the complete order-five integer agreement Gram matrices at degrees three and four; it verifies their ranks 425 and 429 over the prime field of order 101 using exact modular elimination. It loads all four sparse integer kernel vectors, checks each product against the full cubic Gram matrix is exactly zero, checks their four anchor coordinates form the identity and checks their nonzero-support sizes 16, 16, 134, 120. It also confirms full cubic recovery in orders two, three and four.

The second program enumerates the 429 states independently via interlacing monotone triangles, constructs the two Gram matrices from the independent enumeration and checks the ranks 425 and 429 over the prime field of order 1009. Both programs completed with PASS outputs from the actual package files.

## Mathematical force and limitations

Nonzero minors modulo either prime prove nonzero integer minors and hence lower bounds on real rank. Four independent exact integer annihilators prove the matching upper bound at degree three; the full modular rank at degree four proves real invertibility. The Gram matrix is the exact product of the complete cylinder evaluation matrix with its transpose, so its real kernel gives all signed measures invisible to those marginals. No random sampling, approximate numerics or infinite extrapolation is involved. Independent external validation has not been performed.
