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

The statement was checked by reconstructing the Hermite normal form of all finite-colength \(k[[x]]\)-sublattices in \(k[[x]]\oplus k[[x]]y\), imposing the exact \(y\)-stability condition, and comparing the resulting contact classification against the generating function. The odd valuation of \(x^{2d+1}\) is essential to the all-characteristic bound.

The independent finite-check program is `verify_contact.py`, executed with `python3 verify_contact.py`. It printed `FINITE_FIELD_STABILITY_AND_SERIES_TEST_OK 48`. It enumerates residues for selected higher cusps over \(\mathbb F_2\) and \(\mathbb F_3\), checks their stability equations, and compares coefficients through colength 21. The finite calculation cannot establish the unrestricted theorem.

The all-field motivic assertion concerns reduced locally closed strata; it does not assert that the representing Hilbert schemes are reduced. In the related fat-branch identity the arbitrary-germ extension is a dependency on Corollary 6.8 of Huang--Jiang--Oblomkov, not proved anew. The earlier unrefined formula is used as a consistency check. Historical-priority uncertainty remains concerning extraction from older semigroup ideal classifications.
