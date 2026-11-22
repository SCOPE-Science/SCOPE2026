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

# Reproducibility and verification limits

`RESULT.md` supplies a complete analytic argument for the local stability threshold. The exact normalization, pairwise equilibrium, pairwise trace, base determinant, homogeneous trace, and mixed-derivative identity can be rechecked with `python3 CHECK.py`; dependencies are Python 3, SymPy, NumPy and SciPy. Independent numerical trace-zero computations for two rate permutations and three perturbation sizes are included in that checker only as a consistency test.

The proof's implicit-function step requires \(1/2<p<1\), fixed nonzero zero-sum mortality direction, and sufficiently small heterogeneity and triadic mixture. Neither finite calculation nor the checker certifies any larger parameter domain, global dynamics, or absolute publication priority. Independent scientific audit has not been performed.
