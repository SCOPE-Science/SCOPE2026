---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A nonalgebraic type over named parameters is determined by its lower ideal and upper filter, with all lower points strictly below all upper points. Finite extension realizes such a pattern and homogeneity makes its realizations one complete type; algebraic equalities and parameter automorphism orbits are not counted. In family I (only A below and B above), allowed pairs correspond to independent sets of the omission graph H. In family II (some A above), no parameter is below; select a nonempty set S of A above and the set of B incomparable, with all their cross-pairs absent. This counts i(G)−2^b, and the dual counts i(G)−2^a. For a k-edge omission matching, family I allows three rather than four choices per defect, and families II and III contribute 2^a−1+k and 2^b−1+k because a nonempty omitted rectangle is one edge. This checks the exact count including k=0. For independent defects of bounded total intensity, the maximum defect probability tends to zero and the sum of squared probabilities does too, so the total count tends to Poisson(λ). The expected number of row collisions is at most half the total intensity times the maximum row intensity, and likewise for columns, so the matching formula applies with probability tending to one. Both sides diverge, hence the additive terms vanish on normalization. The deterministic three-family bound is three times the normalizer and gives all fixed moments in both models; the Poisson generating function gives the stated mean and variance. In the balanced outer regime the expected normalized family I equals E[(1−q)^(XY)] for independent Bin(n,1/2) X,Y; excluding the event min(X,Y)<n/3 costs at most 2exp(−n/18), and the rest is at most exp(−q n²/9). The other two normalized expected counts are each at most ((1+q)/2)^n. Markov therefore proves collapse for q→0 and n²q→∞; a no-defect union bound proves the lower side. No conclusion near q=1 follows. Independently written finite computations agreed on 682 small bipartite graphs, 46 matching cases and one direct expected-count enumeration. Frozen verify.py and verification_output.txt were inspected, not run; the finite computations corroborate the identities only.

## originality

PASS

The general finite identity, ideal/filter description and exact matching specialization are known or immediate and are excluded from the defended originality. The surviving contribution is the random normalized type spectrum: the rare-defect distribution with its moments, rectangular inhomogeneous extension and sharp balanced outer regimes, distinguished from merely averaging an independent-set count.

## value

PASS

The number of available complete named one-point patterns is a natural finite invariant of a homogeneous structure. The result determines precisely when a few random missing comparisons cause a macroscopic reduction, and the nonconstant limit for λ>0 quantifies actual sample-to-sample fluctuation that the mean by itself would miss. Identifying the three-of-four obstruction per isolated defect and the row/column conditions for its persistence makes the limit interpretable beyond identical omission probabilities. The result is restricted to this near-complete setting and does not imply a general random-poset entropy law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
