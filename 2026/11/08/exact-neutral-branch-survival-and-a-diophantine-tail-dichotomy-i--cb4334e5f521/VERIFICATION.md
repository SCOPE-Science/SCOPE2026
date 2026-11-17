---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

At center parameter b=1 with 0<c<4 and uniform initial z in K_2, J preserves Q=x²-2(1-c/2)xy+y², and linear conjugacy turns neutral constraints into tangent strips about a disk of radius R=h sqrt((4-c)/4). The circular gaps g of the first N angles j alpha mod1 give area(K_N)=2R²/sin(theta) sum tan(pi g/2), hence P(L>=N)=sin(theta)/2 sum tan(pi g/2). Dense irrational normals yield a limiting ellipse with positive mass pi sin(theta)/4; rational alpha=p/q yields exact q-gon mass q sin(theta)/2 tan(pi/(2q)). For irrational angles f(g)=tan(pi g/2)-pi g/2 is bounded below by c*g³. Jensen gives >=const N^-2; bounded continued-fraction type gives max gap O(1/N) and matching upper bound, and unbounded successive denominator ratios yield N_k² D_Nk->infinity. Independent rational checks c=1,2,3 reproduced eternal-survivor masses .75,1,.75; these finite checks do not establish the Diophantine limit.

## originality

PASS

Gardini-Radi-Schmitt-Sushko-Westerhoff 2023 full public manuscript establishes exactly this three-branch map and the neutral b=1 rational invariant polygon/irrational invariant ellipse, so those geometric components alone are PRIOR. Relevant original section and conclusions were inspected. The submitted exact finite-horizon distribution over uniform K_2 and the sharp iff bounded-type rotation criterion for excess survival are not in the inspected primary statements. Related published rotation and tangential polygon geometry supplies ingredients but no covering exact first-departure law for this map was found. Qualified best-of-knowledge PASS for those substantive new quantitative conclusions.

## value

PASS

The map is an established model and its center bifurcation has a meaningful geometric metastability question. A full first-departure distribution with a positive survival atom and a sharp arithmetic tail dichotomy is a natural nontrivial quantification of neutral-branch persistence rather than a decorative area computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
