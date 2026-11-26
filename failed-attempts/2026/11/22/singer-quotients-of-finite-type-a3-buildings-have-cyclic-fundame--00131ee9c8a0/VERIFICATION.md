---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

If a nonscalar a fixes a subspace of dimension j, then that subspace is a vector space over F_q(a), forcing [F_q(a):F_q] to divide gcd(4,j). Only j=2 permits degree 2, and the fixed two-spaces are then exactly the F_(q^2)-lines, in one orbit, all with stabilizer H=F_(q^2)^*/F_q^*. No nontrivial stabilizer of a positive-dimensional simplex is possible because its vertices have distinct types and it includes a 1- or 3-space. There are (q^2+1)(q^2+q+1) two-spaces, leaving q free orbits after removing the spread orbit. Direct flags counts give q^2+q+1 orbits for each of the three edge types and (q+1)(q^2+q+1) triangle orbits. Independently, Euler averaging over the type-preserving action gives chi=[1+q^6+q(q^2+1)]/[(q+1)(q^2+1)]=q^3-q^2+1: the identity contributes the building Euler characteristic and the q nonidentity elements in H each contribute the discrete spread. The simply connected building and Armstrong's ordinary orbit-space theorem give pi1=G_q/H, cyclic of order q^2+1 with no coprimality needed. H1 is its abelianization; H2 is the free top cellular kernel, with rank chi-1. I inspected verify_singer_building.py and VERIFICATION.md without running the script. Its recorded ranks and integral Smith factors at q=2,3 check the homology cases, not the nonabelian fundamental group or the quantifier over all fields.

## originality

FAIL

The central invariant package is covered by the explicit scope and outputs of the earlier published general Singer-subgroup classification, 321e74dc927b. Vector dimension four and the full projective Singer group are included. The earlier stated outputs, the fundamental group and all rational Betti numbers for that very quotient, determine all the present integral groups because the quotient is two-dimensional. The cell-vector addendum is standard flag counting from spread isotropy and does not supply a distinct substantive remainder. This decision credits affirmative coverage of the quotient and invariants, not a retrieval failure or a title match.

## value

FAIL

The quotient is natural and the formula correct, but the submitted fundamental group and homology do not constitute an additional invariant beyond the earlier all-Singer-subgroup classification. In dimension two all the extra integral information is forced by the fundamental group, rational ranks, and freeness of top homology. The orbit-cell supplement is routine spread and flag arithmetic from the same geometry. No new attaching-map, integral module or other independently needed unresolved invariant is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
