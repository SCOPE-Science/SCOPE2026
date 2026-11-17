---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

C: A dominated committee pair has an ordered disjoint equal-cardinality exchange t<=min(k,m-k). For one voter, P[#Y>=#X] = (1+binom(2t,t)/4^t)/2, yielding rho_1=3/4, rho_2=11/16, rho_3=21/32 and decreasing higher-t terms. All-equality probabilities are (binom(2t,t)/4^t)^n. An independent, fully exhaustive 256-row bitmask calculation over all 56 t=1 and 420 t=2 events gave sharp maximal pair overlaps 160/256,160/256,152/256 for (1,1),(1,2),(2,2). Bonferroni and union bounds therefore prove the displayed finite-n error envelopes and the nonlocal conditional law; the five-voter four-column witness (3,5,10,28) demonstrates true two-swap improvement. Finite certificate handles fixed eight-bit overlap only; all n follow from analytic bounds.

## originality

PASS

O: PASS best-of-knowledge. Schünke (2026) full primary text establishes structural Single Dominance Only in interval approval domains and discusses unrestricted multi-exchange phenomena, not the fair-coin probability or exact 3/4 and 11/16 exponents. General fractional-PO and committee-testing literature addresses different predicates. A direct bound for all committees under iid approvals was not found; unindexed probability enumerations remain a residual risk.

## value

PASS

V: PASS. Quantifies when single-candidate efficiency checks mislead on unrestricted random profiles and supplies the exact leading rate of genuinely nonlocal committee Pareto failures, with an all-finite-n error bound and explicit witness. The two scales are mathematically motivated by minimal exchange sizes, rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
