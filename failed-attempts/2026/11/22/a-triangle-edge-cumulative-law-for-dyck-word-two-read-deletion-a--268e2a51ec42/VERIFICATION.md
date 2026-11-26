---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Proposition 9 supplies the exact-two distinct-deletion-output criterion. In a fixed-weight binary layer the alternating disagreement interval is even; deleting it gives a Dyck context, and both phases are admissible exactly at a positive marked vertex. The three disagreement masks satisfy XOR, and three nonempty interval masks with this relation must consist of two adjacent pieces and their uniquely longest union. Balance makes each piece even. The third vertex is an even splice of the two phases, so all three remain Dyck; the union, its cut and the third vertex recover all tuple data. Zero-height marks split into two Dyck paths, so H_r=(2r+1)C_r−C_{r+1}=binomial(2r+1,r−1) for r≥1, H_0=0. The weight 2(k−1) for a long edge of half-length k gives the sum, the cumulative law including n=1, and the formal generating functions. H_r~2rC_r and the eventual backward ratio bound less than one give dominated convergence with constants 4/9 for triangles and 2/3 for edges relative to nC_n; the incidence ratio tends to 2. Independently rebuilt the graph from actual output intersections through n=8, yielding E=(0,1,6,27,111,441,1728,6733) and T=(0,0,2,14,68,290,1172,4628). Inspected both supplied programs and VERIFICATION.md without executing them; the motif code counts and checks uniqueness through n=8 but guards its explicit Dyck-membership assertion by n≤7. This small documentation overstatement does not affect the analytic proof or the independent direct check.

## originality

FAIL

The exact Dyck census does not appear merely by substituting q=2 and N=2n in the unrestricted total. Nevertheless the claimed canonical classification and all quantitative consequences are immediate from the already explicit unrestricted unique-splice normal form restricted to the published marked-positive-height Dyck edges. Neither comparison source alone prints the claimed series; the two exact statements jointly cover it by the parity restriction and immediate summation below.

## value

FAIL

The exact triangle count of this natural confusability graph is a relevant statistic, but this particular increment is mechanically implied by the existing canonical triangle motifs and exact Dyck edge bijection: every eligible edge has the same fixed number of viable splices at each half-length, with no additional height interaction. The recurrence, coefficient list and limiting edge incidence are consequences of that weighted count rather than independently unresolved invariants in the record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
