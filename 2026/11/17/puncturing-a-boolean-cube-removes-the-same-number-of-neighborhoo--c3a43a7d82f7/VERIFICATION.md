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

The exact independent graph-based finite checker is `artifacts/verify.py`, requiring Python 3.9 or later and no third-party libraries. Run `python3 artifacts/verify.py` from the package root. The attached `artifacts/verification_output.txt` is the recorded stdout and ends with `PUNCTURED_CUBE_NEIGHBORHOOD_INTEGRAL_PROOF_MOD2_CHECK_PASS`.

For \(n=3,4,5,6,7\), the code enumerates both parity components from genuine common-neighbor simplices in the punctured graph. It verifies actual connectedness and computes mod-two first boundary ranks. The observed first Betti number vanishes in both shores; the computed Euler characteristic gives the expected second Betti number under the proved two-dimensional collapse. At dimensions \(3\le n\le6\) the checker additionally replays **every** specified elementary free-face collapse and tests uniqueness of cofaces. At dimension seven the finite collapse is not replayed, but the general proof applies.

The integral homotopy statement is justified by a symbolic simplicial collapse, direct nullhomotopies of all missing triangle boundaries, the nerve theorem, and Hurewicz–Whitehead. Mod-two computational evidence is corroborative only. No independent audit, machine-assisted infinite certification, or claim about multiple graph-vertex deletions is made.
