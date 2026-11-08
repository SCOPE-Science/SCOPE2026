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

# Reproduction

With Python 3, run `python verify_cycle.py cycle_witness.json` in the directory containing the two files. The independent enumerator reconstructs all 15 and 42 cycles of the two small graphs. It checks the 3-point and 4-point static witnesses, all 31 internal nodes and 32 leaves of the depth-five adaptive tree, each leaf's realizability, and the lack of 4-point shattering in the 9-edge boundary case. The expected final output begins `CYCLE_K3_B_SHATTERING_VERIFIED`.

The unbounded-parameter upper bounds are mathematical rather than finite-experiment claims. The lower bounds for all larger right sides follow by embedding the fixed witnessed configurations. Historical coverage beyond accessible indexed material is unresolved. Independent audit remains unperformed.
