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

PASS: For the Ising wheel W_n=K_1 join C_n with J>0,h>0,n>=5, exact flip energies are 2J s(a-M) at the hub and 2J x_i(a-s-x_{i-1}-x_{i+1}) at the rim. Their nonnegative inequalities are necessary/sufficient even at ties. The s=+1 small-field words are cyclic maximal independent sets counted by Perrin P_n; s=-1 is their spin reversal with two even alternating words excluded by hub magnetization. At a=1, hub -1 gives Lucas L_n-2 epsilon_n; hub +1 counts cyclic words with no triples, positive magnetization cutoff Q_n. At 1<a<3, isolated negatives, run lengths and M cutoff give polynomial parity cases; at a=3 independent-set binomials give the boundary row; at a>=n hub flip determines 1,2,1 state counts. Entropies log plastic constant, log golden ratio, 0 follow automata and bounded polynomial counts. Independent direct brute force checked all nine sampled fields at n=5..11 (63 exact cases); it does not prove all n.

## originality

PASS

Best-of-knowledge: exact published same-object claims and primary literature compared by statement/implication, with strong prior ingredients acknowledged and residual risks retained. The complete accepted contribution is not shown covered by the inspected sources.

## value

PASS

PASS: The weak local-minimum landscape of a canonical frustrated wheel exhibits a discontinuous entropy enhancement precisely at a marginal field and a collapse immediately afterward. The all-field all-rim exact classification and parity effects describe a natural dynamical-stability observable, not a merely renamed Perrin sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
