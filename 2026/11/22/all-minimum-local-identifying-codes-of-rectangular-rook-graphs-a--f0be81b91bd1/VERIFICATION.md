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

Compile and run the two standalone C++ sources, and run the independent Python script (Python 3.10 or later):

```sh
g++ -std=c++17 -O2 local_ident_direct.cpp -o direct
./direct
python3 local_ident_occupancy.py
g++ -std=c++17 -O2 optimal_codes_direct.cpp -o templates
./templates
```

The observed outputs of these exact distributed source files appear in `CHECKS.txt`. The direct algorithm compares closed-neighborhood masks on every adjacent pair; the independent Python algorithm checks equivalent incidence conditions. The template generator independently compares **all** vertex pairs for ordinary identification.

The exhaustive verifiers establish only their finite cases. The arbitrary-parameter result follows from the complete mathematical argument in `RESULT.md`; the programs are not an infinite proof. No independent review or audit has been performed.
