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

# Reproducing the finite-rank proof

Use Python 3 with its standard library and run:

```sh
python3 check_exceptional.py
```

The script reconstructs the three-cycle conjugacy quandles without downloaded tables. It generates every normalized degree-three generator, calculates its four signed boundary terms (dropping degenerate pairs), verifies the integer chain identity, and computes the complete degree-three boundary ranks in characteristics two and three. The field-three coefficients are encoded as disjoint coefficient-one and coefficient-two bit planes, and every arithmetic operation is an exact bitwise truth-table implementation of finite-field addition. The pivot insertion algorithm is a standard Gaussian elimination proof of matrix rank. All generated triples are included, not a sample; there are respectively 7,220, 60,840, and 333,270 at five, six, and seven letters.

The lower-dimensional boundary has rank one less than the number of quandle elements, which follows from connectedness and is checked by graph traversal. The script checks right self-distributivity and \(\partial_2\partial_3=0\). It verifies characteristic-two ranks with reversed row order in every case, and characteristic-three ranks with reversed order at five and six letters. A five-letter calculation checks against the already-known coefficient dimensions. `CHECK_OUTPUT.txt` is a record of a complete successful checker execution, not a substitute for running the checker itself.

The output does not determine torsion exponents, non-tested prime characteristics, the whole integral homology or any higher homology. Independent mathematical audit has not been performed.
