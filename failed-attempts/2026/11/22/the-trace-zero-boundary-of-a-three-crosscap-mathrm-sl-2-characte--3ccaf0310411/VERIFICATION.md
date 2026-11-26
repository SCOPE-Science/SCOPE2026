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

Cayley–Hamilton gives C²=-I and A²B²=-I. If a is nonzero then A is a polynomial in A²=-B⁻² and commutes with B; otherwise B²=I and B=±I in SL₂(C). Thus T=AB is regular semisimple with eigenvalues i,-i, including at a=0 or b=0. Conjugate T to diag(i,-i); the slice has A=diag(t,t⁻¹), B=diag(i/t,-it), C=[[u,v],[w,-u]], with u²+vw=-1. The diagonal torus gives opposite weights to v,w and the only additional weight-zero generator vw equals -1-u². On the reduced representation boundary restriction of conjugation invariants to the slice is injective because the slice meets every orbit; its image contains t,t⁻¹,u by the trace formulas. Exactness of invariants for the reductive group identifies the reduced quotient with the reduced trace-zero stratum. The trace equations follow by multiplication; (a±ib)/2 are mutual inverses, and s/(2i)=u. Projection forgets u. The naive section has dimension two and the point (a,b,c,p)=(2,2,0,1) is extraneous.

## originality

FAIL

A distinct indexed global classification for the identical group, ordered trace words and reduced affine GIT quotient contains the entire frozen conclusion. Its four coordinates are a,b,c,s, not Chen’s a,b,c,p. Setting c=0 in the global equation gives the cylinder, and restriction of the three global trace identities yields all the missing seven-trace equations; its boundary projection is also explicitly stated. Both records have the same catalogue date. The companion calls the boundary an earlier related calculation, but that does not establish a publication order or identify an independent earlier author. This decision is about demonstrated coverage, not a claim of earlier priority. Chen’s paper alone does not cover the frozen result.

## value

PASS

The mathematical boundary classification addresses a specific gap in the motivating paper, distinguishes the reduced affine quotient from the deficient projection, and gives a global coordinate choice even at exceptional slice parameters. That is useful geometry, not just the c=0 substitution in Chen’s four-trace equation. It adds no distinct conclusion beyond the companion global classification; that is the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
