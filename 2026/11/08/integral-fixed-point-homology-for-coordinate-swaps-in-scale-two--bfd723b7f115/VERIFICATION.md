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

PASS. The fixed points in a simplicial realization are modeled by barycenters of vertex orbits, not only individually fixed vertices. With m=n-2, the A_z,B_z,C_z orbit compatibility table is reconstructed from Hamming distances: within A/B d<=2, across A-B only z=w, C-A or C-B d<=1, and no distinct C pair. The A/B subcomplex is two ordinary VR(Q_m;2) copies connected by 2^m edges, with free H_1 of rank 2^m-1. Each C_z link is two simplices joined by m+1 cross edges, homotopy-equivalent to a wedge of m circles. Their cone attachments give relative H_2=Z^(m*2^m), and the integral connecting map is the differences of cube-neighbor cross-edge generators: since the m-cube graph is connected, it surjects onto H_1 of rank 2^m-1. Kernel is free Z^((m-1)*2^m+1), H_3=Z^(2*c_m), others vanish. Van Kampen normal generation gives pi_1=0. The n=2 orbit model is a 2-simplex. The code's n=2..7 mod-2 checks corroborate only finite Betti ranks; no torsion or universal theorem is inferred from them. The Adamaszek–Adams ambient sphere theorem is used for the two base layers.

## originality

PASS

PASS (best-of-knowledge). Adamaszek–Adams gives ambient VR hypercube sphere types and multiplicities, Bendersky–Elia–Grbić ordinary ambient cohomological information, and Galetto–Montaño–Wellner an ambient rational homology representation. None of the checked statements implies integral geometric fixed-locus H_2, H_3, torsion-freeness or fundamental group. Fixed-point Euler/Lefschetz traces are weaker than these invariants. Related indexed Čech and constant-weight Rips results concern different complexes. Unindexed equivalent calculation remains a risk.

## value

PASS

PASS. A coordinate transposition is an elementary generator of hypercube symmetry; its geometric fixed locus includes barycenters of swapped vertex pairs and is a natural invariant not determined by ordinary or rational equivariant ambient homology. The explicit torsion-free H_2 rank and simple connectivity for every n, despite ambient reduced homology concentrated in degree 3, is a reusable structural equivariant-topology calculation, not a trivial parameter specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
