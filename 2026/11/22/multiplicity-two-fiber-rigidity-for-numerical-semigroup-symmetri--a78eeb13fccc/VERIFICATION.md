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

The source uses the original pseudo-Frobenius set and retains the Frobenius row. Removing a original gap positions before the first positive member moves that member from m to m-a. At output multiplicity two exactly one of the m-1 low gaps survives. In an ordinary source that survivor is F, giving T_1. Otherwise F is not a low gap; write u for the unique low gap that is not pseudo-Frobenius. Each m+i for i≠u (1≤i<m) belongs to the source. If m+u belonged too there would be a complete interval of length m starting at m, forcing ordinariness. If u>1, the pseudo-Frobenius gap 1 added to the member m+u-1 forces the missing m+u, a contradiction. With u=1 and m≥3, addition of m and the identity 2m+1=(m+2)+(m-1), with m-1 pseudo-Frobenius, fill [2m,3m-1] and hence the tail. Thus the only nonordinary sources of multiplicity at least three are B_m; directly their PF set is {2,…,m-1,m+1}, so they are almost symmetric and map to T_2. At multiplicity two the least odd member determines T_g and there is no deletion; B_2=T_2. For g≥3 the complementary pairs containing 0,1,2 are distinct and forced, leaving exactly 2^(g-3) sets, of which only T_g occurs. The unrestricted proof is independent of the supplied verify.py/VERIFY_OUTPUT.txt check through F=20 (601 almost symmetric sources, 46 in the slice); the checker was inspected, not executed. RESULT.md Step 2 does not need its aside about a positive small element; the defining ordinary case is no positive member strictly below the conductor.

## originality

PASS

Pass for the full inverse classification on the multiplicity-two target slice, not the definition, output symmetry, standard form of multiplicity-two semigroups, or every individual image example. The strongest matching distinct indexed record gives particular common examples, without the all-source exclusions or higher-genus rigidity. No priority between same-day results is inferred.

## value

PASS

The source paper explicitly asks what the symmetrization can hit. This solves the smallest possible nontrivial target slice over the full source domain: it rules out all nonsemigroup targets of multiplicity two, gives infinite fibers precisely in genera one and two, and yields unique reconstruction above genus two. That structural exclusion, not the routine count of complementary pairs, explains the exponential rarity and the value of the invariant. It makes no claim about targets of higher multiplicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
