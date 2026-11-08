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

# Reproducible exact verification

Execute `python3 artifacts/verify_integral.py` using the standalone script in this package. The actual output is stored in `artifacts/verification_output.txt`; the verifier uses only Python's standard library.

The script enumerates every local edge-variable monomial basis element in the weight-three full-vertex reduced Świątkowski complex, including rows of every boundary matrix that are identically zero. It proves nonplanarity using the bipartite planar girth bound and enumerates all deletions of zero, one or two vertices to establish three-vertex-connectivity. These graph properties only support source applicability and literature comparisons; the full integral homology computation relies on the complete chain differential itself.

Exact integer checks include both compositions of adjacent boundaries, \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\); three exhaustive Smith unit eliminations; a complete rank-one proportionality and gcd calculation on the residual degree-two boundary; and an independent repeat of the degree-three elimination under a different pivot priority. All reductions are unimodular and use no floating-point arithmetic. The recorded dimensions and invariant factors are documented in `RESULT.md`.

No formal external certification or independent audit was carried out. The code uses an established quasi-isomorphism theorem; it does not independently prove that underlying theorem. These calculations do not address any particle number other than three or any other graph.
