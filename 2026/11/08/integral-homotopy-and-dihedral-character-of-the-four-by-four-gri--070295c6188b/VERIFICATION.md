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

PASS. Independent full enumeration of 1820 vertex quadruples finds 405 independent four-sets, 60,723 nonempty complement-of-independent-four faces with reported f-vector. Reconstructed pivot matching from inspected source yields 30,319 disjoint pairs; the full 469,288 oriented cover relations admit a topological ordering of every face, leaving one critical vertex and 84 critical 8-cells. Forman thus gives integral homotopy wedge of 84 S8, not merely Betti ranks. Signed fixed-face Lefschetz numbers over all faces for e,r,r2,r3,s,rs,r2s,r3s were independently checked to be (84,0,4,0,-10,-10,-10,-10), agreeing with determinant-sign times the three-subsets-of-nine-squares fixed-point counts. As reduced homology is in degree8 only, these equal the rational character, so Q[D4]-module equivalence follows; no integral module equivalence claimed. /mnt/data/scope03_independent_check_20261108.py replayed enumeration, acyclicity and character.

## originality

PASS

PASS only for homotopy wedge and rational dihedral character; the numerical beta8=84 was already published by Bayer et al (arXiv:2209.13503 Table 3) and is **excluded** from the originality claim. Other relevant grid theorems at cut threshold 2 or 3, and Resultary total-three-cut 4x4 (wedge 36 S10), concern different complexes; none directly implies the global discrete-Morse 4-cut collapse or its full rational character. Residual possible unindexed higher-cut equivariant results.

## value

PASS

PASS. For this natural smallest 4x4 grid in the high-threshold total-cut problem, a published table already gave beta8=84, but an explicit full integral homotopy (as opposed to field homology) and complete dihedral representation are finer structural invariants. The rational orientation twist of the 84 triples of unit squares gives a geometrically interpretable symmetry refinement; neither is a trivial duplicate of the published numeric rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
