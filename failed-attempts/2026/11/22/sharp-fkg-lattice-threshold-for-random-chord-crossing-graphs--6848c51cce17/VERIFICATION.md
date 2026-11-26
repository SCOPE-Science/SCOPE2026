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

The rank order of the iid atomless endpoints is uniform. Forgetting labels gives a uniformly random matching and replacing labels uniformly recovers the labelled edge states. For n=1,2 the lattice is a chain. At n=3 the masses by edge count are 1/3, 2/15, 1/15, 1/15 per state; the two elementary squares are strictly log-supermodular. Chain the elementary log-increments to obtain all Boolean lattice inequalities (or check all 64 pairs). At n=4 the exact labelled probabilities for empty, only 12, only 34 and only 12+34 are 2/15, 2/45, 2/45, 4/315, giving the defect ratio 6/7. The marginalization proof works even with zero masses: in its notation B≥C,D and AB≥CD imply A+B≥C+D by (B−C)(B−D)≥0 when B>0, with a separate trivial B=0 case. The induced first-four law is unchanged at larger n, so every larger law fails. Inserting positive edge activities multiplies both sides of each inequality by the same factors. Conditioning on the uniform endpoint gap of the common chord gives adjacent covariance E[(2L(1−L))²]−1/9=1/45; disjoint edges depend on independent endpoints. A fresh exact enumeration over permutations of individually distinguished endpoints, with one endpoint anchored and the opposite-arc test, checked all n=3 pairs, the n=4 witness and covariances, and n=5 projection.

## originality

FAIL

The sharp chord-MTP2 classification is mechanically recoverable from exact older chord-diagram forest enumeration, elementary lattice squares and standard marginal closure; absence of the MTP2 terminology in that enumeration does not restore originality. In particular, Acan's 2013 proof, Eq. (2.4.1), gives the decisive 2K2 count, not just a total two-crossing count. The same source supplies every probability needed for the three-chord base case. Positive modular tilts do not change any lattice defect in any law, and the indicator covariances are also already implied by known crossing statistics. This is a concrete prior implication, not an inference from a search miss or an inaccessible paper.

## value

FAIL

The distinction between pairwise nonnegative dependence and the FKG lattice condition is a well-motivated question, and the example is useful pedagogically. As submitted, however, the claimed new cutoff and exact defect are a recombination of the already available small-state counts with elementary finite checks and standard closure. The tilt invariance adds no model-dependent information, and the covariance is likewise an already determined statistic. There is no surviving new dependence invariant or structural behavior beyond those mechanical deductions in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
