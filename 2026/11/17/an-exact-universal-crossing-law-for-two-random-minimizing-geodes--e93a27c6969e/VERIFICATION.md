---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Nearest-lift angular differences U,V are independent uniform(-L/2,L/2), and each vertical pair is independent uniform[0,H]. On overlap of vertical ranges length h, relative horizontal coordinate traverses a lifted interval length ell=h|U/a-V/b|<=|U|+|V|<=L. Its starting phase is Haar-uniform modulo L, yielding conditional crossing probability ell/L and at most one intersection outside null degeneracies. Averaging two centered uniform slopes of half-ranges L/(2|a|),L/(2|b|) yields 1/(4m)+m/(12M²), m=min(|a|,|b|), M=max. The normalized vertical interval-overlap kernel is J(A,B)=r s(1-s)-r³/3 with r=min(A,1-A,B,1-B) and s=max(min(A,1-A),min(B,1-B)). Integrating over 0<A<B<1 after four-region partition yields exact 65/216-2log2/9. Anisotropic scaling of x,y preserves intersections and nearest angular lifts, not a claim of isometry. The proof is exact and all-ratio.

## originality

PASS

On the stated bounded primary literature and Resultary comparisons, the exact final claim is neither stated nor directly implied by the identified relevant antecedents; known special cases and methodology were credited. This is best-of-knowledge, not proof of global novelty. See four explicit implication checks, actual source inspections, and residual risks.

## value

PASS

This exact crossing probability is a natural integral-geometric invariant of two minimizing arcs on the flat cylinder with boundary, with unexpectedly aspect-independent constant and single-intersection rigidity. It differs substantively from closest closed-torus, round-sphere, and random-walk segment laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
