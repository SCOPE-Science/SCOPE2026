---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The residue homomorphism sends phi to 3 and gives the displayed sextic up to a nonzero scalar. In the affine chart w=1 the derivative in w requires S=1 or 3, and each nonzero x,y,z has fourth power 1. At infinity S cannot be 0 and scaling to S=1 gives the same fourth-power condition. This exhausts the geometric singularities, not just rational points, and gives the six sign/permutation orbits (6,24,12,8,3,12). Independent exact arithmetic gives local Hessian determinants (1,1,4,4,4,4) modulo 5, 91 F5 points, and F25 chart counts (1510,137,3,1), summing to 1651. Resolving the ordinary nodes adds 65q points over Fq. Crepancy and rationality of the nodes give K²=24 and chi=11; Noether's formula yields Euler characteristic 108, and h¹(O)=0 and duality give b₁=b₃=0 and b₂=106. The two traces are 390 and 2650; purity bounds each squared eigenvalue by magnitude 25 and equality forces every squared eigenvalue to equal 25. The first trace then gives the stated multiplicities and zeta function in the trace-formula convention. This is a statement about eigenvalues, not a claim of semisimplicity or a Néron–Severi calculation.

## originality

FAIL

A distinct earlier Resultary result states the same arithmetic theorem under the same residue specialization. Its polynomial is the negative of the frozen polynomial modulo 5, and it already gives 65 rational ordinary nodes, b₂=106, the identical eigenvalue multiplicities, all extension counts and the identical zeta function. The frozen point counts and smooth count are immediate specializations and subtraction. Using elementary derivatives instead of a Gröbner certificate for node exhaustion does not make the frozen arithmetic finding original.

## value

FAIL

Determining the zeta function of this ramified fiber would be a worthwhile exact arithmetic invariant if not already known. Here the entire invariant and maximality theorem are already available, as is the full node claim. The alternative local verification is useful corroboration but does not supply a distinct scientific finding at the stated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
