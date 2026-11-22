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

The exact-rational standalone diagnostic is `checks/median_hull_exact.py`. It exhaustively enumerates affine break-line intersections for each of 1,500 sampled rational three-dimensional pairs and checks explicit sharp witnesses in dimensions three to seven; output: `TORRICELLI_L1_RIGIDITY_EXACT_CHECK_OK 4510`. It does not exhaust all vector inputs. The proof in `RESULT.md` establishes the bound and rigidity by exact median identities and directional derivatives. The comparator literature and remaining bibliographic risk are identified in `REVIEW.md` and `AUDIT.json`.
