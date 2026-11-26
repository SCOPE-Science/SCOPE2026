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

For B the indicator of the forbidden cells, double-centering gives the orthogonal projection PB because the discarded row/column effects pair to zero with all zero-margin matrices. Each feasible X satisfies <X-U,PB>=-k/(mn). Thus feasibility implies PB is nonzero, and Cauchy–Schwarz gives the degree bound. Its denominator comes from <PB,B>=k-sum(r_i^2)/n-sum(c_j^2)/m+k^2/(mn). For k at most min(m,n), each degree square sum is at least k, with simultaneous equality precisely for a matching. In that case every (PB)_ij on the mask is D/(mn), where D=(m-1)(n-1)+k-1. The candidate U-PB/D has zero forbidden entries, correct margins, and off-mask entries with numerators mn, n(m-1), m(n-1), or mn-m-n over mnD, all nonnegative. It is an equality case of Cauchy–Schwarz, proving attainment; strictness for every other feasible mask follows from the degree bound. For the divisible case, alternatively use ||X-U||_F^2=||X||_F^2-1/(mn) and apply Cauchy–Schwarz to the mn-k allowed cells of total mass one. Equality forces constant mass there, which has the required margins exactly when the mask is biregular. Its existence follows by giving each row a consecutive block of k/m distinct residues from the sequence 0 through k-1 modulo n; whole residue cycles give k/n in each column. These arguments address uniqueness and all claimed endpoints. The frozen line 60 calls the 941 optional cases nonmatching, but the script counts all feasible iterations, including matching and singleton masks, and may sample duplicates. That changes neither theorem nor equality proof.

## originality

PASS

The supported distinct contribution is the fixed-cardinality mask comparison, especially the exact sparse matching optimum and characterization, tied to a degree-sensitive certificate. The elementary allowed-cell mass bound and the general idea of projecting in a transportation polytope are not credited as independent new results. General fixed-mask minimum-norm work is directly relevant; its unresolved full-text scope is recorded rather than treated as evidence of noncoverage.

## value

PASS

The center-to-face distance is a natural Euclidean invariant for a fixed number of imposed zeros. The exact classification resolves whether collisions of forbidden positions can ever make the nearest face closer in the sparse regime, and quantifies the trade-off through degree dispersion. The attained bound distinguishes separated sparse masks from balanced dense ones and is more informative than a per-mask optimization routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
