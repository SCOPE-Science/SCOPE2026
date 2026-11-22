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

The package contains `code/exhaustive_peel.cpp`, `code/exhaustive_paths.cpp`, and their full expected text outputs under `data/`. Both programs require C++17, with no external packages. From the root of the extracted files, run:

```
g++ -std=c++17 -O3 -mpopcnt code/exhaustive_peel.cpp -o exhaustive_peel
./exhaustive_peel > peel_reproduced.txt
g++ -std=c++17 -O3 code/exhaustive_paths.cpp -o exhaustive_paths
./exhaustive_paths > paths_reproduced.txt
```

Compare the reproduced files byte-for-byte with `data/peel_output.txt` and `data/paths_output.txt` on the same implementation. The first output includes explicit periodic and maximal-depth witnesses. Both independently derived complete first-entry/period profiles agree. The source algorithms perform full finite integer enumeration rather than random sampling. The directed arc definitions, bit numbering, activation threshold and state-space range are specified in `RESULT.md`.

# Scientific verification and limits

The Paley graph has quadratic-residue out-neighborhood \(Q=\{1,2,3,4,6,8,9,12,13,16,18\}\); the carousel uses offsets 1 through 11. Each has 8,388,608 labelled binary states. The profiles sum to exactly this number for each network. Direct update iterations from Paley state `15611` have least period four, and from carousel state `63` have least period twenty-three. Paley input `23807` requires exactly ten updates to enter a cycle; carousel input `171551` requires exactly four. All other states have first-periodic-entry time at most those bounds by exhaustive classification.

The computer programs are independent *same-package algorithms*, not a substitute for independent mathematical auditing. They do not prove results for any other graph order. Historical priority has been compared to the stated sources but not conclusively established.
