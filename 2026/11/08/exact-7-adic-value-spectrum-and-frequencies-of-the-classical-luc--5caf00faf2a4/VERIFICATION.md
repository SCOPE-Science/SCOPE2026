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

# Verification protocol and limits

Run `python3 verify_lucas7.py` with the Python 3 standard library. The script computes the classical Lucas recurrence over each proposed full period for moduli \(7,49,343,2401,16807\), compares the actual multiplicity of *every* residue with the exact square-root formula, and checks that no prime-factor quotient of the period works as a shorter period. It also checks \(L_{16}=2207\), \(F_{16}=987\), and \(2205=45\cdot49\).

Observed execution summary: `VERIFY_OK levels=1..5 exact_individual_residues=19607 least_periods=PASS`. The individual represented-residue counts are \(7,37,253,1759,12307\), and the least periods are \(16,112,784,5488,38416\). These are reproducibility checks over finite sets, **not** a proof for arbitrary exponents. The unlimited assertion follows from the stated p-adic exponential/logarithm isometry, the exact quadratic branch change of variable, and residue-root counting as proved in `RESULT.md`.

No independent audit or external formal certification has been performed.
