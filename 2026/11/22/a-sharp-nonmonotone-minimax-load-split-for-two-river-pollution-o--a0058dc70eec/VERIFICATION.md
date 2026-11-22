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

Run `python3 verify.py` using Python 3 and its standard library. The supplied code computes both exact-rational quadratic maxima with \(z=e^{-kt}\) and checks the proposed optimal allocation and optimum for representative rational separations and 3,000 randomized exact-rational cases. An execution of the bundled file reported `PASS: 16432 exact-rational assertions`.

For a universal mathematical verification, see the complete four-step proof in `RESULT.md`: fixed-site equal responses provide the first sharp lower bound, and strict monotonic tradeoff at two fixed active peaks provides the second. The exact restrictions \(0<q<1\) and \(0\le w\le1\), the boundary \(q=1/3\), and the behavior of both endpoints are proved symbolically. Exhaustive checking of every real parameter was neither performed nor claimed.

Relevant earlier theoretical sources establish model equations, critical-deficit convexity and numerical water-quality allocation formulations. The claimed special global minimax classification has not received independent audit or verified historical priority. The experiment does not provide calibration for field or policy deployment.
