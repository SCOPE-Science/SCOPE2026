---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For the positive (m+2)-braid diagram, direct word length gives (m+1)(m+2)n+3m+7 crossings. The source genus g=((m^2+3m+2)n)/2+m+3 and braid index m+2 make the standard lower bound c(K)>=2g+b-1 equal exactly the displayed diagram crossing count, proving equality. Writing b=m+2 gives c=b(b-1)n+3b+1 and c=(b+1)^2 at n=1. The source also realizes every complement by filling a fixed cusped hyperbolic parent M, homeomorphic to the complement of census link L14n61770; strict hyperbolic Dehn-filling volume decrease gives one uniform upper bound. A fresh algebraic replay checked the lower-bound equality for m=3..19 and n=1..9.

## originality

FAIL

Every load-bearing ingredient is already published in the same primary source or is a standard immediate theorem: the source gives the explicit positive braid, exact genus, exact braid index, and a single fixed hyperbolic parent whose Dehn fillings are the knot complements. The crossing formula follows by substituting the source genus and braid index into the classical c>=2g+b-1 bound and observing equality with the displayed positive-braid word length. The bounded-volume statement follows immediately from standard strict volume decrease under hyperbolic Dehn filling. The combined volume-density conclusion is therefore an elementary corollary of already published data rather than an independent theorem under the implication-based originality bar.

## value

FAIL

Bounded volume with diverging crossing number is an interesting description of the family, but here it is obtained by a one-line equality in a standard crossing bound and a standard filling-volume inequality applied to facts already central to the source construction. With no new extremal boundary, mechanism or optimization, it is a routine corollary under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
