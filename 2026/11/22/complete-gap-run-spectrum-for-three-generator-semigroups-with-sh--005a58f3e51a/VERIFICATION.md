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

The gcd is one and the three generators are distinct and minimal since a+5<2a. For m≥2, the explicit D_m fixed-summand offsets follow from D_{m+1}=D_m∪(3+D_m)∪(5+D_m), with m=2 and the first nonempty central interval at m=3 checked directly. For rows m≤k+3, 5(m−2)<2a rules out every representation with at most m−2 summands; later rows are full because the second offset set covers 1,2,4,7. Each row starts with ma∈S, so missing intervals cannot join. In rows 2…k the duplicate singleton at m=2 is counted once; row k has a tail only for r≥2. Counting singletons for k≥2 gives 4k+2·1_{r≠1}+1_{r∈{2,3,4}}, and the usual doubletons in rows 1…k+1 gain exactly one at r=3. The initial tails decrease by 5, with the terminal length 3 in row k only at r=4. Direct endpoint checks at a=8 give (B_1,B_2)=(7,3) and only long length 7, and at a=9 give (7,2) and long lengths 3 and 8. Independent shortest-path Apéry computation through the exact conductor (python3 /workspace/branches/449e0ad0-5943-41f6-ba70-695bc066e6c4/independent_apery_check.py; saved check-8-1000.txt) agreed on all 993 semigroups a=8…1000 and 499,479 length slots. The run was bounded corroboration; the offset proof establishes the full quantifier. The uploaded checker was not run.

## originality

PASS

The exact invariant is the multiplicity distribution of all maximal missing runs, not residue frequencies of individual gaps, genus, Frobenius number, or only singleton incidence. The strongest matching run-spectrum record in Resultary has a different affine triple and a different law. The inspected general methods recover membership case by case but do not evaluate this all-a histogram or its short-run transitions. No exact prior implication was found in the closely compared sources.

## value

PASS

This is a complete spacing invariant for an infinite family of genuinely three-generated numerical semigroups. It separates a uniform multiplicity-one arithmetic progression of long gaps from a five-class correction for the short gaps. That distinction is not encoded by genus or conductor; the full formula answers which deserts occur and how often, including the many short ones.

The dated certificate retains the supplied scientific assessment, sources and limitations.
