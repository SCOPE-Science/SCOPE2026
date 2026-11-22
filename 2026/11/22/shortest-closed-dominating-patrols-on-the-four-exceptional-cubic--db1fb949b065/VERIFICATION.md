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

# Reproducible verification of finite patrol classification

Unpack `check_watchman.py` and `check_watchman.cpp` from the same result record, preserving their exact decoded bytes. Execute:

```sh
python3 check_watchman.py
c++ -O2 -std=c++17 -Wall -Wextra -pedantic check_watchman.cpp -o check_watchman
./check_watchman
```

Both programs must print `ALL PASS`; the Python implementation additionally prints all ten spatial orbit representatives. The C++ implementation exhausts every rooted vertex sequence up to the optimum length, checking all earlier even lengths and all support-type subtotals. The Python implementation checks both the exact rooted-walk dynamic recurrence and direct DFS enumeration, then enumerates all graph automorphisms by pairwise distance preservation, acting on canonical cyclic words. The two programs use independent adjacency generators and counting methods.

Expected \((w(G),\text{rooted count},\text{temporal classes})\): Heawood \((10,10920,546)\), Möbius–Kantor \((8,96,6)\), Pappus \((12,5400,225)\), Desargues \((10,240,12)\). Expected spatial orbit counts: \((5,1,3,1)\); the exact orbit sizes and walks are documented in `RESULT.md`.

**Scope and limits:** These are exhaustive finite proofs for four fixed, labeled simple graphs only; they are not infinite-family theorems. Checks make no inference from a timeout or sampled enumeration. They do not establish first publication priority. External independent validation is not part of this package.
