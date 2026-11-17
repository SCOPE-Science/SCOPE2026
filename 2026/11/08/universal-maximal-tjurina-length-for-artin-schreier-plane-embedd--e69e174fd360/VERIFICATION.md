---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The affine chart Z=1 is nonsingular because the derivative of y^q-g(x^p)-x with respect to x is -1. At infinity the leading coefficient forces P=[0:1:0] as sole point. In Y=1 coordinates, h=z^(d-q)-G(x,z) consists solely of p-th powers, so f_x=-z^(d-1), f_z=-(d-1)x z^(d-2). In R=k[[x,z]]/(h), z is a nonzerodivisor because h(x,0)=-a_m x^d !=0. The short exact sequence R/(z^(d-2) m) over R/(z^(d-2)) has extra k length one, giving 1+d(d-2)=(d-1)^2. Independent exact finite-field Groebner calculations for p=2 and p=3 with d=6 yielded length 25, supporting the unrestricted regular-sequence proof.

## originality

PASS

Kollár 2026 constructs the same Artin–Schreier plane embedding and studies affine identification and characteristic-two cusp properties. The cited construction is prior and not credited. His inspected examples do not state this uniform all-characteristic/all-polynomial local Tjurina algebra length. General maximal-Tjurina literature in characteristic zero concerns different singularity hypotheses; this positive-characteristic wild Jacobian thickness is not inferred from those results alone. Best-of-knowledge original exact invariant, with risk that a standard intersection-number lemma already implies it.

## value

PASS

The precise local nonreduced Tjurina length is a natural invariant in positive-characteristic wild singularities, independent of q and all lower coefficients, and gives a complete family-wide numerical answer. The formula is derived by a short nonzerodivisor length argument but is not just an arbitrary finite sample or a renamed parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
