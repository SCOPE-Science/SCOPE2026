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

# Verification

`verify.py` is a standalone Python 3 script relying only on standard-library integer bit operations and recursion. Run `python3 verify.py` from its directory. It computes the finite compatibility graph from the literal prefix–suffix rule and searches every prefix subset subject only to proved upper-bound and dominance rules. Its separately transposed graph search finds the same optimum.

Expected and verified values by forbidden-overlap cutoff one through seven: `1, 2, 6, 20, 64, 216, 744`. At cutoff seven the forward and transposed searches visited 9,209 and 9,191 nodes, retaining 4,604 and 4,595 memo states. It also verifies that the 24 listed prefixes have exactly 31 compatible suffixes, checks every such pair directly as strings, and compares the optimized computation with a direct all-subsets calculation for cutoffs at most four.

The exhaustive finite check proves only the coefficient 744 at cutoff seven; the published proof's exact middle-word factorization extends it to all blocklengths at least fourteen. This certificate does not prove statements for larger cutoffs or other alphabets. The earlier lower witness was previously published, and historical priority is not independently certified. `verification_output.txt` records a successful local execution; output alone is not a proof without inspecting and running the code.
