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

The algebraic argument is in `RESULT.md`; finite checks are corroboration, not an infinite proof.

With a C++17 compiler and Python 3, execute from the directory containing the files:

```sh
g++ -std=c++17 -O2 check_prime_fields.cpp -o check_prime_fields
./check_prime_fields
python3 check_gf4.py
```

`check_prime_fields.cpp` enumerates the \(n(n+1)/2\) functional coefficients, builds the full multiplication Gram matrix directly from the rule \(E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell}\), computes its rank by modular Gaussian elimination, independently sums the ranks of the rectangular blocks, and compares the maximum-rank multiplicity against the theorem for ten cases. These are actual computations over the prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), not experiments with a rounded real rank.

`check_gf4.py` explicitly implements arithmetic in \(\mathbb F_2[t]/(t^2+t+1)\). It exhausts all coefficient assignments for dimensions two and three, compares direct and block ranks, and checks 5,000 independently seeded dimension-four cases. Its first two cases are boundary and extension-field checks; the main result concerns \(n\ge3\).

The recorded runs appear in `CHECKS.txt`. All reported tests passed. Larger dimensions and other fields are covered by the proof, not by computation. Neither checker certifies historical priority or supplies an independent mathematical audit.
