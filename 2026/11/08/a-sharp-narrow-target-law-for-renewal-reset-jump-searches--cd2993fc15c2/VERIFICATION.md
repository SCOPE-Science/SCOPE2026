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

# Verification notes

The proof's critical inputs are boundedness of each convolution density, independence of jump displacements and competing clock pairs across events, a geometric excursion count and \(\mathbb E\min(T_d,T_s)<\infty\) for the finite-mean claims. The pairwise Bonferroni correction has the explicit bound \((2\varepsilon\|f\|_\infty)^2p^2/q^2\), uniform over the number of jumps. The geometric-series remainder in `checker.py` bounds truncated numeric sums; reported decimals are diagnostic, not claimed exact constants.

Running `python3 checker.py` from the extracted package succeeds. The script uses only the Python standard library and checks the single-visit/double-visit bounds at four target radii, a bounded Gaussian convolution tail, and four Pareto clock exponent regimes. The analytical infinite-event and small-target limits are reconstructed in `RESULT.md`; finite checks cannot certify them independently. The limiting capture-time law needs finite expected cycle duration. No independent audit or external certification was performed.
