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

The standalone command `python3 verify.py` completed successfully with output `VERIFY_OK cyclic_necklaces= 209 brute_lengths=1..14 partition_lengths=1..25`. It builds all binary input and output rotation classes on rings of sizes 1–14 and independently counts predecessor orbits. It also exhausts all integer partitions of every ring length 1–25 and compares their optimal necklace degrees with the closed formulas. This finite confirmation does not prove the all-length theorem; the proof uses the gap model, Burnside's lemma, and integer-break inequalities. Independent audit is not yet performed.
