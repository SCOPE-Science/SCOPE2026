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

# Verification and scope

The supplied \(\texttt{verify.py}\) uses only Python's standard library. Running \(\texttt{python verify.py}\) reconstructs the ten complementary triple pairs on a six-set, checks all label-permutation signed determinants, directly forms the oriented fundamental chain of its cross-polytope boundary and verifies all boundary coefficients are zero. It then checks transposition action on this actual chain, global maximality of the separating face for ground sets of sizes six through ten, and the sixth-exterior-power trace identity on selected permutations.

The exact number of six-support cycles for a general ground set is a binomial coefficient; their primitive independence is shown by dual maximal-simplex cocycles in the proof, not inferred from enumeration. The rational spanning assertion uses the published all-parameter Betti theorem in Feng (2026), Section 6, rather than an unprovided full complex computation.

The verification does not establish the absence of torsion in the remaining integral ninth homology, integral homology of quotients, or homology representations outside degree nine. The finite program is a reproducibility check, not an independent audit.
