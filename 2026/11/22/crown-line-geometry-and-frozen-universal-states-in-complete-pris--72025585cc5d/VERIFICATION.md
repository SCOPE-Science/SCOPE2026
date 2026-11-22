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

# Reproduction and verification

In a directory containing the two bundled `.py` files, run:

```sh
python3 verify_bruteforce.py
python3 verify_structure.py
```

Both programs use only Python 3's standard library. They were executed from the actual packaged source paths with exit code zero. The observed output was:

```text
BRUTE_OK 4 26 72 48 2 4
BRUTE_OK 5 42 160 120 2 4
BRUTE_OK 6 62 300 240 2 4
BRUTE_OK 7 86 504 420 2 4
BRUTE_OK 8 114 784 672 2 4
STRUCTURE_OK 4 12 26 72 48 12
STRUCTURE_OK 5 20 42 160 120 20
STRUCTURE_OK 6 30 62 300 240 30
STRUCTURE_OK 7 42 86 504 420 42
STRUCTURE_OK 8 56 114 784 672 56
STRUCTURE_OK 9 72 146 1152 1008 72
STRUCTURE_OK 10 90 182 1620 1440 90
STRUCTURE_OK 11 110 222 2200 1980 110
STRUCTURE_OK 12 132 266 2904 2640 132
STRUCTURE_OK 15 210 422 5880 5460 210
STRUCTURE_OK 25 600 1202 28800 27600 600
STRUCTURE_OK 50 2450 4902 240100 235200 2450
```

The direct program enumerates every originally labeled blue subset with at most \(n\) vertices through \(n=8\), not just expected candidates; it separately checks all legal jumps/slides and all-pairs shortest paths and shortest-route counts. The second program builds only abstract off-diagonal pairs, independently checks the incidence-distance expression and counts shortest antipodal paths for \(n\le12\), and verifies closed structural counts at larger orders. Neither finite range proves the result for arbitrary \(n\); the universal first-force, adjacency and bridge arguments in `RESULT.md` do that. No external certification is asserted.
