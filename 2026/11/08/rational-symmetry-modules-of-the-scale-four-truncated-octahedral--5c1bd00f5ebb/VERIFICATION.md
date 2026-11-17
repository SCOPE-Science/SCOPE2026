---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

At inclusive Kendall graph distance 4 on all 24 permutations of four labels, independently enumerated all 17,372 nonempty simplices with face vector (24,228,1112,3042,4848,4592,2592,822,112). Inspected actual exhaustive verify.py: constructs forbidden graph pairs, 8,682 acyclic discrete Morse matches, six critical degree-4 and three critical degree-5 cells, primitive rank-one integer Morse differential (0,1,1,0,-1,1), gradient projection/lift chain maps, all 48 symmetry actions and character decomposition. Independent complete 48-element signed simplicial Lefschetz calculation checked the submitted H4-minus-H5 character on every group element; 10 class pairs agree with S^(2,1,1) tensor 1 plus S^(2,2) tensor epsilon in H4 and (1+sgn) tensor 1 in H5. Together with inspected exact Morse chain model this yields claimed rational modules and one invariant H5 line. Original heavier lift/project calculations were not independently replayed; Lefschetz by itself would not prove the separate module split.

## originality

PASS

Prior full-graph Rips homotopy filtration and mod-two persistence of the same four-letter permutahedron explicitly give the scale-four Betti ranks 5 and 2 but no natural S4 x C2 rational representations. A separate November 8 symmetry result concerns scales two and three and does not cover scale four. The full scale-four representation split appears novel on inspected evidence.

## value

PASS

PASS: The complete 48-element symmetry representations at a canonical mixed 4/5-dimensional graph-Rips stage add structural information beyond already published nonequivariant filtration and characteristic-two barcodes; the natural automorphism decomposition identifies precisely which degree survives rational quotienting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
