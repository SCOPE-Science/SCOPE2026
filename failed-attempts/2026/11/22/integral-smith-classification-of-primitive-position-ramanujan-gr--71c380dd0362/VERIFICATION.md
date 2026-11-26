---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At a prime, the unit Gram matrix is the reduced complete-graph Laplacian pI_(p−1)−J_(p−1). Adjoining a zero yields a matrix integrally equivalent to pI_p−J_p by replacing its last row and column by their sums; this verifies the asserted nonzero Smith list, including p=2. At p^e with e≥2, the prime-power Ramanujan identity gives exactly p^(e−2)(p−1) identical blocks p^(e−1)(pI_p−J_p) because each retained residue class modulo p^(e−1) is present in full. Tensoring the integral local equivalences by CRT preserves unimodularity. For a given p the valuation e−1 occurs on R_n/(p−1) positive factors, the rest have valuation e, and sorting valuation lists separately produces the claimed chain. This proves the rank, zero block, torsion order and exponent formula. Positivity in the squarefree case is Gram positivity at full rank. The 1×1 calculation at n=1 is consistent.

## originality

FAIL

The full-residue theorem's numerical invariant factors alone would not determine arbitrary principal Smith submatrices, but its published proof gives a blockwise integral calculation that determines this particular restriction mechanically. At e≥2 units retain a known number of whole, already-classified blocks. At e=1 they retain precisely the reduced Laplacian, with the already-classified nonzero block (delete one row/column after two sum replacements). The CRT and primewise assembly are the same as those in the full-residue proof. This establishes corollary-level coverage of the complete claimed classification, not just of its spectrum or rank.

## value

FAIL

Primitive-position sampling is natural and integral torsion is distinct from spectral data. But for this slice every needed local integral factor is already in the broader computation: the restriction removes whole copies or the single zero direction, then repeats the same CRT assembly. The explicit restatement is useful as an expository corollary, not a non-mechanically-implied exact invariant under the review criterion. The consequences are formal and do not leave a distinct surviving mathematical remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
