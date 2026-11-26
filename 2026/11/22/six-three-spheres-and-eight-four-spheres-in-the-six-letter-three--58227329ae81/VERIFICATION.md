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

Generating both orientations on each three-element support gives 40 permutations. Their distinct ordered subwords form a regular CW complex with simplex face posets and f-vector (6,30,120,247,194,40). Reconstructing the oriented face incidences and applying a separate topological sort verifies the 311 disjoint reversed Hasse edges are acyclic, with critical counts one vertex, six 3-cells and eight 4-cells. Independently computing integer Smith forms of the unreduced boundaries (including checking their composition) gives ranks (5,25,95,146,40) and Betti numbers (1,0,0,6,8,0). Thus the critical 4-to-3 differential has rank zero over Q, hence is zero over Z; this confirms the needed conclusion without relying on the uploaded signed recurrence. In that Morse CW model the 3-skeleton is a wedge of six S³, and the Hurewicz isomorphism makes each vanishing cellular boundary equivalent to a null attaching map. Purity is dimension five, so nonzero lower-degree homology obstructs pure shellability.

## originality

PASS

The supported distinct claim is the specific mixed-dimensional integral wedge and hence nonshellability for this 40-generator ordered-word complex. The strongest same-alphabet examples use different facet sets and give distinct invariants. The indexed general conjugacy-class bound or a theorem on fundamental groups is not a calculation of the two higher-dimensional wedge counts.

## value

PASS

Using the whole three-cycle class selects a natural generator family, rather than arbitrary permutations. The result gives a pure five-dimensional example with lower homology in two different degrees and an actual two-connected integral wedge type. It distinguishes homology, homotopy and shellability for a specific natural complex beyond the general low-connectivity bounds and Euler-characteristic data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
