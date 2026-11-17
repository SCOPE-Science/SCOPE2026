---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

With exactly three marker ones an Abelian cube contains either zero ones or one in each of its three equal-length blocks. All-zero distinct factors are precisely 0^(3t) up to floor(max gap/3). Every three-one cube includes all marked ones and its literal content is uniquely specified by block length t and start s; the exact three inequalities on one positions yield lambda_t<=s<=upsilon_t and the sum in (1). Double counting by t,start,and one position in each block proves total sum (n-3t+1)t^3 and the rational generating-function term; inclusion-exclusion on four gaps gives the zero-only term. Uniform composition gaps converge to Dirichlet(1,1,1,1), the Lipschitz Riemann-sum limit is H(G), mean 1/270. The ordered uniform-three-point feasible region z<3y,3y-x<2 has volume 7/9 and therefore the zero atom is 2/9. Finite literal factor/continuum grid checks are corroboration, not an infinite proof.

## originality

PASS

Best-of-knowledge new distinct-factor, fixed-Hamming-weight-three Abelian-cube formula and quadratic-scale law. Earlier cube avoidance and average occurrences in unrestricted random words are different theorems/sampling measures, not implications of these exact conditional factor counts.

## value

PASS

Three ones are the first nontrivial fixed weight supporting 3-block Abelian cubes with nonzero markers; an exact factor enumerator, rational aggregate, and nondegenerate limit with rational atom and mean are natural reusable invariants in Abelian stringology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
