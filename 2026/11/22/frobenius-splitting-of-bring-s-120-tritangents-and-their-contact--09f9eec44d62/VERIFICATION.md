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

# Exact verification and limits

Run `python3 verify_bring.py` with SymPy available. `verification_output.txt` records its exact output. The code checks the identities for the cubic roots, non-stall fifth-degree coordinate polynomial, and all six Frobenius root/quadratic swap types. It confirms all 120 geometric plane labels and 60 stall labels have uniform \(d\)-cycles and all 120 non-stall labels have uniform \(\operatorname{lcm}(d,e)\)-cycles. It performs additional finite characteristic tests, including projective-plane distinctness for fields \(\mathbb F_{43},\mathbb F_{59},\mathbb F_{97},\mathbb F_{131},\mathbb F_{227}\) and actual tangency contact calculations when the five coordinates are rational.

The uniform theorem for **all** characteristic-at-least-eleven finite fields relies on the proof in RESULT.md, not solely on finite test output. Characteristic seven and below, twists, and complete curve zeta functions are not evaluated. No independent validation has occurred.
