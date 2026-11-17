---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Matrix-forest theorem yields partition polynomial q(q+N)(q+a)^(b-1)(q+b)^(a-1) and independent Bernoulli root indicators. Pair a-1 old (q/(q+a),q/(q+b)) Bernoulli factors against new (q/(q+a+1),q/(q+b-1)) factors: degree 0,1,2 coefficients proportional to (ab,qN,q^2) versus ((a+1)(b-1),qN,q^2), so each pair has the asserted likelihood-ratio orientation. Remaining singles decrease strictly. Convolution by independent Poisson-binomial log-concave factors preserves LR order (TP2 Toeplitz kernel); interval-positive support and a strict Bernoulli change give strict all interior tails. Sum of individual means simplifies to printed rational gap. Verified exact LR minors, tails and mean for N<=11 and three positive rational fugacities. Algebraic proof covers all finite N and real q>0.

## originality

PASS

Székely (2004) full four-page primary article and its Jin–Liu input formula enumerate rooted forests with prescribed root locations; they do not compare different bipartitions in LR order. Avena et al. use the known det(qI+L) and fugacity monotonicity on a fixed graph, not graph-shape balancing. General spectral Bernoulli factorization does not give stochastic order when individual parameters move in opposite directions; the complementary pair matching and total positivity argument are additional exact content. No identified previous Resultary result supplies the same comparison.

## value

PASS

Root fugacity q controls cluster count in a natural random-forest measure. The theorem orders the full distribution across all graph bipartitions and all fugacities, determining extremal shapes, not just an isolated moment, and provides a precise constructive comparison despite opposing movements of individual Bernoulli parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
