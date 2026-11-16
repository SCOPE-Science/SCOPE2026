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

# Reproducibility and precise limits

The theorem uses exact integers and unnormalized Walsh characters on \(\mathbb F_2^{3n}\). The primary argument is the signed assignment formula in `RESULT.md`, not a numerical extrapolation. It establishes all-width divisibility, exact witnesses for the smallest nonzero multiplier, and the zero-frequency threshold. The \(n=4\) rank and the displayed finite spectral counts are exhaustive computational consequences.

Two independent programs are supplied:

```sh
g++ -std=c++17 -O2 check_walsh.cpp -o check_walsh
./check_walsh
python3 check_independent.py
```

The C++ program enumerates all matrices from the row-pair collision constraint, computes every integer Walsh coefficient for \(2\le n\le7\), and checks cardinalities, zero counts, minima, witnesses, and Parseval. Its expected final marker is `C4FREE_WALSH_ALL_CHECKS_PASS`.

The Python program directly checks all \(2^{3n}\) binary matrices for \(2\le n\le5\), then uses an independent explicit injection formula and eight-state accumulation to compare complete small spectra and sample frequencies through \(n=20\). Its expected final marker is `C4FREE_INDEPENDENT_BRUTE_AND_FORMULA_PASS`. The random examples use a fixed deterministic seed.

Computer checks through finite \(n\) do not by themselves certify the infinite statement. No stronger claim, independent mathematical audit, or exhaustive historical-priority guarantee is made.
