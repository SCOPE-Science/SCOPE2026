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

# Mathematical verification

The proof in `RESULT.md` establishes the all-size and limiting statements. The standalone `check_adjacent.cpp` independently and exhaustively reconstructs both matchings and all baseline-pivotal indicators for market sizes two, three and four, and compares the resulting totals with exact rational coefficients of the product probability-generating function.

Compile and execute: `g++ -std=c++17 -O3 -Wall -Wextra -pedantic check_adjacent.cpp -o check_adjacent && ./check_adjacent`.

Observed `total / unchanged / pivotal counts`:

- 2 pairs: `4 / 0 / [0,4,0]`.
- 3 pairs: `1728 / 576 / [576,864,288,0]`.
- 4 pairs: `26873856 / 11197440 / [11197440,11570688,3732480,373248,0]`.

Each event space is exhaustive for that number of pairs. These finite computations are corroboration and are not presented as proofs for every population or for asymptotics. There has been no independent external audit.
