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

# Verification of the exact delay-stability staircase

Execute `python CHECK.py` with NumPy and SymPy. The checker reconstructs the model's positive equilibrium and exact coefficients using rational arithmetic; verifies that \(\omega_+\omega_-=\gamma\) and that the imaginary characteristic equation and crossing derivative hold for both frequencies in four parameter cases; checks the integer staircase; and computes the winding number of the characteristic function along a positively oriented rectangle containing all potentially unstable zeros at seven delays.

Recorded successful execution:

`VERIFY_OK exact_family=1 frequencies=8 crossing_signs=8 staircase_sizes=4 argument_principle_cases=7`

For the family at \(r=1\), the checked delays \(0.5,1.2,7.5,7.95,8.1,8.25,15.0\) give respectively \(0,2,2,0,0,2,2\) right-half-plane roots. The analytic proof, rather than finite tests, establishes the results for all real delays and all positive parameters satisfying the theorem's hypotheses. This is not an independent scientific audit.
