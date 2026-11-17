---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The graph C_n□K_3 has four distinct neighbours per vertex for n≥3. Fixed opinion condition is at least two of four agreeing neighbours (tie retains current opinion); the 64 pair-column transfer has exactly 182 legal transitions. A labelled closed walk gives one fixed assignment, so F_n=tr(T^n). The explicit characteristic polynomial factorization yields the four power sums and the unique leading eigenvalue 3, while the remaining roots have modulus <2. Independently reconstructed T and computed the exact 64×64 characteristic polynomial using SymPy; verified factorization and counts F_3..F_6=32,94,218,712. This is exact finite algebra plus a valid transfer-bijection proof, not finite enumeration claimed as infinite proof.

## originality

FAIL

A 2026-11-02 publication already studies C_3□C_n, graph-isomorphic to C_n□K_3, under the identical majority/tie rule. It states the identical 64×64 transfer characteristic polynomial and exactly the same all-n fixed-state law and growth constant, with the extra random-tie comparison. The later finding is directly covered.

## value

FAIL

Fixed-state entropy on a narrow four-regular graph is a meaningful natural invariant, but this identical graph, transfer determinant, entropy and counts were already published. Rewriting C_3 as K_3 and rechecking the determinant is not a separately valuable unknown classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
