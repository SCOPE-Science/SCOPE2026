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

The commutator subgroup is the prime kernel and is fully invariant; for generator images (a^s,a^t b^k) the conjugation relation is s(u^k−u)=0. With s≠0 faithfulness forces k=1; when k=0 the order relation forces t=0. These constraints are sufficient by the presentation. In normalized color c=t/(1−u^k), a nonzero nonunit is (k,c); its product with (l,d) is (kl,c) for kl≠0 mod r and the trivial map otherwise. A unit acts on colors from the left by x↦sx+t/(1−u), and from the right leaves the nonunit unchanged. Thus the nonunit has p−1 commuting units (its color stabilizer), p(gcd(k,r)−1) commuting nonzero nonunits from zero products, and r−gcd(k,r) others of its own color, plus the trivial map. The affine-unit centralizers have p units for a nonzero translation and p−1 for a nonidentity multiplier; only the latter fixes one color and admits r−1 commuting nonunits. This gives all coefficients and the only coincidence, d=1 with the multiplier stratum, since r≥3 and d<r. The identity and trivial map alone have full centralizer. Nonunit image order is r/d, idempotence is k²=k mod r (2^ω(r) residues including zero), and unit conjugacy consists of the affine classes and one orbit per nonzero k, plus the trivial map. The degree-weighted sum counts ordered commuting pairs, with leading p³ for fixed r as asserted. A separate direct enumeration over all generator image pairs in four explicit groups, comparing their actual values on the two generators under composition, matched the full spectrum and color test, including composite and prime-power complements.

## originality

PASS

The supported distinct claim is the composition-centralizer spectrum and the arithmetic commutation rule for the whole endomorphism monoid of this family, with their calculated consequences. The closest primary comparator covers the same group family but a different transformation semigroup. Existing affine automorphism and metacyclic classification results establish part of the ambient structure, not the interaction with nonunits.

## value

PASS

The natural smallest prime-kernel Frobenius family allows the complete composition-commutation invariant, not just unit centralizers or its average, to be read off from divisibility in the complement. The field-color rule shows exactly how changing from a prime to a composite complement changes graph connectivity between color classes; together with the distribution it gives directly usable input for commuting-graph and endomorphism-monoid comparisons. This is a uniform structural result, not a table of small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
