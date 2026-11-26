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

PASS

Maximality forces exactly one representative of every cluster. With equal cluster size, the independent core-first indicators and iid cluster minima independent of them give the stated greedy law on the induced candidate set B. Intra-clique label permutations act transitively on each compatible private output, giving the same uniform conditional kernel under both laws and hence exact reduction of TV to core TV. Under the candidate law conditioned on independence, B has the uniform MIS core marginal ν, and greedy leaves B unchanged. Writing ε=Pr(B not independent) and ζ for the greedy core law conditional on this event gives μ=(1−ε)ν+εζ. Since ζ puts no mass on the empty set, εν(∅)≤TV(μ,ν)≤ε. Here ε=1−Z_H(t)/(1+t)^r=|E(H)|t²+O_H(t³) and ν(∅)=1+O_H(t). This proves the sharp coefficient and the exact empty-event obstruction. For a complete core, symmetry puts all opposite-signed discrepancies on the singletons, giving equality in the empty-event lower bound. For unequal positive sizes the candidate order need not be uniform, but the first candidate must still be accepted if B is nonempty; independence of the indicators gives the asserted all-private probability and the weighted all-subsets sum strictly dominates its independent part precisely when H has an edge.

## originality

FAIL

Direct coverage in the earlier dated Resultary record c584f3577759: exactly the equal-size full law, uniformity iff edgeless, and complete-core TV. The fixed-core expansion for arbitrary H is an elementary corollary of this full law and its count of maximal independent sets; the heterogeneous all-private test only changes independent cluster-success probabilities. These are statement-level comparisons against the actual earlier result, not an inference from similar titles or from chronology alone.

## value

FAIL

The full law would be a useful structural observation if not already covered. Its surviving additions do not constitute a separate substantive result at this scope: the fixed-core bias coefficient counts excluded pairs after the exact-law mixture reduction, and heterogeneous rigidity is the same empty-output obstruction with variable weights. More tests, changed parameters, or relabeling do not rescue the covered finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
