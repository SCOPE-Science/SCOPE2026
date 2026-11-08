---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

The exact finite computation is run with `python check_exact_random_gh.py`. The script directly enumerates every labelled simple graph and every three-color initial state for \(1\le n\le5\), calculates integer-weighted joint probabilities for both a uniform three-state distribution and a biased \((1/2,1/3,1/6)\) distribution, and compares against an independently implemented multinomial/binomial formula using `fractions.Fraction`. For every connected graph/coloring pair it also directly iterates the original three-state update for three steps, checking primitive-period-three equivalence to the successor-neighbor condition.

The finite critical-window simulation is run with `python check_poisson_window.py`. A fixed seed generates independently sampled undirected edges and initial colors; the script checks deficiency counts and directly iterates successful states. It compares the empirical means and zero-mass frequencies with the predicted Poisson limits at \(n=300\). No convergence proof is inferred from the simulation.

Captured standard output files are `check_exact_random_gh.out` and `check_poisson_window.out`. No third-party Python packages are required. All calculations can be reproduced offline. The proof's critical steps—mutual independence of deficiency indicators conditional on colors, class-size concentration, and connectivity—are analytic and do not depend on a finite census.

The checks do not establish anything about individual-graph (quenched) periodic fractions, asymptotic basin structure, other primitive periods or global literature priority. Independent external validation has not been performed.
