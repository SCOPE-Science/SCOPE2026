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

The symbolic verifier `verify_symbolic.py` uses exact \(\mathbb F_{625}\) arithmetic with quartic modulus \(t^4-2\). It checks all twenty-eight constructed lines, every ordinary-line square identity, distinctness, invariance under fifth powers, and the exact orbit histogram \(2^2 4^6\), as well as the \(12\)-triple diagonal-normal-form orbit. It prints `VERIFY_OK` on success.

Independently, `verify_f25.py` works in \(\mathbb F_{25}=\mathbb F_5[s]/(s^2-2)\), exhausts all projective line representatives, and algebraically tests whether the restricted quartic is a scalar multiple of a binary quadratic square. It checks \(31\) lines over \(\mathbb F_5\) and \(651\) lines over \(\mathbb F_{25}\), finding exactly \(0\) and \(4\), respectively.

A finite-field enumeration alone is not a proof about all extension degrees; the complete extension-degree result follows from the explicit fifth-power Galois orbits in the symbolic proof. The published projective classification and the classical count of twenty-eight odd theta characteristics are separate mathematical premises. Independent audit was not performed.
