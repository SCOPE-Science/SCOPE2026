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

# Verification instructions

Build the standalone C++17 implementation included as `checker.cpp`:

```sh
g++ -O3 -std=c++17 checker.cpp -o checker
./checker
```

The run must terminate with `CERTIFICATE_OK`. It confirms that the two literal witness sets have distinct words, cover all 243 length-five targets and that the 33-word set omits `012` under one deletion. It then proves by exact combinatorial backtracking that no 30-word insertion cover exists and no 32-word insertion cover can avoid `012`. The search covers all possible words: there are 81 candidate length-four centers, 243 length-five target words, and 27 length-three possible deletion outputs. The only pruning criteria are necessary inequalities or coverage-state memoization justified in the proof.

Expected selected output:

```text
witness=31 insertion_covered=243 avoid_012=0
witness=33 insertion_covered=243 avoid_012=1
bound=30 forbidden=none feasible=0 forced=3 nodes=7615421 memo_states=2262551
bound=32 forbidden=012 feasible=0 forced=8 nodes=23213 memo_states=11211
CERTIFICATE_OK
```

Finite enumeration is exhaustive for the stated fixed parameters only; it does not certify a general infinite-family theorem. Independent mathematical validation has not been performed.
