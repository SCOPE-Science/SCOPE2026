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

The frozen RESULT.md specifies the even-weight F2^5 Cayley graph and polyhedral Hom cells. Its five generators have unique nonzero F2 relation (1,1,1,1,1), forcing each closed 5-step walk to use each generator once, giving 16*5!=1920 vertices. Recoloring directions correspond to adjacent generator swaps; only nonadjacent source positions commute. The 2D cubical f-vector (1920,4800,2400), local C5 links, two squares per edge and connectedness from generator swaps and weight-two translations establish a closed surface. The signed incidence propagation in inspected verify.py provides coherent orientation, hence chi=-480 and genus 241. The affine S5 action changes permutation parity, giving the claimed sign orientation representation. An independent combinatorial calculation recovered 1920 walks, 2400 squares, chi and genus. The test alone is not an infinite theorem; this is a finite exact object with exhaustive enumeration specified.

## originality

PASS

Direct Hom(C5,five-regular Clebsch) genus and affine sign representation are not implied by square-free-target Hom theorems or by topology of independence/neighborhood complexes of the same graph. This is qualified priority, not a global novelty proof.

## value

PASS

The folded five-cube is a natural symmetric strongly regular graph; its ordinary pentagon Hom complex is a nontrivial, explicit high-genus orientable graph-coloring manifold with an informative integral orientation character, a structural invariant not a renamed textbook exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
