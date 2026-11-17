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

For the height-one 2m-vertex crown with 2m edges, twisted degree-one cocycles correspond to edges allowed by the dihedral symmetry, and degree-zero cochains to its fixed vertices. For identity, connected weighted-cycle incidence rank is 2m-1 iff holonomy=1, else 2m, giving dimensions 1/0. Nonidentity rotations have no fixed vertices; ±1 rotations allow m edges, other shifts zero. Each reflection allows four edges and two disjoint nonzero fixed-vertex coboundaries, giving dimension 2 in all characteristics. Unit groups modulo central scalars and multiplicative holonomy classes yield |Aut A|=2m q^(2m)(q-1)^(2m). Classes then give Pr[m]=1/m, Pr[2]=1/2, Pr[1]=1/(2m(q-1)), residual Pr[0], and E[d]=2+1/(2m(q-1)) while weak limit has mean 1. Independent weighted cochain ranks verified through m=12 over p=2,3,5 (873 cumulative crown assertions); source independently provides defining skew-Leibniz checker. The all-m proof is structural, not finite extrapolation.

## originality

PASS

Fornaroli–Khrypchenko, arXiv:2307.08439 Corollary 3.8, already give the general twisted-cohomology reduction and isolated small-crown Examples 3.14–3.15, 3.22. Neither the all-m dihedral edge/coboundary ranks nor the full automorphism-uniform distribution and rare-large-dimension limit appears there. Related crown Lie-automorphism theory addresses a distinct property. No Resultary match covering the new full spectrum beyond the assigned record.

## value

PASS

Outer twisted derivation dimension is a natural obstruction to innerness. The complete crown-family automorphism classification discovers a genuine symmetry-sensitive 0/1/2/m spectrum and a rare-event failure of uniform integrability; this is a meaningful infinite-family cohomological invariant, not a routine one-off substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
