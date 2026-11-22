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

The two complete and independently constructed implementations below establish the 168-by-288 configuration census and test all 3,360 eligible hyperoval-fiber pairs, with 82,944 matching pairs per fiber pair. Assertions inspect every candidate within the fixed finite domain. They do not depend on random sampling, numerical tolerances, logs from previous computations, untrusted input data, or an asserted unexplored automorphism reduction.

## C++17 verification (standard library)

```bash
g++ -O3 -std=c++17 check_affine.cpp -o check_affine
./check_affine
```

The source constructs \(\operatorname{PG}(2,4)\) from affine points, slopes and the line at infinity. It independently enumerates the hyperovals and matchings, applies complete pairwise bitset-intersection tests, and checks all stated totals, component facts and sharp exclusions. Exit status zero and the `PASS` lines indicate that all assertions completed.

## Independent homogeneous-coordinate verification

```bash
OPENBLAS_NUM_THREADS=1 python3 check_homogeneous.py
```

Install the optional Python checker dependency using `python3 -m pip install -r requirements.txt` if NumPy is not already installed.

This source uses normalized triples in \(\mathbb F_4^3\), normalized linear forms and vectorized NumPy bit-count comparisons. It independently checks every possible six-point set, all residual perfect matchings, every within-fiber matching pair, every 3-intersection fiber pair and all quotient distances. Requires Python 3 with NumPy; tested with NumPy 2.3.5. The C++ checker requires no third-party runtime libraries.

## Checked finite values

- 168 hyperovals and six disjoint lines per hyperoval;
- 288 residual perfect matchings per fiber; 48,384 total minimum maximal matchings;
- 40 quotient neighbors for every hyperoval, quotient diameter two;
- 216 seven-edge bridges and zero six-edge bridges per 3-intersection fiber pair;
- 725,760 cross-fiber seven-exchange edges, 943,488 internal edges, 1,669,248 total;
- 30 cross neighbors per optimum, and global degrees 67 and 71 with 24,192 configurations each;
- complete absence of moves under three or fewer changes, 168 components through threshold six, and connectivity at threshold seven.

The mathematical lower bound and interpretation of the exhaustive certificate are given in RESULT.md. Independent scholarly audit has not been performed; no originality claim is inferred solely from search results or computation.
