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

# Verification and limits

Run `python3 verify.py` from the same directory as this file. Python 3.9 or later suffices and no external packages are used. The checker constructs actual full opinion-update matrices on small positive reciprocal connected bipartite graphs; uses exact rational Gaussian elimination to solve the perfect-prediction fixed-point systems at finite platform susceptibilities; checks the proposed stationary measure, even/odd weights, invariance of the weighted mean, the complete graph-level equilibrium, and star values. Its output on the reviewed source is: `PASS: 4752 exact stationary-measure and fixed-point identities on connected bipartite graphs; star hub weights 4/5 16/17 32/35`.

The mathematical proof covers all finite connected reciprocal bipartite graphs of arbitrary size and every integer \(K\ge1\), whereas the checker samples finitely many rational cases. The proof's essential noncomputational ingredients are two-part degree-weight reversibility, the identity \(H^2=abI\), uniqueness of the primitive Markov stationary law, and the Abel/Perron consensus limit. No finite experiment is treated as proof of an infinite quantifier.

Historical priority has not been exhaustively established: a related finite-round theorem may exist in unindexed or inaccessible sources. No independent scientific validation has been performed.
