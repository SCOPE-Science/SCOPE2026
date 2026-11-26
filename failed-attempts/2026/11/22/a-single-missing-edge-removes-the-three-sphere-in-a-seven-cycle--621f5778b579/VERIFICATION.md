---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A separate include/exclude enumeration and recomputation using the published vertex orders reproduced face counts 5282, 5647, 365 (including the empty faces), Morse pair counts 2638, 2821, 181, full acyclicity, and the critical-cell dimensions. The three projected integral 4→3 coefficients in X are zero. This determines the intact wedge because the 3-skeleton is S³ and the integral degree classifies its 4-cell attaching maps. The faulted and link models have one vertex and only 4-cells or one 2-cell, respectively. The new faces are exactly the union of the two ends of e with each face of the link. The resulting cofiber is the double suspension of the link, hence S⁴. The integral cofiber sequence forces a surjective Z→Z connecting map and an isomorphism on H₄. By Hurewicz in the 3-connected target this identifies the inclusion as the claimed wedge projection, and the 42-edge automorphism orbit supplies the universal edge statement. VERIFICATION.md and verify.py were inspected, not executed; the independent enumeration, directed Hasse test and signed projection supply the finite replay. Further, the prior results imply the same claim by a different proof, as detailed below.

## originality

FAIL

The exact faulted type and relative map follow mechanically from the earlier star-cluster decomposition and edge-deletion cofibration plus the already known integral intact type. Here is the decisive implication, which is stronger than noting shared ingredients. Fix v=(0,0), and let K=st(v)∩SC(v), with SC(v) the union of the stars of its four neighbors w; put L_w=st(v)∩st(w). Antolín Camarena–Carnero Bravo Lemmas 21 and 18 identify each L_w with I(G_{3,3})≃S² (open and closed neighborhood unions agree for adjacent v,w; their Eq. (1) gives h(0,3)=1). In the notation of their Theorem 23 proof, K=A∪B, the unions of the two L_w on either side of v. Within each side the intersection is contractible by Lemma 21, and the proof of Theorem 23 at r=2 gives A∩B a wedge of 2-spheres, in particular H̃₁(A∩B)=0. Two applications of Mayer–Vietoris show that the four inclusion-induced H̃₂(L_w) classes generate H̃₂(K). The star and star cluster are contractible and cover I(G), by the triangle-free star-cluster construction. The natural Mayer–Vietoris boundary identifies H̃₃(I(G)) with H̃₂(K), which is Z by the published intact type. The stabilizer of v is transitive on its four neighbors (cycle reflection and permutation of the other two colors), so each of the four generator images in Z has the same absolute value. Since they generate, that value is 1. Applied naturally to the two cones v*L_w and w*L_w, the same Mayer–Vietoris boundary identifies the map H̃₃(ΣL_w)→H̃₃(I(G)) with H̃₂(L_w)→H̃₂(K). Thus the attaching map in Adamaszek Proposition 3.4 has degree ±1 onto the sole intact 3-sphere: the intact complex is 2-connected, so Hurewicz detects this S³ map. Its homotopy cofiber is the three intact S⁴ summands; the inclusion is their wedge projection, and the quotient is Σ²L_w with connecting degree ±1. This uses explicit earlier decomposition and intersection statements, ordinary exactness and symmetry; no faulted complex enumeration or new attaching computation is required. The earlier sources do not need to name the exact deleted graph in a headline for this implication to hold.

## value

FAIL

An exact integral inclusion for a natural one-edge perturbation would be useful if it filled an unresolved gap. Here that precise invariant, including the primitive attachment, is already mechanically obtainable from the earlier star-cluster and cofiber calculations by exactness and stabilizer symmetry. The correct finite certificate provides corroboration but does not fill a remaining mathematical gap in the frozen claim. No genuinely new surviving claim or repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
