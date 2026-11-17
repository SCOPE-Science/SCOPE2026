---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

PASS. For every nonempty finite loopless simple H, in B(K1 vee H) the two rim-sheet full simplices P0,P1 lie in connected Z=Ind(B(H)); the two new hub cones attach along these contractible bases and are homotopically inessential, while the hub-hub edge joins two points of the connected rim-cover complex and adds precisely one S1. This gives Ind(B(H^+)) ~= Ind(B(H)) vee S1. For wheel rim Cn (n>=5), its Kronecker cover is C_(2n) if n odd or two disjoint Cn if even; known cycle independence sphere homotopy gives z,d with d>=2. Carnero Bravo's general three-residue Mycielskian join/suspension theorem, with the special ell=0 cone case, yields all displayed wedge ranks and dimensions. The extra oriented hub edge is the integral H1 generator since Z has H1=0; sheet swap reverses it and rim dihedral maps preserve it. Verified source definitions and finite verifier logic (75 labeled small graphs, 5 wheel covers, six Mycielskians), but mod-two experiments are not infinite/integral proof.

## originality

PASS

PASS best-of-knowledge. Carnero Bravo arXiv:2601.13432 states a general Mycielskian homotopy decomposition for arbitrary graphs but does not explicitly compute the wheel's Kronecker cover/added S1/deck sign in the inspected family examples. Antolín Camarena–Carnero Bravo treat cycle products (rim input), Goyal–Shukla–Singh complete graphs. An unindexed general cone-cover splitting may be known and would weaken the novel contribution; no explicit dominating formula located in read primary results and Resultary.

## value

PASS

PASS. Wheel graphs are a canonical nonbipartite family and generalized Mycielskians form a standard graph construction; the transferable cone-Kronecker-cover splitting supplies an explicit all-wheel, all-layer homotopy classification, mixed sphere dimensions and a nontrivial natural deck action on H1. These are structural facts not mechanically tabulated from the general theorem without the additional cone-cover analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
