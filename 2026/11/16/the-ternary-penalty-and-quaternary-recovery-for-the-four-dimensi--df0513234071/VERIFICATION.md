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

# Exact verification

From this directory compile `g++ -O3 -std=c++17 checker.cpp -o checker`, then run `./checker 2`, `./checker 3`, `./checker 4`. These were run after copying all verification sources into the final artifact directory and yielded `CHECK_PASS` in every alphabet. The enumerated normalized candidate counts were 2,048; 177,147; and 4,194,304. Their exact minima were 336, 384, 336; strict next values were 400, 396, 368; and normalized minimizer counts were 12, 240, 24. The source calculates the exact cyclotomic norm, including a second, mathematically independent convolution calculation for each minimizer.

The canonical optimizer lists are `q3_optimizers.txt` and `q4_optimizers.txt`, each containing one 16-digit canonical phase exponent per line. `python orbit_checker.py 3 q3_optimizers.txt` and `python orbit_checker.py 4 q4_optimizers.txt` returned `ORBIT_CHECK_PASS`; the normalized orbit sizes were respectively 48+192 and 12+12. Exhaustive radix loops, exact arithmetic, and the free phase normalization establish full coverage; the test does not extrapolate from a numerical sample. Supplementary discrete Fourier quadrature corroborated both representative moment values.

All claims concern root-of-unity alphabets of orders two through four, not arbitrary continuous complex phases. The certificate is computer-assisted and independently audited mathematical correctness or historical novelty are not asserted.
