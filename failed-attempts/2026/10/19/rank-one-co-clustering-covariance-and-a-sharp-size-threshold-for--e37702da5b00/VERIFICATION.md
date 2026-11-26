---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

FAIL

The covariance, exactly rank one, root formula, and directions of the signs are correct. Marking a fixed r-subset as an exact block factors its EPPF into the probability of that event and the shifted complement EPPF. Averaging the two occupied-pair cases gives the bracket in RESULT.md lines 50–54, including empty or singleton remainders where the complement term vanishes. The endpoint F_n(1)=(n-1)[(n-2)q-np]<0 also proves nonzero rank, and F_n(n)=n(n-1)(1-p)>0. The quadratic has precisely one root in (1,n), the displayed plus root; the limit and Ewens specialization follow directly. But line 19 as written asserts uniqueness of a real threshold by its signs tested only at integer r, which in general does not identify a unique real number. For n=2, alpha=0, theta=1, the root is 5/3 and every real number in (1,2) separates the same two integer signs. Defining the threshold as the unique real zero and then deducing the integer signs is the correct statement, and is what the proof establishes. The covariance itself was independently corroborated by exact sequential seating with signed weights through n=7 at three parameter pairs, including negative theta. Replay the analytic argument at RESULT.md lines 42–56. The frozen check.py was inspected, not executed; it checks finite moments on four unweighted graph families, not the threshold uniqueness wording.

## originality

FAIL

The exact covariance and sign root follow directly from the prior size-biased deletion and insertion theorem, not merely from knowing the name or density of the model. Pitman–Yor Technical Report 433, §6.1, Propositions 32–33, gives a beta-distributed distinguished mass independent of the normalized residual PD(alpha,theta+alpha) frequencies. Mark any specified r-set using one member as the distinguished first sample; conditional on the distinguished mass, membership of the other labels is Bernoulli and their outside draws use the independent residual frequencies. This is the exact conditional theorem needed for the calculation, throughout the claimed parameter domain. Only hypergeometric pair incidences, linearity/exchangeability, and the quadratic formula remain. No prior verbatim printed threshold is asserted.

## value

FAIL

Edge-weighted co-clustering is a useful statistic, and the formula is a convenient explanatory example. But the graph generality here is only linearity and exchangeability, the covariance is a mechanical conditional mean from the existing deletion law, and the boundary adds the roots of that same elementary quadratic. Correcting the threshold wording would not leave a distinct substantive claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
