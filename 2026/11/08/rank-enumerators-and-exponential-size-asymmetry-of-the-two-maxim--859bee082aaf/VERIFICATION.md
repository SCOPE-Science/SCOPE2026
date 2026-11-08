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

Run `python3 verify_regular.py` with Python 3.10 or later (standard library only). The program enumerates all \(4m^{2m}\) equivalence-preserving transformations for \(m=2,3,4\), computes rank and whether the image is confined to one equivalence class, and compares the observed distributions with independent Stirling-number calculations of all four enumerator polynomials. For \(m=2,3\), a second method directly searches all preserving maps \(g\) for the equation \(fgf=f\), checking the regularity criterion independently. It prints the rank distributions and a final `VERIFICATION_OK`. Full expected stdout is in `verification_output.txt`.

Checks are finite, not a substitute for the all-size proof. The convergence argument is symbolic and uses a standard concentration inequality. The code does not exhaustively check inverses for \(m=4\), but does enumerate all maps at that size and verify every polynomial coefficient. No independent mathematical audit has been performed.
