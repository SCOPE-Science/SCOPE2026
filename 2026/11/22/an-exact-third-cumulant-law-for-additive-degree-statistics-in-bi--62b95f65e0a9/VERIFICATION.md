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

# Reproducibility and limits

Running `python3 checker.py` in the extracted package performs 195 exact rational finite-graph assertions and reports `PASS: 195 exact rational third-cumulant assertions`. It enumerates all simple labeled graphs through six vertices for seven degree scores and three rational edge probabilities and also checks the total-degree special case through 39 vertices. These assertions are finite consistency checks, not a certification of the infinite-sample theorem.

The proof is analytic: vertex-triple classification, conditioning on shared edges, centered-edge monomials, and convexity of an explicit sparse-limit exponential polynomial. The exact definitions and boundaries are supplied in `RESULT.md`. Independent mathematical validation has not been performed. The sparse sign conclusion does not apply as a finite-size uniqueness assertion.
