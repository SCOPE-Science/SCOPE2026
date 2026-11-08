---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For all n>=3, the proof correctly encodes centered cyclic triangles as -Q/4, Q a signed incidence-line-graph Rademacher chaos; kappa4(Q)=-2M+24S follows from even-degree edge multigraphs. BB^T=nI-J determines tr(A^4); nonbacktracking 4-cycle extraction gives S=n(n-1)(n-2)(n-3)(n-7)/8, hence the displayed polynomial. Independent exact tournament enumeration n=3..6 and trace/symbolic equality of old and new moment formulas corroborate, while the all-n proof is algebraic.

## originality

FAIL

A decisive all-n fourth CENTRAL moment formula for exactly the same random circular-triad count was published by Kendall and Babington Smith in 1940 as an explicit conjecture and subsequently proved by P. A. P. Moran in 1947, as documented in Berry–Johnston–Mielke, A Chronicle of Permutation Statistical Methods (2014), section 3.3 pp.113–114 and footnote 12. Symbolic simplification of that printed formula minus three squared known variances reproduces this result’s exact fourth cumulant polynomial IDENTICALLY. Its claimed n=8 sign threshold follows immediately from that polynomial. The additional signed-four-cycle identity is a reformulation through the quadratic Rademacher expansion and trace, not an independent new substantive claim. This is strong prior mathematical coverage, not a merely inaccessible or keyword-matching source.

## value

FAIL

FAIL as a research contribution: paired-comparison fourth moments and the exact all-n fourth-cumulant value were already conjectured in 1940 and proved in 1947; the n=8 sign change and leading 12/n kurtosis are immediate manipulations. The signed line-graph proof is mathematically sound but a short equivalent way to compute a known natural statistic, with no demonstrated additional independently useful new invariant or structural theorem. This is known-table/formula recomputation, not a surviving original valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
