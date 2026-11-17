---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For d>=1 and q=2^f, the group-algebra basis change in the frozen RESULT.md makes full-cube adjacency A satisfy A^2=(d mod 2)I with N/2 Jordan two-blocks. The one-leaf update B(x,s)=(Ax+se,e^T x) decomposes for odd d into one J3(0) plus an involutory N-2-dimensional complement (fixed dimension (N-2)/2). For even d, explicit B^2,B^3,B^4,B^5 and rank B=N/2+2 yield one J3(0), N/2-2 J2(0), and a two-dimensional swap recurrent subspace. Thus B^5=B^3 != B^2 and every exact first-entry/period census follows from kernel filtration; one three-block gives Pr(T=3)=1-1/q. Independently rebuilt GF(2) adjacency, matrix powers, ranks and B^5=B^3 for d=1..6; d=1 zero recurrent space and d=2 zero J2 blocks checked. Finite tests do not prove the family, the algebraic decomposition does.

## originality

PASS

Specific one-vertex ADDITION, rather than prior one-vertex DELETION or an every-vertex corona, has a different Jordan Fitting decomposition, uniform exact three-step entrance rate and parity-dependent recurrent space not derivable by parameter substitution from the known puncture Jordan forms.

## value

PASS

A single local graph defect sharply changes linear automaton transient behavior in both parities, producing a dimension-independent exact three-step clock while even and odd recurrent dimensions differ radically. The complete finite-field joint time/period census is a natural structural invariant and useful boundary example, not merely a generic linear-algebra method or arbitrary small graph table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
