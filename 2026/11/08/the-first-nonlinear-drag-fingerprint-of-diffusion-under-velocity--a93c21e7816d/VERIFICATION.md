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

# Reproduction and limits

Run `python3 VERIFY.py` with Python 3. The script uses only `fractions` and `itertools` from the standard library and checks stationary linear moments, two independently derived formulas for linear diffusivity, the exact cubic Poisson-resolvent identity, the derivative with respect to cubic drag at zero, the no-reset first-cycle response, and rational large-rate limits for a fixed grid of parameter choices. It also reproduces the two factorial contributions that sum to the analytic coefficient. Printed PASS counts refer only to finite identity checks.

The complete finite-drag asymptotic statement is established by the coupling and Green–Kubo proof in `RESULT.md`: first-reset resolvent, exponential-age expansions, a resolvent difference of order \(r^{-6}\), and exact assembly of the \(r^{-5}\) term. Finite arithmetic does not certify the infinite-rate theorem or publication priority. The analysis assumes a stationary symmetric telegraph sign that persists across velocity resets, a compact invariant velocity region, and fixed positive \(\lambda\) and \(\Sigma\).
