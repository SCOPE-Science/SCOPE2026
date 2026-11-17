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

The theorem is valid for all q>=2,k>=1,h>=1 and positive integer per-position gap-difference intervals. Relabel the permutation so each letter equals the source position modulo q. For each demanded consecutive residue, the first s_i=min(q,b_i-a_i+1) allowed differences contain exactly the allowed residues, each with one minimal representative. These independent minimal steps and the earliest initial phase u_0 give a bijection between distinct infinite-host query strings and tuples (x,d_1,...,d_{h-1}). Their earliest endpoint is x+sum d_i, so the generating polynomial and exact finite cutoff at qk-1 follow. Max endpoint is (q-1)+sum_i(a_i+s_i-1), proving sharp saturation; full alphabet universality further requires all s_i=q. The uniform alternating-binomial identity follows from summing the factored geometric polynomial. h=1 empty-product case checked. An independent combinatorial enumeration of all selected positions on 330 bounded configurations, including nonuniform gaps, matched the polynomial; the unrestricted theorem is proved by the bijection rather than the finite test.

## originality

PASS

No earlier inspected theorem determined distinct interval-gapped query-language coefficients for all repeated permutations and arbitrary position-dependent intervals. Existing studies introduce gap-constrained matching/universality with general complexity classifications, and the exact repeated-permutation *unconstrained* embedding-multiplicity theorem is not an interval-gap count. Best-of-knowledge novelty is the explicit polynomial and sharp saturation, not ordinary permutation-subsequence identities.

## value

PASS

The constrained-subsequence language is a natural object for formal-language matching. Exact distinct-output counts and sharp universality thresholds are useful in restricted periodic hosts where generic gap-constrained decision problems are difficult. The q-ary residue bijection is structural and computes all nonuniform interval profiles, not a renamed textbook counting exercise. Its narrow structured-host scope and elementary proof limit generality but do not remove its mathematical utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
