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

# Reproduction and boundaries

This is a complete finite verification for the declared group and binary alphabet. From this directory run:

```sh
python3 line_incidence_checker.py
cc -O3 -std=c11 -Wall -Wextra -Werror full_direct_check.c -o full_direct_check
./full_direct_check
```

The first program generates the exact pair/triple-pencil counts by row-choice enumeration, deduces the six-pencil membership histogram by binomial inversion, and checks the complete rank distribution and total. Its critical triple-pencil counts use 3,125 and 100,000 enumerated row assignments respectively; no numerical approximations enter.

The C program, with a distinct loop and counting method, tests every integer bitmask from zero through \(2^{25}-1\), computes the six pencil balances directly, and stores its rank-by-weight distribution. It asserts all global totals and the total number of masks. The saved output from both executions is `verification_counts.txt`. No external data files or packages are required. The compiled executable is not required for reproduction and is not embedded.

The proof of the cyclotomic zero criterion, the pencil-intersection symmetry, the Boolean two-direction rigidity, and the counting inversion is in `RESULT.md`; computation is used only for the explicitly finite triple-pencil counts and exhaustive independent corroboration. Nothing here proves an infinite-field theorem, conditioning bounds, or bibliographic uniqueness. An independent mathematical audit has not been performed.
