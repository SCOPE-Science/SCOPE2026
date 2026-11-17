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
# Reproducibility and scientific limits

The complete theorem and proof are in `RESULT.md`. The two standalone programs are `check_exact.py` (standard Python, no third-party packages) and `check_direct.cpp` (C++17). Recreate their recorded outputs with:

```sh
python3 check_exact.py > check_exact.out
c++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct
./check_direct > check_direct.out
```

`check_exact.py` checks all 243 local length-five windows and every starting configuration for rings of length three through ten. Its exact rational interpolation and transfer-matrix arithmetic check the pulse-number polynomial, extinction and periodic-state counts. `check_direct.cpp` independently updates configurations directly, exhaustively for lengths three through twelve, without using the symbolic transfer matrix. The outputs included in this package were produced by running those files; the exact statements for all lengths rest on the proof, not on extrapolation from enumeration. The original literature search does not guarantee historical uniqueness. No independent audit or certification has been performed.
