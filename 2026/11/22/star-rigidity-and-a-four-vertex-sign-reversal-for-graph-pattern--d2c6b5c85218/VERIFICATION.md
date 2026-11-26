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

For each column, the supported columns of A are independent by positive definiteness. In a tree the distance-two row sets of different neighbors of j are disjoint. Squaring their residuals yields s_i x_i², leaving one central residual z and one term (w_ij x_0−d_i x_i)² per neighbor. Eliminating the x_i in the normal equations gives r_i x_i=w_ij(d_i x_0−z), (1+V_j)z=1−D_j x_0, and D_j z=E_j x_0. Since w_ij<d_i and r_i≥d_i², the subtractions from d_j total less than d_j (empty sum handled by the singleton case); thus D_j>0 and Δ_j>0. This proves the local sign formula, including the diagonal. At a hub E_j=0, and at a leaf with one neighbor the sign numerator reduces to d_i d_j−w_ij²>0. At unit weights, ((1+μ)d_i+s_i)/r_i<1 by the positive difference (1+μ)d_i(d_i−1)+μs_i, so (1+μ)D_j−E_j>μ(deg(j)+1+μ)>0 whenever j has a neighbor. For the weighted P4, in column 2 take r_3=5t²+4t+1, D_2=t+3/2−t²(2t+1)/r_3, E_2=t⁴/r_3 and V_2=1/4+t²/r_3. Substitution gives the stated rational expression, in particular −357/124695=−7/2445 at t=9. Its denominator has positive coefficients and the numerator has exactly one positive zero (one sign change and opposite endpoint signs). Fixing the enlarged support at zero attachment weights causes no discontinuity because the relevant Gram matrix remains positive definite; the columns outside the P4 cannot change this coefficient at the limit. Every nonstar tree has such an induced P4. The supporting exact-arithmetic checker was inspected, not run; the proof covers the full quantifiers.

## originality

PASS

Standard SPAI elimination is prior; the new contribution is the weighted-tree sign criterion and topology classification with its sharp witness and the unweighted guarantee. Closest indexed sign reversals concern different matrix constructions. The inspected M-matrix result assumes rather than proves optimizer nonnegativity.

## value

PASS

This resolves exactly when graph structure alone guarantees positivity for a standard approximate-inverse objective on trees. The negative coefficient despite strict diagonal dominance separates inverse positivity from sparse approximation positivity. The all-unit-weight theorem, minimal heterogeneous obstruction, and local criterion distinguish the regimes and can be used without computing a dense inverse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
