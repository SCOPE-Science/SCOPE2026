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

Frozen RESULT.md:24 calls the directed condition strictly weaker under n≥1. At n=1, W_1(G) is a group and has just one idempotent, so the two conditions coincide. The complete /workspace/repairs/2/RESULT.md qualifies strictness to n≥2, proves it with two different constant base maps and all identity labels, treats n=1 explicitly, and leaves the polynomial and asymptotic for all n≥1 unchanged. Re-audited the corrected statement: h(f([n]))=A∪T; idempotence is automatic on A, while each x∈T requires an f(x) in the disjoint fiber h⁻¹(x)∩B. Pick those distinguished preimages injectively, then send each remaining B point anywhere in A∪T. Choosing T, the other C and D values, and the ordered partition gives exactly the displayed base multiplicity. On the free G-set, idempotence is equivalent to identity labels on the image of an idempotent base. At a product root in T, solve once for the free g_x as k_{f(x)}⁻¹ without commuting labels, yielding one factor q removal per root, none on A. Thus the displayed coefficient/exponent hold also for nonabelian G. For fixed n each rank-one base pair with a common root has degree 2n−2 in q; any distinct-root rank-one pair loses one degree and higher rank loses at least one. That gives the leading numerator n q^(2n−2) and denominator n² q^(2n−2), with the n=1 ratio identically 1. Supplementary independent replay: python /workspace/audit_checks/02_full_action.py composes the full maps on [n]×G (not the delivered checker's label criterion) and agrees in every rank cell for S3 and C6 at n=1,2,3, totals 1,109,11989. Frozen verification/verify.py and its captured output were inspected, not executed. Neither enumeration certifies the general theorem. Only finite group alphabets are addressed, and n is fixed in the limit.

## originality

PASS

For the corrected claim, novelty is qualified to the unrestricted finite-group ordered three-rank polynomial with the additional directed-product lift constraint, its group-order universality and resulting probability law. The trivial-group polynomial, individual-idempotent count and commuting untwisting are existing work. The n=1 qualification and constant-map witness are boundary facts, not originality claims.

## value

PASS

For the repaired all-n statement, the polynomial gives the three-rank distribution of a natural directed semigroup event not read off from either an unlabeled rank total or a commuting count. It separates a genuine free-action lift obstruction from the base-map constraints, explains why multiplication can be nonabelian while the census depends only on order, and supplies a closed fixed-n probability limit. The n=1 edge repair is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
