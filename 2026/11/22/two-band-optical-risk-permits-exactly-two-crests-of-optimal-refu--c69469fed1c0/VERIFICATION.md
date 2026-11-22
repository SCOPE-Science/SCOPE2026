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

# Reproducibility and verification

The theorem and all limiting assertions are proved in `RESULT.md` by positivity of the depth Hessian, the implicit-function theorem, strict monotonicity of the scaled depth, the sign pattern of an exponential polynomial, and Rolle's theorem. The three turns are isolated by the rational intervals \((0,1/10)\), \((1/10,1/2)\), and \((1/2,1)\), with no numerical root-count assumption.

For supplementary finite numerical checks, run `python3 verify_two_band.py` in the directory containing this file and the standalone checker; Python's standard library suffices. A deterministic execution returned `PASS: 32145 supplementary assertions` and these critical triples \((y,k,z)\): approximately \((0.056957651754755,0.185150520028520,0.307628905098304)\), \((0.243623046943661,1.289371124425487,0.188947186987931)\), and \((0.999997870855995,3.591113515890582,0.278464567168660)\).

These finite floating-point tests support transcription of formulas and example values but are not proofs of completeness, strict real inequalities, exact comparisons, or global behavior; the proof in `RESULT.md` supplies those. No independent scientific or external audit was performed. The physical model is schematic and makes no predictions about a specific species or habitat.
