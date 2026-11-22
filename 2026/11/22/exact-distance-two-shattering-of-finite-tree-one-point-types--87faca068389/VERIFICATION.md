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

The general argument is the unique-midpoint lemma plus an exhaustive local classification of possible exact-radius-two traces when parameters share one tree neighbor. This proves the global no-four-shattering bound, the complete criterion for shattered triples, their nonduplicated sum over centers, and the sharp eleven-vertex minimum.

Run `python3 verify.py` to independently enumerate distance-two traces in finite test trees. The program performs 18,889 labelled-tree checks (all Prüfer-code trees of orders three through seven, plus fixed-seed larger samples), validates the claimed triple-count equation, and checks the explicit eleven-vertex witness. Expected output: `VERIFY_OK 18889 trees; eleven-vertex witness and exact triple formula`.

The computation is finite and does not certify the all-order theorem on its own. The all-order conclusion rests on the written proof. There has been no independent proof audit or exhaustive historical-priority audit.
