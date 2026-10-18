---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For the 16-vertex cubic Möbius–Kantor graph GP(8,3), independently reconstructed its full shortest-path metric: 24 edges, diameter four, and eight disjoint distance-four antipodal pairs. Exact inclusive clique enumeration produced face vectors r1=(16,24), r2=(16,72,112,48), r3=(16,112,448,1120,1792,1792,1024,256); independent F₂ ranks give b1(r1)=9, b2(r2)=9,b3(r2)=2,b7(r3)=1. The source proof goes beyond F₂: the two 8-vertex bipartition induced subcomplexes at r2 are S³ (joins of four S⁰), the mixed face complex retracts to either triangle-neighborhood complex D_X,D_Y≃∨9S¹ by a relative vertex-toggle matching, and the two maps into S³ are null since the domains are graphs and S³ is 2-connected; the homotopy pushout is ∨9S²∨2S³. r3 is the join of eight S⁰ giving S⁷; r4 is full simplex. The inspected source verify.py and morse_certificate.json show the intended finite checks; the actual distance enumeration agrees. Since positive-degree homology at successive stages lies in disjoint degrees, all positive-degree persistence maps across thresholds vanish, giving the all-field bars claimed. Correctness PASS, independently of prior coverage.

## originality

FAIL

FAIL: an already-published Resultary/SCOPE source states exactly the same full graph-metric inclusive Vietoris–Rips *homotopy filtration* for the same Möbius–Kantor graph G(8,3), all r≥0, including ∨9S¹, ∨9S²∨2S³, S⁷ and contractibility. I fetched and read its entire RESULT.md (Git blob 577ac1dcff8834c9135c23be8fb57b230438986e); it proves the r=2 wedge by 118 acyclic Morse pairs and zero exact signed Morse boundary. The submitted alternative relative homotopy-pushout proof cannot restore theorem-level originality. Its claimed all-field barcode follows directly and formally because these prior homotopy stages have mutually disjoint positive homology degrees and the degree-zero transitions are graph connectivity. This is a decisive mathematical claim-vs-prior implication, not a shared title or merely matching numerical examples. No chronology beyond current public coverage is invented.

## value

FAIL

FAIL as an independent new scientific claim: the full canonical graph's homotopy-stage sequence has already been published, and the barcodes are elementary functorial consequences of those exact prior stages. Alternate proof style and a restatement of the forced interval list do not establish a remaining motivated unknown exact invariant or structural theorem. The existing original calculation is mathematically interesting, but the submitted content does not add sufficiently independent value beyond the covered result; it is preserved as failed, not superficially repaired.

The dated certificate retains the supplied scientific assessment, sources and limitations.
