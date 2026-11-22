---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Every allowed partition has 2, 3 or 4 blocks and any comparable chain has distinct block counts; hence no nontrivial automorphism can exchange vertices of a setwise fixed simplex, proving |Δ(P)|^g = |Δ(P^g)| exactly. There are 4140 set partitions, 378 even-block proper vertices, 1995 comparable pairs and 1890 three-term chains. Every nonidentity D8 permutation has cycle type (8),(4,4),(2,2,2,2) or (1,1,2,2,2), with multiplicities 4,2,5,4. Independently regenerated all vertices and full chain complex and greedily found all requested free-edge/triangle elementary collapses for representatives: 0/2/90/42 collapses and remaining connected graph ranks 0/0/16/0, respectively; no residual triangles. This independent collapse algorithm did not reuse the provided collapse ordering; the provided finite certificate and its verifier were also inspected. S8 relabeling conjugacy reduces the fifteen cases to those four. These are exact finite exhaustions, with no claim for larger n.

## originality

PASS

Hanlon 1981 computes fixed-point partitions in the ordinary unrestricted partition lattice. Wachs 1996 analyzes 2-divisible partition shellability and a full Sn top homology basis/character, but does not specify geometric fixed-space homotopy types of the restricted eight-label fixed subposets; Lefschetz traces do not force collapsibility or a circle-wedge type. Arone–Brantner 2021 concerns the *full* partition complex rather than restricting to all-even blocks, and fixed spaces can change under deletion. No exact 16-circle fixed-space table found in Resultary beyond the assigned self-indexed record. The older restricted-partition literature remains a priority risk, not proof of coverage.

## value

PASS

The natural first two-dimensional 2-divisible partition order complex admits a complete element-fixed homotopy classification, not merely its homology character. Five particular involutions have 16 independent 1-cycles while the other ten fixed spaces collapse to points; the distinction is geometrically surprising and fully certified by replayable finite elementary collapses. A complete exact classification of this canonical small case is mathematically motivated without needing a conjectural all-n extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
