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

With Python 3, run `python verification.py`. No third-party library, input corpus, network service, or external executable is required.

The program directly constructs the six-permutation transition matrices for each of the four canonical forbidden trigrams. Exact polynomial determinant expansion and the rank-one determinant update reproduce all four symbolic generating functions; this finite algebraic identity holds for every \(k\ge1\) by the transfer formula. It additionally compares 120 recurrence coefficients and exhaustively tests all 20,439 ternary words at lengths three, six, nine, checking direct subsequence universality and 81 individual forbidden-pattern counts.

The finite enumeration is an independent test, **not** the proof for arbitrary \(k\). The transfer decomposition and determinant identities are the general proof. This verifies only the stated mathematical claim; it is not independent scientific validation or a check for every equivalent result in the literature.
