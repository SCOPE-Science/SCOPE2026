---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the corrected RESULT.md, the SRG common-neighbor identity reduces to A^2=A+I+J, and the constants and the zero-sum subspace split since v is odd. A kills the former and acts with exact period three on every nonzero vector of the latter. Expanding B=A+ee^T and writing u=Ae and w=1+e gives B^3+I=ww^T+uu^T. The nonempty proper support of u within that of w makes them independent; the three pairings vanish by evenness, so the defect has rank two and square zero over every stated field. The image plane has order three and no fixed line of eigenvalue one; hence B^6=I, the global order is six, and ker(B^2+I)=ker(B+I) since (B+I)x for B^2-fixed x is both in that plane and fixed. The fixed space of B within span(1,e,u) is exactly span(1+u). Therefore the dimensions at powers one, two, three are 1,1,v-2, giving the stated configuration counts and then the orbit counts. The frozen closing sentence could incorrectly identify the former transient sector pointwise with primitive six-cycles: e lies outside the zero-sum subspace but B^3 e=e and Be!=e. A direct binary five-cycle check also finds 1 fixed, 3 period-three, and 12 period-six states among the 16 formerly transient states. The corrected finding states the true population-level distinction and does not assert a pointwise conversion.

## originality

PASS

For the corrected population theorem, the binary conference adjacency identity and broader themes of feedback and short periods are prior. The inspected sources do not subsume the site-independent rank-two defect and complete configuration and orbit census for this first-order map on all stated state fields and graphs. This is a best-of-knowledge comparison, not a priority attestation.

## value

PASS

The corrected theorem identifies an exact, uniform effect of a one-site change on bijectivity and recurrence for a natural parameter class, with all least-period populations rather than one witness or a general order bound. The contrast between an unmodified noninvertible rule and a period-six invertible rule, together with the rank-two description, is meaningful without any false pointwise correspondence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
