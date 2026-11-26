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

An independent replay (/workspace/review-evidence/3-replay.py, passing the frozen certificate.json path as its sole argument) regenerated each independence complex by enumerating all vertex masks against explicit Hamming-distance-one edges. It recovered 742/785/837/901/981 nonempty faces and verified the 367 pivot pairs, all 2816 Hasse incidences by DFS acyclicity, and exactly one vertex and seven 3-face critical cells. Thus the intact complex has a CW model of seven 3-cells attached to a point. The first fault fills e*L with intersection (∂e)*L; the replay verified all eight strict free coface pairs taking L onto the three-edge matching independence sphere. The attached S³ is the four-edge octahedral sphere. The replay checked its signed integral boundary vanishes and {0,6,11,13} occurs with coefficient one and has no proper coface. Its dual cochain is closed and evaluates to one, yielding a primitive element. Hurewicz for the two-connected wedge and the unimodular change of basis on that wedge show the cofiber removes exactly one sphere (and the natural homology map is split onto). The replay verified the frozen collapse pairs for K₂→K₁, K₃→K₂, K₄→K₃, counts 26, 32, 40, by checking the unique strict coface and exact end complex. The 24 actions realizing S₄ carry a flag A⊆B to the canonical flag of sizes |A|,|B|; translations and coordinate permutations carry the canonical matching to all eight classes. This proves actual relative collapses for the claimed inclusions, including equal sets by the empty sequence. No extension to arbitrary matchings, larger cubes, or equivariant homotopy type is inferred. The supplied checker was inspected, not executed; no field Betti number is used to establish the integral result.

## originality

PASS

The intact wedge, its specific primitive octahedral carriers and generic edge cofibration are all known. The distinct result is the action of the first deletion on integral homology and actual stabilization by relative collapses under all subsequent deletions in the same parity class. No inspected existing result supplies that relative classification.

## value

PASS

This is a natural symmetry orbit of parallel faults on the smallest hypercube supporting these nontrivial octahedral classes. It distinguishes the first deletion from every later inclusion by identifying the exact primitive integral class lost and by showing elementary relative collapses rather than just Betti number stability. These are independently useful facts about the diagram of fault complexes, not further counts of the intact complex.

The dated certificate retains the supplied scientific assessment, sources and limitations.
