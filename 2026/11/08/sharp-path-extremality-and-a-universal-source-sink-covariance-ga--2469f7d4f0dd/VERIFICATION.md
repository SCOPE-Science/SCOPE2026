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

# Verification record

The proof reconstructs the exact mixed covariance from degree-local source/sink indicators, then completes squares. For every nonpath tree, the leaf count is at least three. Four or more leaves give a stronger gap than \(13/64\); exactly three leaves force one cubic vertex and give the bound with equality exactly when its three neighbors are of degree two. This derives the global bound without exhaustive enumeration.

The standalone `verify.py` checked exact rational identities on every Prüfer-coded labelled tree through seven vertices. Every orientation was enumerated for each labelled tree through six vertices, independently of the degree formula. Three-armed equality trees were constructed for every order from seven to fifty. Successful invocation: `python3 verify.py` produced `VERIFY_OK 71605 exact assertions; all labelled trees n<=7, orientations n<=6`.

The checker is a finite corroboration, not an infinite proof or an external certificate. Historical novelty is a qualified best-knowledge assessment. Independent mathematical audit has not been performed.
