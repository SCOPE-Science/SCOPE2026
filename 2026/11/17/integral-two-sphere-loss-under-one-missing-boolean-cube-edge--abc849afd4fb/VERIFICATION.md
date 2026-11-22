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

For n>=3, parity sheets retain the halved-cube 1-skeleton; exactly one generating n-simplex facet is trimmed. The >=3-face unique-center property allows explicit descending free-face collapses to a 2-complex, and deleted central triangles are replaced by three-triangle disks with the same boundaries, preserving pi1=0. Exact f-vector and Euler characteristic give lambda_n=2^(n-3)(n^2-5n+8)-n+1. The pair K=K_prime union simplex(F) has intersection a base simplex plus n-1 spokes, hence H2(K,K_prime)=Z^(n-2); H1(K_prime)=0 makes inclusion split and primitive. Orthogonal-coordinate permutations act on spoke differences by the integral augmentation lattice. An independent neighborhood-face enumeration and mod2 boundary calculation checked both parity sheets for n=3,4,5,6; this finite check does not prove the integral all-n claim.

## originality

PASS

Best-of-knowledge PASS following direct full-text comparison with the closest intact-cube theorem and separate vertex-puncture work; the relative edge-puncture theorem is not implied by either.

## value

PASS

A single edge defect is the minimal graph perturbation preserving all vertices and all parity-sheet edges. The full integral response, explicit primitive local tetrahedral sphere carriers, and nontrivial S_(n-1) augmentation representation are useful structural topological information not implied by the intact-cube Betti numbers; n3 contractibility is a genuine boundary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
