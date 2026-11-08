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

# Verification record

Both checkers use the original incidence-algebra multiplication rule rather than relying exclusively on the closed formulas. They require only a Python 3 standard-library interpreter.

Run `python verify.py` and `python verify_gf4.py` in the directory containing these files. The outputs are stored verbatim in `verification_output.txt` and `verification_gf4_output.txt`. The last expected markers are `LAYERED_INCIDENCE_RADICAL_POWER_CENSUS_PASS` and `LAYERED_INCIDENCE_GF4_EXTENSION_PASS`.

The prime-field checker exhaustively enumerates full radical elements for widths \((1,1,1,1),(2,1,2),(2,2,2),(1,2,1,2)\) over \(\mathbb F_2\) and widths \((1,2,1),(2,1,2)\) over \(\mathbb F_3\). It then enumerates consecutive blocks for three more cases, tests nonconsecutive-block independence on 1,536 reproducible randomly chosen inputs, and verifies the width-two formulas using exact fractions for 50 field/height pairs. In particular, the full \(\mathbb F_2\) radical for widths \((2,2,2)\) yields \(928,2592,576\) elements at ranks \(0,1,2\) of the top power.

The second checker constructs \(\mathbb F_4\) as \(\mathbb F_2[t]/(t^2+t+1)\), carries out elimination using explicit extension-field operations, and exhausts the full radicals for widths \((1,2,1)\) and \((2,1,2)\), together with all consecutive-block assignments for widths \((2,2,2)\). Both characteristic-two and odd-characteristic examples are covered.

The mathematical proof is independent of these finite experiments. The extension-field checker tests the nonprime-field scope, but no finite collection of checks proves the universal theorem. Historical priority is provisional and independent mathematical review has not been performed.
