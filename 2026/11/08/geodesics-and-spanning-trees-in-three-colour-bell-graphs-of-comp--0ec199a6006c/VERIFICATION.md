---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For labelled K_{m,n} with m,n>=3, unlabelled proper partitions into at most 3 blocks have one common root (the bipartition), with every non-root partition splitting exactly one side into two unnamed classes. Restriction/deletion adjacency within one side corresponds to flipping one bit modulo global complement, so its factor is the simple folded cube P_s=Q_s/(x~complement x); cross-branch adjacency is impossible off the root. Thus the Bell graph is P_m∨P_n and has order 2^(m-1)+2^(n-1)-1, unique cut vertex and no Hamilton cycle. The quotient cube is a 2-cover for s>=3: distance between orbits is min(h,s-h), and geodesic count is d!, or 2d! when h=s/2, including geodesics to the root. Cross-factor routes concatenate uniquely at root, giving diameter floor(m/2)+floor(n/2). Even-weight Walsh cube characters descend to P_s, with Laplacian eigenvalues 2j of multiplicity C(s,j) for even j; Kirchhoff gives T_s=2^-(s-1) product_{j>=2 even}(2j)^C(s,j) and tau= T_m T_n. For m=n=3 one gets K4∨K4, 7 vertices, 12 edges and 256 spanning trees.

## originality

PASS

Asgarli–Krehbiel–MacLean earlier recognize one folded-cube factor as the Bell 2-colour graph of an edgeless host and study star cases. This is acknowledged and is not itself new. The actual three-colour Bell graph of a genuine K_{m,n} joins TWO such factors at the common two-class partition, and the exact interbranch geodesic multiplicities, diameter and spanning-tree census are not implied as published statements by that one-factor result. Named 3-colouring reconfiguration graphs differ: they have colour labels and can be Hamiltonian in sizes where the unlabelled Bell graph has a cut vertex.

## value

PASS

A full structural decomposition of a canonical unlabelled recolouring graph, together with all-pairs shortest reconfiguration counts and its exact spanning-tree complexity, is a naturally useful combinatorial classification. Distinguishing its non-Hamiltonian behaviour from named-colour recolouring graphs also resolves a meaningful normalization distinction. These exact invariants go beyond merely renaming one previously known folded cube.

The dated certificate retains the supplied scientific assessment, sources and limitations.
