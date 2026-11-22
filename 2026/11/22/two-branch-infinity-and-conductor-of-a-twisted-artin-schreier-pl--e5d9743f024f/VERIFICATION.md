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

# Verification of the plane-model boundary theorem

The proof is in `RESULT.md` and the exact standalone check is in `verify_plane_model.py`. Run `python3 verify_plane_model.py` in the directory containing the files. The checker has no external dependencies and prints `ALL_EXACT_CHECKS_OK` on success.

Its ten parameter-pair checks verify the initial local tangent monomial, the branch valuation and gcd conditions, numerical-semigroup gap counts (exhaustively for smaller degrees), contact order, conductors and genus identities. In the examples \((p,n)=(3,2),(5,2)\), it obtains cusp pairs \((16,19)\) and \((72,77)\), respectively, with total delta invariants \(151\) and \(2770\). The Newton polygon, Hensel branch count, complete tame semigroup statement and conductor formula are proved uniformly in `RESULT.md`; finite tests do not exhaust all primes or degrees.

The initiating paper's smooth-projective genus, maximality and automorphism claims are used as known context and are not independently certified here. Only correctness, originality and value of the new embedded-geometry statement underwent the recorded self-review. Independent audit has not been performed.
