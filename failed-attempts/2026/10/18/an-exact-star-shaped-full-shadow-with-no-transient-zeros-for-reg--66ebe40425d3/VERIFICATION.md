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

After z=lambda*w, the chain rule on w^r Q(w^d) gives the stated residue and degree. For r=0, ordinary Rolle intervals account for every root of Q' with the retained endpoint factor; Q'(0)/Q(0) is the negative sum of reciprocal roots counted with multiplicities. If r>0, the weighted polynomial u^(r/d)Q(u) adds the interval from zero to the first positive root. Those disjoint intervals and the endpoint multiplicity exhaust the new degree, so the interior roots are simple and a lost endpoint root cannot return; constant reduced polynomials cause no exception. The core is a subset of the shadow by definition in Hägg–Shapiro I (p. 4); their Theorem 1.4(i) supplies connectedness and containment of the vertices. These facts and finite-level localization force every interior point of every spoke and the center, by separation of the leaves. The frozen text's shorthand attribution of the subset inclusion to (i) is harmless with the definition. Independent replay: python3 /workspace/branches/replay_exact_audit.py 5 used explicit binomial/factorial coefficients, exact endpoint division and Sturm counts for 567 descendants; the uploaded checker was only inspected. The arbitrary orders and d follow from proof, not the replay.

## originality

FAIL

The exact classification is covered by a distinct indexed record, not just a similar title: Resultary 9054e99efdbc proves the all-orders support, center factor, interior simplicity, endpoint multiplicity and shadow/core equality for z^d-1 in all d>=2. The scalar change z=lambda*w, lambda^d=a, and affine covariance transfer all those conclusions to the frozen family; the degree and dimension statements are immediate. Independently, Hägg–Shapiro III gives the main geometric conclusion in a stronger signed-radial family and supplies the pooled measure for this exact special case. The finite-level multiplicities not asserted in III are already in the other indexed record, leaving no distinct verified remainder. This finding of demonstrable coverage is not a claim about first discovery or historical priority: the indexed comparator has a later catalogue path date, and the priority chronology of the authors' Part III copy is not established here.

## value

PASS

As a mathematical classification, this is useful: it gives both the exact support of every finite derivative and the absence of transients for a canonical family, without replacing the complete shadow by a single differentiation-ratio limit. That utility is not a claim of a new contribution: explicit coverage is decisive on the originality axis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
