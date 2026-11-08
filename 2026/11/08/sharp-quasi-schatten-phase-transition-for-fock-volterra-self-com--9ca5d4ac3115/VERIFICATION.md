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

# Verification and boundaries

The core calculation starts from the exactly normalized Fock monomials \(e_n=z^n/\sqrt{n!}\). The coefficient identities were derived by direct integration, adjoint multiplication and cancellation, with the boundary indices \(n=0\) and \(n=1\) checked explicitly. The formula for \(\operatorname{Tr}(C_g)\) uses absolute summability of the three nonzero diagonals and an exact finite telescoping identity. The two-sided singular-value bounds use the standard three-term singular-value inequality and a concrete compression to index pairs \(3k\) and \(3k+1\). The infinite sign multiplicities use disjoint test pairs and the min--max principle for compact self-adjoint operators.

The standalone `checker.py` uses only Python standard-library modules and was run directly with `python3 checker.py`, producing `EXACT_FOCK_VOLTERRA_COMMUTATOR_OK 21010`. Its finite checks consist of 1,050 independent comparisons with the directly multiplied matrix coefficients and 19,960 rational identities for partial traces and squared off-diagonal magnitudes. Finite tests do not certify claims about all indices or all complex coefficients. The analytic proof supplies those quantifiers.

The motivating source was first published online October 21, 2026, despite the source journal volume being dated 2027. The closest primary article was read in full via its accessible HTML; its Proposition 2.6 establishes compactness rather than the current sharp spectrum and Schatten results. Independent mathematical review and publication-priority certification have not been performed.
