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

Conditional on retaining the root, a retained target is reachable exactly when no consecutive pair of its ancestors is deleted. Jump over isolated deletions for sufficiency. For necessity, if a deleted vertex y has deleted parent x on the ancestral path, an edge leaving the strict-descendant subtree of y can exit only from a child of y to y or x; both are deleted. For an independent one-type reconstruction, collapse each deleted bridge between two retained vertices. Each retained individual discovers one effective child from each retained original child, or the retained grandchildren through an original child that is deleted. Discovery of a retained successor reveals no offspring below it. Different successor subtrees are disjoint, so the retained genealogy is Galton–Watson, and the cluster size is its total progeny. Its mean is R=mp+m²p(1−p). For 0<p<1 the effective offspring variable has positive probability of zero (delete all original children and grandchildren, which are finite almost surely), so at mean ≤1 extinction is almost sure, and above 1 survival has positive probability. The quadratic crosses 1 once in (0,1), at q_m as stated; p=0 gives the empty cluster and p=1 reduces to the original supercritical tree. The geometric progeny mean gives 1/(1−R) subcritically and divergence at criticality. With η finite, the individual per-original-child contribution has mean u=p+(1−p)mp and second factorial moment (1−p)ηp². For the random sum the second factorial moment is B(p)=ηu²+m(1−p)ηp². Its PGF is φ(pz+(1−p)φ(1−p+pz)); the finite-second-moment Taylor expansion (uniform near q_m by the composed expansion of φ at 1) gives R h−B(p)h²/2+o(h²) on the survival side. The positive solution tends to 0 as p decreases to q_m, by continuity of the PGF and the sole critical fixed point. Hence h/(p−q_m) tends to 2R′(q_m)/B(q_m), with u(q_m)=1/m and R′(q_m)>0. Conditioning is essential: unconditionally multiply by p and obtain residue q_m K for the survival slope. The expected level recurrence also follows by partitioning the feasible ancestral words by their final one-site step or deleted/retained two-site step. Inspected the frozen checker but did not execute it. Replay: python3 -B /workspace/review_evidence/independent_checks.py 1, testing 1,024 site assignments on an irregular tree, 11,264 memberships, 11 exact rational marginals at p=1/3 and the effective offspring moments by exact convolution for four p values. Finite corroboration only; the genealogy and expansion establish the unbounded theorem.

## originality

PASS

The distinct claim is the exact annealed Bernoulli site threshold, susceptibility and finite-second-moment slope on the grandparent graph of a BGW tree. Generic branching-process machinery, not these particular formulas, is background. The closest verified same-graph thresholds and susceptibility calculations concern independent bonds.

## value

PASS

Site versus bond dependence on the same family of random graphs is a motivated contrast. The exact threshold fixes the role of the first moment, whereas the critical survival slope detects the second factorial moment and the explicit susceptibility demonstrates a divergent mean despite almost-sure critical extinction. These are natural observables across all allowed offspring laws, not a numerical value for just one tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
