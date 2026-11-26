---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

By exchangeability the two-version probability of a prescribed diagonal choice is a/k and of a prescribed off-diagonal choice is (1−a)/(k(k−1)). For the cross moment the same-cell, nonattacking, same-row and same-column contributions respectively are a_m b_n, (m−1)(n−1)/(mn), (1−b_n)/m and (1−a_m)/n. Subtracting one gives the covariance product; the variance follows from nonattacking pairs in one version. For distinct cells with repeated rows or columns, a compatible fixed mark assignment forces two singleton-version cells in any repeated row or column, in opposite versions, with off-diagonal paired-choice probability at most 1/(k(k−1)); common marks cannot participate in a repeated row or column. Multiplying over independent rows and columns bounds each fixed r-cell joint event by O_r((mn)^−r); the proportion of non-nonattacking tuples is O_r(1/m+1/n). Nonattacking tuples give precisely the product rare-event factorial moments in the limit. The same argument for marks in disjoint spatial rectangles yields their independent Poisson limits by Riemann sums. First moments bound total mass on the compact square, giving tightness, and boundary-null rectangles determine the limit. No ratio condition is used. Independently reconstructing the payoff refresh formula, with j of the candidate's competitors refreshed, a retained candidate must be largest in a pool of k+j independent draws. For a refreshed candidate, the pool has k+j+1 draws, its two draws include the global maximum with probability 2/(k+j+1), and conditional on which one wins its partner must rank first among the other version's k draws, with probability 1/k. Summing over j gives the frozen finite expression. With L retained out of k, this also gives common-argmax probability E[(L+2(k−L)/k)/(2k−L)]. The binomial concentration of L/k about q, the uniform bound of 2/k on the second contribution, and bounded continuity of x/(2−x) prove the limit including q=0,1. Substituting yields the three stated intensities and their bivariate Poisson consequences, including 1/9 shared intensity at half retention. Independent exact rank and map checks passed.

## originality

PASS

The strongest inspected parallels give a single-game count law, within-game dependent payoffs, different perturbations, or overlaps of independent matchings. They do not supply the two-version agreement product, independent common and exclusive spatial populations, and coordinate-retention specialization for these reciprocal maps. The familiar one-game Poisson marginal and abstract bivariate Poisson construction are not awarded novelty by themselves.

## value

PASS

Equilibrium robustness cannot be read off unchanged marginal counts. The exact factorization makes that dependence measurable by two observable agreement probabilities, while the limit distinguishes shared equilibria from appearances and disappearances with locations. The distribution-free refresh specialization quantifies the cost of perturbation in natural independent-payoff games, even for highly unbalanced growing action grids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
