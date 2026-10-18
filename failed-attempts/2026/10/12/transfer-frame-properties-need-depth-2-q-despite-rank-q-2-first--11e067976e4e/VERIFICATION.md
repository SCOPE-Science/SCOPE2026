---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Induction for rho_0=R and rho_(i+1)(x,y)=exists z(rho_i(x,z) and rho_i(z,y)) yields exact length 2^i reachability and quantifier rank i; adding two universal quantifiers gives rank q+2. The transfer axiom Diamond^(2^q)p -> Diamond p attains modal depth 2^q, and Balbiani et al. Theorem 6.1 is an all-(m,n) absolute minimality theorem, including n=1<m=2^q. Independently checked 1,590 complete property/valuation equivalences for all digraphs with 1-3 vertices and q=1..3. The finite checks do not prove minimum depth; the inspected theorem does.

## originality

FAIL

The actual same-class modal-depth minimum is the m=2^q, n=1 specialization of Balbiani et al. Theorem 6.1 for every transfer pair m != n. The FO rank q+2 is the classical repeated-squaring reachability formula plus two outer quantifiers, not a new nonstandard argument. Selecting exponential m adds no new invariant or structural obstruction. This is covered by a stronger prior theorem and a routine textbook FO construction, irrespective of the absence of that exact juxtaposition in the source.

## value

FAIL

The exhibit is a correct expository illustration of known FO/modal succinctness, but adds no motivated new theorem beyond a parameter substitution into an all-transfer-axioms minimality theorem and the familiar repeated-squaring formula. The quantitative outcome is mathematically predetermined, not a new unknown exact invariant or substantive gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
