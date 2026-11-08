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

# Reproducible verification

The proof in `RESULT.md` establishes the exact girth classification for every integer base and nonnegative shift.

Run `python3 verify.py`; it checks forest/first-cycle thresholds for 1,071 parameter pairs with bases 2 through 15, including explicit simple-cycle witnesses. Run `python3 verify_girth.py`; a separate breadth-first-search implementation computes the girth of the graph from the first three edge weights across 82 small parameter pairs and compares all three regimes. Both should terminate with `*_OK` output.

These computations inspect finite three-weight subgraphs and do not prove that omitted higher weights create no additional cycles. That critical infinite step is established by the maximum-edge and residue-class arguments in the symbolic proof. The equivalence to Abelian maximal pattern complexity relies on the published incidence-forest theorem. Independent external audit has not been performed.
