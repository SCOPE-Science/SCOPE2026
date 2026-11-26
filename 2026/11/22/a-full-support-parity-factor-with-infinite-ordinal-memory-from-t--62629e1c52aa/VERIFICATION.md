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

Solving T_t(x)=x gives the internal threshold u=1/(2−t)>t. Each allowed sign-to-sign branch covers its entire destination interval affinely. Thus a uniform distribution on the current interval conditioned on any positive-probability finite history pushes, on conditioning on the next sign, to uniform there again. State 0 forces a rise, and the ascending-to-ascending probability is (tu)/u=t. This gives the claimed stationary Markov matrix with genuinely nonconstant transition rows. Independence gives the product law; restrict to hidden states 00 and 11 for parity-zero runs, with Q=[[0,1],[ab,cd]], and stationary row (ab,1)/D. In scaled notation s=ab, h=cd, the first determinant times D² is (1+s)[h(2s+h)+s(1+s)]−(2s+h)²=s(1−s−h)² with 1−s−h=c+d−2cd>0. The recurrence propagates it by −s; the two simple eigenvalues have distinct moduli, with the positive Perron component nonzero by positivity. Hence r_n varies for arbitrarily long prefixes, impossible under the finite-order conditional definition. All words are legal as hidden 11 can persist, both one-parity states can alternate, and either connects back to 11. The product hidden transition is primitive, and exponential strong mixing passes to the parity factor. For the trajectory maps themselves, exponential decay for Lipschitz versus bounded observables follows because every length-j product branch maps affinely onto the whole square and has diameter O(max(c,1−c,d,1−d)^j); averaging a Lipschitz observable on each cylinder and changing variables bounds its covariance with any bounded observable at time j. This is a regular-observable dynamical mixing claim, not uniform probabilistic strong mixing of the exact real-valued trajectories. Independent finite reproduction by forward affine partitioning at preimages of t and u, tagging each affine cell by its sign word and summing cell lengths, gave F_1,…,F_6=(5/9,1/3,2/9,5/36,13/144,11/192) at c=d=1/2 and (23/40,3/10,141/800,783/8000,279/5000,25137/800000) at c=2/5,d=3/4. All parity words at those lengths had a path and all adjacent available recurrence/defect equalities checked exactly. The frozen inverse-interval checker was inspected rather than executed; neither finite check proves the all-length real-parameter assertion.

## originality

PASS

Qualified pass for the two-source XOR theorem with its all-interior order obstruction and run law, not for general hidden infinite memory or single-map ordinal coding.

## value

PASS

The natural ordinal coarse-graining distinguishes full symbolic support, exponential loss of dependence with lag, and exact finite-order prediction. The all-parameter alternating difference and its explicit asymptotic predictability rate give more than the existence of a hidden Markov counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
