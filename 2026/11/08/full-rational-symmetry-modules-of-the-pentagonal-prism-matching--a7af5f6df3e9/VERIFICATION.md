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

# Reproducible verification

From a directory containing the enclosed files, execute `python3 verify.py` with SymPy installed. The program constructs the 15 graph edges and enumerates every disjoint-edge subset. It forms augmented signed simplicial boundaries, checks that consecutive boundaries compose to zero, and computes full rational ranks without relying on finite-field ranks for the unrestricted complex.

For each of the three canonical involutions, it constructs signed eigenspace chain bases and computes modular lower bounds on the eigen-boundary ranks. Because each pair of lower bounds sums to the *exact* rational rank of the full boundary, the bounds are proven exact over the rationals. All 20 group elements undergo complete signed chain-equivariance and reduced Lefschetz checks.

The program was executed on the enclosed source; `verification_output.txt` is its stdout. Terminal result: `PENTAGONAL_PRISM_MATCHING_REPRESENTATIONS_EXACT_PASS`.

This verifies the finite chain calculation subject to the correctness of the explicitly provided algorithms and standard integer/rational linear-algebra operations. It does not determine integral homology or equivariant homotopy type, independently audit the proof, or certify worldwide novelty.
