---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The 4/5 bound follows universally from Rayleigh vector (1,-1) on two nonadjacent cores, (2,-2) on attached private leaves: norm²=10 and total outgoing core transition budget ≤2, giving quotient at least 4/5. Balanced equal multipartite cores with core-edge 3/(5d) and leaf-edge 2/5 have zero core holding; their adjacency eigenvalues d,0,-m reduce P to 2×2 symmetric blocks with all nontrivial eigenvalues in [-4/5,4/5] and an attained 4/5. Equality for K_{p,q} forces Rayleigh eigenvector equality for every same-side pair: leaf weights 2/5, total core weights 3/5, equal crossing weights and hence p=q, with star case impossible by central row budget. Compactness gives strict >4/5 for unequal p,q. Independent rational block spectra tests covered balanced r,m in 2..6, but universal proof is analytic.

## originality

PASS

Earlier October 25 Resultary theorem already proved same 4/5 optimum/complete equality class for vertex-and-edge-transitive cores; the balanced multipartite optimizer is known and NOT new. A November 8 separate theorem gives further pendant rigidity for vertex-/edge-transitive leaf coronas. The surviving exact nontransitive universal lower bound and global all-weights uniqueness/equality iff balanced among arbitrary complete-bipartite (including unbalanced and stars) are not implied by prior transitivity-restricted statements. Earlier standard fastest mixing SDP theory covers methods, not this generalized obstruction. Best-of-knowledge qualified O PASS.

## value

PASS

The 4/5 obstruction is a sharp graph-independent mixing-rate barrier for one-private-leaf extensions of ANY noncomplete connected core, including irregular graphs; the complete-bipartite equality rigidity classifies a fundamental asymmetric family and globally optimizes over nonsymmetric-by-automorphism weights. These are structurally motivated rather than an arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
