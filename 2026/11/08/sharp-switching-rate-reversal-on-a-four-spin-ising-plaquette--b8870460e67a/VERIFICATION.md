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

Run the supplied `verify.py` with Python 3. It constructs the exact rational generators of the four spin orbits and, independently, the full 16-spin-configuration times two-reservoir system. It computes stationary probabilities via exact fraction Gaussian elimination, verifies agreement with the closed energy formula, checks the factored derivative at multiple rational parameters, and checks the constant-term sign boundary. On the packaged copy the output was:

`PASS: 34 exact rational assertions; quotient/full generators and derivative`

The universal root count follows instead from the signed coefficients and Descartes' theorem in `RESULT.md`, with the open domain \(\gamma>0\) and threshold \(w=6\) treated explicitly. Endpoint asymptotics are deduced by implicit differentiation and dominant balance, not by finite extrapolation. The package does not claim formal proof-assistant certification or an independent scientific audit.
