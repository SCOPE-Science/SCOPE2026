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

Direct elimination of the two equilibrium ODEs at r=Y/X proves X=(ah-cr)/(h+r²), c=b+v(1-hq), u=r(b+v+rX)/h, and u_c=a(b+v)/c. Differentiation yields the published strictly positive lower bound for u'(r); total T-a=r[(ah-c)-(a+c)r]/(h+r²) has derivative numerator h(ah-c)-2h(a+c)r-(ah-c)r² and exactly one positive critical root if ah>c, none otherwise. Perron eigenvalue sign at origin and Dulac divergence -1/Y-1/X-vq/X²-hu/Y² establish extinction/global positive attractor with boundary behavior. Mutant invasion determinant simplifies exactly to (c+Y)(u_hat-u); resident trace is negative. Verified ODE residuals, derivative identities and determinant independently symbolically with SymPy (all zero), after reading actual RESULT.md and 3,664-byte CHECK.py. The finite rational script is supplemental, not proof.

## originality

PASS

Wu (2016) has essentially identical two-patch loss equations and fixed reverse-migration trait but assumes both intrinsic patch resources positive and addresses evolutionarily stable *migration*, not negative-growth sink total biomass optimization. The mutant selection part is largely a specialization/algebraic consequence of Wu; not claimed independently novel. Conservative source-sink biomass work addresses h=q=1; full joint interior optimum/physical T in the two-loss sink regime not found in accessible primary texts. Strong related-model risk retained.

## value

PASS

A physically meaningful source/sink biomass-management boundary specifies whether migration loss can be outweighed by net biomass gain and proves uniqueness of optimal export. It distinguishes maximizing total population from the direction of rare-mutant selection with two independent survival losses. Unlike the known qualitative disagreement, its sharp loss-dependent source-sink criterion and quantitative optimum can be directly used in this precise model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
