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

# Reproducibility checks

The exact finite necessary-condition enumeration runs using `python verify_conic_cutoff.py` with Python 3 and the standard library. It considers all nonnegative integer vectors consistent with the near-free \(r=k\) identity, pairwise Bézout, the singularity Tjurina counts, and Zieliński's orbifold inequality, for each \(k\in\{5,6,7,8\}\). Observed counts of admissible numerical profiles are 98, 37, 0, 0 respectively. Without \(D_4\) triples the counts are 1, 0, 0, 0; the unique five-conic vector is \((13,0,0,1,6)\). The script emits `CONIC_CUTOFF_ARITHMETIC_PASS`.

The exact explicit witness check runs using `python verify_four_conic_example.py` with Python 3 and SymPy. It verifies that the four quadratic forms are nonsingular and checks the displayed factorization identities for the four order-four contacts and the two residual four-point intersections. It constructs the coefficient matrix for homogeneous Jacobian syzygies in degrees zero through three over the rationals, with nullities exactly \((0,0,0,1)\). This proves the minimal syzygy degree is three for this exact rational polynomial. It emits `FOUR_CONIC_INCIDENCE_PASS 4_A7 8_nodes` and `FOUR_CONIC_MDR_3_PASS [0, 0, 0, 1]`.

The projective incidence classifications also follow from the exact identities printed in RESULT.md, together with Bézout and the nonvanishing discriminants of the residual pair restrictions. The code does not attempt to enumerate all complex conic arrangements, and a finite enumeration alone cannot prove an infinite nonexistence theorem. The universal restrictions are established by the argument in RESULT.md using published external inequalities. Independent scholarly and historical-priority audits have not been performed.
