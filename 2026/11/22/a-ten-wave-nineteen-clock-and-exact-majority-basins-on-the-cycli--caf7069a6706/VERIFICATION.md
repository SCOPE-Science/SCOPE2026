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
# Reproducible verification

Unpack the embedded files into a single directory. The complete Python functional-graph certificate can be regenerated with:

```bash
python3 verify_functional.py --json output_functional.json
```

The independent C++ direct-update checker can be regenerated with:

```bash
c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct
./verify_direct
```

`output_direct.txt` is the expected text output of the C++ verifier; `output_functional.json` is the recorded JSON census from the Python verifier. The programs compute transitions with different algorithms and neither reads the other's output. Python enumerates all 524,288 states and builds their complete functional graph, checks ten separate rotation-orbits and all their 190 labelled phase transitions, then independently derives exact attraction basins. C++ examines all 524,288 states directly, checks period and entry by iterate identities, verifies all 190 phase rotations and all basin counts, and recomputes the prior Paley-19 comparison with a separately generated residue offset set.

The finite proof is conclusive for the specific 19-vertex, 9-out-neighbor majority map. No behavior on other graph orders and no independent mathematical validation is established.
