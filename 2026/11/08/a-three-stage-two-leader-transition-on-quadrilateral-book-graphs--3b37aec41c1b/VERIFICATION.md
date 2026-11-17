---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For each integer m>=2, B_m has an edge joining two hubs and m length-three paths between them. The grounded Green identity J({s,t})=(sum_z R_zs+sum_z R_zt)/2 - (2m+2)R_st/4 - sum_z (R_zs-R_zt)²/(4R_st) follows by minimizing current-splitting energy. Five resistance values and six symmetry orbits yield exactly the rational formulas H=4m/3, A=(8m²+33m-5)/(3(2m+7)), B=(8m²+45m-17)/(6(m+5)), C=2(7m²+21m-10)/(3(2m+7)), D=(12m²+25m-29)/(6(m+3)), E=2(4m²+9m-11)/(4m+13). Explicit positive gaps J_A-J_H=5(m-1)/(3(2m+7)), J_C-J_H=2(m-1)(3m+10)/(3(2m+7)), J_D-J_E=(4m²+17m+19)/(6(m+3)(4m+13)), plus J_B-J_H=(5m-17)/(6(m+5)) and J_E-J_H=2(m+3)(4m-11)/(3(4m+13)) and signed E-B difference, prove all three regimes. Independently inverted every two-leader grounded matrix at m=2..6, giving m=2: 2 optima J=46/21; m=3: 6 optima J=95/24; m>=4 both hubs J=4m/3. IMPORTANT minor proof typo in RESULT.md: its argmin current fraction alpha is printed as (R_zs-R_zt+R_st)/(2R_st) but direct differentiation gives (R_zt-R_zs+R_st)/(2R_st). Its boxed minimum-energy Green formula and all six costs are correct, as confirmed by independent inversion; correction of the intermediate alpha sign does not alter the final claim. This is explicitly recorded, not silently concealed or treated as formal proof certification.

## originality

PASS

Fitch–Leonard's all-graph joint-centrality expression is the known general transformation of this objective, not an explicit optimization result on K_(1,m)×K2. Patterson–McGlohon–Dyagilev treat paths and rings. The quadrilateral book differs from triangular friendship/windmill and the single-hub diamond bouquet by its two hubs and four-cycle pages. The exact m=2,3,>=4 optimal-type transitions require nontrivial six-orbit resistance evaluation and were not present in inspected prior statements.

## value

PASS

The Cartesian product of a star with an edge is a canonical series-parallel graph family with two common hubs, modeling multiple parallel pathways. Two perfect leader placement is an intrinsic exact inverse-trace design problem. The nonmonotone geometric change in optimal pair type at two successive page counts and complete rational ties/inequalities is a meaningful natural structural classification, not an arbitrary finite-size calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
