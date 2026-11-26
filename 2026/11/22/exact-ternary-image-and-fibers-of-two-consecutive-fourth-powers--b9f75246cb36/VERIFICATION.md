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

Centering with t=2x+1 gives 8G=t^4+6t²+1. For t≡±1 mod 3 the target is 1 mod 3 and the derivative is a unit, giving exactly one root per class at every finite level and full 3-adic coverage of that output ball. On t=3s the normalized displacement is H(s)^2, with H(s)=sR(s) and R(s) the Hensel square root of 1+(3/2)s² congruent to 1. Factoring R(s)^2−R(u)^2 shows H(s)−H(u) is s−u times a factor congruent to 1 modulo 3; hence H induces a bijection at each precision and on the inverse limit. The singular outputs are c+27H(s)^2/4, disjoint from the first ball. For k≤2 the singular branch contains 3^(k−1) inputs and one output. For k≥3 there are nine lifts from each square root modulo 3^(k−3) to s modulo 3^(k−1), including the modulus-one case k=3. At j>0 a zero square has 3^floor(j/2) roots; an even positive or zero valuation 2a<j with square unit part has 2·3^a, and other targets have none. Summing the image by attained valuations gives Q_3 and the limit 1/3+(3/8)/27=25/72. Independent finite replay compared each target for k=1…9, confirming counts 2,4,10,29,85,254,760,2279,6835 and all fiber sizes; the all-k argument is analytic, not inferred from this check.

## originality

PASS

The inspected works do not determine this combination of centered even quartic with coefficient 6, the prime three, and target-by-target lift counts. Credit is for the exact singular image and finite fibers together with smooth-branch coverage, not Hensel's lemma, finite-field counts or the square-root formula by themselves. The check is bounded; relevant abstract-only sources are not used to assert whole-paper noncoverage.

## value

PASS

For a natural sum of consecutive powers the singular class is genuinely different from the two smooth classes. Its square obstruction and lift factor solve the congruence and determine the multiplicity of every solution at every precision, beyond selected finite counts or an image-density estimate. This survives the corrected scaling and provides a reusable complete local invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
