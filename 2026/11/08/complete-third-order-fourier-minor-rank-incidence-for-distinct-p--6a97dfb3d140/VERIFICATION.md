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

The complete algebraic proof is in RESULT.md. Compile and run the embedded standalone C++17 exact cyclotomic checker with:

`c++ -O3 -std=c++17 checker.cpp -o checker && ./checker`

The checker constructs the relevant cyclotomic polynomials from exact integer polynomial division, reduces the determinants in exact integer bases, compares with the residue-incidence classification, and verifies all global counts. Its complete enumerations cover \((p,q)=(2,5),(3,5),(3,7)\). The observed rank distributions are \((0,1600,12800)\), \((300,13800,192925)\), and \((1470,91728,1675702)\); the success marker is `ODD_SEMIPRIME_3X3_EXACT_TESTS_PASS`.

The exhaustive checks are finite examples. The proof, not a finite scan, establishes the theorem for every pair of distinct primes. No claim of independent validation is made.
