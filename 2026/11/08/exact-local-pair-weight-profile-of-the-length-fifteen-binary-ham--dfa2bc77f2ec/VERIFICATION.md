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

The theorem is a finite enumerative statement proved by exhaustive dynamic programming with complete state recurrence in `RESULT.md`. `verify_profile.py` evaluates the memoized suffix recurrence, checks all seven coefficients, orbit division, witnesses and factorial moments. `forward_profile.cpp` independently uses forward transfer of polynomial distributions and verifies two normalized starting pairs.

Reproduction from the extracted package:

```sh
python3 verify_profile.py
c++ -O3 -std=c++17 forward_profile.cpp -o forward_profile
./forward_profile
```

Observed checks:

```text
VERIFY_OK (17106784, 26741280, 15750240, 4524160, 683520, 57216, 1600) states 319502
FORWARD_VERIFY_OK 17106784 26741280 15750240 4524160 683520 57216 1600 0 0 0 0 0 0 0 0 0
```

The mathematical reduction from Hamming-codewords to xor-zero triples, the free group action and the finite recurrence are explicitly derived in `RESULT.md`, rather than inferred from these outputs. The recurrences make no claim about other Hamming lengths. The numerical result has been checked within this package; no independent scientific audit or priority certification has been performed.
