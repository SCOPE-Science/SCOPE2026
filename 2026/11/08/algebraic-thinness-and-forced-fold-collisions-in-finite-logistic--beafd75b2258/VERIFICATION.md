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

For 0<alpha<beta<=4 and finite equality-invariant S, if f_alpha is injective on S then both proportional maps permute S, giving S=(beta/alpha)S, impossible for a nonzero finite set; hence two distinct complementary points are forced by f_alpha(u)-f_alpha(v)=alpha(u-v)(1-u-v). Equality-invariance and S != {0} supply an interior point z, whose separately finite forward orbits satisfy two preperiodicity equations within N iterates. Removing endpoint factors z and (1-z) yields Q_{m,n}; specialization alpha=2 and nonzero leading-beta coefficient show each resultant is a nonzero bivariate polynomial. Summing degree bounds yields B_N candidate z roots and B_N partner values per z; countable union of proper algebraic loci proves null/meagre parameter-pair exceptional set and countable vertical sections. Independent Sympy checked all nine nonzero resultants for N=2, plus exact witness alpha=3/2, beta=3, S={1/3,2/3}. The all-N nonzero proof is analytic, not inferred from the finite check.

## originality

PASS

Best-of-knowledge new all-cardinality algebraic thinness and vertical-finiteness obstruction for finite equality-invariant sets under a pair of distinct logistic maps. Earlier primary work supplies explicit finite constructions but no comparable uniform generic-nonexistence theorem in the material read.

## value

PASS

The theorem answers a motivated global structural question: despite explicit finite toss-and-catch sets, nearly every pair of distinct logistic parameters has no nontrivial finite equality-invariant set. Constructive algebraic certificates for each size and finite fibers of fixed-alpha partner values give a useful exact rarity obstruction, rather than a tiny-instance type check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
