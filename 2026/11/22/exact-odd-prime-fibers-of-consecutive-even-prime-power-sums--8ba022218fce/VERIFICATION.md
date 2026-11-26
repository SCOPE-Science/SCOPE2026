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

For d=2p^s, v_p(binomial(d,j)) is at least s-v_p(j). On x=a+pu the linear term divided by p^(s+1) reduces to 2(2a+1)u; j-v_p(j)≥2 for every j≥2, including at p=3. For a≠−1/2 the normalized polynomial is a unit linear map plus p times an integral polynomial, hence a surjective isometry by contraction. Reflection x↦−1−x identifies the two branches in each regular pair, and the reduction 2(x+1/2)^2+1/2 separates all different pairs from each other and the critical class. In the central coordinate x=−1/2+pu, only even powers occur, the quadratic coefficient is exactly A p^(s+2), and the higher coefficients have an extra p after factoring that term. For U integral, the square root g of 1+pU congruent to 1 satisfies (g(u)−g(v))/p=(U(u)−U(v))/(g(u)+g(v)), so u↦ug(u) is identity plus p times a 1-Lipschitz map and is a bijective isometry. At k≤s+1 each pair of classes has 2p^(k−1) inputs and the central class p^(k−1); above that, regular outputs have 2p^s inputs and each central root modulo p^(k−s−2) lifts p^(s+1) times, including at k=s+2. Square-shell counts give Q_p and square-shell measure p/(2(p+1)); the regular and scaled-square measures add to the claimed p^(1−s)/(2(p+1)).

## originality

PASS

The inspected comparisons cover unrestricted sums, finite-field value questions, or different explicitly classified p-adic polynomials. The distinct supported content is the full branch and fiber classification for the consecutive line at the ramified exponents 2p^s, uniformly over every odd prime and depth. Hensel and square counting are standard, not credited as new. This is a best-of-current-evidence judgment, not a proof of priority.

## value

PASS

Restricting a modular representation problem to consecutive inputs removes the usual independent-variable sumset structure. The exact two lifting depths identify which targets remain attainable, give their full multiplicities (not just image size modulo p), and quantify how the critical branch contributes to the measure. Uniformity in the ramified exponent and at p=3 makes the classification useful beyond a worked finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
