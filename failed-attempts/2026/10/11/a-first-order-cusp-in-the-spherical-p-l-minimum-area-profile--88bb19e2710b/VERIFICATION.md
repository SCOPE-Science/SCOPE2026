---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The statement is correct for spherical convex bodies on S² with minimum width 0<w<pi. The Freyer–Sagmeister sharp classification gives regular minimizing triangles for 0<w<=pi/2 and polars of spherical Reuleaux triangles for pi/2<w<pi. For acute w, spherical Pythagoras yields cos(s)=cos(w)cos(s/2); putting c=cos(w) and q=cos(s) solves q=(c²+c sqrt(c²+8))/4, and equilateral spherical cosine law plus spherical excess gives area 3 acos(q/(1+q))-pi. For obtuse w, put t=pi-w; the spherical polar identity gives area(U_t°)=2pi-per(U_t), with each of the three small-circle arcs of length sin(t)acos(cos(t)/(1+cos(t))). At the transition both branches give pi/2. One-sided differentiation gives 3/sqrt(2) and 3; their difference is positive. Independent symbolic calculations reproduced all four exact limits, and also checked the boundary limits M(w)->0 as w->0+ and M(w)->2pi as w->pi-. The source code verify.py was inspected as data, not blindly executed. The bounds 0<w<pi and the meaning of minimum spherical width are essential; nothing about smooth dependence of optimizer shapes is proved.

## originality

FAIL

A decisive pre-assignment primary source was missed by the submitted self-review: Fodor and Sagmeister, arXiv:2606.02882v2 (dated 6 October 2026), Lemma 4.2 on page 12 and its explicit sharp extremal-perimeter formula on page 13. For a spherical convex body of diameter D, that lemma gives the exact maximum perimeter P(D), with Reuleaux-triangle extremizers for D<pi/2 and regular-triangle extremizers for D>=pi/2. The lemma itself states the polar duality per(K)=2pi-area(K°), so the assessed optimal-area function is identically M(w)=2pi-P(pi-w), with no new geometric inequality required. The explicit prior formulas are P(D)=6 sin(D) asin[1/(2 cos(D/2))] for D<pi/2, and P(D)=6 acos[(cos D+sqrt(cos²D+8))/4] for D>=pi/2. Differentiating at D=pi/2 yields P'_-(pi/2)=3 and P'_+(pi/2)=3/sqrt(2), and hence the assessed left/right M slopes are respectively 3/sqrt(2),3. Thus the complete exact function and the slope discontinuity are elementary reparametrized consequences of an earlier published stronger scalar extremal profile, not a separately original result; absence of the word cusp in the earlier paper does not avoid implication.

## value

FAIL

Differentiability across the natural optimizer-regime transition is a motivated question, and an exact first-order cusp would be a legitimate structural boundary if it were not already determined by a published complete scalar profile. Here the 2026-10-06 Fodor–Sagmeister sharp maximal-perimeter profile is exactly equivalent to M(w) for all widths, by M(w)=2pi-Pmax(pi-w). Its derivative jump is obtained by differentiating two explicit elementary formulas at D=pi/2. The assessed submission supplies no new variational theorem, finite cutoff, stability bound, previously unknown independent invariant, or nontrivial analysis beyond this textbook calculation. The exact slopes are correct but a routine recomputation of an already published complete extremal function, so no separate scientific contribution survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
