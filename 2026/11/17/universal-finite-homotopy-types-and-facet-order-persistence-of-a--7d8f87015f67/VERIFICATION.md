---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The construction places a single binary chip at each chain origin and one at each target in first facet. Every auxiliary chain is degree-one and fires at its unique predetermined round t. For every t, each target receives at most one chip and its firing set is exactly F_t, while auxiliary vertices p_(j,v,t) with j>t fire once. Thus sigma_t=F_t ∪ {p_(j,v,t):j>t}; all auxiliary vertices belong to a unique generating simplex and are dominated by an anchor in F_t. Deleting them gives compatible stagewise strong collapses to every K_r; homology persistence is natural over any ring. The ten listed RP2 triangles give the integer Smith diagonal [1]^9,2 and H1=Z/2; node/chip counts 142 and 30 match formula. Domain: nonempty finite K, arbitrary facet order, parallel sink-excluded firing, binary initial data. Independent small examples checked; not a proof by enumeration.

## originality

PASS

The motivating 2026 sandpile-homology paper defines the same firing complex and explicitly asks about arbitrary wedge realizations and integral torsion; known path, cycle, bidirected-star, and four-chip torus results are special cases, not arbitrary facet-list realizations. The present tree construction realizes every nonempty finite simplicial complex and every chosen order of facets stagewise, with an integral RP2 example. This is a best-of-knowledge, not certified exhaustive, priority decision.

## value

PASS

Universal realizability of arbitrary finite simplicial homotopy types (including integral torsion) within rooted tree sandpiles directly resolves a previously posed existence question and gives a usable stagewise persistence construction. This is a structural theorem and algorithmic witness, not a renamed textbook homotopy calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
