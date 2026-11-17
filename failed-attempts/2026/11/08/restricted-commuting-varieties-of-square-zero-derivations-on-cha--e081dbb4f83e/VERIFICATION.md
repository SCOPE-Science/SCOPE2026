---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Derivation D(t)=a(t²)+t b(t²) (even N) or a(t²)+t b(t²) with a in t² times even polynomials (odd N), D²(t)=ffprime gives ab=b²=0 in the appropriate truncated coefficient ring, and [D,E](t)=ad+cb. Choosing minimum nonzero valuation among b_i and using commuting constraints forces all a_i into a common annihilator and all b_i into the same u^j ideal, so every tuple belongs to some V_j^r. Each V_j is h-dimensional, pairwise intersection h-l+j, and the nested hyperplane union gives T_{N,r}(q)=(floor(h/2)+1)q^{rh}-floor(h/2)q^{r(h-1)}. Independent exhaustive binary polynomial coefficient pair enumeration h=1..4 agrees. Domain arbitrary characteristic-2 field, all N>=2 and r>=2, reduced variety only.

## originality

FAIL

FAIL: a published stronger theorem on exactly the same Der(k[t]/t^N), characteristic two, all N>=2 and all arities r>=1 already proves identical common-component rigidity, identical irreducible components and pair intersections, identical total count, AND the full joint rank polynomial. The current claim is a direct specialization, not a distinct theorem. Both recorded same publication date Nov 8, 2026: no intra-day chronological priority asserted; mathematical statement coverage is decisive.

## value

FAIL

FAIL: correct structural result is already contained in the stronger full joint-rank distribution and contributes no independent new mathematical invariant, classification, or boundary. Existing single-operator component results were earlier background; the published joint-tuple theorem fully covers the current multi-operator contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
