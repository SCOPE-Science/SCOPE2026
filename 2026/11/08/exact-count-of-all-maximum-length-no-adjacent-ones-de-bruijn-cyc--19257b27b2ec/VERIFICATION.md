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

# Verification procedure and boundaries

The enumeration proof is in `RESULT.md` and covers every integer \(n\ge2\), using the prior known optimum-support theorem of Chee et al. (2024). Reproduction of its finite numerical table uses only the files included alongside this document.

1. With Python 3, run `python3 verify.py counts.csv`. This performs independent exact-integer full-graph Bareiss cofactors for \(2\le n\le12\), a separately constructed compressed-graph Bareiss computation for \(3\le n\le15\), exhaustive enumeration of balanced minimum deleted-edge sets for \(2\le n\le7\), and a direct circular-word/rotation census for \(2\le n\le6\). The checked run printed `FULL_GRAPH_DETERMINANTS_OK_2_TO_12`, `INDEPENDENT_COMPRESSED_BAREISS_OK_3_TO_15`, `UNIQUE_MAXIMAL_SUPPORT_ENUMERATION_OK_2_TO_7`, `DIRECT_CIRCULAR_WORDS_OK_2_TO_6` and `VERIFY_OK`.
2. With a C++17 compiler and Boost.Multiprecision headers, compile `g++ -std=c++17 -O2 count_cycles.cpp -o count_cycles` and execute `./count_cycles 15`. The output is exactly `counts.csv`. CRT modulus accumulation exceeds the proved combinatorial bound \(2^{F_{n-1}-1}\), so these reconstructed nonnegative integers are exact.

The finite enumeration checks are cross-checks of the recurrence-free construction and determinants, not proofs of the assertions for arbitrarily large \(n\). The previously known all-order optimality and uniqueness are cited from Chee et al. (2024); the newly assessed complete-cycle counting formula follows from a proved forced-corridor arborescence bijection, BEST and the directed matrix-tree theorem in `RESULT.md`. No independent scientific audit has been conducted.
