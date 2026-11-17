---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For B=J_n^{⊕r}, n≥2, the centralizer is M_r(F_q[t]/t^n). Nilpotence is detected by residue; q^{r²−r} nilpotent residue matrices each have q^{r²(n−1)} lifts. A nilpotent commuting matrix is regular as an F_q-linear operator exactly when its residue is rank-(r−1) regular nilpotent and its determinant has t-valuation one, by Smith factors and one-dimensional kernel. Counting the nonzero determinant linear functional gives |GL_r(q)|q^{r²(n−1)−r}, density Φ_r(q). Cyclic-vector lifting establishes the companion-matrix/Eisenstein-polynomial orbit labels; centralizer size (q−1)q^{rn−1} gives equal orbit size. I independently enumerated all 2×2 matrices over F₂[t]/t^2 and /t^3 via direct matrix multiplication and powers: respectively 64/24 and 1024/384 nilpotent/regular, with 2 classes of size 12 and 8 classes of size 48 via trace/determinant. These finite tests corroborate the proof but do not establish all q,r,n.

## originality

FAIL

FAIL because the 2026-10-25 published general finite-field nilpotent-centralizer theorem explicitly covers arbitrary Jordan partitions, including λ=(n^r), and gives the same regular-nilpotent density Φ_r(q) and the exact cardinality of every parameter fiber. In the published theorem the complete GL(A)-orbit of each regular commuting B is uniquely labeled by the valuation-r polynomial f_B with A=f_B(B), uniformly ranging over (q−1)q^{nr−r−1} choices, and each orbit has |C_GL(A)|/((q−1)q^{rn−1}) elements. This IS the submitted orbit count and uniform size under a different complete orbit coordinate. Replacing the earlier valuation-r orbit parameter by an Eisenstein companion characteristic polynomial is a standard equivalent coordinatization of the same cyclic modules; it does not make the original full final claim independent. The source’s 2026-10-04 dual-number special case is weaker, but the overlooked 2026-10-25 stronger theorem is decisive.

## value

PASS

Conditional constant-density and exact regular-nilpotent orbit stratification are natural structural invariants of commuting Jordan matrices; the result is mathematically useful and nontrivial. The new submission nonetheless fails originality because all principal exact counts and full conjugacy-orbit classification were published beforehand for more general Jordan partitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
