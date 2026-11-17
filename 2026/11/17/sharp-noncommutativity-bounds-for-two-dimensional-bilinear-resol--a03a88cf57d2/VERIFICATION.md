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

# Reproducibility and analytical checks

The stated domain is complex two-dimensional Hermitian matrices with both eigenvalues strictly positive and unequal, with noncommutation. The external moment-completion equivalence used in the proof is Tian's Theorem 4.1, Section 4 of arXiv:2611.03081v1, for precisely this domain.

The exact eigenvalue computation for the rank-one sum can be reconstructed from its trace and determinant. The commutator norm is the magnitude of one off-diagonal entry after diagonalizing the first projection. The global optimization is a one-variable calculus identity whose maximum is attained at overlap \(1/2\), and each equality condition can be checked explicitly.

Run `python3 checker.py` with Python 3 and NumPy. It verifies exact witness relations and evaluates both fixed-ratio regimes on a deterministic mesh of spectra and overlaps. The executable is supplemental verification of finite calculations only: it does not establish the continuous optimum or the existence of the representing positive operator-valued measure. Those facts rest on the provided proof and the cited source respectively.

The source-inspection limits concern older general commutator results, not the algebraic proof. Independent audit and publication-priority certification have not been carried out.
