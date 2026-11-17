---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The original algebra has genuine automorphisms phi(t)=ut+vt^2+wt^3, u!=0; therefore phi(t^2)=u^2t^2+2uvt^3 and phi(t^3)=u^3t^3. The local orbit equations split into x_1!=0 (solve v,w), x_1=0,x_2!=0 (force c square and, in characteristic 2, e=0 and f=u^3), and x_1=x_2=0 (force f cube). This proves necessary/sufficient lower-triangular forms for arbitrary fields, including imperfect ones; in odd finite q the diagonal square/cube image sizes give q^3(q-1)^3/(2 gcd(3,q-1)), and in even q they give q^2(q-1)^2. A nontrivial local but nongenuine example exists outside F_2. Direct orbit-definition enumeration for F_2 and F_3 and inspected independent F_4/F_5 checker support boundary groups; arbitrary-field proof does not depend on finite enumeration.

## originality

PASS

Arbitrary-field local automorphisms of the three-dimensional null-filiform associative algebra: best-of-knowledge comparison of exact mathematical statements and their logical implications found no dominating prior result for the specified original parameter range. Previously published general and overlapping special-case results are explicitly credited. Novelty is not inferred from an unsuccessful search; see named comparisons and residual access risks.

## value

PASS

The exact pointwise-local-to-global classification over every field records a real characteristic-two rigidity boundary, genuinely distinct from the previously known characteristic-zero triangular normal form. Square/cube residue groups and a unique F_2 local-to-global field are natural algebraic invariants potentially useful when extending local-automorphism rigidity over finite and imperfect fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
