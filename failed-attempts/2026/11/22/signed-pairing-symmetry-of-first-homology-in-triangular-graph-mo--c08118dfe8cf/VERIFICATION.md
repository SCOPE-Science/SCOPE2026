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

FAIL

The central integral isomorphism and Pieri decomposition are correct. A simple root path contains any given disjoint pair and third root edge, leaving only clique faces and isolated extra 1-cells. The relative complex is free in degree 1 and the pair sequence gives the signed lattice integrally. The five S4 character values are 3, 1, -1, 0, -1, as for (3,1); Pieri gives interlacing with (3,1), including small n. However, Finding line 26 uses the pointwise stabilizer of an orbit, whereas the true formula (Proof line 72) uses the stabilizer of ONE matching in the orbit. For Q=S5 there is one orbit and its pointwise stabilizer is trivial: a permutation fixing every matching preserves every four-element support and thus fixes every label. The frozen wording then predicts invariant rank one, but a matching has an orientation-reversing stabilizer element and the rank is zero. The distinction matters and is not fixed by passing finite tests.

## originality

FAIL

No explicit prior statement of the new-looking signed lattice was located, but it is a mechanical corollary of two exact prior theorems. The first identifies all higher faces with those of the clique subcomplex, with exactly the disjoint-pair edges added; the second gives connectedness and H1=0 for that subcomplex. Naturality identifies absolute H1 canonically with the sole relative chain group, with the usual oriented edge signs. Induction and Pieri mechanically read off the additional claims; there is no extension or new topological assertion to establish. This is an implication finding, not an assertion that either paper printed the module formula.

## value

FAIL

The signed integral invariant is natural and more informative than Betti numbers, but here the already-determined complex adds only 1-cells and the old H1 vanishes. The full action is forced directly by the oriented basis of those cells, and the decomposition is a textbook Pieri multiplication. Correcting the orbit-stabilizer wording would not leave a distinct nonmechanical invariant to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
