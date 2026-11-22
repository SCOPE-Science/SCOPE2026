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

# Verification record

Two independent C++17 verifiers were compiled from the separately included source files with standard optimization and executed successfully:

```sh
g++ -O3 -std=c++17 verify_lucas.cpp -o verify && ./verify
g++ -O3 -std=c++17 alternate_lucas.cpp -o alternate && ./alternate
```

The first printed `VERIFY_OK`, and the second printed `ALTERNATE_OK`. Each directly constructed the Lucas-cube vertex set, checked every candidate in the two boundary layers, independently counted symmetry classes and verified full coordinate-dihedral invariance minima. The final dimension-seven lower/upper finite layers were of sizes \(\binom{29}{10}=20{,}030{,}010\) and \(\binom{29}{11}=34{,}597{,}290\). The checker determines the former contains no identifying code and the latter contains exactly 259.

The exact tables and witnesses are in `CENSUS.json`. The result is a finite, complete computation for dimensions two through seven, not proof of a pattern at larger dimensions. Independent mathematical audit remains not performed.
