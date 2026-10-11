---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Using \(x=\cos^2(k/2)\) and \(y=k^2\), direct symbolic expansion verifies that the published \(j=1,3\) secular bracket factors exactly as \((2(y+1)x-y)(2(y+1)x-1)\), while the \(j=0\) and \(j=2\) residual factors are the two respective factors. This gives the two tangent equations. The two root sets are disjoint, and differentiating their scalar equations proves every positive root simple. Each factor occurs in exactly three symmetry sectors, so the corresponding graph eigenspace has multiplicity three. Standard pole/regular-point expansions give the stated \(\sqrt2/K_n\) and alternating \(L_n^{-2}\) offsets. The assigned verifier and an independent symbolic factorization both reproduce the exact algebra.

## originality

FAIL

The load-bearing exact secular determinants are already published by Exner and Lipovský, sector by sector, for this same equilateral preferred-orientation octahedron. The audited two equations are obtained by a one-line algebraic factorization of the published \(j=1,3\) bracket together with the already displayed \(j=0\) and \(j=2\) residual factors. Under an implication-based originality standard, the exact root description and triple sector occurrence are therefore mechanically contained in the primary source even though its theorem statement records only asymptotic localization for those branches. The sharper leading offsets are routine expansions once the factors are written.

## value

FAIL

An exact factorized presentation is convenient, but here it is obtained by elementary factorization of a published same-object secular polynomial, followed by routine root differentiation and asymptotic expansion. It adds no new spectral mechanism or nontrivial boundary beyond information already encoded exactly in the source, so it does not clear the independent-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
