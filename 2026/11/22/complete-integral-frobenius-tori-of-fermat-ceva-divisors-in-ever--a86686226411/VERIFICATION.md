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

# Mathematical verification and limitations

The proof in `RESULT.md` constructs an explicit Galois-invariant spanning tree. This is the infinite structural argument for the integral lattice identity and cannot be replaced by a numerical test.

To replay the independent finite consistency tests packaged with the proof, execute `python3 verifier.py` with Python 3 and the standard library only. Its deterministic output is supplied in `verifier_output.txt`. The script reconstructs full branch-incidence graphs, contracts the prescribed forest, adds the two fixed edges, checks the resulting spanning tree and its Frobenius stability, verifies chord and cycle-basis permutations, and checks Frobenius orbit counts from exact gcd formulas in 128 admissible degree-and-field pairs. It then directly counts projective points over nine prime fields and 24 prime-power extension configurations, using the original defining polynomial, to compare against the known normalization point-count expression.

The final observed marker is `ALL_FERMAT_CEVA_TORUS_AND_ZETA_CHECKS_OK`. The direct finite-field enumerations corroborate implementation and edge cases; they do not certify the result for all \(n\) or fields. The published all-twist normalization point-count identity is treated as prior work, not as the novel claim. The maximal torus quotient, not the complete group-scheme structure of the possibly nonsplit unipotent radical, is classified. No external mathematical audit has been performed.
