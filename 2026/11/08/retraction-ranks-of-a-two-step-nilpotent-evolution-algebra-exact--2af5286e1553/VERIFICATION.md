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
# Computational checks and mathematical limits

Run `python verify.py` from the directory containing this file. The standalone script uses Python 3.9 or later and no external libraries.

The test independently iterates matrices for the quotient and extension blocks, checks zero products and square preservation over the finite field, composes the resulting algebra endomorphisms, and retains exactly those that square to themselves. It checks the **complete** labeled endomorphism space, not samples, at \((n,q)=(1,2),(2,2),(3,2),(2,3),(2,4)\). Its rank multiplicities are \((1,1)\), \((1,16,1)\), \((1,192,144,1)\), \((1,54,1)\), and \((1,128,1)\), respectively. A polynomial-basis implementation handles \(\mathbb F_4\). The run prints `VERIFY_OK` after all assertions pass.

The same script evaluates exact rank weights using log-gamma arithmetic and compares them with the moving discrete-Gaussian profile for field sizes \(2,3,4\) and \(n=100,300,1000\). Observed total-variation errors were below \(0.018\) in these cases and decreased with increasing \(n\) in the tested examples. These are numerical consistency checks and not a substitute for the uniform asymptotic argument.

The proof in `RESULT.md` supplies the algebra endomorphism classification, the finite-field count, the rank identification, and the fixed-field asymptotic tails. There is no computer proof, independent mathematical audit, or global publication-priority certification.
