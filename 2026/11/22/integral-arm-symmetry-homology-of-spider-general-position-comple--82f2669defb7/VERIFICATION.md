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

# Exact finite reproducibility checks

Run `python3 check_spider.py` from this package directory using Python 3 (standard library only). The checker constructs each test tree and its full all-pairs graph distance matrix, enumerates all subsets independently against the no-geodesic-triple rule, compares with the stated complete simplicial structure, and checks reduced mod-two Betti numbers using exact binary elimination. For every arm permutation in the tested groups it directly computes signed simplicial Lefschetz traces, then compares them with traces deduced from the claimed integral modules. Exact averaging checks geometric-quotient rational Betti ranks.

The test covers nine distinct pairs \((r,\ell)\): \((3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2)\). A successful run reports 981 simplicial faces, 336 signed group-element tests and `PASS`. These checks establish the finite cases only; the complete integral theorem for all arm lengths and numbers of arms follows from the stated chain and join proof. Mod-two ranks alone do not prove integral torsion-freeness. The checker does not establish independent review, novelty, or the absence of hidden quotient torsion.
