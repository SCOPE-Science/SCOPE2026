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

For the nonabelian projection, factor images commute. Each proper image of an S3 input factor is abelian (the proper quotients are trivial or C2), and every C2 factor has abelian image. Thus an onto projection requires one full S3 image, whose centralizer kills every other projected factor. That one map is an automorphism, with six choices. Abelianization gives independent sign and central bits. Given a target S3 sequence its source is unique; the remaining affine central equation is solved by P(sigma). Its dual is Laurent multiplication (up to reversing the indexing convention), injective exactly for nonzero P and surjective exactly for monomials. For an onto F, the central subgroup is preserved and maps onto itself, and the quotient is alpha composed with the shift by k. Compact-group addition and the scalar Laurent entropy result apply: the scalar interval has endpoints min(0,min supp P) and max(0,max supp P); the quotient contributes |k| log 6 by taking a power eliminating alpha. If P=0, finite local surjectivity holds exactly when Q can vary a sign independently of the one S3 input fixed by the output; this means a nonzero coefficient outside k. Counting all parameter choices gives the three rule totals, including no false positives at r=1. On 0,...,r−1 there are 2^d polynomials of degree d, precisely one monomial per degree, and 6^k2^d=3^k2^(k+d) separates all entropy pairs. Independent permutation-table enumeration gives 64 one-factor endomorphisms and 168 locally onto two-site maps; 144 satisfy the proved global criterion and 96 the unit criterion. Replay: python3 /workspace/branches/independent_reproduction.py 5.

## originality

PASS

The distinctive result is the joint all-neighborhood classification and exact census of global, reversible, locally onto and one-sided entropy fibers for S3×C2. General linear entropy/addition formulas, S3 classification alone and image-graph methodology are not new. The closest sources inspected do not give this joint census. The cited 2024 paper's exact tables could not be checked; no exclusion of their coverage is inferred from failure to retrieve them.

## value

PASS

The hexagon group is a natural small nonabelian product alphabet for which onto local maps and onto global dynamics genuinely differ. The full support-size census quantifies this distinction and the decay of the reversible fraction, and the one-sided classification gives explicit level sizes rather than a rule-by-rule algorithm. These exact joint counts can benchmark general image-graph/entropy procedures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
