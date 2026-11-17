---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

On each labelled K_{a,b,c} under simultaneous strict open-neighborhood majority with individual tie retention, a nonuniform shore in a periodic 2-orbit must be frozen: no update can recreate nonuniformity after a strict majority. One reversing shore is impossible. Exactly two reversing shores must be oppositely monochromatic and equal in size t; their fixed third shore of size c with h one-bits gives exactly C(c,h) solutions iff |2h-c|<t. With three reversing shores there is one orbit exactly when the maximal shore size is unique. These disjoint cases establish P_2=1_{unique largest}+sum_{i<j:n_i=n_j} sum_h C(n_k,h)1_{|2h-n_k|<n_i}, counted as UNORIENTED temporal 2-orbits, for every positive a,b,c. Direct independently written bitmask enumeration matched (1,1,1):0, (1,1,2):3, (1,1,4):7, (1,2,3):1, (2,2,3):7 and (2,2,2):6. Finite tests corroborate, not prove the universal classification.

## originality

FAIL

Decisive mathematical coverage: the complete published October 25 exact-periodic-orbit census already gives the identical P_2 formula for ALL positive unequal and equal shore sizes with precisely the same majority/tie convention and labelled unoriented orbits; moreover it computes fixed points and dynamical zeta. A November 1 publication independently repeats the exact same formula and equal-size transition. The November 8 submission offers no remaining novel theorem after removing already published full coverage. The full scientific RESULT.md texts of both earlier results, including proofs, were actually read, not merely retrieved by title.

## value

FAIL

An equality-sensitive primitive-cycle count is naturally motivated and mathematically correct, but the entire desired classification and its significant phase transition had already been established in stronger published results on October 25 and November 1. A third presentation of the same proof and all-parameter formula, without a distinct invariant, structural refinement or new boundary, supplies no independent mathematical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
