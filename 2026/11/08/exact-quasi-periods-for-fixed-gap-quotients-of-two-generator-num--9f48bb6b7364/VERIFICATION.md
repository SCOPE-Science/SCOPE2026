---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For S=<a,a+h>, Sylvester F=a²+(h−2)a−h and symmetry yield G=(F−w)/p where w is the least element of S in F mod p. Writing w=ta+hy with 0≤y≤t yields the exact first feasible (I_r,J_r) at t≤p−1 when a>h(p−1); w<F follows from a>p. At residue 0, (I,J)=(p−1,p−1), unique among residues; a triple CRT argument rules out every alternate period d with p∤d despite admissible gcd(a,h)=1. Independent exact direct-membership checks matched 321 instances of p,h,a. The proof, not the finite checks, supports all parameters.

## originality

PASS

Closest Feihu Liu 2026 special case has gap h=1, and the other paper imposes a divisor condition not present here. Neither stated prior result derives the all-fixed-coprime-h explicit coefficients with exact minimal period p; best-of-knowledge priority with possible unindexed general quotient theorem.

## value

PASS

A full natural fixed-gap two-generator family replaces a lone example. The exact eventual residue formula and sharp minimal period solve a structural complexity question, including a nontrivial admissible-domain CRT obstruction to period collapse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
