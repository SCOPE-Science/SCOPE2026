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

Contracting the n-c bridges of a connected unicyclic graph gives T_G=x^(n-c)(y+x+...+x^(c-1)); at fixed order the cycle length can also be read from T_G(1,1). An independent census over labelled edge sets, canonically quotiented and using the subset-rank definition of the actual Tutte polynomial, gives 1,2,5,13 unlabelled classes and only the two listed ties, at n=6. Structurally, cycle length 3 at n=6 allows attachment-size patterns (3,0,0), (2,1,0) and (1,1,1) with 4,2,1 rooted-tree possibilities, respectively. Only the attached fork and the chain-plus-leaf repeat a degree profile. For c=4 the two extra vertices give a single chain, two leaves at one vertex, or one leaf at each of two vertices either adjacent or opposite; only the latter pair ties. The other cycle lengths at n=6 give one graph each. Nomizu's theorem identifies the dimensions with those of the graph CE complex (which is defined over Q and extends to the real invariant complex). Exact rational elimination in an independent implementation confirms every differential rank and Betti entry in the four vectors, including the total ranks 1280/1320 and 1280/1316 and the splits 76/75 and 76/77 at degree three. The replay also checks d squared on all 4096 basis monomials per graph, Poincare duality and Euler characteristic.

## originality

PASS

The supported contribution is the paired finite classification with complete Betti data, in particular the two exact separations of total rational Betti rank at the first size. The four-cycle pair already occurs in a distinct prior record. Its twin status and the use of the CE model, support decomposition, or a formula for b3 are not separately original contributions. The inspected broader results do not supply the higher Betti entries or totals of the two pairs.

## value

PASS

Degree sequence and the Tutte polynomial are natural joint graph descriptors. The exact totals show that even the total rational cohomology is not fixed by the joint invariants, a stronger information-loss statement than finding a difference at one degree. The complete pairs at the first possible order give concrete counterexamples and exact benchmark profiles for broader formulas, not simply new names for the known four-cycle pair or a substitution into a low-degree formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
