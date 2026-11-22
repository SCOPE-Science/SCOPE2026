---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

At frozen tree ec171182 verified the graph is a simple theta network with terminal edge plus two internally disjoint paths of lengths a,b>=2. A spanning tree omits one edge from two different terminal paths, giving ab+a+b trees; the unnormalized tree-indicator Walsh transform is (product of all edge signs)[XY+delta(X+Y)]. Taking kernel absolute average over independent Rademacher path sums X,Y and terminal sign delta gives E max(|XY|,|X+Y|). Checked integer correction exactly for zero variables and equal/opposite-sign nonzero integer pairs; binomial identities for E|S_n|, Pr(S_n=0), and Pr(S_n=1) yield the claimed parity-sensitive norm for ALL a,b>=2. Exact zeros solve (X+delta)(Y+delta)=1, so require both path lengths even and have the stated binomial multiplicity. An independently implemented connected-spanning-tree enumeration, complete Walsh transform and norm/zero calculations for all 24 test pairs from 2..6 with a+b<=11 matched the formula. In particular finite checks supplement, not replace, the all-parameter analytic proof. Translation-averaged projection optimality follows if optimizing all projections onto the range; the stated theorem directly concerns the indicated Fourier projection and convolution zeros.

## originality

PASS

A uniform signed-tree character formula, complete exact parity zero law, sharp endpoint norm in central binomial coefficients and parity-sensitive asymptotics for the two-path-plus-direct-edge theta family are absent from the inspected general matrix-tree theorem and other graph-family Walsh results. It is not a cactus because its three cycles overlap in edges.

## value

PASS

Unlike a routine fixed finite case, this is a uniform theorem for a natural noncactus bicyclic graph family with sharp parity classification of convolution invertibility and an exact endpoint projection invariant. The two long-path lengths represent independent structural degrees of freedom, and the closed central-binomial expression could be used as a benchmark for harmonic operators on graphic matroid bases. Distinct parity asymptotics reveal a genuine analytic boundary rather than a cosmetic table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
