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

The hub-free subcomplex is A=∗ᵢ Ind(P_{mᵢ−2}); at most one spoke can be chosen, and each spoke attaches a cone on the join with only that petal's factor shortened by one endpoint. To see the path recurrence, for a path on n≥3 vertices send vertex n−2 to n, fixing the other vertices. This gives a simplicial retraction on independence complexes contiguous to the identity, since N(n)⊆N(n−2); deleting n−2 leaves P_{n−3} and an edge. The recurrence and the n=0,1,2 bases give the three residue types. In the 2-residue case the shortened factor includes by a homotopy equivalence: the added endpoint has contractible link Ind(P_{3k−2}). With at least two 0-residue petals the base and every spoke link are contractible. With one such petal, the base is contractible, and its two spokes have spherical links S^{K−2}; their maps factor through the contractible base even after the first attachment. With no 0-residue petals the base is S^{K−1}; 1-residue links are contractible. If there are any 2-residue spokes, the first kills the base and the other 2ν₂−1 have null-homotopic attaching maps and add its suspensions. All attachments are along subcomplexes. For triangular petals the shortened factor is the augmented join unit; r≥2 ensures an exceptional spherical link is nonempty. Since K≥2, the noncontractible cases have positive reduced homology in the specified degree. Line 10's u₀ is a notation typo for ν₀, whose meaning is unambiguous from the definition and proof.

## originality

PASS

The equal-petal case and the general qualitative outerplanar conclusion have exact prior coverage and receive no new credit. The supported distinct claim is the full residue interaction for arbitrary petal lengths, including the conditional multiplicities and the sharp mixed contractibility criterion.

## value

PASS

Vertex-gluing cycles of arbitrary lengths is a natural family where the broad outerplanar theorem leaves all numerical invariants undetermined. The mixed theorem identifies a new contractibility boundary through the number of 0-residue petals, and determines the dimension and multiplicity in every other residue pattern, rather than just giving another equal-petal count. The endpoint-inclusion analysis explains the distinction between killing a sphere and adding suspensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
