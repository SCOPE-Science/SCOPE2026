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

A set globally dominates the graph and its complement iff it meets each part. Selecting one singleton from each of s parts forces s distinct complementary-support hub blocks, each with at least r-1 vertices. Marking r-1 vertices per hub and charging remaining nonsingleton vertices gives E=N-classes >= s(r-2)+(r-s)(m-s)/2, valid at s=0 and s=r. For m>=3r-6 the bound is >=r(r-2) for s<=r-2 and s=r, and >=r(r-2)-1/2 for s=r-1, where E integer finishes the argument. The r disjoint minimal hubs attain equality, while m>=3r-4 rules out s<r strictly and forces all hubs minimally supported. Their uniquely omitted parts label the otherwise unordered blocks, giving product falling-factorial bijection. Independently verified threshold inequalities for r=4..49 and product for (8,9,10,11): 120708403200; this arithmetic check is not the proof.

## originality

PASS

Anholcer et al. establish the definitions, multipartite lower-bound hub constructions, exact numbers for at most three parts, and pose a general multipartite conjecture. The separately published complete four-partite formula now covers the submitted GC equality for r=4 (and in broader size ranges), but not r>=5, the large-r rigidity, or enumeration of all maximizers. Those surviving components require the submitted excess inequality and equality analysis. The full original 32-page paper could not be read due access; priority is qualified.

## value

PASS

For every number r>=5 of parts and arbitrary unbalanced sufficiently large sizes, the theorem establishes a matching universal upper bound for an explicit infinite tail of a published conjecture and an exact structural/counting classification of all optimal labeled partitions. Even though four-part GC values are known, general-r rigidity and the product census answer a motivated structural question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
