---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Under the stated HOMFLY–PT normalization P_K(1,z)=Conway_K(z), so dDelta=span Delta=deg Conway <= dH=deg_z HOMFLY. The standard Ozsvath–Szabo and Rasmussen slice-genus inequalities give 2|tau|<=2g4<=2g and |s|<=2g4<=2g. Failure of either candidate therefore forces dDelta<2|tau| or dDelta<|s| respectively, hence dDelta<2g. For knot Alexander polynomials the span dDelta is even, so 2g-dDelta>=2. If dDelta=2g neither candidate can fail. Fibered knots satisfy Alexander span=2g. These are mathematically correct elementary implications; finite verifier.py is merely numerical arithmetic sanity check.

## originality

FAIL

The CURRENT source arXiv:2605.22652v5 already proves relation 40 dDelta<=dH in §2 (lines 327–340), Proposition 5.19 gives 2|tau|,|s|<=2g4<=2g in precisely the setting of candidates c8/c9, Proposition 5.23 chains Alexander degree to HOMFLY dH, and its §5.4 Proposition 5.26 extracts candidate-failure necessary conditions by graph transitivity. Combining these already juxtaposed inequalities gives the entire Alexander-sharp conclusion with no new mathematical lemma: if dDelta=2g then automatically dH>=2g>=2|tau|,|s|. The defect>=2 is just integrality and even parity. Thus the final claim is a routine corollary of published stronger statements; missing verbatim wording is not novelty, and no novel classification or independent table survives.

## value

FAIL

The exact counterexample filter is the immediate strict contrapositive of two pre-existing inequalities and even parity; it neither exhibits a new knot, proves a new invariant relation, computes an unknown invariant, nor rules out a previously untested mathematical class by a nonstandard argument. The source already emphasizes this kind of inequality-graph propagation. Correctness and source-specific presentation do not make this textbook transitivity calculation a substantive new research result. Fibered-knot restatement is a standard automatic specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
