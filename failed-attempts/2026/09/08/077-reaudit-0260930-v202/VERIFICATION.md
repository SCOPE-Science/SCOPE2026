---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Independent exact arithmetic reproduced each h*-vector from the standard weighted-simplex age histogram, then reproduced all L(0..9) values from L(k)=sum_j h*_j binom(k+6-j,6). Direct facet-inequality enumeration of P gave 8,8,9 lattice points for t=1,3,9; each listed 2P witness satisfies the 2P inequalities and has no decomposition as a sum of two P lattice points.

## originality

FAIL

Braun–Davis–Hanely–Lane–Solus provide a complete IDP classification for reflexive weighted-projective-space simplices with at most three distinct non-unit weights. These examples have only the non-unit weights {2}, {2,3}, or {2,9}, so their IDP status is within that prior complete classification. The exact h* and Ehrhart rows are standard finite consequences of the weights via the age/Ehrhart formulas rather than an independent theorem.

## value

FAIL

The three-row segment is explicitly vacuous for the forward IDP-implies-unimodal question, and its non-IDP status lies in a prior complete classification. The remaining exact polynomial/vector data are routine finite evaluations of canonical formulas. Under the audit bar this is a known/mechanically implied narrow slice rather than a motivated new boundary or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
