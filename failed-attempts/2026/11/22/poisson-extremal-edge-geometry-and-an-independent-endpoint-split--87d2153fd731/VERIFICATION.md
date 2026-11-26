---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The contracted weighted Laplacian cofactor gives the forest inclusion probability n^(-k) times the product of component sizes, including the spanning-forest and empty-forest cases. In bounded opposite corners there are O(n) candidate edges and maximum candidate degree O(sqrt(n)). The number of ordered k-tuples with a shared endpoint is O_k(n^(k-1/2)); their inclusion probabilities are O_k(n^(-k)), or zero for cycles. Matchings have exact inclusion probability (2/n)^k, so Riemann counting and factorial moments give independent Poisson counts, with local first moments providing vague tightness. A limit minimizer exists and is unique almost surely, has density 2 exp(-(x+y)^2), and sum/ratio coordinates have Jacobian equal to the sum. Triangle truncation and the vanishing empty-triangle probability justify using the argmin, and D_n is the minimizing coordinate sum minus 1/sqrt(n); the tie-breaking and axis boundaries do not affect the limit. The frozen Prüfer code and 906 recorded assertions were inspected but not re-executed and are not needed for this analytic proof.

## originality

FAIL

The distinct indexed result 9c51476f4360 proves a stronger full induced-subgraph total-variation comparison with G(m,2/n), valid in particular for m=O(sqrt(n)). The assigned opposite-corner PPP is a projection and independent-Bernoulli limit of that comparison, and its endpoint law is the usual minimizer of the projected limit. This is demonstrated stronger coverage, not a date-based claim about priority or a match inferred from the same limiting density.

## value

FAIL

The maximal span is a natural statistic, but this finding as a separate contribution is a straightforward application of the already indexed stronger graph approximation. Relabelling and edge restriction transfer all required process control, and the PPP minimizer uses only a triangle area and a change of variables. No distinct surviving claimed invariant or estimate requires repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
