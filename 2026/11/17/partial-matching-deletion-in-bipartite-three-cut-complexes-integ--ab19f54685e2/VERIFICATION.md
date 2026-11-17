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

Run `python3 artifacts/verify.py` from the extracted package root. This checker reconstructs the graphs from adjacency, enumerates every disconnected triple and every Alexander-dual face independently of the claimed star decomposition, computes complete mod-two boundary ranks, and tests 65 parameter triples with both exceptional cases. The program also checks the four-cycle span of the link graph in all ordinary cases and identifies the non-four-cycle exceptional link.

The recorded output in `artifacts/verification_output.txt` is reproduced by the same extracted program. These are finite tests over a field, not an integral certificate and not evidence about untested parameters. The universal integral theorem is established by the direct link-cycle surjectivity proof, long exact sequences, fundamental-group argument and Hurewicz–Whitehead steps in `RESULT.md`. No independent audit or validation has been performed.
