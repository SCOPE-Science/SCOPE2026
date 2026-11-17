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

Write X=N+sum eps_j Y_j with N^2=0 and NY_j+Y_jN=0; fixed residue rank r gives flag count [n r]_q[n-r r]_q|GL_r|. In the U,W,Z splitting s=n-2r, each Y_j has unrestricted A,D,F,G blocks totaling 2r(n-r) coordinates plus free s-by-s K_j. The actual R^n field-linear rank is (d+1)r+rank(K_1;...;K_d), giving [s t]_q[ds t]_q|GL_t| and the claimed formula. Kernel-image gives homology dim (d+1)n-2h, exactness iff appropriate parity/dimension. Independently computed q=2,n=2,d=2 joint rank counts 1,45,210,48 in their proper (r,h) cells. The size-two rank gap for d>=3 follows from r=0 versus r=1 supports.

## originality

PASS

Best-of-knowledge surviving contribution is the exact joint field-rank versus residue-rank and homology-dimension distribution over NONPRINCIPAL split radical-square-zero algebras of arbitrarily many nilpotent directions, with acyclicity boundary and genuine missing ranks. Earlier Bockstein/Smith census covers chain rings of length two, equivalent to d=1; it does not control d>=2 where the secondary map stacks ds-by-s blocks. General unrefined square-zero lifting counts are known but do not determine this secondary-rank refinement.

## value

PASS

Natural periodic-complex and nonprincipal finite-local-algebra rank invariant, including an exact acyclicity parity criterion and sharp rank gaps already in n=2. A general all-n all-d Gaussian formula over a motivated class gives concrete homological data; not just a tiny computation or rebranding of d=1 chain rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
