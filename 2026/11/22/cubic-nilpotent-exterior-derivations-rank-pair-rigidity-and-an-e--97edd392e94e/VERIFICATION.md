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

The complete proof is contained in `RESULT.md`; the critical arguments are the ordinary characteristic-three restricted-power identity, the explicit small-block exterior modules, the modular tensor products, the extraction of short Jordan multiplicities, and the nilpotent centralizer orbit formula. All apply to arbitrary characteristic-three fields and unrestricted generator dimension.

To replay the direct defining-identity tests, run `python3 verify_exterior3.py` with Python 3 and no external dependencies. It builds the original wedge derivations and independently computes their matrices and ranks over the prime field. It exhausts all generator matrices for dimensions one through three; checks every cubic-zero case; and checks forty canonical Jordan types in dimensions up to eight. Expected marker: `EXTERIOR_CUBIC_JORDAN_VERIFIED`.

The tests do not enumerate every matrix in dimension four or higher, do not test general extension-field coefficients, and do not replace the structural proof. No independent mathematical audit has been performed. Priority remains provisional, including for general modular tensor Jordan-decomposition literature.
