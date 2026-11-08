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

# Verification

The proof reconstructs both Rota–Baxter-system equations over an arbitrary field; no characteristic restriction is imposed. A nonzero rank-one image generator must square into its own line. This is either the unit line or a square-zero radical line. All cases are proved necessary and sufficient, including the one-zero cases. The finite-field enumerations count actual ordered linear maps, not tensor representatives or isomorphism classes.

The included standalone `roba_pair_check.py` enumerates **every** map of rank at most one on the specified finite-dimensional algebra, forms every ordered pair, multiplies basis outputs in the original algebra and evaluates **both** defining identities for all ordered basis inputs. Its category counts are then checked against the theorem. In particular, the checker performs no initial restriction to the theorem's normal forms. It uses prime-field arithmetic for orders 2, 3 and 5 and polynomial extension-field arithmetic for order 4.

Replay: `python roba_pair_check.py 2:1 3:1 5:1 2:2 3:2 4:2 2:3`.

Observed total solutions for the seven checks in this order: 14, 37, 113, 90, 565, 2062, 962. The success marker is `ROTA_BAXTER_SYSTEM_RANK_ONE_ORIGINAL_IDENTITIES_OK`. The recorded output is included as `CHECKER_OUTPUT.txt`. All seven checks are exhaustive within the stated finite configurations, but not exhaustive across all fields and all radical dimensions.

Incidence dimensions are established algebraically from irreducible projective-line parameter bases and the ranks of the annihilator vector bundles. The statement deliberately does not infer global irreducible-component information from these locally closed strata.
