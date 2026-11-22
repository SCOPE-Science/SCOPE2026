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

# Reproducible finite checks

Run `python3 verify.py certificate.json` from this directory using a Python 3.10+ standard-library interpreter. The verifier constructs the full graph and every independent face from scratch, and reads the accompanying integer pair certificates. It checks each of 367 base matching pairs and all 2,816 acyclicity incidences; the remaining critical cells are one vertex and seven three-cells. It independently validates the eight elementary collapses of the first-fault residual link onto an octahedral two-sphere, and verifies every one of 26, 32 and 40 relative collapse pairs for later fault stages. It checks a maximum-size tetrahedron witnessing primitive attachment, and directly verifies the generated symmetric action on the four chosen graph edges and all eight equivalent parity classes.

The independent mod-two chain-rank calculations give degree-three Betti numbers `(7,6,6,6,6)` for zero through four faults, with all other reduced Betti numbers zero. They corroborate but do not replace the integral primitive cofiber argument and verified collapse certificates. The proof uses Hurewicz only for the two-connected intact complex established by the complete discrete-Morse matching, and the checked signed octahedral cycle to establish a primitive killed class. No infinite graph family or arbitrary graph-fault class is verified.

The exact expected last verifier line begins `VERIFY_OK_Q4_PARITY_CLASS_EDGE_FAULT_SATURATION`.
