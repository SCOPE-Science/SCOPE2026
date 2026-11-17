---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Edge survival indicator gives G_i(p)=sum_{e:i descendant} length(e)(1-p)^{|C_e|}. For <=4 taxa, an LCA split is singleton-versus-other or (2,2), so gain difference after dividing by q=1-p is monotone or affine and has at most one strict crossing. At 5 taxa only (3,2) produces quadratic Aq^2-Bq+C; conditions C>0, 0<B<2A, B^2>4AC, A-B+C>0 characterize two roots inside (0,1). Given rational witness yields G_a-G_d=q(q-1/5)(q-4/5), with a dominating b,c and d dominating e, so a globally wins near both ends. Direct rational checks at five q values confirm crossings; symbolic proof handles continuum.

## originality

PASS

General Noah’s Ark/HED/HEDGE formulas and priority optimization are established prior. They do not give the sharp five-taxon two-return boundary or full quadratic crossing criterion for common survival probability under arbitrary positive branch lengths. The independent new part is this exact finite structural threshold.

## value

PASS

The smallest tree that permits loss and return of a uniquely optimal single-taxon protection choice is a natural policy-sensitivity boundary. The if-and-only-if 3+2 quadratic criterion and explicit positive-edge witness are nonroutine structural facts; no broader portfolio result is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
