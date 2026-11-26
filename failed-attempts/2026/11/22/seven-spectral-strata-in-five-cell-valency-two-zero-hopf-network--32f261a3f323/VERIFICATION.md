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

The residual eigenvalue is real and r=tr(A)-2; the norm bound and simplicity leave r in {-2,-1,1}. Monic integer division gives integral q in {1,2,3,4}. I independently enumerated all 759,375 row-multiset matrices in Python, using traces A through A^5 as exact power sums (Newton identities give the polynomial), not determinant interpolation. I partitioned the accepted labeled states into full simultaneous-permutation orbits and computed reachability by Boolean transitive closure. The seven rows (labeled, classes, strong labeled, strong classes), in the claimed order, were (1800,15,600,5), (1620,15,420,5), (120,1,120,1), (360,4,60,1), (7620,66,3420,29), (3540,30,1140,10), and (6900,60,540,5). All 21,960 accepted matrices were weakly connected, also a consequence of the simplicity of eigenvalue 2: disconnected weak components would each have row sum 2. Using rows as outward lists reverses every arrow and does not change either connectivity predicate. The analogous independent four-cell run found only q=1, with nine isomorphism classes; fewer than four cells cannot contain the four distinct required eigenvalues. The first-at-five claim follows.

## originality

FAIL

A distinct same-date Resultary synchrony census packages a complete five-cell representative database for exactly the assigned zero-Hopf spectral family, with r, omega_squared, labeled orbit sizes, and the full matrices. Aggregation and elementary reachability applied to its 191 stored records reproduced every entry of the seven-stratum table, not just the totals. The high-frequency strata and their strong witnesses are in that exact database; their first-at-five interpretation follows immediately from the known four-cell q=1 result and the minimum dimension. The database is distinct from the assigned record; its shared date and its reference to an earlier spectral census do not establish publication order or identify that earlier record.

## value

FAIL

A complete exact five-cell zero-Hopf catalogue is well motivated as the dimension after the nine-class baseline. But the assigned aggregate and its only additional interpretation, the q=3,4 onset, can be read off the exact same-family catalogue with grouping, reachability and the known four-cell spectrum. This submission does not add a structural criterion for the frequencies, a new invariant, or a separate result whose scientific value survives that exact coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
