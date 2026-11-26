---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The odd-characteristic hyperelliptic quotient over F3 is P1, and choosing a rational infinity gives y^2=a f(x) with f monic squarefree of degree 9 or 10. These degrees account for 10 branch points, including infinity exactly in odd degree. The two leading square classes have identical counts over F9 and F81. The fresh census used exact quadratic characters and one or two points at infinity, respectively; it found 13,122 and 39,366 squarefree forms, with minimum B4 values 0 and 2. The sole zero is the monic degree-nine polynomial x^9−x, with N2=N4=10. Its two F3 twists are isomorphic by x↦−x, so the count is of F3 classes, not only presentations. Fresh replay: python3 /workspace/branches/471463d8-8bf5-404d-914a-b003b672463a/audit_record4.py; census.out alongside it records the full run. The supplied verification sources were inspected, not executed. In the family, the derivative is −1 and the smooth odd-degree model has genus (q^2−1)/2 and one rational infinity. For z=x^{q^2}−x≠0 in F_{q^4}, z^{q^2−1}=−1, so z^{(q^4−1)/2}=−1 because (q^2+1)/2 is odd. All remaining points are exactly the q^2 branch points from F_{q^2} and infinity. Thus 4B4=N4−N2=0. For all r≥5 one has q^{r/4}>1+sqrt(q^2−1): check q=3 directly and use q^{1/4}>1+1/q for q≥5. The universal positive closed-point criterion following Eq. (8) on p. 4 of arXiv:2310.11218 (just before Prop. 2.2) gives the upper threshold 5 for all curves, and the witness gives the lower threshold. This proves neither uniqueness outside the hyperelliptic locus nor a classification for other q.

## originality

FAIL

The central hyperelliptic uniqueness statement is a direct consequence of an exact candidate Weil-polynomial table for the relevant quadratic extension, not an unresolved gap requiring the monic census. The indexed genus-four threshold result separately states the same q=3 threshold and witness. The all-odd-q threshold is not stated in that record, but follows from the known Hermitian maximality result by taking its elementary hyperelliptic quotient and quadratic twist, followed by the existing universal threshold bound. These are implication findings, not claims that both assertions have been printed verbatim elsewhere.

## value

FAIL

An exact closed-point threshold and its exceptional curves are well motivated. Here the claimed inverse classification is determined by the prior exact stability candidates with a short standard double-cover count, while the infinite threshold follows from an extremal Hermitian quotient, its twist, and the known bound. The census usefully checks the arithmetic but its auxiliary counts of monic presentations are not a separate motivated invariant. No separately valuable unknown classification or threshold remains within the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
