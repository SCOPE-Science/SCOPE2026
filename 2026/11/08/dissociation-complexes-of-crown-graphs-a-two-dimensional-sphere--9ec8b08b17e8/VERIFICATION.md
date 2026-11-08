---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the crown-graph dissociation theorem

Run `python3 verify.py` (Python 3.8+; standard library only). The script constructs the crown graph from its specified missing matching and tests every vertex mask independently of the theorem's face classification. It independently checks all candidate subsets and their one-vertex extensions for maximality, verifies both exact polynomials, and computes simplicial mod-two boundary ranks.

Actual run completed with `VERIFY_OK orders=3..8 subsets=87360 face_enumerator=PASS facet_enumerator=PASS all_feasible_sets=PASS homology_mod2_n3..8=PASS`. For each order \(3\le n\le8\), all \(2^{2n}\) subsets were examined, not sampled. For \(n=3,4,5,6,7,8\), all simplicial boundary columns were constructed directly from enumerated faces and their ranks reduced over \(\mathbb F_2\).

The proof's integral wedge decomposition is independent of computation: it uses an explicit simplicial deformation retract and a homotopy pushout of contractible complexes. Computations do not certify infinite claims, integral torsion, absence of prior work, or independent review. No such stronger computational conclusion is asserted.
