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

# Verification of the stated theorem

The proof in `RESULT.md` is analytic. The attached script `scripts/check_replicator_corner_law.py` independently differentiates the explicit logit potential, checks the Hamiltonian first integral symbolically, and tests the two-term period and corner time weights by numerical trajectory integration. The exact inverse-branch coarea convolution, integrability of the derivative defects, and weak-measure limit are mathematical arguments, not consequences of finite calculations.

For the example \(F(y)=-1+3.5y-0.5y^2\), \(G(x)=-2+5.2x-0.2x^2\), direct integration with event-based first return reports absolute period errors near \(4.28\times10^{-3}\), \(4.41\times10^{-6}\), and \(3.7\times10^{-9}\) at energies \(10\), \(25\), and \(50\) relative to \(1.25E+7.060638472266\ldots\). The last value approaches the integration tolerance. Measured four-quadrant physical-time fractions at energy \(50\) agree to within \(0.002\) with theoretical limits \((0.4,0.2,4/15,2/15)\).

To reproduce, install dependencies from `requirements.txt` and execute `python scripts/check_replicator_corner_law.py`. Expected terminating marker: `REPLICATOR_CORNER_PERIOD_CHECK_OK`. The finite experiments do not prove the \(E\to\infty\) theorem, rule out earlier mathematics, or provide independent audit.
