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

The toric formula correctly specializes to \(R=(r+2)/(r+a+b)\). Using the canonical region \(0\le d=b-a\le r\), \(1\le a\le r+d\), normalized lattice points converge to uniform area on the stated triangle. Intersecting \(x+2y\le L\) with that triangle gives the displayed piecewise survival law, and direct integration gives mean \(\log3/3\). The verifier checks the Reid--Tai region, exact counts/extrema, survival continuity, and mean convergence.

## originality

FAIL

Li gives the toric barycenter formula for the greatest Ricci lower bound and Berman--Berndtsson extend it to toric log Fano varieties. Separately, the already published Resultary record 'A triangular classification of canonical and terminal two-heavy weighted projective spaces' gives exactly the canonical lattice region used here. Once those prior inputs are combined, the limiting distribution is the elementary push-forward of uniform lattice points in a triangle under \(1/(1+x+2y)\); the survival pieces and mean are routine polygon-area and integral calculations.

## value

FAIL

Uniformly averaging a known rational invariant over a previously classified triangular lattice family is a reasonable descriptive statistic, but the piecewise law and mean are elementary area/integration consequences and do not add a new rigidity mechanism, difficult exact invariant, or nontrivial asymptotic phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
