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

Weighted K_{a,b} tree degree generating polynomial P X^(b-1)Y^(a-1) follows from the standard complete multipartite matrix-tree theorem. Supplying unit current between two a-side vertices gives R_eff=(1/x1+1/x2)/Y and edge-insertion determinant lemma gives Z1=P X^(b-1)Y^(a-2)(Y+x1+x2). Dividing and extracting degree-one coefficients yields pA=(1-1/a)^(b-1), endpoint pA*(b+1)/(b+2), and nonendpoint B-side pB'=(b+1)/(b+2)(1-1/b)^(a-2), so the displayed Δ follows by subtraction. For a>=3 the first term increases with b and second decreases; at b=a-1 sign is negative, at b=a positive; a=2,b=1 gives exact equality via 0^0=1. Checked source verifier parses real graph Laplacian cofactors and enumerates small trees, plus 120x120 exact signs; script inspected, not rerun. Full infinite proof algebraic.

## originality

PASS

Klee-Stamps/Clark provides baseline enumerator, rank-one update is standard; no inspected primary work states the added within-side edge mean-leaf change or b=a sign threshold. General degree-correlation identities can in principle derive it but do not by themselves equal an already published full specialization.

## value

PASS

A single added graph edge can *increase or decrease* a natural uniform-spanning-tree statistic, with a sharp bipartition balance boundary for every size. This quantifies a nonmonotone edge perturbation on an elementary natural graph family and can inform random tree sensitivity; despite standard determinant-lemma tools the evaluated sign reversal is not a routine standalone textbook identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
