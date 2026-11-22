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

# Verification

The complete finite inverse recurrence enumerates primitive cyclic classes at all stages from zero through ten. `verify_cyclic_girth.py` and `verify_cyclic_girth.cpp` independently calculate the stage counts, girths and extremal multiplicities and verify the derivative of every constructed inverse. The C++ source additionally directly enumerates every primitive cyclic binary word of period at most \(18\) as a check independent of the inverse generator.

`level_statistics.csv` provides the full finite period distribution at every enumerated stage. The enumerations make no assertions for stages greater than ten. Correctness beyond the finite computational range, where relevant, rests only on the proved inverse lemma and strict period descent; no timeout or partial search is taken as an impossibility proof.

Run using Python 3 and a C++17 compiler:

```sh
python3 verify_cyclic_girth.py
g++ -O2 -std=c++17 verify_cyclic_girth.cpp -o verify_cyclic_girth
./verify_cyclic_girth
```
