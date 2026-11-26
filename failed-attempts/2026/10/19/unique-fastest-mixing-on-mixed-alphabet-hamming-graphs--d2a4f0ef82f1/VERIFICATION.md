---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An independent trace argument works directly on the full feasible set. Let L=I−P, α_i=(q_i−1)/q_i, and x_i=2Σ_{e in direction i}P_e/(Nα_i). If μ(P)≤u, then (1−u)I≤L≤(1+u)I on the mean-zero space. The normalized trace on the coordinate-i mean-zero sector is x_i: an edge in direction i has squared projected incidence-vector norm 2q_i/N, while all other edges project to zero. On the all-coordinate mean-zero tensor sector the squared projected norm of a direction-i edge is 2∏_{j≠i}α_j; its normalized trace is therefore Σ_i x_i. Thus x_i≥1−u and Σ_i x_i≤1+u. Nonnegative diagonals also imply Σ_i α_i x_i≤1 by the total off-diagonal mass. These bounds give u≥1−t, attained by the stated chain whose eigenvalues off constants are 1−kt for 1≤k≤d. At equality one of the aggregate bounds forces every x_i=t; this also holds at the transition. The nonnegative operator L−tI on the mean-zero space has zero compressed trace on each coordinate-i sector, hence vanishes on the sector. Restriction to each i-fiber gives the Laplacian t(I−J/q_i); its entries force all edges, and row sums force holding. The strict holding inequality and the binary-factor corollary follow by substitution. Scope is symmetric matrices (not arbitrary nonsymmetric chains); in the concluding proof sentence 'nonsymmetric' should be read as 'non-invariant under graph symmetries.' Frozen verification notes, requirements and source checks were inspected, not executed; the reduced LP and finite spectra are not a rigidity proof.

## originality

FAIL

The full stated result has demonstrable equivalent coverage in a distinct indexed stronger theorem. Its Fiedler-edge condition is automatic for complete graphs; specialization gives precisely the same allowed chains, unique edge and loop weights, optimum, transition and corollaries for every tuple. A second distinct indexed result gives the same rigidity theorem literally on the heterogeneous d≥3 subdomain. These comparisons establish equivalence/implication in the current corpus, not chronological priority, provenance or dependence; both related paths bear later calendar dates than the frozen path. The verdict is not based on the inaccessible article or merely on the equal-alphabet classic result.

## value

PASS

As a mathematical result the unrestricted rigidity is useful: a symmetry reduction normally only produces an invariant optimum, while this identifies every admissible edge and holding weight, including at the exact no-holding boundary. The covered claim cannot be accepted as a distinct contribution, and no narrower valuable mathematical remainder was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
