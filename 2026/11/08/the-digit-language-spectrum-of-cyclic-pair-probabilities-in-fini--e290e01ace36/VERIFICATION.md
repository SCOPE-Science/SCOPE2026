---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For G of abelian p-power order p^n with conjugate partition r_j, |G[p^j]|=p^{s_j}, hence number of order-p^j cyclic subgroups (p^{s_j}−p^{s_{j−1}})/(p^j−p^{j−1}); each cyclic subgroup has p^{2j}−p^{2j−2} generating ordered pairs. Summation gives p^{2n}θ=1+(p+1)Σ_j p^{j−1+s_{j−1}}(p^{r_j}−1). Each summand is a carry-free run of digit p−1 occupying r_j positions; consecutive starts differ by r_j+1. Rank≥2 implies T≡−1 mod p², numerator≡−p mod p², so reduced denominator p^{2n−1} recovers p,n and digit word recovers partition and invariant factors. Sufficiency follows by constructing that group. Independently tested partitions n=2..9 for primes 2,3,5 and direct sample values 17/32,83/243.

## originality

PASS

The 2026 Chatterjee–Das general cyclic-pair probability paper supplies the Dedekind-psi element-order sum and several rational value bounds, not the complete attainable rational language for abelian p-groups. Amiri/Tărnăuceanu establish fixed-order rigidity of element-order sums; that implies injectivity at fixed order and is NOT new. The submitted strict p-adic denominator and carry-free partition-word condition characterize the entire image with initially unknown prime and group order, a stronger and structurally different inverse statement. No exact covering prior theorem found in searched records; best-of-knowledge only.

## value

PASS

The set of attainable exact values of a standard random generation invariant is a natural inverse algebraic problem. The proved iff rational-digit language, injectivity across all primes/orders in a noncyclic p-group family, and constructive recovery are reusable for classifying groups from observable probabilities; not merely fixed-order injectivity or a finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
