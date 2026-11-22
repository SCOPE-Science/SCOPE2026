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

For uniformly deleting exactly m of n edges (1<=m<=n-1), the retained forest edge-root matrix has independent columns and crosspolytope-volume Jacobian sqrt(det B^T B); each path component on s vertices contributes determinant s. Marking a deleted cyclic edge gives a uniform positive composition (s1,...,sm) of n, hence exact Mellin coefficient and EX=Gamma(m)Gamma(n+m)/(Gamma(2m)Gamma(n)). The exact adjacent-m ratio (n+m)/(2(2m+1)) proves the one-third maximizing m and precise n mod 3 tie, including endpoints. For m/n->q in (0,1), the geometric( q_n ) conditioned-sum representation (conditioned at its mean) plus a two-dimensional lattice Fourier/local-limit argument gives Gaussian log-product fluctuations with regression variance tau(q)^2>0; uniform compact-q Taylor/aperiodicity bounds justify conditioning. Stirling gives F(q) and prefactor sqrt(2/(1+q)); KL tilt Q_q has the SAME geometric mean 1/q and proves F-qmu=q D(P||Q)>0. Independently enumerated all edge-deletion subsets for every n=3..10, computed component-size products and exact means/optima. Asymptotic theorem remains an analytic conditional CLT, not inferred from finite tests.

## originality

PASS

Schmutz–Shapcott 2012 primary theorem proves logarithmic-normal asymptotics of part-products under UNRESTRICTED number of parts in uniformly sampled S-restricted compositions, not compositions of exactly m=qn parts with the conditional-regression variance, nor cycle-forest volumes or sharp m optimum. Donzelmann et al 2026 analyze symmetric-edge polytopes on ER random graphs but study numbers of polytope edges and triangulation edges, not this random cycle deletion volume statistic. Classical matrix-forest determinant and rooted-forest composition enumerators provide background, not the linked optimum, conditional CLT and strict annealed-typical KL separation. No earlier exact coverage identified; priority remains best-of-knowledge, with conditional composition literature risk explicitly acknowledged.

## value

PASS

An exact graph-geometric invariant on a natural edge-percolated cycle model has a nontrivial finite optimum at deletion fraction one third and a rigorously quantified distinction between mean and typical intrinsic volume. The shared fixed-m composition mechanism, conditional fluctuation coefficient and KL rate form a mathematically motivated complete analysis; classical Gram determinants alone do not make it a textbook renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
