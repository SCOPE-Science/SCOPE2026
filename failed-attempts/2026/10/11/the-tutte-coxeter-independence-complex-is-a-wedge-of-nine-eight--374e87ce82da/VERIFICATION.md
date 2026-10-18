---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. The canonical 15-duad/15-syntheme incidence graph of K6 has 30 vertices, 45 edges, girth 8. Independently regenerated all 476,186 nonempty independent faces, the 15-entry face vector and 238,088 stagewise toggle pairs, with precisely one critical vertex and nine critical 8-cells. Exact local recreation /mnt/data/scope08_tutte_recheck.py topologically sorted all 3,461,400 Morse-oriented Hasse covers, not merely trusting VERIFY_OK. Since the acyclic CW complex has no cells between dimensions 1 and 7 and only nine degree-8 cells, all attachments are constant, proving wedge^9 S8 integrally. This does not assert a family theorem.

## originality

FAIL

FAIL: strong earlier coverage by mathematical implication. Regard the synthemes as the 15 hyperedges (perfect matchings) of the 15-duad ground set; the hypergraph independence complex J is precisely the no-perfect-matching complex NPM_6. Linusson–Shareshian–Welker Corollary 1.2 (2004 arXiv, published 2008) gives J≃ wedge^9 S5 for k=3. For the 15-duad Alexander dual J*, combinatorial Alexander duality gives reduced integral H7(J*)=Z9 and no other positive reduced homology. Every triple of deleted duads leaves a perfect matching: K6 has 15 perfect matchings and each duad lies in only 3, so deleting at most three edges hits at most nine matchings. Thus J* contains the full 2-skeleton of the 14-simplex and is simply connected; Hurewicz/Whitehead upgrades its integral homology to J*≃wedge^9 S7. The independence complex of the duad–syntheme incidence graph is homotopy equivalent to ΣJ*: cover it by the simplex on duads and the union of stars of synthemes, both contractible; the intersection is exactly J*, so their union is the suspension homotopy pushout. This proves exactly Ind(T)≃wedge^9 S8 from earlier LSW and standard topology (consistent with Tsukuda 2017 incidence/Alexander-dual theory), regardless of whether the exact numerical special case was separately tabulated. A new exhaustive verifier is valuable corroboration, but the mathematical finding was already implied.

## value

FAIL

FAIL. A correct exhaustive graph certificate for a canonical cage is reproducible and potentially useful as validation, but the asserted exact integral homotopy type is a direct corollary of a published stronger perfect-matching-avoidance theorem plus standard incidence cover and homological duality. It therefore lacks a surviving new motivated invariant or nontrivial gap under the required value standard; the new matching data are verification, not a separate final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
