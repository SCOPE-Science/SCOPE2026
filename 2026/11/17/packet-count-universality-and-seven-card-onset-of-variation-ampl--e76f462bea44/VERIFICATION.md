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

# Verification procedure

Run `python check.py` in the directory containing these files, using Python 3 and only its standard library.

The exact-rational checker independently evaluates the binomial-count formula for every prefix step through nine sites and separately enumerates each inverse binary label word, verifying the exact coefficients and the first amplification at seven sites. It also checks direct two- and three-packet enumeration for small decks, the exact composition identity \(T_{n,2}^2=T_{n,4}\) through five sites, and weighted two-packet probability mass and packet bounds. The intended final status is `ALL_INVERSE_RIFFLE_VARIATION_CERTIFICATES_PASS`.

The checker verifies **finite tests only**. The general packet-count limit, its Hoeffding error estimate, sharp all-dimensional upper bound and noncommuting limits rely on the analytical proof in `RESULT.md`. No numerical test is treated as a proof of these infinite assertions.

The scientific priority comparison remains provisional because some historical dynamical-systems literature was accessible only through summaries. No independent mathematical audit has been performed.
