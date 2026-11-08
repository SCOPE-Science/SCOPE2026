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

# Reproducibility

Run `python3 verify.py` with Python 3.10+ and standard library only. The verifier builds each labelled simple graph by hand from its pair-coordinate adjacency rule, repeatedly applies the literal blue-vertex/unique-white-neighbour forcing rule, and enumerates every initial blue subset for ten graph profiles. It independently implements the proposed structural criterion, coefficients, minimum cardinality, and minimum multiplicity.

A separate direct boundary assertion checks that a 12-blue configuration in `C_5[K_3]` succeeds and is inclusion-minimal, contradicting the earlier value 13 in arXiv:1607.04071v1, Corollary 3.17. The executed check reported `VERIFY_OK profiles=10 candidate_sets=128832 zero_forcing_sets=6962 literal_rule=PASS all_polynomial_coefficients=PASS minimal_counts=PASS`. Its ten parameter profiles are documented in `RESULT.md` and the source. Boundary cases include the complete-base three-cycle, the complete square of the five-cycle, and the smallest clique size. This is bounded computational corroboration; the unrestricted formulas rest on the accompanying proof. No separate human or independent mathematical audit was performed.
