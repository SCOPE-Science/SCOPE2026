---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Verified normalized area polynomial Q=XYZ+(1-X)(1-Y)(1-Z), six mixed corners, and exact local chart Q=xi eta+omega(1-xi-eta). For p=xi eta=ta and xi=p^u, eta=p^(1-u), omega=tb, independently computed |det(d(xi,eta)/d(p,u))|=|log p|, giving t²|log(ta)| da du db. On fixed delta=1/5 box, 0<a<=5/4, 0<b<=5/3, almost-everywhere indicator converges to 1(a+b<1,0<u<1), dominated by C(1+|log a|). L1 local subprobability density/(t² log(1/t)) tends to unit density on 3D simplex chart, mass 1/2 per corner. Maesumi exact scalar F_Q(t)=3t² log(1/t)+O(t²) makes outside-corner conditional mass negligible; normalizing yields corner 1/6, U uniform, density 2 on a+b<1 jointly in TV. Q/t->Beta(2,1) follows from A+B but not novel. The affine-invariant side-uniform domain and finite-threshold delta marking checked.

## originality

PASS

Maesumi 2018/2019 established same polynomial and scalar CDF (hence Beta tail); neither the full primary paper nor related site sampled inclusion depth theorem supplies conditional marks, uniform log splitting and Dirichlet area-budget independence. A previously published square-interior near-maximal-area result has similar logarithmic-product/Dirichlet technique but different sampling distribution and opposite extremal event; it does not imply this law as a corollary.

## value

PASS

A well-motivated marked rare-event geometry theorem: the known logarithmic small-area tail hides six inequivalent degeneration mechanisms and a conditional shape law. A full total-variation limit, independent scale splitting, and Dirichlet budget for a natural geometric model are precisely useful beyond an exact scalar area distribution. No novelty claimed for scalar tail or Beta marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
