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

The actual package fixes F4 polynomial basis and 10 cubic monomials, normalizes scalar classes via first nonzero coefficient, and tests every one of (4^10-1)/3=349525 forms on all 21 PG(2,4) points and 21 lines using gradients and field operations. Independently implemented a separate exact C++ incidence census: 248928 forms have only nonsingular rational zeros, precisely 6328 are each blocking and tangent-filling, intersection 6328, symmetric difference 0; 280 selected have 9 rational zeros and 6048 have 10. Inspected separate bundled geometric checker: 1008 nonsingular conics each with 6 disjoint rational lines yield exactly 6048 products LQ, while 280 nine-point unital configurations form Hermitian orbit; full PGL3(F4) order 60480 and orbit-stabilizer yield 216 and 10. Actual geometry explains Hermitian smoothness and LQ rational nonsingularity despite geometric reducibility. All finite forms, lines and projectivities exhaust the finite universes; this is a finite exhaustive theorem, not extrapolation.

## originality

PASS

Published October 26 full F4 cubic theorem already counts 11368 tangent-filling forms, proves 280 no-rational-line/smooth Hermitian and 11088 with rational line component. Those exact portions are acknowledged as known. Its result does not establish blocking equivalence on all rational-pointwise nonsingular cubics or the distinguished 6048 external line–conic projective orbit with two-sided equivalence. Primary Asgarli/Ghioca papers show Hermitian examples and general incidence frameworks, not the accessible exact joint classification. Originality PASS applies only to this surviving joint property and external-line/conic case, with older finite-geometric table risk.

## value

PASS

Blocking and tangent filling are two independently natural incidence properties; an exact equivalence inside the rationally nonsingular F4 cubic locus is a structural finite-geometric phenomenon. The complete 6328 forms and two projective orbits including rationally nonsingular but geometrically reducible external line-conics answer a motivated natural classification that earlier smooth-Hermitian-only counts cannot replace.

The dated certificate retains the supplied scientific assessment, sources and limitations.
