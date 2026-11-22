---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible exact checks

Run from the directory containing this file:

```shell
python3 checks/verify_unicyclic_six.py > reproduced.json
```

`checks/verification_output.json` records the complete reference output. The script requires **Python 3 standard library only**. It enumerates every labelled simple connected unicyclic graph on 3–6 vertices by choosing precisely \(n\) edges, then identifies unlabeled classes by checking all \(n!\) relabelings. It verifies the two named collision pairs by canonical graph signatures, not only by the number of classes. The asserted class counts are \((1,2,5,13)\).

For each of the four labelled six-vertex graphs, the script enumerates the \(4096\) exterior monomials in the graph Chevalley–Eilenberg complex, builds all signed differential columns, verifies the square of the differential is zero on every basis monomial, and computes rational ranks block-by-block with exact Fraction arithmetic. It recomputes all Betti numbers from rank-nullity and asserts the expected vectors, Poincaré duality and Euler characteristic zero. The output's `differential_ranks` array is the rank of \(C^{k-1}\to C^k\) for \(1\le k\le12\).

As a cross-check independent of the sparse-rank implementation, a separate NetworkX graph-atlas enumeration and SymPy exact-rational DomainMatrix elimination gave the same four Betti vectors. This ancillary implementation is not required to reproduce the standalone certificate.

**Proof limits.** Exhaustive search proves only the finite unicyclic range through six vertices, and exact rational linear algebra proves rational Betti dimensions rather than integral homology or ring structure. The identification with rational cohomology of the compact graph nilmanifold is the standard Nomizu theorem for rational two-step nilpotent Lie algebras. No independent audit or definitive novelty certification has been performed.
