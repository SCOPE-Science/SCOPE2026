---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The mean return from y is |y-x|/a by the one-sided first hitting law of a Brownian motion with constant drift toward x; only that conditional mean enters the regeneration. Subtracting the stopped exit-potential identity from the renewal equation gives p times the mean time difference as the expected alarm contribution |y-x|/a+f(x)-f(y). Since f(z)=z(L-z)/(2D), its strict interior chord bound is |f(y)-f(x)|<(L/(2D))*|y-x| for y!=x. The killed alarm law has positive density, so every positive rate is strictly worse at A<=2, including equality. In dimensionless units the success probability is S/sinh(k), S=sinh(k*u)+sinh(k*(1-u)); integrating the killed Green kernel on either side uses integral_0^u (u-y)*sinh(k*y) dy=(sinh(k*u)-k*u)/k^2 and its reflected version, giving the stated exploratory and return terms. The derivatives at u=0 of these normalized terms are tanh(k/2)/k and (1-k/sinh(k))/A respectively. Their difference from the baseline slope 1/2 tends to 1/A-1/2, so for A>2 one first takes a large finite k, and only then a positive sufficiently small u. The derivative at zero rate is the r=0 Green integral of the same alarm bracket (divide the renewal identity by r and use p->1); independently integrating its two polynomial pieces gives 117623/800000000 at the witness. The independent replay `python3 /workspace/branches/brownian_review_check.py` bounds the mean strictly between 0.00439269746548251 and 0.00439269746548252 by exact rational odd-power sinh series bounds, below 0.00495. The witness calculation is not a substitute for the analytic all-rate threshold proof.

## originality

PASS

Best of current knowledge: the all-rate existential threshold A=2 and the finite-rate reversal with positive initial slope in this specific bounded return-inactive model are distinct. Chen–Tang–Li already solve the identical mean-time model and report rapid-return finite-rate optima; no novelty is assigned to the model, renewal decomposition, or all-rate mean formula.

## value

PASS

The exact drift-speed threshold answers whether any rate is worth trying in an existing model, and separates an all-rate strict obstruction from the weak-reset cutoff of 4. The constructive near-boundary argument and a certified failure of the local diagnostic make the distinction useful. The result is existential in position and rate, not an optimizer formula for every position.

The dated certificate retains the supplied scientific assessment, sources and limitations.
