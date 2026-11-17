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

# Reproduction and scope

Execute `python3 verify_affine_quotient.py` using Python 3.9 or later, from a directory containing the extracted script. The program uses only the standard library and fully reconstructs the defining graph and open-neighborhood complex. The recorded exact output is `verification_output.txt`; the success marker is `PALEY17_AFFINE_3LOCAL_QUOTIENT_PASS`.

It checks the complete face vector, graph symmetry, 136 group images per representative, orientation-reversal annihilation for coefficient localization at three, exact integer chain compositions, modular ranks in every degree, the explicit 4-by-9 boundary and an exact determinant-12 minor. Signed Lefschetz traces on all 136 automorphisms independently check vanishing rational invariants. Rank and determinant data plus the topological transfer lemma give the infinite-group statement about homology of the finite quotient: none of the finite checks alone is being confused with an infinite-family proof.

**Limits:** No unlocalized integral homology at the primes two or seventeen is claimed. No homotopy classification is claimed. This is a reproducible same-model calculation; independent mathematical audit has not been performed.
