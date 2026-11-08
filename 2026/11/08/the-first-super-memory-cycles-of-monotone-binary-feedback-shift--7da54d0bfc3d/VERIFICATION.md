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

# Verification of the finite classification

The standalone files `verify_bruteforce.cpp` and `verify_pruned.py` test the full finite range of candidate periods greater than their memory, for each memory from one to six. Sperner's inequality gives the exhaustive cutoff \(L\le\binom{n}{\lfloor n/2\rfloor}\), so no length above this cutoff can occur. The direct C++ search visits all \(2^L\) binary rooted words; the independent Python algorithm prunes only when already completed ordinary length-\(n\) windows are comparable, followed by an exact cyclic-boundary test. Both compare the complete canonical-rotation sets and their rooted counts.

Reproduction commands, from the directory containing the files:

```sh
c++ -std=c++17 -O2 verify_bruteforce.cpp -o verify_bruteforce
./verify_bruteforce
python3 verify_pruned.py
```

Expected final output markers: `BRUTEFORCE_VERIFY_OK` and `PRUNED_VERIFY_OK`. Both appeared in the actual pre-delivery execution. The Python program additionally verifies coordinatewise monotonicity of the synthesized feedback on all comparable six-bit inputs and verifies the prescribed successors of the cycle words. The `counts.tsv` table lists the full exact enumerated range. Assertions are checked from each package source; no external tables, runtime-specific logs, or private files are needed.

A finite exhaustive certificate proves only the enumerated portion. The antichain criterion and Sperner cutoff are essential to convert it into a proof for every feedback function in the stated six widths. These checks are not independent scientific review or historical-priority certification.
