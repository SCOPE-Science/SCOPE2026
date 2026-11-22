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

# Exact verification and limitations

Compile `verify_binary_four.cpp` with a standard C++17 compiler using `-O3`, run without input arguments and compare the resulting text with `output_binary_four.txt` (the number of memo states is deterministic for this implementation). The program performs two exhaustive dynamic programs: a Held–Karp overlap maximum for each input mask and a memoized, tie-complete minimum-compression Greedy recurrence on canonical endpoint-pair multisets. It enumerates all nonempty subsets up to the four-element reversal/complement group; the computed orbit count is checked against 16959.

The computed global maximum is exactly \(17/11\); the only four labeled maximizing masks are `1343`, `5431`, `60584`, and `64672`. The input associated with the first mask is displayed in the result document. The program explicitly reconstructs a length-17 legal maximum-overlap Greedy history and a length-11 common superstring, and independently runs direct string-based Greedy recursion for this input. Its final assertion checks both the optimum and the complete equality orbit.

The complete all-subset claim uses the published Greedy endpoint-overlap invariant for equal-length substring-free input. The verifier does not formalize this independently of the mathematical proof; its independent literal-word recursion validates the sharp example. The work is not an independently audited or formally certified theorem.
