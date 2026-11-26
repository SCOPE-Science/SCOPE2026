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

A rooted c-cycle with c≤d has equality pattern exactly congruence mod c and an arbitrary c-letter color word; all iterates are distinct when c>d. This gives T and forces one short cycle per necklace, even for imprimitive colorings, because visible cycle length and rooted word are independent data. Every long vertex realizes just one new type, so at least q^(d+1) long vertices are needed. The balanced de Bruijn graph is strongly connected (append the destination word), so an Euler circuit supplies exactly that budget and is longer than d. At equality, each long vertex is canonically labeled by its window, and the successor map in those labels is precisely a matching of incoming to outgoing arcs at every state. Conversely color an arc by its first letter: overlap recovers all d+1 letters, and excluding permutation cycles of length at most d ensures distinct iterates. On a forbidden arc cycle of length ℓ≤d, two coincident states would give the same length-ℓ rotations of the periodic word and hence identical arc labels, a contradiction. Thus all forbidden events are simple state cycles; distinct ones sharing an arc cannot simultaneously be cycles of a permutation, and arc-disjoint ones prescribe disjoint matching pairs. This gives the factorial weights. Unique window labels fix the long part pointwise, and each short necklace permits exactly c/π rotations; orbit–stabilizer proves the labeled census. An independent small calculation enumerated simple graph cycles by DFS from the least state in each cycle, giving 2,3,5,8 forbidden cycles at binary depths 1–4 and weighted totals 1,3,40,7749. For q=3,d=1, forbidding the one loop-to-itself pair leaves 3!−2!=4 choices at each of three states. The two cyclic color words 0001 and 0111 exhaust the eight binary triples exactly once between them, confirming the depth-two multi-cycle example.

## originality

PASS

Forward profiles, de Bruijn Euler tours, circuit partitions and Burnside counting are prior ingredients. The distinct result is the forced short-cycle budget together with the characterization and exact exclusion census of all optimal long parts; the sources inspected do not give that result or a dominating case.

## value

PASS

The minimum-size universal test structure is a natural question once forward profiles are fixed. The count of profiles alone does not solve it, since short colored necklaces can consume multiple vertices for repeated rooted words. The forced partition, complete optimizer parametrization and effective isomorphism/labeled census add structural information that a single de Bruijn example cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
