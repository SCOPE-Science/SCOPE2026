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

For GP(10,2), the exact bitmask recurrence α(M)=min(4,max(α(M\{i}),1+α(M\N[i]))) independently enumerated 12,217 nonempty faces and f=(20,190,1140,3335,4632,2660,240). Independently implemented the stated ordered vertex-matching algorithm: precisely 6,031 disjoint incident pairs, one critical zero-cell and 154 critical 5-cells. Directly formed all 57,940 Hasse covers, reversed matched arrows and topologically sorted all 12,217 faces, proving acyclicity and thus an integral wedge of 154 S5 by Forman (not merely mod-two homology). Independently enumerated all 120 automorphisms using graph isomorphisms and computed the signed fixed-face reduced Lefschetz traces. The eight (cycle type, multiplicity, trace) classes exactly match the source: identity 154; 2^8 1^4: -10 (15); noncentral 2^10:-6 (15), central 2^10:+6 (1); 3^6 1^2:+4 (20); 6^3 2:0 (20); 5^4:-1 (24); 10^2:+1 (24). Their sum is zero; no rational invariant top-homology class.

## originality

PASS

Earlier Kim–Lew defines I_k(G) and proves general bounds; Filakovský treats square-sequence graphs built from C4 attachments, not the girth-five dodecahedron; Carnero Bravo treats different total-cut graph families. Explicit earlier dodecahedral total-three-cut and Heawood fourth-robust homotopy calculations concern different graph/threshold complexes. Nothing inspected implies this exact 154 S5 homotopy and 120-character table.

## value

PASS

A complete integral Morse homotopy and full 120-element rational symmetry character for the classical 20-vertex dodecahedral graph at the first unclassified fourth robustness level is a natural and nontrivial finite topological invariant. The exact acyclic matching and character give reusable structural data beyond a low-cost negative or simple rank calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
