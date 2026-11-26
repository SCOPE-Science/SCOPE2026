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

Common atomless endpoints have uniformly random ranks and may be handled in uniform-quantile coordinates. For any 0<b<1/2, the probability that min R<b or max L>1-b is at most 2nb². A left-anchored interval reaching the midpoint has probability b, as does a right-anchored one, so the union of the two missing-anchor events has probability at most 2(1-b)^n. When present under the extreme bounds, the anchors intersect and their union dominates; a single interval that serves as both anchors is universal and can be paired with another, and the complete case also gives a pair for n>=2. Substituting b=2 log(n)/n gives the claimed inequality for n>=9. Any common neighbor of the two disjoint extremal intervals spans [min R,max L], hence is universal, and if the extremes are not disjoint the graph is complete. This proves D<=2 iff U>0, including the disconnected convention. The exact 2/3 universal probability is independently supported by Diaconis–Holmes–Janson. By the interval Helly property the complete event is precisely that all matching pairs cross the midpoint cut in endpoint ranks; its probability is n!/(2n-1)!! = 2^n/binom(2n,n). Subtracting yields the two exact diameter probabilities and the claimed missing-mass bounds. Total domination cannot use one vertex, and a connected dominating pair yields both the connected-domination claim and the diameter bound.

## originality

FAIL

A distinct indexed Resultary record on the identical random-interval model already contains the same two mutually adjacent, midpoint-spanning anchors and the same cutoff-dependent failure estimates in its actual proof §6. Its specific cutoff delta=n^(-3/4) is not essential: the displayed estimates are 2n delta² and (1-delta)^n for each missing anchor, so the present exact epsilon is obtained by replacing delta with 2 log(n)/n and applying 1-b<=exp(-b). The dominating-pair and total/connected-domination consequences apply to that very same pair. The comparator's unbridged-pair count equals zero exactly when D<=2, and its zero-mass limit, its diameter upper bound, and the vanishing complete mass already imply the two/three diameter split. The finite D<=2 identity transfers the classical exact universal-vertex law by the same gap-bridging criterion applied to the extremal pair, and the complete and D=2 terms use the elementary midpoint matching count. The quantitative headline and limits thus have demonstrable equivalent coverage or are routine deductions from it; the finite identities do not establish a substantively distinct finding. Both indexed records have the same displayed date; this decision is about scientific coverage, not historical priority, authorship or dependence.

## value

FAIL

The geometry and exact diameter probabilities are useful to state clearly, but the contribution beyond the inspected coverage is a parameter substitution in the existing anchor bound and elementary exact consequences of the classical universal probability and matching model. The chosen logarithmic cutoff gives an explicit faster convergence bound but does not resolve a new mechanism, sharp order, or other substantive gap. No separate nonroutine remainder of the frozen claim was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
