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

# Reproduction

Compile `verifier.cpp` using `g++ -std=c++17 -O3 verifier.cpp -o verify_omega` and run `./verify_omega 4 64`. Every even input in this finite range is enumerated; the largest input performs a complete \(2^{31}\)-subset inclusion–exclusion. Expected two-column integer values are in `counts.csv`; timing numbers printed by the program need not reproduce.

Compile `gray_check.cpp` using `g++ -std=c++17 -O3 gray_check.cpp -o gray_check` and run `./gray_check 48 64` to cross-check all nine new lengths with a different occupancy-counter implementation and Gray-code subset order. Both complete enumerators check the final \(h=64\) case.

The published Mossinghoff–Trudgian exact values for all even \(4\le h\le46\) coincide with the output, and the nine remaining values satisfy the published Table 2 bounds. The rational factor \(S_{64}\) can be independently reproduced by summing each `counts.csv` coefficient divided by the product of \((p-2)\) for primes \(3\le p<h\), using arbitrary-precision fractions. No finite computation proves any claim about the infinite tail or the truth of the prime-tuples conjecture.
