---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. For an unweighted connected tree with m>=2 edges, bipartite edge orientation makes K=B^TB SPD, entrywise nonnegative and irreducible with simple Perron eigenvalue L and u>0. At h=2/L the exact integral Taylor remainder for cos is strict whenever sin z !=0 despite the vanishing quadratic descent bound. Compactness and steps tending to zero force every orbit to a single binary equilibrium. At every non-antiphase equilibrium KD_q is similar to symmetric K^(1/2)D_q K^(1/2) and has a positive eigenvalue, hence expanding multiplier; a nontrivial real-analytic Jacobian determinant ensures preimages of null local center-stable sets are null. This global endpoint component is also known in stronger form from the prior 2026/11/1 Resultary theorem; its coverage is acknowledged, not claimed new. The genuine additional critical law uses A=I-2K/L, a simple -1 Perron center and stable transverse spectrum. Odd center graph y=au+a³w+O(a^5) has w=-(I+A)|u-perp^(-1)QK(u³)/(3L), giving a'=-a+ca³+da^5+O(a^7), c=Σu_i^4/3 and d=Σu_i³w_i-Σu_i^6/60. Thus 1/a_{n+1}²-1/a_n²=2c+(2d+3c²)/W_n+O(W_n^-2), W_n=a_n^-2, yielding W_n=2cn+b log n+H+o(1), b=(2d+3c²)/(2c) for all basin orbits outside the codimension-one strong-stable fiber. For the four-vertex path exact w verifies c=1/8,d=-(1+sqrt2)/768,b=(17-sqrt2)/96. Own independent exact symbolic calculation reproduced the nontrivial coefficient. This is an asymptotic local formula plus a.e. basin conclusion, not a finite-time global error rate.

## originality

PASS

Originality assessed against semantic published research and the listed primary sources; substantial previously established components explicitly credited. Global endpoint dynamics are completely covered, but the general tree-specific fifth-order Perron logarithmic coefficient survives as an independently meaningful non-implied part.

## value

PASS

PASS for the surviving unique log law, not the already-covered global endpoint theorem. The rate of approach along a nonuniform graph's critical Perron mode is mathematically motivated in synchronization, and the graph-dependent fifth-order correction is a genuine structural invariant requiring transverse center-manifold analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
